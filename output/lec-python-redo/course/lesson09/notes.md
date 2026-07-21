### Day 09 · 模块与高级:Python 的"大招"

> **痛点**:你的代码全在一个文件里,上万行,改一处怕牵全身。今天你将学会拆分成模块、用生成器省内存、用装饰器增强函数 —— 真正高手技能。
> **类比**:模块像"工具箱" —— 把工具分类放,用时取;装饰器像"给手机套壳" —— 不改变手机,但增加功能;生成器像"自助餐" —— 吃多少拿多少,不浪费。
> **解释**:**模块 = 代码组织;生成器 = 惰性计算;装饰器 = 增强函数;上下文管理器 = 资源管理**。

---

#### 三种 import —— 三种"借工具"方式

> **痛点**:你想用其他文件里的函数,不知道怎么导入。
> **类比**:import 像"借工具" —— 可以借整个工具箱、只借一把锤子、或给锤子起个别名。
> **解释**:`import 模块`、`from 模块 import 函数`、`import 模块 as 别名`。

```python
# 方式1:import 模块(模块名.函数名)
import math
print(math.sqrt(16))           # 4.0

# 方式2:from 模块 import 函数(直接用函数名)
from math import sqrt, pi
print(sqrt(16))                # 4.0
print(pi)                      # 3.14159...

# 方式3:as 别名(给模块/函数起短名)
import numpy as np             # 起别名 np
from math import sqrt as my_sqrt
print(my_sqrt(16))             # 4.0

# 不推荐:from 模块 import * (导入所有,名字冲突)
# from math import *           # 污染命名空间
```

**逐行解剖**

- `import math` = 导入整个 math 模块,用 `math.xxx` 访问
- `from math import sqrt` = 只导入 sqrt,直接用(简洁)
- `import numpy as np` = 起别名(约定俗成:np/pd/plt)
- `import *` = 导入所有,容易名字冲突(不推荐!)

> **ASCII 三种 import 图**
> ```
> import math       → math.sqrt(16)     (模块名.函数)
> from math import → sqrt(16)           (直接用)
> import np as     → np.array([1,2])   (别名)
> ```

**常见错误**

> 1. **错误现象**:循环导入(A import B, B import A)
>    **原因:**模块互相导入。修正:重构代码,提取公共模块
> 2. **错误现象**:`from math import sqrt` 后用 `math.pi`
>    **原因:**只导入 sqrt,math 模块没导入。修正:`import math`

---

#### 自定义模块与包 —— 代码的"货架"

> **痛点**:你想把电商订单系统的代码拆成多个文件,方便维护。
> **比喻**:模块是"一个 .py 文件";包是"一个文件夹"(里面多个模块)。
> **解释**:同目录 import;包 = 文件夹 + __init__.py。

```python
# 项目结构:
# lec_shop/
# ├── __init__.py         # 包的标识(可以为空)
# ├── order.py            # Order 类
# ├── vip_order.py        # VipOrder 类
# └── utils.py            # 工具函数

# order.py
class Order:
    def __init__(self, oid, product, price):
        self.oid = oid
        self.product = product
        self.price = price

# utils.py
def format_price(price):
    return f"￥{price:.2f}"

# main.py(使用自定义模块)
from order import Order
from utils import format_price

order = Order("A001", "书", 59.9)
print(format_price(order.price))    # ￥59.90
```

**逐行解剖**

- `order.py` = 一个模块,里面定义 Order 类
- `from order import Order` = 从 order 模块导入 Order 类
- `__init__.py` = 标记文件夹为包(可以为空)
- 同目录的 .py 文件可以直接 import

> **ASCII 模块与包结构图**
> ```
# lec_shop/                  ← 包(文件夹)
# ├── __init__.py            ← 包标识
# ├── order.py               ← 模块(文件)
# ├── vip_order.py           ← 模块
# └── utils.py               ← 模块
#
# from order import Order    ← 导入模块里的类
# ```

**常见错误**

> 1. **错误现象**:`ModuleNotFoundError: No module named 'xxx'`
>    **原因:**模块不在搜索路径。修正:同目录或加 sys.path
> 2. **错误现象**:包没有 __init__.py(Python 3.3 之前)
>    **原因:**旧版本需要 __init__.py。修正:加空 __init__.py

---

#### 生成器 yield —— "自助餐"式计算

> **痛点**:你想生成 100 万个数,列表太占内存。
> **比喻**:生成器像"自助餐" —— 吃一个拿一个,不一次性摆满桌;列表像"套餐" —— 一次性全端上来。
> **解释**:`yield` 返回一个值并暂停,下次从暂停处继续,惰性计算。

```python
# 列表(一次性全部生成,占内存)
def make_list(n):
    return [i * i for i in range(n)]

# 生成器(惰性计算,省内存)
def gen_squares(n):
    for i in range(n):
        yield i * i            # 产生一个值,暂停

# 使用生成器
gen = gen_squares(5)
print(next(gen))               # 0(第一个)
print(next(gen))               # 1(第二个)
print(next(gen))               # 4(第三个)

# 生成器也可以用 for 遍历
for sq in gen_squares(5):
    print(sq)                  # 0 1 4 9 16

# 生成器表达式(类似列表推导,但用圆括号)
gen = (i * i for i in range(5))
print(list(gen))               # [0, 1, 4, 9, 16]
```

**逐行解剖**

- `yield i * i` = 产生值并暂停,下次从 yield 后继续
- `next(gen)` = 取下一个值,没有则 StopIteration
- 生成器只能用一次,用完就没了
- 生成器节省大数据内存(按需计算!)

> **ASCII 生成器执行图**
> ```
> gen = gen_squares(3)
>
> next(gen) → yield 0 → 暂停 → 返回 0
> next(gen) → yield 1 → 暂停 → 返回 1
> next(gen) → yield 4 → 暂停 → 返回 4
> next(gen) → 无值 → StopIteration
> ```

**常见错误**

> 1. **错误现象**:生成器用完后再遍历没结果
>    **原因:**生成器只能用一次。修正:重新创建
> 2. **错误现象**:`return` 和 `yield` 混淆
>    **原因:**return 结束函数,yield 暂停并返回值

---

#### yield from —— 生成器的"快捷方式"

> **痛点**:生成器里要遍历另一个序列,写 for 循环麻烦。
> **比喻**:yield from 像"中转站" —— 把另一个生成器的值直接转发过来。
> **解释**:`yield from 可迭代对象` 等价于遍历并 yield 每个元素。

```python
# 不用 yield from(手写 for)
def gen_manual():
    for x in range(3):
        yield x
    for x in "abc":
        yield x

# 用 yield from(简洁)
def gen_yield_from():
    yield from range(3)        # 等价于 for x in range(3): yield x
    yield from "abc"           # 等价于 for x in "abc": yield x

print(list(gen_yield_from()))  # [0, 1, 2, 'a', 'b', 'c']

# yield from 用于扁平化嵌套
def flatten(nested):
    for sublist in nested:
        yield from sublist     # 转发子列表的每个元素

nested = [[1, 2], [3, 4], [5]]
print(list(flatten(nested)))   # [1, 2, 3, 4, 5]
```

**逐行解剖**

- `yield from range(3)` = 等价于 `for x in range(3): yield x`
- `yield from` 可以简化生成器委托
- 适合合并多个可迭代对象或扁平化

> **ASCII yield from 图**
> ```
> for x in range(3):    yield from range(3)
>     yield x       ≡   直接转发每个元素
>
> 嵌套列表 [[1,2],[3]]
>    │
>    ▼ yield from
> 扁平化 [1, 2, 3]
> ```

**常见错误**

> 1. **错误现象**:`yield from` 后面跟非可迭代对象
>    **原因:**`yield from` 需要可迭代对象。修正:`yield` 单个值
> 2. **错误现象**:忘记 `from`,只写 `yield`
>    **原因:**`yield range(3)` 返回的是 range 对象,不是值

---

#### 上下文管理器 __enter__/__exit__ —— 自定义"自动门"

> **痛点**:你想让任意对象支持 with 语句(自动管理资源)。
> **比喻**:上下文管理器像"自动门" —— 进门自动开,出门自动关。
> **解释**:实现 `__enter__` 和 `__exit__`,对象就可以用 with。

```python
# 自定义上下文管理器
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        """进入 with 时调用,返回值赋给 as 后的变量"""
        self.file = open(self.filename, self.mode, encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """离开 with 时调用,即使出错也执行"""
        self.file.close()
        return False             # False = 不抑制异常

# 使用
with FileManager("test.txt", "w") as f:
    f.write("Hello")
# 自动关闭,不需要 f.close()
```

**逐行解剖**

- `__enter__` = 进入 with 时返回资源(赋值给 as 后的变量)
- `__exit__` = 离开 with 时清理资源(即使异常也执行)
- `exc_type/exc_val/exc_tb` = 异常信息(没有异常则为 None)
- `return False` = 不抑制异常(让异常继续传播)

> **ASCII 上下文管理器图**
> ```
> with FileManager("f.txt") as f:
>     f.write("Hello")      ← __enter__ 返回 f
>                           ← __exit__ 自动关闭
>
> 即使 f.write() 出错,__exit__ 也执行 ✓
> ```

**常见错误**

> 1. **错误现象**:`__enter__` 忘了 return
>    **原因:**as 后的变量是 None。修正:`return self.file`
> 2. **错误现象**:`__exit__` 返回 True 隐藏了异常
>    **原因:**True 表示抑制异常。修正:通常返回 False

---

#### 装饰器 —— 函数的"增强器"

> **痛点**:你想给函数加日志/计时功能,不想修改原函数。
> **比喻**:装饰器像"给手机壳" —— 不改变手机,但增加保护;`@decorator` 是语法糖。
> **解释**:装饰器是接收函数、返回新函数的高阶函数。

```python
import time

# 定义装饰器
def timer(func):
    """计时的装饰器"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)    # 调用原函数
        print(f"{func.__name__} 耗时 {time.time()-start:.3f}s")
        return result
    return wrapper

# 使用装饰器(语法糖)
@timer
def slow_function():
    time.sleep(0.1)
    return "done"

result = slow_function()
# 输出:slow_function 耗时 0.101s
```

**逐行解剖**

- `def timer(func):` = 装饰器函数,接收原函数
- `def wrapper(...):` = 包装函数,加额外逻辑
- `func(*args, **kwargs)` = 调用原函数
- `@timer` = 语法糖,等价于 `slow_function = timer(slow_function)`

> **ASCII 装饰器原理图**
> ```
> @timer
> def slow_function():   等价于
>     ...
>
> slow_function = timer(slow_function)
>                        │
>                        ▼
>                 返回 wrapper 函数
>
> 调用 slow_function() 实际调用 wrapper()
>    ├── 计时开始
>    ├── func() = 原函数
>    └── 计时结束
> ```

**常见错误**

> 1. **错误现象**:装饰器返回了 wrapper 但没调用原函数
>    **原因:**忘了 `func(*args, **kwargs)`。修正:调用并返回
> 2. **错误现象**:装饰后函数名变成 wrapper
>    **原因:**没加 @functools.wraps。修正:见下文

---

#### functools.wraps —— 保留函数"身份证"

> **痛点**:装饰后,函数名变成 wrapper,文档字符串丢失。
> **比喻**:@wraps 像"保留身份证" —— 穿了新衣服,但身份证还是本人。
> **解释**:`@functools.wraps(func)` 把原函数的名字/文档复制给 wrapper。

```python
import functools

def my_decorator(func):
    @functools.wraps(func)          # 保留原函数的元信息
    def wrapper(*args, **kwargs):
        """wrapper 的文档"""
        print(f"调用 {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """打招呼"""
    return f"你好, {name}"

# 没 @wraps:wrapper / wrapper 的文档
# 有 @wraps:greet / 打招呼
print(greet.__name__)              # greet(不是 wrapper!)
print(greet.__doc__)               # 打招呼
```

**逐行解剖**

- `@functools.wraps(func)` = 把 func 的 `__name__`/`__doc__` 复制给 wrapper
- 装饰器内加 `@wraps` 是良好实践
- 不加 wraps 会导致调试困难(函数名全变成 wrapper)

> **ASCII @wraps 效果图**
> ```
> 没 @wraps:
> greet.__name__ = "wrapper"  ← 名字丢了!
> greet.__doc__  = "wrapper 的文档"
>
> 有 @wraps:
> greet.__name__ = "greet"    ← 保留原名
> greet.__doc__  = "打招呼"   ← 保留原文档
> ```

**常见错误**

> 1. **错误现象**:装饰器忘了加 @wraps
>    **原因:**调试时函数名全 wrapper,分不清。修正:始终加
> 2. **错误现象**:wrapper 的文档覆盖了原函数
>    **原因:**@wraps 把原函数文档复制过来。修正:不写 wrapper.__doc__

---

#### 执行过程跟踪

```python
# --- 执行过程 ---

# import math
#   ① 查找 math 模块(sys.path)
#   ② 加载并执行模块代码
#   ③ 创建模块对象,赋值给 math

# from math import sqrt
#   ① 加载 math 模块
#   ② 从模块取出 sqrt
#   ③ 赋值给当前命名空间的 sqrt

# def gen_squares(n):
#     for i in range(n):
#         yield i * i
#   ① 定义生成器函数
#   ② gen = gen_squares(5) → 创建生成器对象(不执行)
#   ③ next(gen) → 执行到 yield,返回 0,暂停
#   ④ next(gen) → 从 yield 后继续,返回 1,暂停

# @timer
# def slow_function(): ...
#   ① 等价于 slow_function = timer(slow_function)
#   ② timer 返回 wrapper 函数
#   ③ 调用 slow_function() = 调用 wrapper()
```

---

#### 常见错误汇总

> 1. **错误现象**:`ModuleNotFoundError`
>    **原因:**模块不存在或路径不对。修正:检查文件名/路径
> 2. **错误现象**:`StopIteration`(生成器用完)
>    **原因:**next() 取完了。修正:for 循环自动处理
> 3. **错误现象**:装饰器导致函数名混乱
>    **原因:**没加 @functools.wraps。修正:始终加
> 4. **错误现象**:`yield` 在普通函数外使用
>    **原因:**`yield` 只能在函数内。修正:定义函数

---

#### 学员代码区

在 VS Code 新建 `day09.py`,补全下面的代码:

```python
# TODO: 定义 timer 装饰器,打印函数执行时间
import time


# TODO: 用 @timer 装饰 slow_function
def slow_function():
    time.sleep(0.1)
    return "done"

# TODO: 定义一个生成器 gen_fib(n),生成前 n 个斐波那契数


# TODO: 定义上下文管理器 Database,进入时打印"连接数据库",
# 退出时打印"关闭数据库",使用 with 测试

```

---

#### 参考答案

```python
import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} 耗时 {time.time()-start:.3f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(0.1)
    return "done"

def gen_fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

class Database:
    def __enter__(self):
        print("连接数据库")
        return self
    def __exit__(self, *args):
        print("关闭数据库")

with Database() as db:
    print("查询数据")
```

---

## 明日衔接

- 明天 Day 10 学什么:**进阶主题**(迭代器/推导式/常用标准库实战)
- 今天遗留的概念:今天学了模块和高级特性,还没学如何在真实项目中应用
- 脚手架递进预告:Day 10 综合 Day 1-9 知识,完成一个电商订单系统的完整项目
