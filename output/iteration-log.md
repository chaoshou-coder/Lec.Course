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
