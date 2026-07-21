### Day 13 · 阶段复习与 NumPy/Pandas 入门

> **叙事锚点**:电商订单系统 —— 从购物车项目到数据分析入门

今天完成两件大事:用**购物车项目**把 Day01-12
的全部语法焊接成一个完整系统,再用 **NumPy/Pandas**
打开数据分析的大门。

---

**本课知识地图**

| 知识点 | 解决什么问题 |
| --- | --- |
| 购物车项目综合 | 把 12 天语法焊成一个真实控制台应用 |
| NumPy 数组 | Python 列表数值运算慢,需要 C 级向量化 |
| NumPy 广播 | 不同形状数组也能直接运算 |
| Pandas Series | 带索引的一维数据(像 Excel 一列) |
| Pandas DataFrame | 带标签的二维表格(像 Excel 一整页) |
| Pandas 选择 loc/iloc | 按标签或位置精确选取数据 |

---

## 阶段复习:购物车项目

把 Day01-12 全部语法焊接成一个完整的控制台项目。

**功能 checklist**:
- 商品列表(字典 + 列表)
- 菜单循环 `while True` + `break`
- 同商品数量累加
- 结算 + 总价(`累加器在循环外`)
- `try/except` 异常加固
- JSON 持久化:`save_cart()` / `load_cart()`
- OOP 版:`Product` 类 + `Cart` 类

#### 购物车项目综合 —— 从 dict 到完整系统

> **痛点**

学了 12 天语法,每个点都练过,但从没把它们
**组合**成一个真实项目,遇到综合场景就无从下手。

> **类比**

每个语法是一块积木,之前只练习了单块的形状,
今天要拼出一辆完整的车。

> **解释**

项目 = 数据(列表/字典) + 函数(封装逻辑)
+ 异常(健壮性) + 文件(持久化) + OOP(架构)。
购物车是最佳的"最小完整业务系统"。

**ASCII 内存图 —— 购物车的模块关系**

```
main() 调度
  │
  ├── browse_products()  ──→ products 列表
  ├── add_to_cart()      ──→ cart 列表
  ├── view_cart()        ──→ 累加器 total
  └── checkout()         ──→ cart.clear()
        │
  ┌─────┴──────┐
  │ JSON 持久化 │
  │ save_cart() │ ──→ cart.json
  │ load_cart() │ ←── cart.json
  └────────────┘

数据结构:
  products = [{"id": 1, "name": "苹果", "price": 5.5}, ...]
  cart = [{"id": 1, "name": "苹果", "price": 5.5, "qty": 2}, ...]
```

**关键**:累加器在循环外初始化,json 统一 utf-8 编码。

```python
# 示例 1:购物车整合版 —— 产品类 + 购物车类
import json
import os


class Product:
    """商品类:封装商品的基本信息和显示"""
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.pid}. {self.name}  ￥{self.price:.2f}"


class Cart:
    """购物车类:管理商品条目、计算总价、结算"""
    def __init__(self):
        self.items = []  # 每项: {"product": Product, "qty": int}

    def add(self, product, qty=1):
        # 已在购物车 → 数量 +qty
        for item in self.items:
            if item["product"].pid == product.pid:
                item["qty"] += qty
                return
        self.items.append({"product": product, "qty": qty})

    def total(self):
        t = 0  # 累加器在循环外!
        for item in self.items:
            t += item["product"].price * item["qty"]
        return t

    def view(self):
        if not self.items:
            print("购物车为空")
            return
        for item in self.items:
            sub = item["product"].price * item["qty"]
            print(f"  {item['product'].name} x{item['qty']} = ￥{sub:.2f}")
        print(f"总价: ￥{self.total():.2f}")

    def checkout(self):
        self.view()
        self.items.clear()
        print("已结算,购物车清空")

    def save(self, path="_cart.json"):
        # 把 items 转成可序列化的字典列表
        data = [{"id": i["product"].pid,
                 "name": i["product"].name,
                 "price": i["product"].price,
                 "qty": i["qty"]} for i in self.items]
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load(self, path="_cart.json"):
        if not os.path.exists(path):
            return
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        # 重建 items(简化:product 用基本属性重建)
        self.items = []
        for d in data:
            p = Product(d["id"], d["name"], d["price"])
            self.items.append({"product": p, "qty": d["qty"]})


# 使用演示
products = [Product(1, "苹果", 5.50), Product(2, "香蕉", 3.20)]
cart = Cart()
cart.add(products[0])
cart.add(products[0])  # 数量 +1
cart.add(products[1])
cart.view()
# 已结算会清空,这里先只看
```

**逐行解剖**

① `Product` 类封装商品信息,`__str__` 定义打印格式
② `Cart` 类把数据和行为绑定 —— add/view/total/checkout
③ `total()` 累加器在循环外初始化,循环内只累加
④ `save()` 把对象序列化为字典列表,再用 json.dump 写入
⑤ `load()` 读回 JSON,重建 Product 和 items
⑥ `add()` 自动判断:已有商品加数量,没有则新增

**常见错误**

> 1. **错误现象**:总价只显示最后一项
>    **原因**:累加器 `total = 0` 写在循环内,每次被清零
> 2. **错误现象**:中文 JSON 文件打开后是乱码 `苹`
>    **原因**:json.dump 没写 `ensure_ascii=False`
> 3. **错误现象**:程序重启后购物车数据丢失
>    **原因**:忘记调用 save(),或 load() 没在启动时调用

> **问自己**:
> - 为什么 Cart 类比用全局变量 + 函数的方式更好?
> - 购物车用列表而不是字典存储条目,合理吗?
> - 如果加"会员折扣"功能,应该改哪个类?

```python
# ======================
# 学员代码区
# ======================
# 请在 Cart 类中新增 apply_discount(rate) 方法,
# 把所有商品 price 乘以 rate (0~1 之间的小数),
# 打印折扣后总价。注意:不修改 product 原价,
# 只影响总价计算。
pass

# ======================
# 参考答案
# ======================
# class Cart:
#     ... 其他方法不变 ...
#     def apply_discount(self, rate):
#         # 返回折扣后的总价,不修改原价
#         t = 0
#         for item in self.items:
#             t += item["product"].price * item["qty"]
#         discounted = t * rate
#         print(f"原价: ￥{t:.2f}, 折后: ￥{discounted:.2f}")
#         return discounted
```

---

## NumPy/Pandas 入门

从今天起进入数据分析的世界。NumPy 是底层引擎,
Pandas 是上层数据分析工具。

#### NumPy 数组 —— 列表是"杂货铺",数组是"集装箱"

> **痛点**

Python 列表做百万次数值运算非常慢:
每个元素都要类型检查 + 逐个解包。

> **类比**

列表是"杂货铺"(什么都能放,陈列散乱),
数组是"集装箱"(同一种货,紧密排列)。

> **解释**

NumPy 数组是**同类型数据**的连续内存块,
底层用 C 实现,省掉类型检查开销,
向量化运算快 10-100 倍。

**ASCII 内存图 —— 列表 vs 数组**

```
列表 list:
  [ 指针1 → 对象1(类型+值) ]
  [ 指针2 → 对象2(类型+值) ]  ← 每个元素都带类型信息
  [ 指针3 → 对象3(类型+值) ]

NumPy 数组 ndarray:
  [ 1 | 2 | 3 | 4 | 5 ]  ← 同类型,连续内存,无额外开销
   共享 dtype = int64
```

**关键**:数组所有元素共享一个 dtype,强制统一类型。

```python
# 示例 1:数组创建与基本属性
import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a)          # [1 2 3 4 5]
print(a.dtype)    # int64 ← 所有元素共享的类型
print(a.shape)    # (5,)  ← 一维,长度 5
print(a.ndim)     # 1     ← 维度数

b = np.array([[1, 2], [3, 4], [5, 6]])
print(b.shape)    # (3, 2) ← 3 行 2 列
print(b.ndim)     # 2
```

**逐行解剖**

① `np.array([1, 2, 3, 4, 5])` 从列表创建数组
② `a.dtype` 返回数组元素的数据类型,所有元素共享
③ `a.shape` 返回数组的形状(每个维度的长度)
④ `a.ndim` 返回维度数(几维数组)

```python
# 示例 2:常用创建函数
import numpy as np

print(np.zeros((2, 3)))       # 2×3 全 0
print(np.ones((3, 2)))        # 3×2 全 1
print(np.arange(0, 10, 2))    # [0 2 4 6 8]
print(np.linspace(0, 1, 5))   # [0. 0.25 0.5 0.75 1.]
```

**常见错误**

> 1. **错误现象**:`TypeError: data type not understood`
>    **原因**:`np.zeros(2, 3)` 漏写元组括号。修正:`np.zeros((2, 3))`
> 2. **错误现象**:数组全部变成字符串
>    **原因**:混合数字和字符串,如 `np.array([1, "a", 3])`,强制统一为字符串

> **问自己**:
> - 为什么做数值计算时数组比列表快?
> - `np.array([1, 2.5, 3])` 的 dtype 是什么?
> - zeros 和 ones 的形状参数为什么要传元组?

```python
# ======================
# 学员代码区
# =====================
import numpy as np

# 1. 用 np.arange 创建 0~9 的一维数组
# 2. reshape 为 2×5 的二维数组
# 3. 打印它的 shape 和 dtype
pass

# ======================
# 参考答案
# ======================
# import numpy as np
# a = np.arange(10)
# b = a.reshape(2, 5)
# print(b.shape)   # (2, 5)
# print(b.dtype)   # int64
```

---

#### NumPy 广播 —— 不同形状也能算

> **痛点**

两个数组形状不同就直接运算,新手以为一定报错。

> **类比**

广播就像复印机把小图放大到和大图一样,
再叠在一起相加 —— 但只能放大"长度为 1"
或"缺失"的维度。

> **解释**

广播规则:从**最后一个维度**开始对齐,
要么相等,要么其中一方是 1,要么一方缺失。

**ASCII 内存图 —— 广播的本质**

```
a = shape (2, 3)     b = shape (3,)
[[1 2 3]             [10 20 30]
 [4 5 6]]

b 被"拉伸"成 (2, 3):
[[1 2 3]   [[10 20 30]     [[11 22 33]
 [4 5 6]] +  [10 20 30]]  =  [14 25 36]]
```

**关键**:只能补长度为 1 或缺失的维度,
(2, 3) 和 (2,) 不能广播。

```python
# 示例 1:数组与标量的广播
import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a + 10)             # [11 12 13 14 15]
print(a * 2)              # [2 4 6 8 10]
```

**逐行解剖**

① `a + 10` 标量 10 被广播到数组每个元素
② `a * 2` 同理,每个元素乘以 2

```python
# 示例 2:不同形状数组的广播
a = np.array([[1, 2, 3],
              [4, 5, 6]])   # shape (2, 3)
b = np.array([10, 20, 30])   # shape (3,)

print(a + b)
# [[11 22 33]
 # [14 25 36]]
```

```python
# 示例 3:常用索引与切片
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print(a[0])               # [1 2 3] ← 第 0 行
print(a[:, 1])            # [2 5 8] ← 第 1 列
print(a[a > 5])           # [6 7 8 9] ← 布尔索引
```

**常见错误**

> 1. **错误现象**:`ValueError: operands could not be broadcast`
>    **原因**:形状不满足广播规则,如 (2, 3) 和 (2,)
> 2. **错误现象**:忘记 `keepdims=True` 导致形状不匹配
>    **原因**:`arr.min(axis=1)` 返回 (2,),不是 (2, 1)

> **问自己**:
> - (3, 4) 和 (4,) 能广播吗?结果形状是什么?
> - (3, 4) 和 (3,) 能广播吗?
> - 布尔索引返回的结果是几维的?

```python
# ======================
# 学员代码区
# =====================
import numpy as np

# 1. 创建形状 (3, 3) 的数组,值 1~9
# 2. 用布尔索引取出所有偶数
# 3. 计算每一行的和(axis=1)
pass

# ======================
# 参考答案
# ======================
# import numpy as np
# a = np.arange(1, 10).reshape(3, 3)
# print(a[a % 2 == 0])       # [2 4 6 8]
# print(a.sum(axis=1))       # [ 6 15 24]
```

---

#### Pandas Series —— 带索引的一维数组

> **痛点**

NumPy 数组只能用数字下标访问,
现实数据有"姓名""年龄"等标签,需要更灵活的索引。

> **类比**

Series 就像 Excel 的"一列" —— 有值,有标签(index)。

> **解释**

Series = 一维数据 + 索引(index)。
可以用标签访问,也可以用位置访问。

**ASCII 内存图 —— Series 的结构**

```
Series: [10, 20, 30, 40]
index:  [ a,  b,  c,  d]

内部:
  values: [10, 20, 30, 40]  ← NumPy 数组
  index:  [a, b, c, d]       ← 标签

s["b"] → 20  (标签访问)
s[1]   → 20  (位置访问)
```

**关键**:Series 是带标签的一维数组,由 NumPy 数组支撑。

```python
# 示例 1:创建 Series
import pandas as pd

s = pd.Series([10, 20, 30, 40])
print(s)
# 0    10
# 1    20
# 2    30
# 3    40

# 自定义索引
s2 = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s2["b"])            # 20 ← 用标签访问
```

**逐行解剖**

① `pd.Series([10, 20, 30, 40])` 自动分配 0-based 索引
② `s2 = pd.Series(..., index=["a","b","c"])` 自定义标签
③ `s2["b"]` 按标签取值,返回 20

```python
# 示例 2:Series 的常用操作
s = pd.Series([85, 92, 78], index=["张三", "李四", "王五"])
print(s.mean())           # 85.0 ← 可直接调用统计函数
print(s.max())            # 92
print(s[s > 80])          # 按条件筛选
```

**常见错误**

> 1. **错误现象**:索引重复时取值返回 Series 而不是单个值
>    **原因**:标签不唯一,s["key"] 返回多个匹配结果
> 2. **错误现象**:index 长度和数据长度不一致
>    **原因**:创建时 index 参数长度必须等于数据长度

> **问自己**:
> - Series 和 NumPy 一维数组最大的区别是什么?
> - 能不能用字典创建 Series?
> - Series 的 index 可以重复吗?

```python
# ======================
# 学员代码区
# =====================
import pandas as pd

# 1. 用字典 {"数学": 90, "语文": 85, "英语": 88} 创建 Series
# 2. 取出"语文"的成绩
# 3. 计算三科平均分
pass

# ======================
# 参考答案
# ======================
# s = pd.Series({"数学": 90, "语文": 85, "英语": 88})
# print(s["语文"])          # 85
# print(s.mean())           # 87.666667
```

---

#### Pandas DataFrame —— 带标签的二维表

> **痛点**

Series 只是一列数据,现实数据是多列的表格
(姓名 + 年龄 + 成绩),需要二维结构。

> **类比**

DataFrame 就像 Excel 一整页 ——
有行索引(index),有列名(columns),每个单元格有值。

> **解释**

DataFrame 是 Pandas 最核心的数据结构,
由字典创建(键 = 列名,值 = 列数据)。

**ASCII 内存图 —— DataFrame 的结构**

```
DataFrame:
        姓名   年龄   成绩
index
  0     张三   20   85.5
  1     李四   21   92.0
  2     王五   19   78.5

内部:
  columns: ["姓名", "年龄", "成绩"]
  index: [0, 1, 2]
  每列是一个 Series
```

**关键**:字典的键 = 列名,值 = 列数据(按列构建)。

```python
# 示例 1:从字典创建 DataFrame
import pandas as pd

data = {
    "姓名": ["张三", "李四", "王五"],
    "年龄": [20, 21, 19],
    "成绩": [85.5, 92.0, 78.5],
}
df = pd.DataFrame(data)
print(df)
#   姓名  年龄   成绩
# 0  张三  20  85.5
# 1  李四  21  92.0
# 2  王五  19  78.5
```

**逐行解剖**

① 字典的**键**作为列名(姓名/年龄/成绩)
② 字典的**值**作为列数据(每个列表是一列)
③ `pd.DataFrame(data)` 自动分配 0-based 行索引
④ 打印时自动对齐列,显示行号

```python
# 示例 2:基础属性与查看
print(df.shape)           # (3, 2) ← 行数,列数
print(df.columns)         # Index(['姓名', '年龄', '成绩'])
print(df.index)           # RangeIndex(0, 3)
print(df.head(2))         # 前 2 行
print(df.describe())      # 数值列的统计摘要
```

**常见错误**

> 1. **错误现象**:列名变成 0/1/2
>    **原因**:按行构建 `pd.DataFrame([["张三",20,85.5],...])`,子列表是行
> 2. **错误现象**:中文 CSV 读取报 UnicodeDecodeError
>    **原因**:编码问题,修正:`pd.read_csv("f.csv", encoding="gbk")`

> **问自己**:
> - DataFrame 按列构建和按行构建,列名分别是什么?
> - `head()` 默认显示几行?
> - `describe()` 统计了哪些指标?

```python
# ======================
# 学员代码区
# =====================
import pandas as pd

# 1. 从字典创建 DataFrame,包含 "城市" 和 "人口" 两列
# 2. 打印 shape 和 columns
# 3. 打印 describe() 查看统计摘要
pass

# ======================
# 参考答案
# ======================
# data = {"城市": ["北京", "上海", "深圳"],
#         "人口": [2189, 2487, 1768]}
# df = pd.DataFrame(data)
# print(df.shape)      # (3, 2)
# print(df.columns)    # Index(['城市', '人口'])
# print(df.describe())
```

---

#### Pandas 选择 loc/iloc —— 精确选取数据

> **痛点**

要从表格里取特定行和列,只用 `[]` 不够用,
需要更精确的选择器。

> **类比**

loc = 用"标签"找人(按姓名),
iloc = 用"座位号"找人(按第几排第几个)。

> **解释**

- `loc`:用**标签**选(切片**包含右端**)
- `iloc`:用**整数位置**选(切片**不包含右端**)

**ASCII 内存图 —— loc vs iloc**

```
DataFrame:
        A  B  C
index
  x     1  2  3
  y     4  5  6
  z     7  8  9

df.loc["x":"y", "A"]    → 标签,含右端 → x 和 y 行的 A 列
df.iloc[0:2, 0]         → 位置,不含右端 → 第 0,1 行的第 0 列

关键区别:
  loc["x":"y"] 包含 y  ← 含右端
  iloc[0:2]    不含第 2 行 ← 不含右端
```

**关键**:loc 看标签,iloc 看位置,切片右端规则相反。

```python
# 示例 1:loc vs iloc 对比
import pandas as pd

df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]},
                  index=["x", "y", "z"])

# loc:用标签选,切片含右端
print(df.loc["x"])          # x 行的所有列
print(df.loc["x":"y"])      # x 到 y(含 y)

# iloc:用位置选,切片不含右端
print(df.iloc[0])           # 第 0 行
print(df.iloc[0:2])         # 第 0,1 行(不含第 2 行)

# 同时选行和列
print(df.loc["x":"y", "A"]) # x-y 行的 A 列
print(df.iloc[0:2, 0])      # 第 0,1 行的第 0 列
```

**逐行解剖**

① `df.loc["x"]` 按标签选一行,返回 Series
② `df.loc["x":"y"]` 标签切片,**包含右端 y**
③ `df.iloc[0]` 按位置选第 0 行
④ `df.iloc[0:2]` 位置切片,**不包含第 2 行**

```python
# 示例 2:列选择
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})
print(df["A"])              # Series(单列)
print(df[["A", "B"]])       # DataFrame(多列)
```

**常见错误**

> 1. **错误现象**:`KeyError: 0`
>    **原因**:index 是字符串,`df.loc[0]` 找不到标签 0。修正:`df.iloc[0]`
> 2. **错误现象**:loc 切片结果比预期多一行
>    **原因**:loc 切片含右端,新手以为不含

> **问自己**:
> - `df["A"]` 和 `df[["A"]]` 返回的类型一样吗?
> - 什么时候用 loc,什么时候用 iloc?
> - 列名是数字时,loc 和 iloc 会混淆吗?

```python
# ======================
# 学员代码区
# =====================
import pandas as pd

# 创建 DataFrame:
df = pd.DataFrame({"name": ["Amy", "Bob", "Cal"],
                   "age": [25, 30, 35]},
                  index=["a", "b", "c"])

# 1. 用 loc 选取 index="b" 的 name
# 2. 用 iloc 选取第 0 到第 1 行(含第 1 行)
# 3. 用 loc 选取 "a" 到 "c" 行的 name 列
pass

# ======================
# 参考答案
# ======================
# print(df.loc["b", "name"])      # Bob
# print(df.iloc[0:2])              # Amy, Bob(不含第 2 行)
# print(df.loc["a":"c", "name"])  # Amy, Bob, Cal(含右端)
```

---

#### 练习指导

完成下面的练习,巩固今天学的知识点。

**当堂练**(必做):
- 打开 `exercises/13-阶段复习与NumPyPandas/practice01.py` —— 购物车 OOP 版
- 打开 `exercises/13-阶段复习与NumPyPandas/practice02.py` —— NumPy 数组创建
- 打开 `exercises/13-阶段复习与NumPyPandas/practice03.py` —— NumPy 广播与索引
- 打开 `exercises/13-阶段复习与NumPyPandas/practice04.py` —— Pandas Series
- 打开 `exercises/13-阶段复习与NumPyPandas/practice05.py` —— Pandas DataFrame 创建
- 打开 `exercises/13-阶段复习与NumPyPandas/practice06.py` —— loc/iloc 选择

**课后作业**(选做):
- 打开 `exercises/13-阶段复习与NumPyPandas/task01.py` —— 购物车 JSON 持久化
- 打开 `exercises/13-阶段复习与NumPyPandas/task02.py` —— NumPy 统计
- 打开 `exercises/13-阶段复习与NumPyPandas/task03.py` —— Pandas 数据分析综合

**参考答案**:在 `solutions/13-阶段复习与NumPyPandas/` 下找到对应答案。

---

#### 今日小结

| 概念 | 解决的痛点 | 关键语法 |
| --- | --- | --- |
| 购物车综合 | 12 天语法焊接成完整系统 | dict + class + json |
| NumPy 数组 | 列表数值运算慢 | np.array / shape / dtype |
| NumPy 广播 | 不同形状也能算 | 从最后一个维度对齐 |
| Pandas Series | 带索引的一维数组 | pd.Series / index |
| Pandas DataFrame | 带标签的二维表格 | pd.DataFrame(字典) |
| loc/iloc | 精确选取行列 | loc(标签) / iloc(位置) |

---

[← 上一个](../knowledge/12-模块与高级.md) | [返回目录](../README.md) | [下一个 →](../knowledge/14-oop-进阶.md)
