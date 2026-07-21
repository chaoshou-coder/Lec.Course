### Day 09 · OOP 继承 (L2)

> **叙事锚点**:电商订单系统 —— 从 Product 散落的副本到继承体系

今天进入面向对象三大特性的第一个:**继承**。
你会学会:复用已有类的代码、重写父类行为、理解查找顺序。

---

**本课知识地图**

| 知识点 | 解决什么问题 |
| --- | --- |
| 为什么需要继承 | 避免多个类之间复制粘贴重复代码 |
| is-a 关系 | 判断什么时候该用继承 |
| 单继承语法 | 子类自动拥有父类的属性和方法 |
| super().__init__() | 安全调用父类构造函数 |
| 方法重写 override | 子类用自定义行为替换父类 |
| super().方法() | 保留父类逻辑并扩展 |
| MRO 方法解析顺序 | 多级继承时方法查找顺序 |
| isinstance 与类型检查 | 判断对象是否属于某类型 |

---

#### 为什么需要继承 —— DRY 原则

> **痛点**

写几个类发现彼此有大量重复代码。
比如 `Book`(书)和 `Magazine`(杂志)都有
`name`/`price`/`info()` 方法,代码几乎完全一样。
改一个 bug 要改两处,复制粘贴越多越痛。

> **类比**

法律是父类,地方法规是子类:
国家规定"最低工资 A 元",
某市可**重写**为更高的"B 元"。
共性留在国家层面,差异留在地方。

> **解释**

继承让子类**自动拥有**父类的属性和方法,
在此基础上添加或修改,实现**代码复用**。

**ASCII 内存图 —— 无继承 vs 有继承**

```
无继承(重复):                    有继承(复用):
┌──────────────┐                ┌──────────────┐
│ Book         │                │ Product(父类)│
│ name, price  │                │ name, price  │
│ info()       │                │ info()       │
└──────────────┘                └──────┬───────┘
┌──────────────┐                      │ 继承
│ Magazine     │                ┌─────┴─────┐
│ name, price  │                │ Book(子类)│
│ info()       │                │ + weight  │
└──────────────┘                └───────────┘
```

**关键**:无继承时每个类都复制一套,
有继承时共性留在父类,**差异留在子类**。

```python
# 示例 1:无继承 —— 两个类各自复制
class Book:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def info(self):
        return f"{self.name} ¥{self.price}"

class Magazine:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def info(self):
        return f"{self.name} ¥{self.price}"

b = Book("Python 入门", 59.8)
m = Magazine("读者", 10)
print(b.info())  # Python 入门 ¥59.8
print(m.info())  # 读者 ¥10
```

**逐行解剖**

① Book 和 Magazine 的 `__init__` **完全一样**
② Book 和 Magazine 的 `info` **完全一样**
③ 改 `info` 的格式,要改**两处**(容易漏改)
④ 这就是"重复代码"的痛点

```python
# 示例 2:有继承 —— 共性抽到父类
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def info(self):
        return f"{self.name} ¥{self.price}"

class Book(Product):       # 继承 Product
    pass                   # 自动拥有 __init__ 和 info

class Magazine(Product):   # 继承 Product
    pass

b = Book("Python 入门", 59.8)
m = Magazine("读者", 10)
print(b.info())  # Python 入门 ¥59.8
print(m.info())  # 读者 ¥10
```

**逐行解剖**

① `Product` 把共性的 `__init__` 和 `info` 抽出来
② `class Book(Product)` 让 Book **自动拥有**这些方法
③ `class Magazine(Product)` 同样拥有
④ 改 `info` 的格式,**只需改一处**(Product)

**常见错误**

> 1. **错误现象**:以为继承能"自动同步"
>    **原因:**子类一旦重写方法,就不再跟随父类。只在未重写时生效
> 2. **错误现象**:继承层次过深
>    **原因:**A→B→C→D,改底层不知道影响谁。修正:通常不超过两层

> **问自己**(先思考,再看下面的参考答案):
> - 继承和复制粘贴的核心区别是什么?
> - 如果父类改了 `info` 方法,子类会跟着变吗?
> - 什么时候不该用继承?(提示:is-a)

---

#### is-a 关系 —— 判断什么时候该用继承

> **痛点**

不清楚到底该不该继承。
明明是"订单**有**购物车",却写成了"订单**是**购物车"。

> **类比**

把两个类放进"X 是一个 Y"句子,
通顺就用继承,不通顺就用组合(Day11 讲)。

> **解释**

继承 = "是一个"(is-a)关系。
|`Dog` **is-a** `Animal` → `class Dog(Animal)` ✅
|`Car` **is-a** `Vehicle` → `class Car(Vehicle)` ✅
|`Order` **has-a** `Cart` → 不是继承

**判断技巧**:
"订单是一个购物车"?不通顺 → 不该继承。
"狗是一个动物"?通顺 → 该继承。

```python
# 示例:用 is-a 判断继承是否正确
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):      # Dog is-a Animal ✅
    def bark(self):
        print(f"{self.name} 汪汪叫")

class Cat(Animal):      # Cat is-a Animal ✅
    def meow(self):
        print(f"{self.name} 喵喵叫")

dog = Dog("旺财")
dog.bark()  # 旺财 汪汪叫
```

**逐行解剖**

① `class Dog(Animal)` 表示"狗是一种动物"
② Dog 继承了 Animal 的 `name` 属性
③ Dog 自己新增 `bark` 方法
④ 关系明确,代码清晰

**要点**:继承描述的是"分类关系",
不是"包含关系"。组合(Day11)才描述包含。

**常见错误**

> 1. **错误现象**:`class Order(Cart)`
>    **原因:**Order is-a Cart 不通顺。修正:`Order` 里组合 `Cart`
> 2. **错误现象**:为了"代码复用"强行继承
>    **原因:**两个类仅有部分代码相似,语义上无 is-a 关系。修正:用组合

> **问自己**:
> - "学生是一个人"通顺吗?该用继承吗?
> - "订单有商品列表"通顺吗?该用继承吗?
> - 继承和组合各适合什么场景?

---

#### 单继承语法 —— class Child(Parent)

> **痛点**

理解了 is-a 关系,但不知道怎么写语法。

> **类比**

`class 实习生(员工):` 表示实习生**是一种**员工,
自动拥有员工的所有属性和方法。

> **解释**

`class 子类(父类):` 括号里写父类名,表示继承关系。
Python 支持多继承,本节只讲单继承。

```python
# 示例 1:单继承基本语法
class Animal:
    def __init__(self, name):
        self.name = name

    def breathe(self):
        print(f"{self.name} 在呼吸")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} 汪汪叫")

dog = Dog("旺财")
dog.breathe()  # 继承自 Animal
dog.bark()     # Dog 自己的方法
```

**逐行解剖**

① `class Dog(Animal):` 括号里写父类名
② Dog 没有写 `__init__`,但创建时调用的是父类的
③ Dog 没有 `breathe`,调用时沿继承链找到 Animal 的
④ Dog 自己有 `bark`,直接调用

**查找顺序**:子类 → 父类 → 父类的父类 → object

```python
# 示例 2:电商场景 —— Product 基类 + Book 子类
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return f"商品[{self.name}] ¥{self.price}"

class Book(Product):
    def discount(self, rate):
        # 子类新增方法
        return self.price * rate

b = Book("Python 入门", 59.8)
print(b.info())         # 商品[Python 入门] ¥59.8
print(b.discount(0.8))  # 47.84
```

**逐行解剖**

① Product 定义了 `name`、`price`、`info`
② Book 继承 Product,自动拥有 `info`
③ Book 自己新增 `discount` 方法
④ `b.info()` 调用的是 Product 版本

**常见错误**

> 1. **错误现象**:`class Dog Animal:` 忘写括号
>    **原因:**语法错误。修正:`class Dog(Animal):`
> 2. **错误现象**:`class Animal(Dog):` 方向反了
>    **原因:**"动物是狗"不通顺。修正:`class Dog(Animal):`

> **问自己**:
> - 子类能继承父类的 `__init__` 吗?
> - 如果子类和父类都有 `info` 方法,调用哪个?
> - 属性查找顺序是什么?

---

#### super().__init__() —— 安全调用父类构造函数

> **痛点**

子类想扩展父类属性,又不想重复写父类的绑定逻辑。
如 Book 除了 `name`/`price` 还要新增 `author`。

> **类比**

儿子继承了父亲的房子(父类属性),
再加盖一层(扩展属性),
但必须**先**把父亲的房子盖好。

> **解释**

`super()` 返回父类对象,
用来**安全地调用父类方法**。

**ASCII 内存图 —— super().__init__() 调用链**

```
book = Book("Python 入门", 59.8, "张三")

① Python 调用 Book.__init__(book, "Python 入门", 59.8, "张三")
② super().__init__("Python 入门", 59.8)
   → Animal.__init__(book, "Python 入门", 59.8)
   → book.name = "Python 入门"
   → book.price = 59.8
③ 回到 Book.__init__
   → book.author = "张三"
④ 完成

book ──→ ┌────────────────────┐
         │ name = "Python 入门"│
         │ price = 59.8        │
         │ author = "张三"     │
         └────────────────────┘
```

**关键**:`super().__init__()` 必须先调用,
再绑定子类自己的属性,否则父类属性未初始化。

```python
# 示例 1:用 super() 扩展父类属性
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # 先调用父类构造
        self.breed = breed       # 再绑定自己的属性

    def bark(self):
        print(f"{self.name}({self.breed}) 汪汪叫")

dog = Dog("旺财", "柯基")
print(dog.name)   # 旺财(继承自 Animal)
print(dog.breed)  # 柯基(Dog 自己的)
dog.bark()        # 旺财(柯基) 汪汪叫
```

**逐行解剖**

① `super().__init__(name)` 等价于 `Animal.__init__(self, name)`,但更规范
② 必须先调 `super().__init__()`,再绑定子类自己的属性
③ 忘记写 `super().__init__()` 会导致**父类属性未初始化**
④ `dog.name` 是从 Animal 继承的

```python
# 示例 2:电商场景 —— Book 扩展 Product
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Book(Product):
    def __init__(self, name, price, author):
        super().__init__(name, price)
        self.author = author

    def info(self):
        base = f"图书《{self.name}》作者:{self.author}"
        return f"{base} ¥{self.price}"

b = Book("Python 入门", 59.8, "张三")
print(b.info())  # 图书《Python 入门》作者:张三 ¥59.8
```

**逐行解剖**

① Product 绑定 `name` 和 `price`
② Book 用 `super().__init__(name, price)` 复用
③ Book 新增 `author` 属性
④ Book 可以重写 `info` 方法(见下一节)

**常见错误**

> 1. **错误现象**:`AttributeError: 'Book' object has no attribute 'name'`
>    **原因:**忘调 `super().__init__()`,父类属性丢失。修正:加上 `super().__init__()`
> 2. **错误现象**:`TypeError: __init__() missing 1 required argument`
>    **原因:**`super().__init__()` 漏传 name。修正:`super().__init__(name)`

> **问自己**:
> - 如果不调 `super().__init__()` 会怎样?
> - `super()` 返回的是什么?
> - 为什么推荐用 `super()` 而不是直接写父类名?

---

#### 方法重写 override —— 子类替换父类行为

> **痛点**

父类的方法不能满足子类需要。
比如基类 `shipping_cost()` 返回 0,
但实体书要运费,电子书不要。

> **类比**

地方法规可以**重写**国家法律:
国家规定最低税率 10%,某市可规定 8%。
调用时优先执行地方法规。

> **解释**

子类重新定义同名方法,调用时**优先执行子类版本**。

```python
# 示例 1:子类重写父类方法
class Product:
    def shipping_cost(self):
        return 0   # 基类默认免运费

class PhysicalProduct(Product):
    def __init__(self, weight):
        self.weight = weight

    def shipping_cost(self):
        # 重写:实体商品按重量收费
        return self.weight * 8

class DigitalProduct(Product):
    pass  # 不重写,继承基类的 0

p = PhysicalProduct(2)
d = DigitalProduct()
print(p.shipping_cost())  # 16
print(d.shipping_cost())  # 0 (继承自 Product)
```

**逐行解剖**

① PhysicalProduct 定义了 `shipping_cost`,**重写**父类
② DigitalProduct 没有重写,**继承**父类版本
③ 调用时优先看自己有没有,有则用它,没有则找父类
④ 这就是"方法重写"的核心

```python
# 示例 2:电商场景 —— Book 重写 info
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def info(self):
        return f"商品[{self.name}] ¥{self.price}"

class Book(Product):
    def __init__(self, name, price, author):
        super().__init__(name, price)
        self.author = author
    def info(self):
        # 重写:加上作者信息
        return f"图书《{self.name}》作者:{self.author} ¥{self.price}"

b = Book("Python 入门", 59.8, "张三")
print(b.info())  # 图书《Python 入门》作者:张三 ¥59.8
```

**要点**:重写后,该子类的所有实例都用新版本,
不会影响父类或其他子类。

**常见错误**

> 1. **错误现象**:重写时漏写 self
>    **原因:**`def info():` 缺少 self。修正:`def info(self):`
> 2. **错误现象**:以为重写会影响父类
>    **原因:**重写只影响子类,父类方法不变。放心重写

> **问自己**:
> - 方法重写后,父类的方法还在吗?
> - 什么场景下需要重写方法?
> - 重写后还能调用父类版本吗?(提示:super())

---

#### super().方法() —— 保留父类逻辑并扩展

> **痛点**

重写方法时,不想完全替换父类,
而是**保留 + 扩展**。如 Manager 的薪资
= Employee 底薪 + 奖金。

> **类比**

子承父业并扩展:儿子继承了父亲的餐馆,
加上自己的新菜品,但保留招牌菜。

> **解释**

`super().方法()` 先调用父类版本,
拿到结果后再扩展。

```python
# 示例:super().pay() 保留父类计算并扩展
class Employee:
    def __init__(self, name, base):
        self.name = name
        self.base = base

    def pay(self):
        return self.base

class Manager(Employee):
    def __init__(self, name, base, bonus):
        super().__init__(name, base)
        self.bonus = bonus

    def pay(self):
        # 先拿父类的 base,再加上 bonus
        return super().pay() + self.bonus

m = Manager("李四", 8000, 3000)
print(m.pay())  # 11000
```

**逐行解剖**

① `Manager.pay(self)` 先调用 `super().pay()` → 拿到 base
② 再加上 `self.bonus`
③ 效果:8000 + 3000 = 11000
④ 优点:**复用**父类逻辑,而不是复制

**要点**:`super().方法()` 是重写时
保留父类逻辑的标准写法,避免复制粘贴。

**常见错误**

> 1. **错误现象**:忘记调用 super().pay(),直接返回 bonus
>    **原因:**丢失了父类的 base。修正:`return super().pay() + self.bonus`
> 2. **错误现象**:`super().pay` 漏了括号
>    **原因:**拿到的是方法对象,不是调用结果。修正:`super().pay()`

> **问自己**:
> - `super().pay()` 返回的是什么?
> - 什么时候应该用 `super().方法()` 而不是完全重写?
> - 如果父类的 pay 逻辑变了,Manager 会跟着变吗?

---

#### MRO 方法解析顺序 —— 多级继承时怎么查找

> **痛点**

多级继承时,子类和多个父类都有同名方法,
到底用哪个? 出 bug 了不清楚查找顺序。

> **类比**

公司里找人:先找本部门 → 再找上级部门
→ 再找总部 → 最后找集团公司(object)。
有了顺序才不乱。

> **解释**

多级继承时,查找顺序:
**子类 → 父类 → 父类的父类 → object**。
可用 `ClassName.__mro__` 查看。

**ASCII 内存图 —— MRO 查找顺序**

```
继承链: Dog → Mammal → Animal → object

查找 bark 方法:
  ① Dog 自己有 bark? → 没有
  ② Mammal 有 bark? → 没有
  ③ Animal 有 bark? → 有! 用它的
  ④ (如果还没有,最终找 object)

Dog.__mro__ = (Dog, Mammal, Animal, object)
```

**关键**:`__mro__` 告诉你 Python 的查找顺序,
调试多重继承时特别有用。

```python
# 示例:查看 MRO
class Animal:
    def breathe(self):
        print("在呼吸")

class Mammal(Animal):
    def feed(self):
        print("哺乳")

class Dog(Mammal):
    def bark(self):
        print("汪汪叫")

# 查看查找顺序
print(Dog.__mro__)
# (<class '__main__.Dog'>, <class '__main__.Mammal'>,
#  <class '__main__.Animal'>, <class 'object'>)

dog = Dog()
dog.breathe()  # 在呼吸(找到 Animal.breathe)
```

**逐行解剖**

① `Dog.__mro__` 返回一个元组,表示查找顺序
② 顺序:自己 → Mammal → Animal → object
③ `dog.breathe()` 沿这个顺序找到 Animal 的版本
④ 如果所有层级都没有,报 AttributeError

**常见错误**

> 1. **错误现象**:MRO 混乱,多重继承时顺序不清
>    **原因:**画个继承图理不清。修正:用 `ClassName.__mro__` 查看
> 2. **错误现象**:以为"深度优先"就一定正确
>    **原因:**Python 用 C3 线性化算法,不一定深度优先。查 __mro__

> **问自己**:
> - `__mro__` 返回的是什么类型?
> - 如果 Dog 和 Mammal 都有同名方法,用哪个?
> - object 在 MRO 的什么位置?

---

#### isinstance 与类型检查 —— 判断对象是否属于某类型

> **痛点**

需要判断"这个对象是不是某类",写 if-elif
进行类型分发(但这个其实不好,后面会讲)。

> **类比**

isinstance 像安检员问"你是乘客吗?",
答案是 True/False。

> **解释**

`isinstance(对象, 类)` 判断对象是否是该类的实例,
或该类的子类的实例。

```python
# 示例 1:isinstance 基本用法
class Animal: pass
class Dog(Animal): pass

dog = Dog()
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True(沿继承链)
print(isinstance(dog, object))  # True(所有类都继承 object)
print(isinstance(dog, str))     # False
```

**逐行解剖**

① `isinstance(dog, Dog)` → dog 就是 Dog 实例,True
② `isinstance(dog, Animal)` → Dog 继承 Animal,True
③ `isinstance(dog, object)` → 所有类继承 object,True
④ `isinstance(dog, str)` → 毫无关系,False

```python
# 示例 2:isinstance 反模式(能跑但不好)
class Employee:
    def __init__(self, name, base):
        self.name = name
        self.base = base

class Manager(Employee):
    def __init__(self, name, base, bonus):
        super().__init__(name, base)
        self.bonus = bonus

class Sales(Employee):
    def __init__(self, name, base, commission):
        super().__init__(name, base)
        self.commission = commission

# 反模式:if-elif 类型分发
def pay(emp):
    if isinstance(emp, Manager):
        return emp.base + emp.bonus
    elif isinstance(emp, Sales):
        return emp.base + emp.commission
    else:
        return emp.base

m = Manager("李四", 8000, 3000)
s = Sales("王五", 6000, 1500)
print(pay(m))  # 11000
print(pay(s))  # 7500
```

**逐行解剖**

① `pay` 函数用 isinstance 判断类型
② 不同类型走不同计算逻辑
③ 看起来能跑,但有 3 个致命问题

**3 个致命问题**:
1. 每新增一种员工,都要改 `pay` 函数
2. `pay` 函数越来越长,难维护
3. 违反"开闭原则"

**正确做法**:用多态(留到 Day10)
让每个员工类自己实现 `pay()` 方法,
`pay` 函数只需调用 `emp.pay()`。

**常见错误**

> 1. **错误现象**:过度使用 isinstance
>    **原因:**每加类型都要改代码。修正:用多态,Day10 讲
> 2. **错误现象**:用 type(emp) == Manager 判断
>    **原因:**type 不会沿继承链,子类对象不等于父类。修正:用 isinstance

> **问自己**:
> - `isinstance(dog, Animal)` 为什么是 True?
> - `isinstance` 和 `type() ==` 有什么区别?
> - 为什么 isinstance 做类型分发是反模式?

---

#### 综合练习 —— 员工薪资系统

现在把**继承、super、重写、MRO**串成一个真实业务类。

**需求清单**:
1. 基类 `Employee`:属性 `name`、`base_salary`,
   方法 `pay()` 返回 base_salary
2. 子类 `Sales`:新增 `commission`,**重写** pay()
3. 子类 `Manager`:新增 `bonus`,**重写** pay()
4. 用 `super().__init__()` 调用父类构造
5. 用 `super().pay()` 保留父类逻辑并扩展

```python
# 示例:员工薪资系统完整实现
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def pay(self):
        return self.base_salary

class Sales(Employee):
    def __init__(self, name, base, commission):
        super().__init__(name, base)
        self.commission = commission

    def pay(self):
        return super().pay() + self.commission

class Manager(Employee):
    def __init__(self, name, base, bonus):
        super().__init__(name, base)
        self.bonus = bonus

    def pay(self):
        return super().pay() + self.bonus

# 测试
staff = [
    Employee("张三", 5000),
    Sales("李四", 5000, 2000),
    Manager("王五", 8000, 3000),
]
for emp in staff:
    print(f"{emp.name} 薪资: {emp.pay()}")
# 张三 薪资: 5000
# 李四 薪资: 7000
# 王五 薪资: 11000
```

**逐行解剖**

① Employee 定义通用属性和 `pay()` 方法
② Sales 继承 Employee,新增 `commission`
③ Sales 的 `pay()` 用 `super().pay()` 拿底薪再加提成
④ Manager 同理,底薪 + 奖金
⑤ 调用时统一用 `emp.pay()`,各自返回自己的计算

**要点**:这个案例综合了继承 / super / 重写 / MRO
全部知识点,是 OOP L2 的"最小完整案例"。

> **问自己**(综合练习前先思考):
> - Sales 的 `pay()` 为什么用 super() 而不是直接返回 base + commission?
> - 如果新增一个 Engineer 子类,该怎么写?
> - MRO 在这个例子中是什么顺序?

---

#### 练习指导

完成下面的练习,巩固今天学的知识点。

**当堂练**(必做):
- 打开 `exercises/09-oop-继承/practice01.py` —— 继承基类基本用法
- 打开 `exercises/09-oop-继承/practice02.py` —— super().__init__() 扩展属性
- 打开 `exercises/09-oop-继承/practice03.py` —— 方法重写 override
- 打开 `exercises/09-oop-继承/practice04.py` —— super().方法() 保留并扩展
- 打开 `exercises/09-oop-继承/practice05.py` —— MRO 方法解析顺序
- 打开 `exercises/09-oop-继承/practice06.py` —— 员工薪资系统综合

**课后作业**(选做):
- 打开 `exercises/09-oop-继承/task01.py` —— 电商产品类型继承体系
- 打开 `exercises/09-oop-继承/task02.py` —— isinstance 类型检查
- 打开 `exercises/09-oop-继承/task03.py` —— 综合项目:动物园模拟器

**参考答案**:在 `solutions/09-oop-继承/` 下找到对应答案。

---

#### 今日小结

| 概念 | 解决的痛点 | 关键语法 |
| --- | --- | --- |
| 为什么需要继承 | 避免复制粘贴重复代码 | `class Child(Parent)` |
| is-a 关系 | 判断什么时候该用继承 | X is-a Y |
| 单继承语法 | 子类自动拥有父类功能 | `class Child(Parent):` |
| super().__init__() | 安全调用父类构造函数 | `super().__init__(...)` |
| 方法重写 | 子类用自定义行为替换父类 | 重定义同名方法 |
| super().方法() | 保留父类逻辑并扩展 | `super().method()` |
| MRO | 多级继承时查找顺序 | `ClassName.__mro__` |
| isinstance | 判断对象是否属于某类型 | `isinstance(obj, Class)` |

---

[← 上一个:Python 知识](../knowledge/08-oop-封装.md) | [返回目录](../README.md) | [下一个:OOP 多态契约 L3 →](../knowledge/10-oop-多态契约.md)
