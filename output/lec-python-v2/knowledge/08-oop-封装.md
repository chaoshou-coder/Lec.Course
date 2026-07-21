### Day 08 · OOP 封装(L1)

> **叙事锚点**:电商订单系统 —— 从散落的 dict 到 Product 类

今天进入面向对象编程(OOP)的世界。
你会学会:用**类**描述事物,用**对象**承载数据,
用**方法**定义行为,用**属性**封装状态。

---

**本课知识地图**

| 知识点 | 解决什么问题 |
| --- | --- |
| 类与对象 | 把相关的数据和行为打包成一个整体 |
| __init__ 构造函数 | 创建对象时自动初始化属性 |
| self 参数 | 让方法知道"当前操作的是哪个实例" |
| 实例方法 | 让对象自己拥有操作数据的能力 |
| @property getter | 把方法伪装成属性,统一访问语法 |
| @property setter | 写数据时自动校验,拒绝非法值 |
| __str__ 魔术方法 | print(对象) 输出友好可读的信息 |
| 类属性 vs 实例属性 | 区分"共享数据"与"独有数据" |
| BankAccount 综合 | 把六个知识点串成一个真实业务类 |

---

#### 类与对象 —— 图纸与产品

> **痛点**

之前用多个变量描述一个事物(如 name, age, score),
变量散落在各处,传参时容易遗漏,
代码越长越难维护。

> **类比**

**类** = 图纸/模具,**对象** = 按图纸造出的一个个具体产品。
比如"学生"是图纸,"张三"是一个具体的学生。

> **解释**

`class` 关键字定义一张图纸;
用 `类名(...)` 调用图纸,得到一个**实例**(对象)。

**ASCII 内存图 —— 类与对象的关系**

```
        内存
  ┌──────────────────────┐
  │ 类对象 Student       │ ← 图纸(只有一份)
  │   __init__           │
  │   info()             │
  └──────────┬───────────┘
             │ 造出
   ┌─────────┴─────────┐
   ▼                   ▼
┌──────────┐     ┌──────────┐
│ stu1     │     │ stu2     │
│ name=张三│     │ name=李四│
│ age=18   │     │ age=20   │
└──────────┘     └──────────┘
   独立实例          独立实例
```

**关键**:类只有一份,对象可以创建无数个,
每个对象**独立**存储自己的数据。

```python
# 示例 1:定义一个最简单的类,创建两个对象
class Student:
    pass

stu1 = Student()  # 创建第一个对象
stu2 = Student()  # 创建第二个对象

print(stu1)       # <__main__.Student object at 0x...>
print(stu2)       # 地址不同 → 两个独立对象
print(stu1 is stu2)  # False(不是同一个)
```

**逐行解剖**

① `class Student:` 在内存中创建一个**类对象**(图纸)
② `stu1 = Student()` → 分配一块新内存 → 得到一个实例
③ `stu2 = Student()` → 再分配一块**不同**的内存 → 另一个实例
④ `stu1 is stu2` → 比较内存地址 → False(不是同一块内存)

**要点**:每次调用 `类名()` 都会创建**新**的对象,
就像用模具压铸出一个个零件,零件之间互不干扰。

```python
# 示例 2:给对象"手动"绑定属性(不推荐,先理解原理)
class Student:
    pass

stu1 = Student()
stu1.name = "张三"   # 给 stu1 绑一个 name 属性
stu1.age = 18       # 给 stu1 绑一个 age 属性

stu2 = Student()
stu2.name = "李四"
stu2.age = 20

print(stu1.name, stu1.age)  # 张三 18
print(stu2.name, stu2.age)  # 李四 20
# stu1 和 stu2 各自拥有独立的 name/age
```

**逐行解剖**

① `stu1 = Student()` 创建空对象
② `stu1.name = "张三"` 在 stu1 的内存里写入 name
③ `stu2 = Student()` 创建另一个空对象
④ `stu2.name = "李四"` 在 stu2 的内存里写入 name
⑤ 两个对象的 name **互不干扰**

**为什么不用这种方式**:每次都要手动写,
容易漏绑、写错。→ 引出 `__init__` 自动绑定。

**常见错误**

> 1. **错误现象**:以为 stu1 和 stu2 是同一个对象
>    **原因:**每次 `Student()` 都创建新实例,地址不同
> 2. **错误现象**:忘了写括号 `()`
>    **原因:**`stu1 = Student` 是把类本身赋给变量,不是创建对象。修正:`stu1 = Student()`

> **问自己**(先思考,再看下面的参考答案):
> - 类和对象分别对应生活中的什么?
> - 创建两个对象后,修改一个会影响另一个吗?
> - 为什么 `stu1 is stu2` 是 False?

---

#### __init__ 构造函数 —— 给对象"贴标签"

> **痛点**

上一节手动绑属性太麻烦,容易漏写。
能不能在创建对象**的同时**就把属性绑好?

> **类比**

买手机时填写的"配置单":
颜色、内存、价格在出厂时就定好了,
不需要用户拿到手后再贴标签。

> **解释**

`__init__` 是**构造函数**(创建对象时自动调用),
它的参数就是创建对象时要传入的数据。

**ASCII 内存图 —— __init__ 执行过程**

```
stu1 = Student("张三", 18)

① Python 看到 Student(...) → 分配新内存
② 自动调用 __init__(self=新对象, name="张三", age=18)
③ self.name = "张三" → 新对象的 name = "张三"
④ self.age = 18     → 新对象的 age = 18
⑤ 创建完毕,把对象赋值给变量 stu1

结果:
  stu1 ──→┌───────────────┐
           │ name = "张三" │
           │ age  = 18     │
           └───────────────┘
```

**关键**:`__init__` 不需要手动调用,
Python 在 `类名(...)` 时自动触发。

```python
# 示例 1:用 __init__ 自动绑定属性
class Student:
    def __init__(self, name, age):
        self.name = name   # 把参数绑定到对象
        self.age = age     # 把参数绑定到对象

stu1 = Student("张三", 18)
stu2 = Student("李四", 20)
print(stu1.name, stu1.age)  # 张三 18
print(stu2.name, stu2.age)  # 李四 20
```

**逐行解剖**

① `class Student:` 定义类(图纸)
② `def __init__(self, name, age):` 定义构造函数
   - `self` 是**自动传入**的新对象本身
   - `name, age` 是创建时要传入的参数
③ `self.name = name` 把参数值**绑到对象上**
④ `stu1 = Student("张三", 18)` 触发 __init__
⑤ `print(stu1.name)` 读取对象上的属性

**命名约定**:`__init__` 前后各有**两个下划线**,
不要写成 `_init_` 或 `init`。

```python
# 示例 2:电商场景 —— Product 类
class Product:
    def __init__(self, title, price):
        self.title = title
        self.price = price

p1 = Product("Python 入门", 59.8)
p2 = Product("算法图解", 45.0)
print(p1.title, p1.price)  # Python 入门 59.8
print(p2.title, p2.price)  # 算法图解 45.0
```

**常见错误**

> 1. **错误现象**:`NameError: name 'name' is not defined`
>    **原因:**忘记写 `self.` 前缀。`name = name` 只是给局部变量赋值,不是绑到对象。修正:`self.name = name`
> 2. **错误现象**:`__init__` 写错下划线数量
>    **原因:**`_init_` 单下划线不是魔术方法。修正:`__init__` 双下划线

> **问自己**:
> - `__init__` 什么时候被调用?需要手动调用吗?
> - `self.name = name` 等号左边和右边的 name 分别是什么?
> - 如果 `__init__` 漏写了 `self` 参数,会报什么错?

---

#### self 是什么 —— 代表"当前这个实例"

> **痛点**

一个类可以创建很多对象,方法怎么知道
"我现在操作的是哪一个对象"?

> **类比**

考试时每张试卷上都要写姓名。
`self` 就是试卷上的"姓名",
让老师知道"这张卷子是谁的"。

> **解释**

`self` 是实例方法的**第一个参数**,
Python 自动把"当前对象"传进去,
你不需要(也不能)手动传。

**ASCII 内存图 —— self 的本质**

```
stu1 = Student("张三", 18)
stu2 = Student("李四", 20)

stu1.say_hi()  →  Student.say_hi(self=stu1)
stu2.say_hi()  →  Student.say_hi(self=stu2)

内存:
  ┌───────────────┐
  │ Student 类    │
  │  say_hi(self) │ ← 方法只有一个
  └──────┬────────┘
         │ 调用时 self 指向不同对象
    ┌────┴──────┐
    ▼          ▼
┌─────────┐ ┌─────────┐
│ stu1    │ │ stu2    │
│name=张三│ │name=李四│
└─────────┘ └─────────┘
```

**关键**:方法定义时写 `self`,
调用时**不需要**手动传,
Python 自动把"谁调用的"传进去。

```python
# 示例 1:self 让方法知道"我在操作谁"
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        # self 就是调用这个方法的对象
        print(f"大家好,我是{self.name},今年{self.age}岁")

stu1 = Student("张三", 18)
stu2 = Student("李四", 20)
stu1.say_hi()  # 大家好,我是张三,今年18岁
stu2.say_hi()  # 大家好,我是李四,今年20岁
```

**逐行解剖**

① `def say_hi(self):` 定义实例方法,**必须**有 self
② `self.name` 读取**当前对象**的 name
③ `stu1.say_hi()` 等价于 `Student.say_hi(stu1)`
④ `stu2.say_hi()` 等价于 `Student.say_hi(stu2)`

**要点**:虽然 self 可以叫别的名字(如 this),
但**强烈建议**用 self,这是 Python 社区的约定。

**常见错误**

> 1. **错误现象**:调用时手动传 self
>    **原因:**`stu1.say_hi(stu1)` 多余,Python 自动传。修正:`stu1.say_hi()`
> 2. **错误现象**:定义时漏写 self
>    **原因:**`def say_hi(): print(self.name)` 报错: self 未定义。修正:`def say_hi(self):`

> **问自己**:
> - `stu1.say_hi()` 和 `stu2.say_hi()` 调用的是同一个方法吗?
> - 为什么方法定义时要写 self,调用时却不传?
> - 如果把 self 改名成 `abc`,代码还能运行吗?

---

#### 实例方法 —— 对象能做什么

> **痛点**

数据绑到对象上了,但操作这些数据的函数还在外面飘着,
函数一多不知道哪个属于谁。

> **类比**

对象是一台电视机,方法就是遥控器上的按钮。
调音量 → `tv.volume_up()`,
按钮"属于"这台电视。

> **解释**

定义在类内部、第一个形参为 `self` 的函数
就是**实例方法**。通过 `实例.方法()` 调用。

**ASCII 内存图 —— 实例方法的调用**

```
p = Product("Python 入门", 59.8)
p.discount(0.8)

调用过程:
  ① Python 看到 p.discount(0.8)
  ② 找到 Product 类的 discount 方法
  ③ 调用 discount(self=p, rate=0.8)
  ④ self.price = 59.8 * 0.8 = 47.84
  ⑤ 返回 47.84

内存:
  p ──→ ┌────────────────┐
        │ title="Python.."│
        │ price=47.84    │ ← 被方法修改
        └────────────────┘
```

**关键**:实例方法可以**读取**和**修改**对象的数据,
这是它与普通函数最大的区别。

```python
# 示例 1:实例方法读取和修改对象数据
class Product:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def info(self):
        # 读取对象数据,返回描述字符串
        return f"商品[{self.title}] 价格:{self.price:.2f} 元"

    def discount(self, rate):
        # 修改对象数据
        self.price = self.price * rate
        return self.price

p = Product("Python 入门", 59.8)
print(p.info())         # 商品[Python 入门] 价格:59.80 元
print(p.discount(0.8))  # 47.84
print(p.price)          # 47.84(已被修改)
```

**逐行解剖**

① `def info(self):` 无额外参数,只读取数据
② `return f"..."` 返回字符串,不修改对象
③ `def discount(self, rate):` 有一个额外参数
④ `self.price = self.price * rate` **修改**对象数据
⑤ `p.discount(0.8)` 调用后,p.price 已被改变

**要点**:实例方法可以**读取**也可以**修改**对象,
修改后影响会**持久保存**在对象里。

**常见错误**

> 1. **错误现象**:`NameError: name 'title' is not defined`
>    **原因:**方法内忘记写 `self`。修正:`return self.title`
> 2. **错误现象**:`TypeError: Product.info() missing 1 required positional argument: 'self'`
>    **原因:**把方法当函数调用 `Product.info()`。修正:`p.info()`

> **问自己**:
> - 实例方法和普通函数的区别是什么?
> - 为什么实例方法可以访问对象的属性?
> - `p.info()` 和 `Product.info(p)` 效果一样吗?

---

#### @property getter —— 把方法伪装成属性

> **痛点**

有些数据需要**计算**得到(如含税价格),
如果暴露为方法,调用时要写 `p.price_with_tax()`;
如果暴露为属性,又没法计算。
能不能**像属性一样访问,但背后执行计算**?

> **类比**

电视机的"音量"看起来是一个属性,
但背后是电路在实时计算。
`@property` 就是让方法"看起来像属性"。

> **解释**

`@property` 装饰器把方法变成"只读属性",
访问 `obj.xxx` 时自动调用方法,无需括号。

```python
# 示例:@property 把方法伪装成属性
class Product:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    @property
    def price_with_tax(self):
        # 像属性一样访问,但背后是计算
        return self.price * 1.13

p = Product("Python 入门", 100)
print(p.price_with_tax)  # 113.0(没有括号!)
print(p.price)           # 100(原始价格)
```

**逐行解剖**

① `@property` 装饰器,写在 `def` 上方
② `def price_with_tax(self):` 方法名就是属性名
③ `return self.price * 1.13` 返回计算结果
④ `p.price_with_tax` **没有括号**,像属性一样访问

**要点**:`@property` 是**只读**的,
不能给它赋值(赋值会报错)。

**常见错误**

> 1. **错误现象**:调用时加了括号
>    **原因:**`p.price_with_tax()` 报错。修正:`p.price_with_tax`(不加括号)
> 2. **错误现象**:`AttributeError: can't set attribute`
>    **原因:**试图给只读 @property 赋值。修正:加 setter(见下一节)

> **问自己**:
> - `@property` 的方法能不能有参数?
> - 为什么访问 `@property` 不需要写括号?
> - `@property` 和直接定义属性有什么区别?

---

#### @property setter —— 写保护逻辑

> **痛点**

直接把属性暴露在外面,用户可以随意赋值
负数、空串、类型错误。
比如 `acc.balance = -500` 应该被拒绝。

> **类比**

属性像带锁的保险箱:
getter 看内容,setter 控制写入规则,
外部看起来仍是 `obj.xxx` 的写法。

> **解释**

`@xxx.setter` 给写操作加规则,
赋值时自动调用,非法值可以拒绝。

```python
# 示例:@property + setter 保护余额
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance  # 走 setter 校验

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            print("余额不能为负,已忽略")
            return
        self._balance = value

acc = BankAccount("张三", 1000)
print(acc.balance)    # 1000
acc.balance = -500    # 余额不能为负,已忽略
print(acc.balance)    # 1000(没变)
acc.balance = 2000
print(acc.balance)    # 2000
```

**逐行解剖**

① `@property` 装饰 getter 方法
② `def balance(self):` getter 方法名 = 属性名
③ `return self._balance` 返回**私有**属性
④ `@balance.setter` 装饰 setter 方法
⑤ `def balance(self, value):` 接收要赋的值
⑥ `if value < 0:` 校验逻辑
⑦ `self._balance = value` 通过校验后存入

**命名约定**:
getter/setter 方法名相同(都是 `balance`),
真实数据存在 `_balance`(单下划线=内部使用)。

**常见错误**

> 1. **错误现象**:无限递归 `RecursionError`
>    **原因:**setter 里写 `self.balance = value` 会再次触发 setter。修正:`self._score = value`
> 2. **错误现象**:getter 和 setter 名称不一致
>    **原因:**`@grade.setter` 但 getter 叫 `score`。修正:统一用 `score`

> **问自己**:
> - 为什么真实数据要存在 `_balance` 而不是 `balance`?
> - setter 里如果写 `self.balance = value` 会怎样?
> - 如果没有 setter,能给 @property 赋值吗?

---

#### __str__ 魔术方法 —— print(对象) 输出友好信息

> **痛点**

`print(对象)` 默认打印
`<__main__.Student object at 0x7f8b1c>`,
调试时完全看不出对象里装了什么数据。

> **类比**

每个人的"自我介绍":
别人问你"你是谁",你说"我叫张三,今年 18 岁",
而不是说"我是人类,住在地球某处"。

> **解释**

`__str__` 是**魔术方法**,
`print()` / `str()` 调用对象时自动触发,
返回你定义的"友好字符串"。

```python
# 示例:没有 __str__ vs 有 __str__
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

stu = Student("张三", 18)
print(stu)  # <__main__.Student object at 0x...>

# 添加 __str__ 后
class Student2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student(name={self.name}, age={self.age})"

stu2 = Student2("张三", 18)
print(stu2)  # Student(name=张三, age=18)
```

**逐行解剖**

① `def __str__(self):` 定义魔术方法
② 方法名 `__str__` 前后各有**两个下划线**
③ `return f"..."` **必须返回字符串**
④ `print(stu)` 自动调用 `__str__`

**要点**:
- `__str__` 是"给人看的",用于 print 输出
- 还有一个 `__repr__` 是"给程序员看的",用于调试
- 如果只定义 `__str__`,print 用它;repr 也 fallback 用它

**常见错误**

> 1. **错误现象**:`TypeError: __str__() must return str, not None`
>    **原因:**`__str__` 里用 print 而不是 return。修正:`return f"..."`
> 2. **错误现象**:`_str_` 单下划线不生效
>    **原因:**魔术方法必须双下划线。修正:`__str__`

> **问自己**:
> - `__str__` 什么时候被自动调用?
> - `__str__` 必须返回什么类型?
> - `__str__` 和 `__repr__` 有什么区别?

---

#### 类属性 vs 实例属性 —— 共享 vs 独立

> **痛点**

有些数据是每个对象**独有**的(如姓名),
有些数据是**所有对象共享**的(如税率)。
如果每个对象都存一份税率,改起来太麻烦。

> **类比**

- **实例属性** = 每个人的身份证号(各不相同)
- **类属性** = 国家的法律(所有人共享)

> **解释**

- **类属性**:写在类体内、方法外,被所有实例**共享**
- **实例属性**:写在 `self.xxx = ...` 里,**每个实例独立**

```python
# 示例:类属性 vs 实例属性的基本用法
class Product:
    tax_rate = 0.13  # 类属性:所有商品共享

    def __init__(self, name, price):
        self.name = name      # 实例属性
        self.price = price    # 实例属性

    def price_with_tax(self):
        return self.price * (1 + Product.tax_rate)

p1 = Product("Python 入门", 100)
p2 = Product("算法图解", 200)
print(p1.price_with_tax())  # 113.0
print(p2.price_with_tax())  # 226.0
Product.tax_rate = 0.09     # 改税率
print(p1.price_with_tax())  # 109.0(跟着变)
print(p2.price_with_tax())  # 218.0(跟着变)
```

**逐行解剖**

① `tax_rate = 0.13` 类属性,写在方法外
② `self.name = name` 实例属性,写在 __init__ 里
③ `Product.tax_rate` 通过**类名**访问类属性
④ `Product.tax_rate = 0.09` 修改类属性
⑤ 所有实例的 `price_with_tax()` 都受影响

**要点**:
- 类属性用 `类名.属性` 访问
- 实例属性用 `self.属性` 访问
- 修改类属性会影响**所有**实例

**常见错误**

> 1. **错误现象**:通过实例修改类属性
>    **原因:**`p1.tax_rate = 0.09` 创建实例属性,不改变类属性。修正:`Product.tax_rate = 0.09`
> 2. **错误现象**:可变类属性被实例修改
>    **原因:**`tags = []` 所有实例共享同一个列表。修正:在 `__init__` 里 `self.tags = []`

> **问自己**:
> - 类属性和实例属性在内存中分别有几份?
> - 通过 `实例.类属性 = xxx` 会修改类属性吗?
> - 什么时候用类属性,什么时候用实例属性?

---

#### 综合练习 —— BankAccount 类

现在把**六个知识点**串成一个真实业务类。

**需求清单**:
1. `__init__(owner, balance)` 绑定属性
2. `@property` 保护 balance(不允许为负)
3. 实例方法 `deposit(amount)` 存款,返回余额
4. 实例方法 `withdraw(amount)` 取款,超额拒绝
5. 类属性 `bank_name = 'Python 银行'`
6. `__str__` 输出 `BankAccount(owner=xxx, balance=xxx)`

```python
# 示例:BankAccount 完整实现
class BankAccount:
    bank_name = "Python 银行"  # 类属性

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance  # 走 setter 校验

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            print("余额不能为负,已忽略")
            return
        self._balance = value

    def deposit(self, amount):
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if amount > self._balance:
            print("余额不足")
            return False
        self._balance -= amount
        return True

    def __str__(self):
        return (f"BankAccount(owner={self.owner}, "
                f"balance={self._balance})")

acc = BankAccount("张三", 1000)
print(acc)            # BankAccount(owner=张三, balance=1000)
print(acc.deposit(500))  # 1500
print(acc.withdraw(2000))  # 余额不足 / False
print(acc.withdraw(300))   # True
print(acc)            # BankAccount(owner=张三, balance=1200)
print(BankAccount.bank_name)  # Python 银行
```

**逐行解剖**

① `bank_name = "Python 银行"` 类属性,所有账户共享
② `self.balance = balance` 触发 setter 校验
③ `@property` + `@balance.setter` 保护 _balance
④ `deposit(self, amount)` 实例方法,修改余额
⑤ `withdraw(self, amount)` 实例方法,超额拒绝
⑥ `__str__` 返回友好字符串

**要点**:这个类是 OOP 封装的"最小完整案例",
包含了 class / __init__ / self / 实例方法 /
@property / __str__ / 类属性 全部知识点。

> **问自己**(综合练习前先思考):
> - 这个类用到了今天学的哪些知识点?
> - 为什么 balance 要存在 `_balance` 里?
> - 如果取款超额,应该返回什么?
> - 类属性 bank_name 应该在哪里定义?

---

#### 练习指导

完成下面的练习,巩固今天学的知识点。

**当堂练**(必做):
- 打开 `exercises/08-oop-封装/practice01.py` —— 定义 Product 类
- 打开 `exercises/08-oop-封装/practice02.py` —— __init__ 自动绑定
- 打开 `exercises/08-oop-封装/practice03.py` —— self 和方法
- 打开 `exercises/08-oop-封装/practice04.py` —— @property getter
- 打开 `exercises/08-oop-封装/practice05.py` —— @property setter
- 打开 `exercises/08-oop-封装/practice06.py` —— BankAccount 综合

**课后作业**(选做):
- 打开 `exercises/08-oop-封装/task01.py` —— __str__ 魔术方法
- 打开 `exercises/08-oop-封装/task02.py` —— 类属性 vs 实例属性
- 打开 `exercises/08-oop-封装/task03.py` —— 综合项目

**参考答案**:在 `solutions/08-oop-封装/` 下找到对应答案。

---

#### 今日小结

| 概念 | 解决的痛点 | 关键语法 |
| --- | --- | --- |
| 类与对象 | 把相关的数据和行为打包成一个整体 | `class` / `类名()` |
| __init__ 构造函数 | 创建对象时自动初始化属性 | `def __init__(self, ...)` |
| self 参数 | 让方法知道"当前操作的是哪个实例" | 第一个形参写 self |
| 实例方法 | 让对象自己拥有操作数据的能力 | `def method(self)` |
| @property getter | 把方法伪装成属性,统一访问语法 | `@property` |
| @property setter | 写数据时自动校验,拒绝非法值 | `@xxx.setter` |
| __str__ 魔术方法 | print(对象) 输出友好可读的信息 | `def __str__(self)` |
| 类属性 vs 实例属性 | 区分"共享数据"与"独有数据" | 类内方法外 / `self.xxx` |
| BankAccount 综合 | 把六个知识点串成一个真实业务类 | 全部综合 |

---

[← 上一个:Python 入门](../knowledge/07-文件IO与异常.md) | [返回目录](../README.md) | [下一个:OOP 继承 L2 →](../knowledge/09-oop-继承.md)
