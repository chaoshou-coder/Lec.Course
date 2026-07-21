### Day 12 · NumPy 进阶:矩阵运算与随机数

> **痛点**:你知道 NumPy 能做数组运算,却不知道怎么算矩阵乘法、求逆矩阵、生成随机数。今天你将解锁 NumPy 的进阶能力 —— 像数学课一样做线性代数。
> **类比**:Day 11 是"学加减法",Day 12 是"学乘除法和开方" —— 从算术升级到代数。
> **解释**:**NumPy 进阶 = 矩阵运算 + 线性代数 + 随机数 + 文件读写**。

---

#### 矩阵乘法 —— 逐元素 vs 线性代数

> **痛点**:`a * b` 和 `a @ b` 有什么区别?有时候结果完全不同。
> **类比**:逐元素乘法就像"对应座位握手",矩阵乘法就像"行乘列求和"。
> **解释**:`*` 是逐元素乘法(对应位置相乘),`@` 或 `np.dot` 是矩阵乘法(行×列)。

```python
import numpy as np

a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6],
              [7, 8]])

# 逐元素乘法(*) —— 对应位置相乘
print(a * b)
# [[ 5 12]
#  [21 32]]

# 矩阵乘法(@ 或 np.dot) —— 行乘列求和
print(a @ b)
# [[19 22]
#  [43 50]]
```

**逐行解剖**

- `a * b` = 逐元素:`[0,0]=1*5=5`, `[0,1]=2*6=12`, ...
- `a @ b` = 矩阵乘:`[0,0]=1*5+2*7=19`, `[0,1]=1*6+2*8=22`, ...
- 矩阵乘法要求:前列数 = 后行数

> **ASCII 两种乘法对比**
> ```
> 逐元素乘法(*):           矩阵乘法(@):
> [[1,2]   [[5,6]         [[1,2]   [[5,6]
>  [3,4]] × [7,8]]         [3,4]] @ [7,8]]
>    │        │               │        │
>    ▼        ▼               ▼        ▼
> [1×5, 2×6]               [1×5+2×7, 1×6+2×8]
> [3×4, 4×8]               [3×5+4×7, 3×6+4×8]
>
> 结果: [[ 5,12],          结果: [[19,22],
>        [21,32]]                 [43,50]]
> ```

**常见错误**

> 1. **错误现象**:用 `*` 做矩阵乘法,结果不对
>    **原因:**`*` 是逐元素。修正:矩阵乘法用 `@` 或 `np.dot`
> 2. **错误现象**:`matmul: Input operand mismatch`
>    **原因:**矩阵 shape 不满足前列=后行。修正:转置或调顺序

---

#### 线性代数 —— 转置、行列式、逆矩阵

> **痛点**:数学课学的转置、行列式、逆矩阵,怎么用 Python 算?
> **类比**:线性代数就像"数组的变身术" —— 转置是翻个身,逆矩阵是"反过来"。
> **解释**:`.T` 转置,`np.linalg.det` 行列式,`np.linalg.inv` 逆矩阵。

```python
import numpy as np

a = np.array([[1, 2],
              [3, 4]])

# 转置(行变列,列变行)
print(a.T)
# [[1 3]
#  [2 4]]

# 行列式(ad - bc)
det = np.linalg.det(a)
print(det)    # -2.0

# 逆矩阵(a @ a_inv = 单位矩阵)
a_inv = np.linalg.inv(a)
print(a_inv)
# [[-2.   1. ]
#  [ 1.5 -0.5]]

# 验证:a @ a_inv = 单位矩阵
print(a @ a_inv)
# [[1. 0.]
#  [0. 1.]]
```

**逐行解剖**

- `a.T` = 转置:原 `[i,j]` 变成 `[j,i]`
- `np.linalg.det(a)` = 行列式(非零则可逆)
- `np.linalg.inv(a)` = 逆矩阵(满足 `a @ a_inv = I`)
- 行列式为 0 时不可逆(奇异矩阵)

> **ASCII 转置示意图**
> ```
> 原矩阵:       转置后:
> [[1, 2],      [[1, 3],
>  [3, 4]]       [2, 4]]
>
> 第0行变成第0列,第1行变成第1列
> ```

**常见错误**

> 1. **错误现象**:`Singular matrix`
>    **原因:**行列式为 0,不可逆。修正:检查行列式
> 2. **错误现象**:忘记转置后赋值
>    **原因:**`.T` 返回新数组,原数组不变

---

#### 聚合函数与 axis 参数 —— 沿哪个方向"压"

> **痛点**:二维数组求和,是沿行还是沿列?结果完全不同。
> **类比**:axis 就像"压路机的方向" —— axis=0 沿行压(跨行),axis=1 沿列压(跨列)。
> **解释**:`axis=0` 跨行聚合(结果按列),`axis=1` 跨列聚合(结果按行)。

```python
import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

# 全部聚合
print(np.sum(a))       # 21(全部)

# axis=0:跨行(把每列的数加起来)
print(np.sum(a, axis=0))  # [5, 7, 9]

# axis=1:跨列(把每行的数加起来)
print(np.sum(a, axis=1))  # [6, 15]

# 常用聚合函数
print(np.mean(a, axis=0))  # 均值
print(np.std(a, axis=0))   # 标准差
print(np.max(a, axis=1))   # 每行最大值
print(np.min(a, axis=0))   # 每列最小值
```

**逐行解剖**

- `axis=0` = 跨行聚合,结果 shape 是 `(列数,)` —— 每列一个值
- `axis=1` = 跨列聚合,结果 shape 是 `(行数,)` —— 每行一个值
- 想象:axis 指定"消灭哪个维度"

> **ASCII axis 方向示意图**
> ```
> a = [[1, 2, 3],
>      [4, 5, 6]]
>
> axis=0(跨行,↓):     axis=1(跨列,→):
>   ↓   ↓   ↓           → → →
> [1,  2,  3]         [1, 2, 3] → 6
> [4,  5,  6]         [4, 5, 6] → 15
>   ↓   ↓   ↓
> [5,  7,  9]
> ```
> 记忆口诀:**axis=0 跨行消行,axis=1 跨列消列**

**常见错误**

> 1. **错误现象**:axis 方向搞反
>    **原因:**没理解"哪个维度被消灭"。修正:先想结果的 shape
> 2. **错误现象**:`argmax` 返回的不是二维坐标
>    **原因:**`argmax` 返回展平后的索引。修正:`np.unravel_index`

---

#### 随机数生成 —— 让数据"随机出现"

> **痛点**:你想生成随机数据测试算法,不知道怎么控制随机性。
> **类比**:随机数就像"掷骰子" —— seed 是骰子的初始状态,同样的 seed 同样的结果。
> **解释**:`np.random.seed()` 设种子,`rand`/`randn`/`randint` 生成随机数。

```python
import numpy as np

# 设种子(保证可复现)
np.random.seed(42)

# [0,1) 均匀分布
print(np.random.rand(3))      # [0.37 0.95 0.73]
print(np.random.rand(2, 3))   # 2×3 矩阵

# 标准正态分布(均值 0,标准差 1)
print(np.random.randn(4))     # [-0.23  0.45 -1.2  0.89]

# 整数随机[low, high)
print(np.random.randint(1, 10, size=5))  # [7, 3, 5, 8, 1]

# 随机选择
fruits = np.array(["苹果", "香蕉", "橘子"])
print(np.random.choice(fruits, size=3))   # 随机选 3 个
```

**逐行解剖**

- `np.random.seed(42)` = 设种子,保证每次运行结果一样
- `np.random.rand(2,3)` = 生成 2×3 的 [0,1) 均匀分布
- `np.random.randn(4)` = 标准正态分布(钟形曲线)
- `np.random.randint(1,10, size=5)` = [1,10) 的 5 个整数
- `np.random.choice(arr, size=3)` = 从 arr 中随机选 3 个

> **ASCII 随机数分布示意图**
> ```
> rand(均匀分布):       randn(正态分布):
> ┌────────────┐        ┌───┐
> │############│        │ # │
> │############│        │###│
> │############│        #####│
> └────────────┘        └─────┘
>  [0,1) 均匀钟形集中在 0
> ```

**常见错误**

> 1. **错误现象**:每次运行结果都不同
>    **原因:**没设 seed。修正:开头加 `np.random.seed(42)`
> 2. **错误现象**:`randint(1, 10)` 以为含 10
>    **原因:**randint 左闭右开 `[low, high)`。修正:要含 10 写 `randint(1, 11)`

---

#### 文件读写 —— 数组的"存档"

> **痛点**:计算好的数组,下次运行还要重算。
> **类比**:np.save 就像"游戏存档" —— 保存进度,下次直接读档。
> **解释**:`np.save` / `np.load` 存二进制,`np.savetxt` / `np.loadtxt` 存文本。

```python
import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

# 保存为二进制(.npy 格式,保留 shape 和 dtype)
np.save("my_array.npy", a)

# 加载
b = np.load("my_array.npy")
print(b.shape)    # (2, 3)

# 保存为文本(.txt / .csv)
np.savetxt("my_array.txt", a, fmt="%d", delimiter=",")

# 加载文本
c = np.loadtxt("my_array.txt", delimiter=",")
print(c)
# [[1. 2. 3.]
#  [4. 5. 6.]]
```

**逐行解剖**

- `np.save("my_array.npy", a)` = 保存为 .npy 二进制文件
- `np.load("my_array.npy")` = 加载,完整恢复 shape 和 dtype
- `np.savetxt(file, a, fmt="%d", delimiter=",")` = 保存为 CSV 风格文本
- `np.loadtxt(file, delimiter=",")` = 加载文本,默认 float

> **ASCII 文件读写对比**
> ```
> .npy 二进制:              .txt 文本:
>   ┌───────┐                ┌───────────┐
>   │二进制流│                │1,2,3      │
>   │快/保真│                │4,5,6      │
>   │跨平台 │                │慢/可读    │
>   └───────┘                └───────────┘
> ```

**常见错误**

> 1. **错误现象**:`file could not be found`
>    **原因:**路径错误。修正:检查文件路径
> 2. **错误现象**:savetxt 精度丢失
>    **原因:**fmt 默认精度不够。修正:`fmt="%.4f"`

---

#### 苏格拉底引导

1. `a * b` 和 `a @ b` 分别在什么场景下使用?
2. 矩阵不可逆(奇异)时,`np.linalg.inv` 会怎样?怎么提前判断?
3. `axis=0` 和 `axis=1` 怎么记忆?有什么技巧?
4. 为什么要设随机种子?什么时候该设,什么时候不该设?
5. `.npy` 和 `.txt` 各有什么优缺点?什么时候用哪个?

---

#### 学员代码区

在 VS Code 新建 `day12.py`,补全下面的代码:

```python
import numpy as np

# TODO: 创建矩阵 a = [[1,2],[3,4]], b = [[5,6],[7,8]]
a =
b =

# TODO: 矩阵乘法 a @ b
product =

# TODO: a 的转置
transpose =

# TODO: a 的行列式
det =

# TODO: a 沿 axis=0 求和
sum_axis0 =

# TODO: 设种子 0,生成 5 个 [0,1) 均匀分布随机数
rand_nums =
```

---

#### 参考答案

```python
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
product = a @ b
transpose = a.T
det = np.linalg.det(a)
sum_axis0 = np.sum(a, axis=0)

np.random.seed(0)
rand_nums = np.random.rand(5)
```

---

## 明日衔接

- 明天 Day 13 学什么:**Pandas 基础**(Series/DataFrame/CSV)
- 今天遗留的概念:今天学了 NumPy 进阶,还没学表格数据处理
- NCDL 预告:Day 13 用 NCDL 教学法,展示"用循环遍历 DataFrame"反模式
