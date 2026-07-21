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



---

## R4: Claude Code 使用 × DISCOVER

**日期:** 2026-07-21
**测试用例:** Claude Code CLI(工具/元主题)
**能力点:** DISCOVER(需求问答 + 研究)
**产出:** `output/iter-R4-claude-code-discover/requirements.json`
**校验:** ✅ schema 通过(应用了 R1 全部改进)

### 评估发现

✅ R1 改进在工作:
- learner_persona 正确填写(在职开发者/Python 3年)
- topic_type="独立主题" 明确
- acceptance_criteria 覆盖 3 个认知层级
- constraints 没有"或"歧义

❌ 新摩擦点(元主题特化):

1. **target_capability 范围过大** —— 5 件能力塞进 2 周入门课太多。DISCOVER 缺核心/边缘区分。
2. **"理解层" criteria 用"背诵"驱动** —— "5 句话解释"是机械背诵,不是真理解。理解层应该用"教别人/类比/预测失败"。
3. **reference_courses vs reference_resources 混在一起** —— YouTube/awesome-* 不是结构化课程。
4. **缺"学完后真实使用场景"** —— 验收 criteria 不足以覆盖成功场景。
5. **current_level 单维度** —— 工具熟练度和主题深度应分开。

### Skill 改进(暂记,等 R8 后统一起 schema)

methodology/01-discover-target-domain.md:
1. target_capability 收敛(≤3 核心,余下进 scope_out_of_v1)
2. acceptance_criteria "理解层" 用"教别人/类比/预测失败"形式
3. reference_courses vs reference_resources 分离
4. success_scenarios 字段(3-5 个具体场景)
5. current_level 拆 topic_depth + tool_fluency

**note:** R8 后统一起 schema,避免中途多次回滚。


---

## R5: Claude Code 使用 × PLAN

**日期:** 2026-07-21
**测试用例:** Claude Code CLI(工具/元主题)
**能力点:** PLAN(扒 DAG + 推理路径)
**产出:** `output/iter-R5-claude-code-plan/learning-plan.json`
**校验:** ✅ schema 通过 + ✅ topology valid(允许同天强依赖)

### 评估发现

✅ R2 改进在工作:
- 7 个节点标了 teaching_method(ncdl/dual_layer/c8 综合默认)
- 6 天都有 pedagogy_notes
- 4 项剪枝每项都有理由,pruning_review_required=true
- 友好的 day_label(不是 v1-v6 代号)

❌ 新摩擦点(元主题 PLAN 特化):

1. **教学法选择不稳定** —— c6 subagent 和 c5 tools/MCP 都标 ncdl,但这两个的反模式性质其实不同:c6 失败模式是"并发冲突/上下文丢失",c5 失败模式是"tool 调用权限/MCP 配置错误"。一个通用 'ncdl' 字段不能区分反模式类型。

2. **顶层 node min_requirement 偏高** —— c7/c8/c10 都标"能教",但 2 周入门课学员多数只能到达"能写"。"能教"是更高门槛(能向别人解释),不是初学者能快速达到的状态。

3. **没有"核心工作流"路径** —— DAG 中 c8(实战工作流)只有一个,但 Claude Code 的核心使用模式至少 3 种:重构 / 读陌生 codebase / 加新功能。应该拆开还是合并?DAG 没体现这种决策。

4. **tool_fluency 起点没反映** —— R4 发现 current_level 应拆 tool_fluency + topic_depth,但 PLAN 没有对应的"按起点决定从哪里开始"的规则。

5. **没有 feedback loop 设计** —— 学习 Claude Code 必须"用它做真实项目",但 lesson_plan 没有"用 Claude Code 做一个真实 PR"这类综合驱动项。

### Skill 改进(继续暂记,等 R8 后批量应用)

`methodology/02-build-knowledge-dag.md` 与 `03-design-learning-sequence.md`:
1. teaching_method 应该扩展枚举:`ncdl_concurrent_conflict` / `ncdl_hallucination` / `ncdl_permission` 等(NCDL 子类)
2. min_requirement=能教 应仅对 ≥50% 的 days 适用,≤50% 改为"能写"(深度与时间预算匹配)
3. PLAN 技能加"核心场景路径决策"—— 实战节点应拆或合应有明确判据(复杂 → 拆,简单 → 合)

**note:** 等 R8 一起统一应用,继续累积 friction evidence。

---

## R6: pi coding agent 使用 × PLAN

**日期:** 2026-07-21
**测试用例:** pi coding agent(元技能:如何使用 AI 编程代理)
**能力点:** PLAN(扒 DAG + 推理路径)
**产出:** `output/iter-R6-pi-coding-plan/learning-plan.json`
**校验:** ✅ schema + DAG valid(弱依赖同层和工具先行同天都是合理教学法模式)

### 评估发现

✅ R2 改进在工作:
- 8 节点,p2/p4 标 ncdl(下达指令/拆分任务的失败模式),p3 标 dual_layer,p5 标 consumer_gate
- 5 天都标了 pedagogy_notes
- 4 项剪枝都有理由,pruning_review_required=true
- 友好的 day_label

❌ 新摩擦点(元技能 PLAN 特化):

1. **"元技能"DAG 与"编程" DAG 结构不同** —— JS 变量是"概念→应用→综合"的累积结构,pi coding 是"下达→上下文→评估→迭代→实战"的**循环反馈**结构。当前的 DAG 是线性的,无法体现"迭代对话(p7)失败后再回到评估(p5)"这种回环。

2. **teaching_method 标注不一致** —— p2(下达指令)和 p4(任务拆分)都标 ncdl,但 p7(迭代修正)没标。p7 才是 NCDL 的最佳应用场景(展示"错误修正"的失败模式)。

3. **评估节点(p5)位置偏后** —— "如何判断 agent 产出是否正确"应该尽早出现(Day 1 末尾),因为学员从第一次下达任务就需要评估。当前 DAG 把它放在 Day 3,导致前两天学员不知道如何判断产出质量。

4. **缺少"对比体验"设计** —— 元技能学习需要"用 agent vs 不用 agent"的对比,让学员感受差异。当前 DAG 没有这类对比节点。

### Skill 改进(继续暂记,等 R8 后批量应用)

methodology/02-build-knowledge-dag.md:
1. 增加"回环 DAG"结构支持:某些主题(元技能/迭代流程)需要非线性的"尝试→评估→修正→再尝试"循环
2. teaching_method 一致性规则:NCDL 应标在"失败模式最多"的节点,不是随意标
3. 评估类节点前置规则:如果主题涉及"判断产出质量",评估节点应尽量前置(前 1/3 课程)
4. 增加"对比体验"节点类型:适用于元技能/工具类主题

**note:** 继续累积,等 R8 一起统一应用。
