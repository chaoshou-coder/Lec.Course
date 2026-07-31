# /course-agent — 课程生产多 agent 协作

> 一个主 agent 驱动课程生产的全流程:需求问答 → 知识依赖推理 → 并行制课 → 并行验收。
> 状态机架构,软关卡 + 硬验收,用户选择并发度。

## 启动

用户说"我想学 XXX"或"/course-agent"时,从 `IDLE` 进入 `DISCOVER`。

## 状态机执行

完整状态机见 [`state-machine.md`](state-machine.md)。下面是每个状态的执行逻辑。

---

### DISCOVER —— 需求问答 + 研究目标域

**参考:** `methodology/01-discover-target-domain.md`

**执行:**
1. **深挖具体目的**(按顺序五问):
   - Q1: 你要做什么东西?(从抽象→具体)
   - Q2: 做给谁看/用?(受众)
   - Q3: 解决你什么痛点?(真实动机,**最关键**——答不出来回到 Q1)
   - Q4: 什么时候要完成?(时间约束)
   - Q5: 做好了长什么样?(可视化成功标准)
2. 多轮 `ask_user` 敲定其他要素:学员画像、深度、每日时长、验收标准
3. 询问并发度偏好(`build_parallelism` / `qa_parallelism`),见 BUILD/QA 段
4. 用 `web_search` 研究目标域(藤校课程优先),找到 2-3 门参照课程
5. **搜索失败处理(强制 gate):** 如果搜索工具未返回实时结果,**禁止**自作主张继续(包括绕道用 WebFetch),**必须**停下来向用户说明失败原因并请求手动提供参照或确认跳过。记录到 work-log 的 `search_failure_handling` 字段
6. 验证用户设定的 depth_goal 是否合理
7. 产出 `output/requirements.json`(含 `specific_purpose` + `parallelism`),用 `scripts/validate.py` 校验

**软关卡:** 产出后进 `AWAIT_CONFIRM`,向用户展示:
- 终点能力定义
- 参照课程列表
- 建议的深度和时长
- 请用户 approve / reject / revise

**转移:** approve → `PLAN`; reject/revise → 回 `DISCOVER` 调整

---

### PLAN —— 扒知识依赖 DAG + 推理学习路径

**参考:** `methodology/02-build-knowledge-dag.md`, `methodology/03-design-learning-sequence.md`

**执行:**
1. 进入 **Plan Mode**(使用 agent harness 的原生规划模式):
   - **Claude Code:** 调用 `EnterPlanMode`,在 plan 文件中设计 DAG 和编排
   - **Codex:** 使用其 built-in planning 功能(生成 plan.md 供用户审批)
   - **pi agent:** 使用其 task decomposition 模式
   - **zcode:** 使用其 plan mode
2. 在 Plan Mode 内完成:
   - 用**倒推三步法**从终点能力反推知识链条
   - 用参照课程验证 DAG 正确性(gold-set 对比)
   - 应用三大编排原则(工具先行/脚手架递进/螺旋复访)
   - 按 daily_hours 编排每日 lesson_plan
   - 剪掉从终点能力不可达的枝,记录到 pruned_branches
3. 产出 plan 文件,向用户展示:
   - DAG 节点数和层数
   - 学习天数和每日时长
   - 被剪掉的枝(让用户决定是否需要补回)
   - 请用户 approve / reject / revise
4. 用户 approve 后,退出 Plan Mode,产出 `output/learning-plan.json`,用 `scripts/validate.py` 校验

**转移:** approve → `BUILD`; reject/revise → 留在 Plan Mode 调整

---

### BUILD —— 并行 spawn subagent 制课

**参考:** `methodology/04-design-assessments.md`, `methodology/05-production-standards.md`

**并发度(v1.4 新增):**

用户在 DISCOVER 阶段选择 `build_parallelism`(并发 subagent 数):

| 级别 | 并发数 | 适用场景 | 风险 |
|------|--------|----------|------|
| `single` | 1 | 小域(≤5 知识点)、调试模式 | 无并行风险,但慢 |
| `moderate` | 3 | 中等域(6-15 知识点) | 推荐默认 |
| `high` | 5 | 大域(>15 知识点) | 需要更多 token |
| `max` | 不限制 | 超大域(>25 知识点) | token 消耗最大 |

**执行:**
1. 按 `build_parallelism` 将知识点分组,每组 spawn 一个 build subagent
2. 每个 subagent 独立产出自己负责的知识点:
   - `knowledge/NN-title.md`(8 步趁热打铁笔记,含知识地图)
   - `exercises/NN-title/practice01-06.{ext}`(6 道当堂练)
   - `exercises/NN-title/task01-03.{ext}`(3 道课后作业)
3. **工作目录隔离(强制):** 每个 subagent 必须使用**绝对路径**写入产物,禁止相对路径。主 agent 在 spawn 时明确指定:
   - 知识文件路径: `{project_abs_path}/knowledge/NN-title.md`
   - 练习目录路径: `{project_abs_path}/exercises/NN-title/`
   - 禁止在 subagent 内部 `cd` 或使用相对路径
4. subagent 写完后用 `scripts/content-quality-check.py` + `scripts/render-check.py` 校验
5. 失败的知识点单独标记,由主 agent 重试或重新 spawn
6. **重试质量保障(强制):** 重试产出的文件必须通过与原任务相同的质量检查,且主 agent 对比两次产出的质量指标(注释密度、错误段数量),确保重试不降级
7. 所有 subagent 完成后,主 agent 统一检查跨知识点一致性(导航链接、前置依赖)

**导航链接路径规则(v1.4 新增):**

知识文件末尾的导航链接必须用相对路径,**根据目录深度自动选择**:

| 当前位置 | 返回 README | 跳到上一/下一知识点 |
|----------|------------|---------------------|
| `knowledge/NN-title.md`(单层结构) | `../README.md` | `./NN-other.md` |
| `knowledge/sub/NN-title.md`(嵌套结构) | `../../README.md` | `../sub/NN-other.md` |

**判断方法:** 在写路径前,先 `ls` 确认 README 在哪一级目录,然后数层级。

**反例(常见错误):** 假设 README 在上层就用 `../../README.md`,实际只隔一层 → 链接断裂。

**教学法触发(v1.1 R3):**

当 `learning-plan.json` 的节点带 `teaching_method` 字段时,知识点 MD 必须包含对应结构:

| teaching_method | 知识点 MD 必须含 | 练习必须含 |
|---|---|---|
| `ncdl` | Break It 演示段(故意写错代码 → Traceback → Fix) | 至少 1 道找出反模式的题 |
| `dual_layer` | 叙事锚点段(80% 教学时间)+语法点独立样本段 | 业务代码练习 |
| `consumer_gate` | (无限制) | 至少 1 道用消费者函数 ≤4 行门控 |

未标 teaching_method = 默认教学法(纯讲解)。

**文件后缀(v1.1 R3):**

练习文件后缀必须与运行环境一致(从 `requirements.json` 的 `constraints` 推断):
- HTML 课程 → `.html` + `.css` + `.js`
- JS 课程 → `.js`
- Python 课程 → `.py`
- 其他语言 → 对应扩展名

不强制但强烈建议——避免学员混用运行环境。

**BUILD 自检清单(v1.3 R12):**

每个知识点产出后,BUILD 必须对照 PLAN 的 pedagogy_notes 自检:

| 自检项 | 检查方式 |
|--------|---------|
| pedagogy_notes 落地 | 知识点 MD 中哪里体现了 PLAN 标注的编排原则? |
| teaching_method 触发 | 标了 ncdl 的节点是否有 Break It 段? 标了 consumer_gate 的节点是否有消费者函数? |
| 下一知识点衔接 | 知识点 MD 末尾是否有导航链接? |
| 8 步循环 | 痛点/类比/解释/ASCII/执行过程/常见错误/学员代码区/参考答案 是否都在? |

自检结果写入 `knowledge/NN-title.md` 末尾的"BUILD 自检"段。

**转移:** 所有知识点完成 → `QA`

---

### QA —— 并行 subagent 验收

**执行:**
1. 按 `qa_parallelism`(通常 = build_parallelism 或 -1)spawn 多个 QA subagent
2. 每个 QA subagent 负责不同维度:
   - **结构检查 subagent**(无需深领域知识): 所有产物文件存在、格式符合 `05-production-standards.md`
   - **内容正确性 subagent**(需要领域推理): 对照 `acceptance_criteria` 判定是否达成目标
   - **教学法对齐 subagent**: 检查 PLAN 的 pedagogy_notes 是否在 BUILD 中落地
   - **学员视角 subagent**: 评估练习难度、类比可理解性、先修知识覆盖
3. 每个 subagent 独立执行,不读取 BUILD 上下文(只看产物文件)
4. 用 `scripts/content-quality-check.py` + `scripts/render-check.py` 校验知识文件
5. 主 agent 汇总所有 subagent 发现,产出 `output/qa-report.json`,用 `scripts/validate.py` 校验

**QA 跨阶段对照(v1.3 R12):**

QA 不仅查 BUILD 产出,还要对照上游阶段:

| 对照项 | 检查方式 |
|--------|---------|
| PLAN pedagogy_notes → BUILD 落地 | Day 1 标了"工具先行",知识点 MD 是否有可运行代码? |
| DISCOVER criteria → BUILD 覆盖 | 每条 acceptance_criteria 是否都有对应练习? |
| teaching_method → 内容 | 标 ncdl 的节点是否有 Break It 段? |

对照结果写入 qa-report.json 的 `structural_check.details`。

**硬关卡(唯一硬性关卡):**
- `overall_verdict == pass` → `DONE`
- `overall_verdict == pass-with-minors` → `DONE`(标注 minor)
- `overall_verdict == fail` → 按 `recommended_action.type` 回退:
  - `rebuild-lesson` → 回 `BUILD` 重制指定课
  - `rebuild-plan` → 回 `PLAN` 重排
  - `redo-discover` → 回 `DISCOVER`(requirements 级 root cause)

---

### AWAIT_CONFIRM —— 软关卡

agent 进入此状态时:
1. 写 `.gate-pending/{stage}.json`(产物 + 状态 + 选项)
2. 向用户展示当前阶段产物摘要 + 请用户 approve / reject / revise
3. 用户回复后读取 → 决定下一状态

### DONE —— 终态

全部通过,向用户展示课程产出路径,等待新课程启动。

---

## 产物清单

| 产物 | 路径 | 产出态 | schema |
|------|------|--------|--------|
| 课程需求 | `output/requirements.json` | DISCOVER | `schemas/requirements.schema.json` |
| 学习计划 | `output/learning-plan.json` | PLAN | `schemas/learning-plan.schema.json` |
| 知识点材料 | `knowledge/NN-title.md` | BUILD | — |
| 练习文件 | `exercises/NN-title/` | BUILD | — |
| 验收报告 | `output/qa-report.json` | QA | `schemas/qa-report.schema.json` |

## 关键约束

- **独立验收:** QA subagent 不读取 BUILD 上下文(只看产物文件)
- **并行隔离:** 每个 build subagent 写到自己隔离的目录,无共享 mutable state
- **硬关卡只有 QA:** 中间关卡都是软关卡(agent 主动征求确认)
- **schema 校验:** 每个阶段的硬性产出必须通过 `scripts/validate.py`
- **内容质量校验:** BUILD 产出必须通过 `scripts/content-quality-check.py` + `scripts/render-check.py`
- **回退是显式的:** 由 `qa-report.recommended_action` 或用户指令触发,不靠 agent 自行决定
- **工作日志:** 全流程记录到 `output/work-log.json`,追踪效率瓶颈(见 `methodology/07-work-logging.md`)
