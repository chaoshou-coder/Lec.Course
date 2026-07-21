# /course-agent — 课程生产单 agent

> 一个 agent 驱动课程生产的全流程:需求问答 → 知识依赖推理 → 并行制课 → 独立验收。
> 状态机架构,软关卡 + 硬验收。

## 启动

用户说"我想学 XXX"或"/course-agent"时,从 `IDLE` 进入 `DISCOVER`。

## 状态机执行

完整状态机见 [`state-machine.md`](state-machine.md)。下面是每个状态的执行逻辑。

---

### DISCOVER —— 需求问答 + 研究目标域

**参考:** `methodology/01-discover-target-domain.md`

**执行:**
1. 多轮 `ask_user` 敲定五要素:知识域、目的、深度、每日时长、验收标准
2. 用 `web_search` 研究目标域(藤校课程优先),找到 2-3 门参照课程
3. 验证用户设定的 depth_goal 是否合理
4. 产出 `output/requirements.json`,用 `scripts/validate.py` 校验

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
1. 用**倒推三步法**从终点能力反推知识链条:
   - Step 1: 写出终点能力的直接前置
   - Step 2: 递归展开每个前置,直到原子知识
   - Step 3: 合并成 DAG,做拓扑排序
2. 用参照课程验证 DAG 正确性(gold-set 对比)
3. 应用三大编排原则(工具先行/脚手架递进/螺旋复访)
4. 按 daily_hours 编排每日 lesson_plan,溢出则拆分(标记 parallelism_broken)
5. 剪掉从终点能力不可达的枝,记录到 pruned_branches
6. 产出 `output/learning-plan.json`,用 `scripts/validate.py` 校验

**软关卡:** 产出后进 `AWAIT_CONFIRM`,向用户展示:
- DAG 节点数和层数
- 学习天数和每日时长
- 被剪掉的枝(让用户决定是否需要补回)
- 请用户 approve / reject / revise

**转移:** approve → `BUILD`; reject/revise → 回 `PLAN` 调整

---

### BUILD —— 并行 spawn subagent 制课

**参考:** `methodology/04-design-assessments.md`, `methodology/05-production-standards.md`

**执行:**
1. 按 lesson_plan 的每天 spawn 一个 build subagent(并行,无共享 mutable state)
2. 每个 subagent 负责一天的产出:
   - `course/lessonXX/notes.md`(8 步趁热打铁笔记)
   - `course/lessonXX/README.md`(当天入口)
   - `course/lessonXX/in_class/practice01-06.{ext}`(6 道当堂练)
   - `course/lessonXX/homework/task01-03.{ext}`(3 道课后作业)
3. subagent 写完后用 `scripts/validate.py` 校验产出
4. 失败的 lesson 单独标记,不阻塞其他 lesson

**教学法触发(v1.1 R3):**

当 `lesson_plan` 的节点带 `teaching_method` 字段时,notes.md 必须包含对应结构:

| teaching_method | notes.md 必须含 | 练习必须含 |
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

**并行协调:**
- 每个 subagent 写到自己隔离的 `course/lessonXX/` 目录
- 无共享 mutable state,不写共享 manifest
- 失败的 lesson 单独重跑

**转移:** 所有 lesson 完成 → `QA`

---

### QA —— 独立 subagent 验收

**执行:**
1. spawn 全新的 QA subagent(**不读取任何 build subagent 的产出上下文**)
2. QA subagent 接收 `requirements.md` + `learning-plan.md` + 被审课程材料
3. 双轨验收:
   - **结构检查**(无需深领域知识): 所有产物文件存在、格式符合 `05-production-standards.md`
   - **内容正确性**(需要领域推理): 对照 `acceptance_criteria` 判定是否达成目标
4. 产出 `output/qa-report.json`,用 `scripts/validate.py` 校验

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
| 每日课程 | `course/lessonXX/` | BUILD | — |
| 验收报告 | `output/qa-report.json` | QA | `schemas/qa-report.schema.json` |

## 关键约束

- **独立验收:** build subagent 绝不能验收自己的产出(QA 永远是全新 subagent)
- **硬关卡只有 QA:** 中间关卡都是软关卡(agent 主动征求确认)
- **schema 校验:** 每个阶段的硬性产出必须通过 `scripts/validate.py`
- **回退是显式的:** 由 `qa-report.recommended_action` 或用户指令触发,不靠 agent 自行决定
