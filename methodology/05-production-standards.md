# 05 · 自学材料排版规范 —— build subagent 产出笔记时必须遵守的格式标准

> **归属阶段:** BUILD (每个 build subagent 强制参考) + QA (structural_check 依据)
> **原始文档:** Lec.Python `dev/skills/05_Jupyter_Notebook_排版规范.md`
> **用途:** 所有自学笔记材料(self-study notes,取代课堂 slides)必须遵守的排版标准。这是 QA 态 structural_check 的直接依据。
> **版本:** v3.0(2026-07-14),以 OOP Day08-11 notebook 为 gold standard 重写
> **关键升级:** 8 步趁热打铁循环 + ASCII 内存图 + NCDL Break It + 常见错误

---

## 1. 标题层级:h3(天标题) + h4(知识点小节)

```
### Day 08 · OOP 基础                         ← h3(一天内唯一)
#### __init__ 构造函数 —— 给对象"贴标签"       ← h4(小节)
#### 实例方法 —— 对象能做什么                  ← h4(小节)
**逐行解剖**                                    ← 正文加粗(不是标题)
**为什么:**这是解释,不是标题                    ← 正文加粗
```

**规则:**
- `###` 只用一次(当天标题)
- `####` 用于每个知识点的标题
- 不再往下嵌套(不用 `#####`)
- 解释性文字用 **加粗** + 正文,不额外加标题层级

---

## 2. 加粗:只加关键词

```
✅ **类** = 蓝图/模板
✅ 使用 **append()** 方法可以在末尾添加元素
❌ **类是蓝图模板,用来创建对象**(整句加粗)
```

**规则:**
- 每行最多 1 处加粗
- 加粗对象:关键词、方法名、重要概念
- 不整句加粗,除非是"核心定义"

---

## 3. 一个概念 = 一个代码块(or fenced code in notes)

每个示例代码独立一个块,学员可以逐个理解:
```
✅ print("Hello")      ← 块 1:基础用法
✅ print("你好")       ← 块 2:中文
✅ print("A", "B")    ← 块 3:多值

❌ 以上 4 行全放在一个块里(输出混在一起,看不出每个独立结果)
```

---

## 4. 每个知识点 = 完整的 8 步趁热打铁循环

每个完整知识点必须包含以下 8 步,**缺一不可**(QA 态 structural_check 逐项验证):

```
① 概念 md:痛点(为什么需要) → 类比(生活例子) → 解释(是什么)
② ASCII 内存图 md(可选但推荐):文字画内存关系
③ 代码示例 code:每行中文注释 + 执行过程跟踪(必须内嵌在代码块中)
④ 逐行解剖 md:逐行解释语法和参数
⑤ 常见错误 md:学员最容易犯的错(≥2 条)
⑥ 苏格拉底引导 md:问自己(≥3 个引导问题)
⑦ 学员代码区 code:pass 占位
⑧ 参考答案 code:完整可运行代码 + 注释
```

### 4.1 执行过程跟踪格式(最关键)

执行过程跟踪必须内嵌在代码块中:

```python
password = ""
while password != "123":
    password = input("请输入密码:")
print("密码正确,欢迎!")

# --- 执行过程 ---
# 第 1 行 password = "":
#   ① 创建 password,初值空字符串
#
# 第 2 行 while password != "123":
#   ① "" != "123" → True → 进循环
```

**执行跟踪 ≠ 逐行解剖。** 执行跟踪(代码块内注释):逐步解释执行时内存/流程变化。逐行解剖(md):解释语法和参数含义。两步不能合并。

---

## 5. 常见错误格式

```markdown
> **常见错误**
> 1. **错误现象**:`TypeError: ...`
>    **原因**:忘写 self 参数
> 2. **错误现象**:`AttributeError: ...`
>    **原因**:`self.name = name` 漏写
```

每个知识点 ≥ 2 条常见错误。

---

## 6. NCDL Break It 模式(负案例驱动学习)

对于容易理解错误的知识点,故意写错代码让学员读 Traceback:

```python
# ============ BREAK IT 演示 ============
class BrokenAlipay:
    pass  # 漏写 execute 方法!

try:
    checkout(99.0, BrokenAlipay())
except AttributeError as e:
    print(f"报错: {e}")
# ============ END BREAK It ============
```

适用:所有有反模式的模块。不适用于:纯数学/概念(如反向传播推导没有"错法"给学生 break)。

---

## 7. per-Day 禁止语法清单

编写笔记或练习前,必须确认当日知识点范围,禁止使用后续才教的语法:

| Days | 已教 | 禁止 |
|---|---|---|
| Day01 | print/input/变量/类型 | def/class/循环/列表/字典 |
| Day02 | +字符串/索引/切片/f-string | def/class/循环/列表/字典 |
| Day03 | +if/elif/else | def/class/循环/列表/字典 |
| Day04 | +while/for/range | def/class/列表/字典 |
| Day05 | +def/函数 | class/列表/字典 |
| Day06 | +列表/字典 | class |
| Day07-10 | +class/OOP | 外部库 |
| Day14+ | +NumPy/Pandas | sklearn/PyTorch/HF |

**关键:** Day01 只学 print/input/变量/字符串/分支/循环,没有 def 和 class。编写任何材料前必须对照 `learning-plan.md` 确认当日知识点范围。

---

## 8. notes.md 必须含"明日衔接"段(v1.1 R3 新增)

每个 notes.md 末尾必须有一段"明日衔接"(≤3 行):

```
## 明日衔接

- 明天 Day 02 学什么:"三种声明方式的作用域差异"
- 今天遗留的概念:今天只学了"声明",还没学"作用域"
- 可以预告一个 NCDL 反模式(NCDL 节点):"var 的 hoisting 和 TDZ 误解"
```

**为什么:** 让螺旋复访从设计阶段可见,学员知道接下来要学什么,以及今天遗漏了什么。

---

## 9. 与 Lec.Python 课堂 slides 的区别

Lec.Python 产出的 slides 面向**课堂有教师场景**。Lec.Course 产出的笔记面向**自学场景**。差异:

| 维度 | Lec.Python 课堂 | Lec.Course 自学 |
|---|---|---|
| 教师讲解 | 有(教师逐行讲) | 无(笔记必须自解释) |
| 执行跟踪 | 可选 | **必须内嵌**(第 ③ 步) |
| 常见错误 | 由教师口述 | **必须写入笔记**(第 ⑤ 步) |
| 苏格拉底引导 | 不需要 | **必须写**(第 ⑥ 步),因为没有教师引导 |
| 8 步完整度 | 可能跳过 ②⑥ | **8 步必须完整** |

这意味着 Lec.Course 的自学材料信息密度必须**高于**课堂 slides —— 因为学员身边没有教师。

---

## 交叉参考

- **上游:** `04-design-assessments.md`(exercise 文件模板参考本文第 3 节)
- **上游:** `06-subject-specific-patterns.md`(NCDL / 双层覆盖 / 消费者门控的详细展开和示例)
- **下游:** QA 态 structural_check(按本文逐项校验产出格式)
- **下游:** `02-build-knowledge-dag.md` 的"per-Day 禁止语法清单"节
