### Day 05 · 函数:让代码"模块化"

> **痛点**:你的代码越来越长,复制粘贴同一段逻辑到处用,改一处漏十处。今天你将学会把代码"打包"成函数 —— 写一次,用无数次。
> **类比**:函数就像"咖啡机" —— 你投入咖啡豆(参数),它给你咖啡(返回值),内部怎么运作不用管。
> **解释**:**函数 = 可重复使用的代码块**。今天学:定义、参数、返回值、作用域。

---

#### 定义与调用 —— 函数的"出生"和"使用"

> **痛点**:你想把一段常用代码"打包",以后直接调用,不知道怎么写。
> **类比**:定义函数就像"写菜谱" —— 把步骤写清楚;调用函数就像"按菜谱做菜" —— 需要时拿出来用。
> **解释**:`def` 定义函数;函数名加括号调用函数。

```python
# 定义函数
def say_hello():
    print("Hello!")
    print("欢迎来到 Python 世界")

# 调用函数
say_hello()         # 第一次调用
say_hello()         # 第二次调用(复用!)

# 定义带参数的函数
def greet(name):
    print(f"你好, {name}!")

greet("Alice")      # 你好, Alice!
greet("Bob")        # 你好, Bob!
```

**逐行解剖**

- `def say_hello():` = 定义函数,末尾冒号
- 缩进 4 格 = 函数体
- `say_hello()` = 调用函数(执行函数体)
- `def greet(name):` = name 是形参(占位符)

> **ASCII 函数调用示意图**
> ```
> 定义:                    调用:
> def say_hello():         say_hello()
>    打印 "Hello!"            │
>    打印 "欢迎来到..."        ▼
>                        执行函数体:
>                         打印 "Hello!"
>                         打印 "欢迎来到..."
>                        执行完,回到调用处
> ```

**常见错误**

> 1. **错误现象**:定义了函数但没调用,没有任何输出
>    **原因:**定义只是"写菜谱",调用才是"做菜"。修正:加 `函数名()`
> 2. **错误现象**:函数定义在调用之后
>    **原因:**Python 从上到下执行,必须先定义再调用。修正:定义放前面

---

#### 函数四种形式 —— 根据需求选择

> **痛点**:不知道函数要不要参数、要不要返回值。
> **类比**:四种形式就像四种"服务模式" —— 要不要输入?要不要输出?
> **解释**:根据需求组合参数和返回值,得到四种形式。

```python
# 形式 1:无参无返(执行一段操作)
def print_line():
    print("-" * 20)

print_line()

# 形式 2:有参无返(传入参数,执行操作)
def print_star(n):
    print("*" * n)

print_star(5)       # *****

# 形式 3:无参有返(不传入参数,返回结果)
import random
def roll_dice():
    return random.randint(1, 6)

result = roll_dice()
print(f"掷出了 {result}")

# 形式 4:有参有返(传入参数,返回结果)—— 最常用!
def add(a, b):
    return a + b

sum_val = add(3, 5)
print(sum_val)      # 8
```

**逐行解剖**

- 无参无返 = 执行固定操作(如打印菜单)
- 有参无返 = 根据参数执行操作(如打印 n 个星)
- 无参有返 = 返回计算结果(如掷骰子)
- 有参有返 = 最常用!传入数据,返回结果

> **ASCII 四种形式对比**
> ```
> 无参无返: [    ] → 执行操作
> 有参无返: [输入] → 执行操作
> 无参有返: [    ] → 返回结果
> 有参有返: [输入] → 返回结果  ★最常用
> ```

**常见错误**

> 1. **错误现象**:想返回值但忘记写 return
>    **原因:**没 return 的函数返回 None。修正:`return 结果`
> 2. **错误现象**:return 后面又写了代码
>    **原因:**return 立刻退出函数,后面代码不执行。修正:return 放最后

---

#### 参数详解 —— 形参、实参、默认参数、关键字参数

> **痛点**:搞不清形参实参,不知道默认参数怎么用。
> **类比**:形参就像"占位符",实参就像"实际填入的东西";默认参数就像"套餐默认配置"。
> **解释**:调用时实参赋值给形参;默认参数放最后;关键字参数名实对应。

```python
# 形参 vs 实参
def power(base, exp):       # base, exp 是形参(占位符)
    return base ** exp

print(power(2, 3))          # 2, 3 是实参(实际值)→ 8

# 默认参数(必须放最后)
def greet(name, msg="你好"):
    print(f"{msg}, {name}!")

greet("Alice")              # 你好, Alice!(msg 默认)
greet("Bob", "欢迎")        # 欢迎, Bob!(msg 覆盖)

# 关键字参数(指定参数名,不用管顺序)
print(power(exp=3, base=2)) # 8(关键字参数)

# 默认参数必须放最后(错误示例)
# def wrong(a=1, b):        # 报错!
#     pass
# def right(b, a=1):        # 正确
#     pass
```

**逐行解剖**

- 形参 = 定义时的占位符
- 实参 = 调用时的实际值
- `msg="你好"` = 默认参数(调用时不传就用默认值)
- `power(exp=3, base=2)` = 关键字参数(指定名字,不用管顺序)

> **ASCII 参数传递示意图**
> ```
> def power(base, exp):
>     return base ** exp
>
> power(2, 3)
>       │  │
>       ▼  ▼
>     base=2, exp=3
>       │
>       ▼
>     2 ** 3 = 8
> ```

**常见错误**

> 1. **错误现象**:默认参数放在非默认参数前面
>    **原因:**Python 要求默认参数放最后。修正:`def f(a, b=1):` 不是 `def f(a=1, b):`
> 2. **错误现象**:默认参数用可变对象(如列表)
>    **原因:**默认参数只计算一次,可变对象会"累积"。修正:用 None 做默认值

---

#### return —— 带结果回家

> **痛点**:函数算完了,结果拿不出来;return 写了多个,搞不清返回哪个。
> **类比**:return 就像"快递员" —— 把结果送回调用处,到了就下班。
> **解释**:`return` 把结果返回给调用者,立刻退出函数;可以返回多个值(元组)。

```python
# 基本 return
def max_num(a, b):
    if a > b:
        return a        # 返回 a,立刻退出
    else:
        return b        # 返回 b,立刻退出

print(max_num(3, 5))    # 5

# return 立刻退出(后面的代码不执行)
def test():
    print("A")
    return 1
    print("B")          # 永远不执行
    return 2

print(test())           # 输出 A,然后 1

# 多值返回(实际是返回元组)
def get_min_max(numbers):
    return min(numbers), max(numbers)

result = get_min_max([3, 1, 4, 1, 5])
print(result)           # (1, 5)

# 元组解包
smallest, largest = get_min_max([3, 1, 4, 1, 5])
print(smallest)         # 1
print(largest)          # 5
```

**逐行解剖**

- `return a` = 把 a 送回调用处,函数立刻结束
- 函数可以写多个 return,但只有一个会执行
- `return min, max` = 返回元组 `(min, max)`
- `a, b = func()` = 元组解包,把返回值拆成多个变量

> **ASCII return 示意图**
> ```
> def max_num(a, b):
>     if a > b: return a
>     else: return b
>
> x = max_num(3, 5)
>               │
>               ▼
>         返回 5 → x = 5
>
> return 执行后,函数立刻退出,
> 后续代码不执行
> ```

**常见错误**

> 1. **错误现象**:`return` 写成 `return = 5`
>    **原因:**return 是关键字,不是变量。修正:`return 5`
> 2. **错误现象**:以为多值返回是"返回多个变量"
>    **原因:**Python 实际返回一个元组,调用者解包。理解"打包→解包"

---

#### 作用域 —— 变量的"势力范围"

> **痛点**:函数里改了一个变量,函数外的变量也变了,或者反过来,搞不清。
> **类比**:作用域就像"房间" —— 局部变量只在自己房间有效,全局变量全屋有效。
> **解释**:函数内是局部作用域,函数外是全局作用域;局部优先。

```python
# 全局变量 vs 局部变量
name = "Alice"          # 全局变量(函数外)

def show():
    age = 25            # 局部变量(函数内)
    print(name)         # 可以访问全局变量 → Alice
    print(age)          # 可以访问局部变量 → 25

show()
# print(age)            # 报错!age 是局部变量,函数外访问不到

# 修改全局变量要加 global
count = 0

def increment():
    global count        # 声明使用全局变量
    count += 1

increment()
increment()
print(count)            # 2
```

**逐行解剖**

- `name = "Alice"` = 全局变量,函数内外都能访问
- `age = 25` = 局部变量,只在函数内部有效
- `global count` = 声明"我要修改全局变量"(不声明就是新建局部变量)
- 局部变量优先:如果局部和全局同名,函数内用局部的

> **ASCII 作用域示意图**
> ```
> 全局作用域:          函数内(局部作用域):
> ┌──────────┐        ┌──────────┐
> │ name     │◀──────│ 可以访问  │
> │ count    │◀──────│ 可以访问  │
> └──────────┘        │ age(局部) │──▶ 函数外访问不到
>                     └──────────┘
> ```

**常见错误**

> 1. **错误现象**:函数内修改全局变量但没写 global,结果没变
>    **原因:**不写 global 就等于新建同名局部变量。修正:加 `global`
> 2. **错误现象**:函数外访问函数内的局部变量
>    **原因:**局部变量函数结束就销毁了。修正:用 return 返回

---

#### 函数封装实战 —— 计算器和温度转换

> **痛点**:学了函数,不知道怎么把一个小程序封装成函数。
> **类比**:封装就像"打包快递" —— 把相关逻辑装一个盒子里,贴上标签(函数名)。
> **解释**:把常用功能封装成函数,主程序调用,代码清晰可维护。

```python
# 温度转换:摄氏度 ↔ 华氏度
def c_to_f(c):
    return c * 9 / 5 + 32

def f_to_c(f):
    return (f - 32) * 5 / 9

# 主程序
print(f"25°C = {c_to_f(25):.1f}°F")     # 25°C = 77.0°F
print(f"77°F = {f_to_c(77):.1f}°C")     # 77°F = 25.0°C

# 计算器(封装四则运算)
def calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "除数不能为 0"
        return a / b
    else:
        return "无效运算符"

result = calculator(10, 3, "+")
print(result)       # 13
```

---

#### 苏格拉底引导

1. 函数没写 return,调用后赋值给变量,变量的值是什么?
2. 为什么默认参数必须放最后?如果放前面会怎样?
3. 两个函数里都有变量 `x`,它们会互相影响吗?为什么?
4. 什么时候用 global,什么时候用 return 传值?哪种更好?

---

#### 学员代码区

在 VS Code 新建 `day05.py`,补全下面的代码:

```python
# TODO: 定义函数 is_prime(n),判断 n 是否为素数,返回 True/False
def is_prime(n):
    pass

# TODO: 定义函数 fibonacci(n),返回斐波那契数列第 n 项
# 斐波那契:1, 1, 2, 3, 5, 8, 13...(第 1、2 项是 1)
def fibonacci(n):
    pass

# TODO: 调用测试
print(is_prime(7))      # True
print(fibonacci(6))     # 8
```

---

#### 参考答案

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    if n <= 2:
        return 1
    a, b = 1, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b

print(is_prime(7))      # True
print(fibonacci(6))     # 8
```

---

## 明日衔接

- 明天 Day 06 学什么:**列表与元组**(序列容器/增删改查/常用方法)
- 今天遗留的概念:今天学了函数,但还没有批量存储和操作数据的能力
- 脚手架递进预告:Day 6 在 Day 5 函数基础上,对列表数据进行批量处理
