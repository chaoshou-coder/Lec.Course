# Iteration Log

## R1: JS 变量(极小) × DISCOVER

**日期:** 2026-07-21
**测试用例:** JavaScript 变量(let/const/var)
**能力点:** DISCOVER(需求问答 + 研究目标域)
**产出:** `output/iter-R1-js-variables/requirements.json`
**校验:** ✅ schema 通过

### 评估发现

✅ 做得好的:
- acceptance_criteria 3 条,每条都可独立判定
- research_grounded=true,3 门真实参照课程(MDN/javascript.info/freeCodeCamp)
- depth_goal="能写"与小主题匹配
- constraints 具体可执行

❌ 最大摩擦点(按影响排序):

1. **缺少学员画像** —— 没有说明"学员是谁"(自学者?bootcamp?儿童?)。学员画像直接影响例子选择和语言风格。DISCOVER skill 没有要求定义画像。

2. **没区分"独立主题"vs"进阶路径"** —— current_level 提到 HTML 基础,但 JS 变量作为独立主题,其前置应该是"了解编程基本概念"而非 HTML。DISCOVER skill 没有问"这是一个独立主题还是某个路径的第 N 步"。

3. **acceptance_criteria 认知层级单一** —— 3 条都是"应用"层级,缺少"记忆/理解"(如"能背诵三种声明方式的区别")和"分析/评价"(如"能分析一段含作用域的代码并预测输出")的 criteria。

4. **constraints 有歧义** —— "浏览器控制台或 Node.js"是二选一但没明确,BUILD 阶段会产生困惑。

### Skill 改进

**改进文件:** `methodology/01-discover-target-domain.md`

**改进内容:** 在 DISCOVER 产出要求中增加:
1. 学员画像字段(learner_persona):年龄/背景/学习动机
2. 主题类型字段(topic_type):独立主题 / 路径第N步(影响 current_level 怎么写)
3. acceptance_criteria 必须覆盖 ≥2 个认知层级(记忆/理解/应用/分析/评价)
4. constraints 中的二选一必须明确推荐哪个

**为什么:** 这四个缺失会导致 BUILD 产出的例子和语言风格不匹配目标学员,且 criteria 覆盖不完整会影响 QA 验收的有效性。

---

## R2: JS 变量(极小) × PLAN

**日期:** 2026-07-21
**测试用例:** JavaScript 变量(let/const/var)
**能力点:** PLAN(扒知识依赖 DAG + 推理学习路径)
**产出:** `output/iter-R2-js-variables-plan/learning-plan.json`
**校验:** ✅ schema 通过 + ✅ DAG 拓扑一致

### 评估发现

✅ 做得好的:
- 6 节点 DAG,清晰反映 let/const/var 三个分支 + 对比节点
- 4 层拓扑,v2 声明语法是真正的"分流闸"
- 3 项剪枝都有明确理由
- daily_hours 不溢出(每天 1.0-1.5h)

❌ 最大摩擦点(按影响排序):

1. **编排原则落地不可见** —— SKILL.md 要求"应用工具先行/脚手架递进/螺旋复访",但 learning-plan.json 没有字段记录哪些节点体现了哪个原则。agent 产完 DAG 后,用户无法验证编排是否真的落实,只能凭印象判断。

2. **剪枝决策未让用户审核** —— 剪了 TDZ 深入、数据类型、解构赋值,但没让用户在 AWAIT_CONFIRM 阶段决定是否补回。这是 hard-coded 的剪枝,绕过了 user sovereignty。

3. **缺少教学法标注** —— 每个节点有 min_requirement,但没说用什么教学法(NCDL/双层覆盖/消费者门控)。BUILD subagent 在制课时不知道该节点是否触发 NCDL。

4. **节点代号不友好** —— v1-v6 是内部代号,使用者看到的是这些符号。应该有 day_label 字段让用户/QA 能直接读出"Day 1 学什么"。

### Skill 改进

**改进文件:** `methodology/02-build-knowledge-dag.md`, `methodology/03-design-learning-sequence.md`, `schemas/learning-plan.schema.json`

**改进内容:**

1. PLAN 产出增加 `pedagogy_notes` 字段:记录每个 lesson 体现了哪些编排原则(工具先行/脚手架递进/螺旋复访)。
2. PLAN 产出增加 `pruning_review_required: bool` 字段:剪枝必须用户审核确认才能进入 BUILD。
3. learning-plan schema 增加 `teaching_method` 字段(per node):可选值 `ncdl`/`dual_layer`/`consumer_gate`,BUILD 时按此触发对应教学法。
4. lesson_plan 节点增加 `label` 字段:友好主题名(如 "变量概念与声明语法")。

**为什么:** PLAN 产出的 DAG 应该在产物中就体现编排意图,而不是依赖 BUILD 自己重新判断;剪枝不能是 agent 自作主张,必须经过用户审核;教学法标注让 BUILD 和 QA 都知道每个节点的设计意图。

---

## R3: JS 变量(极小) × BUILD (Day 1 only)

**日期:** 2026-07-21
**测试用例:** JavaScript 变量
**能力点:** BUILD(产出课程)
**产出:** `output/iter-R3-js-variables-build/course/lesson01/` (11 文件)
**测试范围:** 仅 Day 1(v1 概念 + v2 声明语法)。Day 2(v3-v5 作用域)+ Day 3(v6 综合)留待 R8 验证。

### 评估发现

✅ 做得好的:
- notes.md 8 步循环完整(痛点→类比→解释→ASCII→执行跟踪→常见错误→学员代码区→参考答案)
- 练习难度递进 ★/★/★★/★★/★★★/★★★ 线性
- 文件头标注完整(难度/知识点/时间)
- 当堂练 6 道 + 作业 3 道 = 符合 schema

❌ 最大摩擦点(按影响排序):

1. **PLAN 标注的教学法未触发** —— R2 给 DAG 节点加了 teaching_method 字段,v3/v4/v5 标了 ncdl,v6 标了 consumer_gate。但 SKILL.md BUILD 段没有说明:当 PLAN 标了 teaching_method 时,BUILD 必须按该教学法产出对应内容(ncdl → Break It 演示;consumer_gate → 消费者函数门控)。R3 的 v1/v2 没标,但 Day 2 会触发这个 gap。

2. **practice 文件用 .py 后缀但内容是 JS** —— 这是 Lec.Python 时代的格式遗留,Lec.Course 是通用框架,跨语言一致性差。R1 constraints 说"运行环境 = 浏览器控制台或 Node.js",所以练习应是 .js 文件。这是个 schema/格式不一致问题。

3. **notes.md 缺"明日衔接"段** —— Day 1 末尾没有提"今天学了概念和声明,明天学作用域差异"。这导致螺旋复访体现不出来,学员可能不知道自己接下来要学什么。

### Skill 改进

**改进文件:** `skills/course-agent/SKILL.md`, `methodology/05-production-standards.md`

**改进内容:**

1. SKILL.md BUILD 段:当 DAG 节点带 teaching_method 时,BUILD 必须显式应用对应教学法:
   - `ncdl` → notes.md 加 "Break It 演示"段 + NCDL 反模式展示
   - `dual_layer` → notes.md 用"叙事锚点(80%)+语法点独立样本(20%)"结构
   - `consumer_gate` → 练习文件必须含消费者函数 ≤4 行
2. SKILL.md BUILD 段:产出文件后缀必须匹配运行环境:
   - HTML 课程 → .html + .css + .js
   - JS 课程 → .js
   - Python 课程 → .py
   (不强制,但 requirements.constraints 应明确推荐)
3. methodology/05:每个 notes.md 末尾必须含 "明日衔接" 段(≤3 行,说"明天 X 课将讨论 Y")

**为什么:** 让 BUILD 真正反映 PLAN 的设计意图,而不是凭 agent 默认行为;改善跨语言/跨主题的兼容性;让螺旋复访从设计阶段就可见。


