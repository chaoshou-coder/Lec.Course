# Lec.Course 迭代经验手册

> 从 R1-R17 提炼的教训。每轮迭代开始前必读。

## 10 条铁律

### 1. 文件后缀必须匹配运行环境(R3/R8 两次犯错)
- JS 课程 → `.js`
- Python 课程 → `.py`
- SQL 课程 → `.sql`
- HTML 课程 → `.html`
- 设计/架构域(不写代码) → `.md`
- 终端命令 → `.sh`

### 2. DISCOVER 必须定义学员画像(R1)
- `learner_persona` 是 schema 必填字段
- 包含:age_stage / background / motivation
- 没有画像 = BUILD 产出例子不匹配目标学员

### 3. acceptance_criteria 必须覆盖 ≥2 个认知层级(R1)
- 记忆/理解层:用"类比/教别人/预测失败"形式,不用"背诵/列表"
- 应用层:用"给定 X,能产出 Y"形式
- 分析/评价层:用"诊断/修正/预测"形式

### 4. PLAN 的 pedagogy_notes 必须可见(R2)
- 每个 lesson 的 `pedagogy_notes` 字段必须填写
- 工具先行:"先教 X 立刻能做 Y"
- 脚手架递进:"每节只引入一个新抽象层"
- 螺旋复访:"核心概念在三个复杂度层级复访"

### 5. teaching_method 标注决定 BUILD 内容(R2/R3)
- `ncdl` → notes.md 必须有 Break It 演示段 + 反模式练习
- `consumer_gate` → 练习必须有消费者函数(≤4 行)
- `dual_layer` → notes.md 用"叙事锚点(80%)+语法点独立样本(20%)"结构
- 未标注 = 默认讲解

### 6. 剪枝必须 user-validated(R2)
- `pruning_review_required: true` 是默认
- AWAIT_CONFIRM 阶段必须展示被剪枝节点

### 7. QA 必须四维检查(R10)
- 知识性内容正确性:随机抽 2-3 个知识点验证定义/示例
- 8 步循环验证:痛点/类比/解释/ASCII/执行过程/常见错误/学员代码区/参考答案
- pedagogy_notes 对照:PLAN 标注的教学法是否在 BUILD 落地
- 学员视角评估:练习难度是否匹配目标学员

### 8. 每个 notes.md 末尾必须有"明日衔接"(R3)
- 明天学什么
- 今天遗留的概念
- NCDL 反模式预告(如果下一天是 NCDL 节点)

### 9. schema 变更必须立即应用,不等批处理(R4 教训)
- R1-R3 的 schema 变更被延迟到 R8,导致中间几轮产出不符合新 schema
- 正确做法:改一轮 schema,下一轮立即用

### 10. reference_courses 和 reference_resources 分离(R4)
- `reference_courses`:结构化课程(有 syllabus)
- `reference_resources`:博客/视频/awesome-list(无 syllabus)

## 防回归检查清单

每轮 BUILD 前,逐项检查:

- [ ] 文件后缀匹配运行环境
- [ ] learner_persona 已填写
- [ ] topic_type 已标注(独立/路径第N步)
- [ ] acceptance_criteria 覆盖 ≥2 个认知层级
- [ ] 每个 lesson 有 pedagogy_notes
- [ ] 标 teaching_method 的节点有对应内容
- [ ] pruning_review_required = true
- [ ] 每个 notes.md 有明日衔接段
- [ ] reference_courses vs reference_resources 分离

每轮 QA 前,逐项检查:

- [ ] 知识性内容正确性抽查(2-3 个知识点)
- [ ] 8 步循环验证(每个 notes.md)
- [ ] pedagogy_notes 对照(PLAN → BUILD)
- [ ] 学员视角评估(难度线性/类比可理解/先修覆盖)
