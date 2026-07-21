### Day 13 · Pandas 基础:表格数据的"瑞士军刀"

> **痛点**:你拿到一份 Excel 数据,用 Python 循环遍历处理,代码写到崩溃。今天你将学会 Pandas —— 用几行代码完成数据读取、筛选、统计,效率提升百倍。
> **类比**:Pandas 就像"Python 的 Excel" —— 所有拖拽、筛选、透视的操作都能用代码完成。
> **解释**:**Pandas = Python 的数据分析标准库**。今天学:Series、DataFrame、CSV 读写、数据选择。

---

#### Series —— 带索引的一维数组

> **痛点**:Python 列表能存数据,但没有"标签"查找不方便。
> **类比**:Series 就像"带编号的档案袋" —— 每个数据都有一个编号(索引),你可以用编号或位置取数据。
> **解释**:Series 是一维带索引的数组,可以看作 Excel 的一列。

```python
import pandas as pd

# 从列表创建 Series(默认索引 0,1,2,...)
s = pd.Series([10, 20, 30, 40])
print(s)
# 0    10
# 1    20
# 2    30
# 3    40
# dtype: int64

# 自定义索引
s2 = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s2)
# a    10
# b    20
# c    30

# 用索引取值
print(s2["b"])    # 20

# 从字典创建
s3 = pd.Series({"北京": 2154, "上海": 2424, "广州": 1868})
print(s3)
# 北京    2154
# 上海    2424
# 广州    1868
```

**逐行解剖**

- `pd.Series([10,20,30])` = 创建带默认索引的 Series
- `index=["a","b","c"]` = 自定义索引(标签)
- `s2["b"]` = 用标签取值
- 从字典创建时, dict 的 key 变成 index

> **ASCII Series 结构图**
> ```
> s2 = pd.Series([10, 20, 30], index=["a", "b", "c"])
>
> 索引:    a    b    c
> ┌────┬────┬────┐
> │ 10 │ 20 │ 30 │
> └────┴────┴────┘
> ```

**常见错误**

> 1. **错误现象**:`KeyError: 'xxx'`
>    **原因:**索引标签不存在。修正:`s.index` 查看可用索引
> 2. **错误现象**:忘记 import pandas
>    **原因:**Pandas 是第三方库。修正:`import pandas as pd`

---

#### DataFrame —— 二维表格

> **痛点**:Series 只能存一列,多列数据怎么存?
> **类比**:DataFrame 就像"Excel 工作表" —— 多个 Series 并排,共用同一个索引。
> **解释**:DataFrame 是二维表格,每列是一个 Series。

```python
import pandas as pd

# 从字典创建 DataFrame
data = {
    "姓名": ["Alice", "Bob", "Charlie"],
    "年龄": [25, 30, 35],
    "城市": ["北京", "上海", "广州"],
}
df = pd.DataFrame(data)
print(df)
#      姓名  年龄  城市
# 0  Alice   25  北京
# 1    Bob   30  上海
# 2 Charlie  35  广州

# 自定义行索引
df2 = pd.DataFrame(data, index=["a", "b", "c"])
print(df2)
```

**逐行解剖**

- dict 的 key = 列名,dict 的 value = 列数据
- 自动创建行索引(0,1,2)
- `index=["a","b","c"]` = 自定义行索引

> **ASCII DataFrame 结构图**
> ```
> ┌───┬────────┬──────┬──────┐
> │   │  姓名  │ 年龄 │ 城市 │
> ├───┼────────┼──────┼──────┤
> │ 0 │ Alice  │  25  │ 北京 │
> │ 1 │ Bob    │  30  │ 上海 │
> │ 2 │ Charlie│  35  │ 广州 │
> └───┴────────┴──────┴──────┘
>      ↑        ↑      ↑
>    Series   Series  Series
> ```

**常见错误**

> 1. **错误现象**:列数据长度不一致
>    **原因:**每列长度必须相同。修正:检查数据
> 2. **错误现象**:列名写错
>    **原因:**列名区分大小写。修正:`df.columns` 查看列名

---

#### 从 CSV 创建 —— 数据的"入口"

> **痛点**:数据都在 CSV 文件里,怎么读进 Pandas?
> **类比**:`pd.read_csv` 就像"打开 Excel 文件" —— 一键把表格读进内存。
> **解释**:`pd.read_csv("文件路径")` 读取 CSV,返回 DataFrame。

```python
import pandas as pd

# 读取 CSV 文件
df = pd.read_csv("students.csv")

# 常见参数
df = pd.read_csv("students.csv",
                 encoding="utf-8",    # 编码
                 sep=",",             # 分隔符
                 header=0,            # 第几行是列名
                 index_col=0,         # 第几列做索引
                 nrows=100)           # 只读前 100 行

# 保存为 CSV
df.to_csv("output.csv", index=False, encoding="utf-8")
```

**逐行解剖**

- `pd.read_csv("students.csv")` = 读取 CSV,返回 DataFrame
- `encoding="utf-8"` = 指定编码(中文常用 utf-8 或 gbk)
- `index_col=0` = 用第一列做行索引
- `df.to_csv("output.csv", index=False)` = 保存,不保存行索引

> **ASCII CSV 读写流程图**
> ```
> ┌──────────┐  read_csv   ┌──────────┐
> │ students │ ──────────▶ │ DataFrame│
> │  .csv    │             │  (内存)  │
> └──────────┘             └──────────┘
>                                │
>                          to_csv│
>                                ▼
>                          ┌──────────┐
>                          │ output   │
>                          │  .csv    │
>                          └──────────┘
> ```

**常见错误**

> 1. **错误现象**:`FileNotFoundError`
>    **原因:**文件路径错误。修正:检查路径或用绝对路径
> 2. **错误现象**:中文乱码
>    **原因:**编码不对。修正:`encoding="gbk"` 或 `"utf-8-sig"`

---

#### 基础属性 —— 数据的"体检报告"

> **痛点**:拿到一个 DataFrame,不知道它多大、什么类型。
> **类比**:DataFrame 属性就像"体检报告" —— shape 是身高体重,dtypes 是血常规。
> **解释**:`.shape` 看行列数,`.dtypes` 看列类型,`.columns` 看列名。

```python
import pandas as pd

df = pd.DataFrame({
    "姓名": ["Alice", "Bob"],
    "年龄": [25, 30],
    "成绩": [88.5, 92.0],
})

print(df.shape)      # (2, 3) —— 2 行 3 列
print(df.dtypes)
# 姓名     object
# 年龄      int64
# 成绩    float64
print(df.columns)    # Index(['姓名', '年龄', '成绩'], dtype='object')
print(df.index)      # RangeIndex(start=0, stop=2, step=1)
```

**逐行解剖**

- `.shape` = (行数, 列数)
- `.dtypes` = 每列的数据类型(object=字符串)
- `.columns` = 列名列表
- `.index` = 行索引

> **ASCII DataFrame 属性**
> ```
> df.shape = (2, 3)
>            ↑  ↑
>            │  └ 列数
>            └──── 行数
>
> df.dtypes:
>   姓名 → object(字符串)
>   年龄 → int64(整数)
>   成绩 → float64(浮点)
> ```

**常见错误**

> 1. **错误现象**:以为 shape 返回"行+列"两个独立值
>    **原因:**shape 是元组。修正:`rows, cols = df.shape`
> 2. **错误现象**:数字列变成 object 类型
>    **原因:**列中有非数字字符。修正:`df["列"] = pd.to_numeric(df["列"])`

---

#### 快速查看 —— 数据的"快照"

> **痛点**:数据太大,想看几行了解结构,print 全部打印太乱。
> **类比**:head/tail/info/describe 就像"数据快照" —— 快速了解数据全貌。
> **解释**:`head` 看前几行,`tail` 看后几行,`info` 看结构,`describe` 看统计。

```python
import pandas as pd

df = pd.DataFrame({
    "姓名": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "年龄": [25, 30, 35, 28, 22],
    "成绩": [88.5, 92.0, 78.5, 95.0, 85.0],
})

# 前 3 行
print(df.head(3))
# 后 2 行
print(df.tail(2))
# 结构信息
print(df.info())
# 统计摘要(只统计数值列)
print(df.describe())
```

**逐行解剖**

- `df.head(3)` = 看前 3 行(默认 5 行)
- `df.tail(2)` = 看后 2 行
- `df.info()` = 显示列名、非空数、类型、内存
- `df.describe()` = 数值列的统计摘要(计数/均值/标准差/最值)

> **ASCII 快速查看示意图**
> ```
> df.head(3):              df.describe():
> ┌──────────────┐         ┌─────────────────┐
> │ 前 3 行数据  │         │  count/mean/std │
> └──────────────┘         │  min/25%/50%/75%│
>                          │  max            │
> df.info():               └─────────────────┘
> ┌──────────────┐
> │ 列名/类型/空 │
> └──────────────┘
> ```

**常见错误**

> 1. **错误现象**:`describe()` 没统计字符串列
>    **原因:**describe 默认只统计数值列。修正:`describe(include="all")`
> 2. **错误现象**:head 打印不全
>    **原因:**列太多被省略。修正:`pd.set_option("display.max_columns", None)`

---

#### 列选择 —— 取出你要的列

> **痛点**:表格有 10 列,你只要 2 列,怎么取?
> **类比**:列选择就像"从档案柜里抽出几个抽屉" —— 只取你需要的。
> **解释**:`df["列名"]` 取单列(返回 Series),`df[["列1","列2"]]` 取多列(返回 DataFrame)。

```python
import pandas as pd

df = pd.DataFrame({
    "姓名": ["Alice", "Bob", "Charlie"],
    "年龄": [25, 30, 35],
    "成绩": [88.5, 92.0, 78.5],
})

# 单列(返回 Series)
print(df["姓名"])
# 0    Alice
# 1      Bob
# 2  Charlie

# 多列(返回 DataFrame)
print(df[["姓名", "成绩"]])
#      姓名  成绩
# 0  Alice  88.5
# 1    Bob  92.0
# 2 Charlie 78.5
```

**逐行解剖**

- `df["姓名"]` = 取单列,返回 Series
- `df[["姓名","成绩"]]` = 取多列,注意双层括号,返回 DataFrame
- 双层括号 `[["A","B"]]` = 把列表传给 df

> **ASCII 列选择示意图**
> ```
> df["姓名"]:              df[["姓名","成绩"]]:
>   姓名                    姓名    成绩
> 0 Alice                0 Alice  88.5
> 1 Bob                  1 Bob    92.0
> 2 Charlie              2 Charlie 78.5
>    │                      │       │
>    ▼                      ▼       ▼
> Series                 DataFrame
> ```

**常见错误**

> 1. **错误现象**:`df["姓名","成绩"]` 报错
>    **原因:**多列要传列表。修正:`df[["姓名","成绩"]]`
> 2. **错误现象**:`KeyError: "xxx"`
>    **原因:**列名不存在。修正:`df.columns` 查看列名

---

#### 行选择 —— loc 标签 vs iloc 整数位置

> **痛点**:你想取第 2 行,或者取索引为 "a" 的行,怎么写?
> **类比**:loc 就像"按名字找人",iloc 就像"按座位号找人"。
> **解释**:`loc` 用标签(索引名),`iloc` 用整数位置(0,1,2,...)。

```python
import pandas as pd

df = pd.DataFrame({
    "姓名": ["Alice", "Bob", "Charlie"],
    "年龄": [25, 30, 35],
}, index=["a", "b", "c"])

# loc:按标签(索引名)
print(df.loc["b"])
# 姓名    Bob
# 年龄     30

print(df.loc["a":"b"])  # 切片(含末尾!)
#      姓名  年龄
# a  Alice   25
# b    Bob   30

# iloc:按整数位置(0,1,2)
print(df.iloc[1])
# 姓名    Bob
# 年龄     30

print(df.iloc[0:2])  # 切片(不含末尾!)
#      姓名  年龄
# a  Alice   25
# b    Bob   30

# 同时选行和列
print(df.loc["a":"b", "姓名"])     # 行切片 + 列
print(df.iloc[0:2, 0])             # 行切片 + 列位置
```

**逐行解剖**

- `df.loc["b"]` = 取索引为 "b" 的行
- `df.loc["a":"b"]` = 标签切片,含末尾(和 iloc 不同!)
- `df.iloc[1]` = 取第 2 行(整数位置)
- `df.iloc[0:2]` = 整数切片,不含末尾
- `df.loc[行, 列]` = 同时选行和列

> **ASCII loc vs iloc 对比**
> ```
> 索引:    a       b       c
> ┌─────┬─────┬─────┐
> │Alice│ Bob │Charl│
> └─────┴─────┴─────┘
> 位置:    0       1       2
>
> loc["a":"b"] → 取 a,b(含末尾)
> iloc[0:2]    → 取 0,1(不含 2)
> ```

**常见错误**

> 1. **错误现象**:loc 切片和 iloc 切片结果不同
>    **原因:**loc 含末尾,iloc 不含。修正:记住 loc 是标签切片
> 2. **错误现象**:`df["b"]` 报错
>    **原因:**`df["b"]` 是取列不是取行。修正:`df.loc["b"]`

---

#### 苏格拉底引导

1. Series 和 DataFrame 的关系是什么?DataFrame 的每列是什么?
2. `df["A"]` 和 `df[["A"]]` 返回的类型有什么区别?
3. loc 和 iloc 的切片边界有什么不同?为什么这样设计?
4. `describe()` 为什么不统计字符串列?怎么让它统计?
5. 什么时候用 loc,什么时候用 iloc?各有什么优势?

---

#### 学员代码区

在 VS Code 新建 `day13.py`,补全下面的代码:

```python
import pandas as pd

# TODO: 从字典创建 DataFrame(列:姓名/年龄/成绩,各 3 条数据)
df = pd.DataFrame({...})

# TODO: 查看前 2 行
print(df.head(...))

# TODO: 查看 DataFrame 结构信息
print(df.info())

# TODO: 取"姓名"列
print(df[...])

# TODO: 取"姓名"和"成绩"两列
print(df[[...]])

# TODO: 用 loc 取索引为 0 的行
print(df.loc[...])

# TODO: 用 iloc 取第 1 到第 2 行
print(df.iloc[...])
```

---

#### 参考答案

```python
import pandas as pd

df = pd.DataFrame({
    "姓名": ["Alice", "Bob", "Charlie"],
    "年龄": [25, 30, 35],
    "成绩": [88.5, 92.0, 78.5],
})
print(df.head(2))
print(df.info())
print(df["姓名"])
print(df[["姓名", "成绩"]])
print(df.loc[0])
print(df.iloc[0:2])
```

---

## 明日衔接

- 明天 Day 14 学什么:**Pandas 进阶**(过滤/分组/合并/缺失值)
- 今天遗留的概念:今天学了 Pandas 基础,还没学数据清洗和分组统计
- 脚手架递进预告:Day 14 在 Day 13 基础上做数据分析实战
