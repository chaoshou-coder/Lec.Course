# 03 · 学习顺序编排 —— 如何把 DAG 拓扑排序编排成可执行的学习计划

> **归属阶段:** PLAN (状态机 `PLAN` 态核心参考)
> **原始文档:** Lec.Python `dev/skills/03_学习顺序编排.md`
> **用途:** 在知识依赖图(DAG)拓扑排序的基础上,安排具体到天的学习顺序,平衡认知负荷和教学效率。
> **适用场景:** 把 `02-build-knowledge-dag.md` 产出的 DAG 转成 `learning-plan.md` 的 daily lesson_plan。

---

## 1. 编排的输入与输出

**输入:**
- 来自 `02-build-knowledge-dag.md` 的 DAG: 节点(`dag_nodes`)、边(`dag_edges`)、拓扑排序结果
- 来自 `requirements.md` 的 `daily_hours`(每日可用时长,仅供参考)和 `depth_goal`

**输出:**
- `learning-plan.md` 的 `lesson_plan` 字段: 每天学哪些节点、目标是什么、预计多久

---

## 2. 三大编排原则

### 2.1 工具先行(Tools-First)

**核心思想:** 先教"能做出有用东西"的工具,再教"底层原理"。

**为什么:** 最大动力来源是"我能做出东西了"。前 10 天都在讲"变量/类型/运算符",学员看不到目标的方向,流失率极高。

**具体策略:**
```
知识点 1: print/input → 立刻能写"自我介绍程序"
知识点 2: 数据类型 + 运算符 → 立刻能写"简易计算器"
知识点 3: 条件分支 → 立刻能写"BMI 计算器"
知识点 4: 循环 → 立刻能写"九九乘法表"
知识点 5: 字符串 → 立刻能写"手机号脱敏"
知识点 6: 列表 → 立刻能写"购物清单"
知识点 7: 函数 → 立刻能写"购物车程序"
```

**工具先行的代价:** 对底层原理理解不深。**解决方案:** 螺旋复访(见 2.3)。

### 2.2 脚手架递进(Scaffolded Progression)

**核心思想:** 每节课只引入一个新抽象层,其余都是已学内容。

**为什么:** 认知负荷理论 —— 人脑同时处理的新概念 ≤ 2 个。一节课同时引入"列表 + 列表方法 + 列表生成式 + 深浅拷贝",学员会崩溃。

**具体策略:**
```
知识点 6: 列表 CRUD (只教创建/索引/append/pop)
知识点 7: 列表方法 (只教 sort/reverse/extend)
Day 8: 列表生成式 (只教 [x for x in ...])
Day 9: 深浅拷贝 + 二维列表
```

**代价:** 课程进度变慢。**解决:** 每节课配足练习(6 道当堂练),确保"学一个会一个"。

### 2.3 螺旋复访(Spiral Revisit)

**核心思想:** 核心概念在三个复杂度层级复访,每次加深理解。

**为什么:** 一次学习无法形成长期记忆,需要在不同场景下反复遇到。

**具体策略(以"函数"为例):**
```
第一层(Day 7-10):  函数基础   → def add(a,b): return a+b → 理解"输入→处理→输出"
第二层(Day 26-31): nn.Module → 函数作为对象传入/返回 → 理解"一等公民"
第三层(Day 44+):   装饰器     → 函数包装函数 → 理解"切面编程"
```

---

## 3. 拓扑排序 → 学习计划的映射规则

这是 PLAN 态最核心的算法:把 `topological_order`(分层结构)转换为按天编排的 `lesson_plan`。

### 3.1 基础映射

```
topological_order = [
  [n1],          # 第 0 层:入度 0
  [n2, n3],      # 第 1 层:互相 parallel
  [n5],          # 第 2 层
  [n6, n7, n8],  # 第 3 层:3 个节点
]

→ lesson_plan = [
  {day: 1, nodes: [n1], daily_goal: "...", estimated_hours: 2},
  {day: 2, nodes: [n2, n3], daily_goal: "...", estimated_hours: 3},
  {day: 3, nodes: [n5], daily_goal: "...", estimated_hours: 2},
  {day: 4, nodes: [n6, n7, n8], daily_goal: "...", estimated_hours: 4},
]
```

### 3.2 daily_hours 溢出拆分(关键规则)

如果某一层的 `estimated_hours > daily_hours`,必须**拆分到连续多天**,并在 lesson_plan 里标记:

```markdown
{day: 4, nodes: [n6, n7], daily_goal: "...", estimated_hours: 2, parallelism_broken: true}
{day: 5, nodes: [n8], daily_goal: "...", estimated_hours: 2, parallelism_broken: true}
```

`parallelism_broken: true` = 这一层因为超出 daily_hours 被拆散,原本可以并行的学习被强制串行。在 QA 态会检查这个标记是否过多(过多 = DAG 粒度不对或 daily_hours 输入不合理)。

### 3.3 高负荷日缓冲策略

连续 3 天都是高负荷(estimated_hours ≈ daily_hours)时,第 4 天安排为**缓冲日**:
- 不排新节点
- 只做练习巩固 + 迷你项目
- QA 态会验证缓冲日是否必要

---

## 4. 编排质量检查清单

输出 `lesson_plan` 前,agent 自检:

| 检查项 | 规则 |
|--------|------|
| 前置完整性 | 每个节点的所有强依赖都排在它之前 |
| daily_hours 不溢出 | 单天 estimated_hours ≤ daily_hours(超出则已拆分) |
| 工具先行 | 产出"能用"的节点优先于纯概念节点 |
| 脚手架递进 | 同一天不超过 2 个新抽象层 |
| 高负荷缓冲 | 连续 ≤ 3 天高负荷 |
| parallel 节点尽量并行 | 同层节点尽量安排在同一天 |

任何一项不满足 = 回 `02-build-knowledge-dag.md` 调整 DAG 或重新编排。

---

## 交叉参考

- **上游:** `02-build-knowledge-dag.md`(产出 DAG 和拓扑排序)、`requirements.md`(daily_hours / depth_goal)
- **下游:** BUILD 态的并行子 agent 调度(每天 = 一个子 agent)、`04-design-assessments.md`(每天的练习设计)
- **产物:** `learning-plan.md`(PLAN 态硬性产出,含 lesson_plan)
- **验证:** QA 态检查 lesson_plan 的前置完整性和 daily_hours 合规性
