# 01 · 开源课程调研方法 —— 如何在 DISCOVER 阶段研究目标域

> **归属阶段:** DISCOVER (状态机 `DISCOVER` 态核心参考)
> **原始文档:** Lec.Python `dev/skills/02_开源课程调研方法.md`
> **用途:** 在需求问答过程中,agent 用这套方法实时研究目标域,验证用户想学的终点能力,并找到高质量参照课程。
> **适用场景:** 新用户启动课程、agent 需要理解陌生知识域、为 DAG 推理收集 gold-set 候选。

---

## 1. 研究在 DISCOVER 阶段的位置

DISCOVER 态的核心任务是产出 `requirements.md`。agent 不能只靠和用户问答 —— 还需要**实时研究目标域**,才能:
- 帮用户把模糊的目标("我想学 AI")收敛成可验证的终点能力("用 HuggingFace LoRA 微调一个文本分类模型")
- 验证用户设定的 depth_goal 是否合理
- 为后续 PLAN 态的 DAG 推理收集 gold-set 候选课程

研究和问答是**交织进行**的,不是先研究再问答。

---

## 2. 推荐搜索路径

### 2.1 藤校公开课优先

| 优先级 | 来源 | 代表课程 | 为什么优先 |
|---|---|---|---|
| ⭐⭐⭐⭐⭐ | MIT OCW / MITx | 6.0001, 6.0002, 6.036 | 课程大纲完整,PS/考试公开,学术严谨 |
| ⭐⭐⭐⭐⭐ | Harvard / edX | CS50P, CS50AI | 项目驱动,check50 自动评测,适合习题参考 |
| ⭐⭐⭐⭐ | Stanford / Coursera | CS229, CS231n, CS224N | ML/DL/NLP 标杆,讲义极高质量 |
| ⭐⭐⭐⭐ | UC Berkeley | CS61A, CS188, Data 8 | 计算思维导向,适合 Python 入门参考 |
| ⭐⭐⭐ | 经典免费教材 | Think Python 2E, py4e, ATBS | 免费在线阅读,习题丰富 |

### 2.2 为什么商业化课程不宜直接参照?

商业化课程(Udemy / 极客时间 / 慕课网等)的目标函数不同:

| 维度 | 开源/藤校 | 商业化 |
|---|---|---|
| **目标** | 知识体系完整 | 完课率、好评率、销量 |
| **深度** | 宁可难也要讲透 | 宁可浅也要"听得懂" |
| **习题** | 有挑战,鼓励犯错 | 平滑,避免学员卡住 |
| **更新** | 学术驱动,慢但准 | 市场驱动,快但可能跟风 |

**用法:** 用藤校课程定骨架,用商业化课程定热点,用社区(GitHub/知乎)定习题素材。

### 2.3 搜索关键词模板

```
# 入门级
"Introduction to Python" site:ocw.mit.edu
"Python for Everybody" site:coursera.org

# 进阶级
"Machine Learning" site:stanford.edu CS229
"Deep Learning" site:cs231n.stanford.edu

# 习题素材
"Python exercises" site:github.com stars:>1000
"Python projects for beginners" site:realpython.com
```

---

## 3. 如何提取一门课的"章节顺序"和"知识点粒度"

### 3.1 提取章节顺序

**Step 1** 找到官方 Syllabus / Schedule(MIT OCW 看 Calendar —— Coursera 看 Weekly Schedule —— 教材看目录)

**Step 2** 把每周主题写成一行,忽略具体习题和阅读材料。

示例 —— MIT 6.0001 提取结果:
```
W1: What is computation? / Branching and Iteration
W2: String Manipulation, Guess-and-Check, Approximations
W3: Decomposition, Abstraction, Functions
W4: Tuples, Lists, Aliasing, Mutability
W5: Recursion, Dictionaries
W6: Testing, Debugging, Exceptions
W7: Object Oriented Programming
W8: Python Classes and Inheritance
W9: Understanding Program Efficiency
W10: Searching and Sorting
```

### 3.2 提取知识点粒度

每个**章节** = 一个**知识点**(不是每个小节)。粒度判断:
- ✅ "列表 CRUD"(操作级,约 1 小时教学)
- ✅ "梯度下降原理"(理解级,约 2 小时教学)
- ❌ "Python 基础"(太粗,不可执行)
- ❌ "会写 for 循环"(太细,合并到控制流)

提取结果直接喂给 PLAN 态的 DAG 推理。

---

## 4. 数据可靠性评估方法

| 评估维度 | 高可信 | 低可信 |
|---|---|---|
| **来源** | 官方 syllabus / 同行评审 | 个人博客 / 营销文案 |
| **时效** | 3 年内更新 | 5 年以上未更新 |
| **完整度** | 有 syllabus + 作业 + 考试 | 只有标题列表 |
| **社区验证** | GitHub star > 1000 / 引用多 | 无引用 / 单来源 |

**用法:** 优先使用高可信来源构建 gold-set,低可信来源只用于"看市场热点"。

---

## 5. 研究结果的消费方式

DISCOVER 态产出的研究成果写入 `requirements.md` 的几个字段:

| 研究成果 | 写入字段 |
|---|---|
| 终点能力定义 | `target_capability` |
| 学员当前水平(对比参照课后) | `current_level` |
| 合理的深度建议 | `depth_goal` |
| 找到的参照课程列表 | `constraints` 里的"参照课程"子字段 |
| 研究是否成功 | `requirements.md` 顶层字段 `research_grounded: true/false` |

**降级策略:** 如果 web_search 不可用,标注 `research_grounded: false`,并在 README 里提示用户手动验证关键依赖。

---

## 交叉参考

- **上游:** 用户启动 /course-agent 时的初始描述
- **下游:** `02-build-knowledge-dag.md`(用这里提取的章节顺序作为 gold-set 验证 DAG)
- **产物:** `requirements.md`(DISCOVER 态的硬性产出)
