### Day 08 · OOP 基础:让代码"活"起来

> **痛点**:你的代码全是变量和函数,数据和操作分离,越写越乱。今天你将学会"面向对象" —— 把数据和操作绑在一起,就像现实中"对象"一样思考。
> **类比**:OOP 像"造汽车" —— 先设计图纸(类),再按图纸生产汽车(对象);图纸定义和方法,每辆汽车独立运行。
> **解释**:**OOP = 把数据和操作封装成对象**。今天学:class、__init__、self、属性、@property、__str__、继承。

---

#### class 定义类 —— "设计图纸"

> **痛点**:你想创建多个"对象"(比如多个订单),每个对象有相同的属性和方法。
> **类比**:类像"设计图纸",对象是"按图纸造出来的产品" —— 一张图纸可以造无数个产品。
> **解释**:用 `class` 定义类,大驼峰命名;类是创建对象的模板。

```python
# 电商订单系统 —— 定义 Order 类
class Order:
    """订单类(电商系统的核心)"""
    platform = "Lec商城"       # 类属性:所有订单共享

    def __init__(self, order_id, product, price):
        """构造函数:创建订单时自动调用"""
        self.order_id = order_id   # 实例属性:每个订单独立
        self.product = product
        self.price = price
        self.status = "待付款"

# 创建对象(实例化)
order1 = Order("A001", "Python入门", 59.9)
order2 = Order("A002", "算法导论", 128.0)

print(order1.product)          # Python入门
print(order2.product)          # 算法导论
print(Order.platform)          # Lec商城(类属性)
```

**逐行解剖**

- `class Order:` = 定义 Order 类(大驼峰命名)
- `platform = "Lec商城"` = 类属性(所有实例共享)
- `def __init__(self, ...)` = 构造函数,实例化时自动调用
- `self.order_id = order_id` = 实例属性(每个实例独立)
- `Order("A001", ...)` = 创建实例,自动调用 __init__

> **ASCII 类与对象关系图**
> ```
> 类(图纸)              对象(产品)
> ┌──────────┐         ┌──────────┐
> │ Order    │ ──new─▶ │ order1   │
> │          │         │ id: A001 │
│ platform  │         │ 59.9     │
> │ status   │ ──new─▶ │ order2   │
> └──────────┘         │ id: A002 │
>                      │ 128.0    │
>                      └──────────┘
> ```

**常见错误**

> 1. **错误现象**:类名用小驼峰 `order`
>    **原因:**Python 约定类名用大驼峰 `Order`。修正:类名首字母大写
> 2. **错误现象**:忘记写 `self` 参数
>    **原因:**实例方法第一个参数必须是 self。修正:`def __init__(self, ...)`

---

#### __init__ 构造函数 —— 对象的"出生仪式"

> **痛点**:你想在创建对象时自动初始化属性。
> **类比**:__init__ 像"出生仪式" —— 每个对象出生时(创建时),自动执行初始化。
> **解释**:`__init__` 在实例化时自动调用,用于初始化实例属性。

```python
class Order:
    platform = "Lec商城"

    def __init__(self, order_id, product, price):
        print(f"订单 {order_id} 创建成功!")   # 自动执行
        self.order_id = order_id
        self.product = product
        self.price = price
        self.status = "待付款"

# 创建对象时自动调用 __init__
order1 = Order("A001", "Python入门", 59.9)
# 输出:订单 A001 创建成功!

# __init__ 的参数
# self:自动传入(当前对象),不需要手动传
# order_id/product/price:创建时手动传入
order2 = Order("A002", "算法导论", 128.0)
```

**逐行解剖**

- `def __init__(self, ...)` = 构造函数,双下划线(魔术方法)
- `self` = 当前对象的引用(自动传入)
- `self.order_id = order_id` = 把参数赋值给实例属性
- 创建对象时 `__init__` 自动执行,不用手动调用

> **ASCII __init__ 执行流程图**
> ```
> order = Order("A001", "书", 59.9)
>    │
>    ▼
> 自动调用 __init__(self, "A001", "书", 59.9)
>    │
>    ├── self.order_id = "A001"
>    ├── self.product = "书"
>    ├── self.price = 59.9
>    └── self.status = "待付款"
>    │
>    ▼
> 返回创建好的对象
> ```

**常见错误**

> 1. **错误现象**:`__init__` 写了 `return` 返回值
>    **原因:**__init__ 不能返回值(只能返回 None)。修正:去掉 return
> 2. **错误现象**:`Order()` 不传参数报错
>    **原因:**__init__ 需要参数。修正:给 __init__ 参数默认值

---

#### self 实例方法 —— 对象的"行为"

> **痛点**:你想让对象有自己的行为(比如订单可以付款、取消)。
> **类比**:实例方法像"对象的行为" —— 订单能付款、能取消、能查询状态。
> **解释**:实例方法第一个参数是 self,代表当前对象,通过 self 访问实例属性。

```python
class Order:
    platform = "Lec商城"

    def __init__(self, order_id, product, price):
        self.order_id = order_id
        self.product = product
        self.price = price
        self.status = "待付款"

    def pay(self):
        """付款"""
        if self.status == "待付款":
            self.status = "已付款"
            return True
        return False

    def cancel(self):
        """取消订单"""
        if self.status in ("待付款", "已付款"):
            self.status = "已取消"
            return True
        return False

    def get_info(self):
        """获取订单信息"""
        return f"[{self.order_id}] {self.product} ￥{self.price} ({self.status})"

# 使用实例方法
order = Order("A001", "Python入门", 59.9)
print(order.get_info())    # [A001] Python入门 ￥59.9 (待付款)
order.pay()
print(order.get_info())    # [A001] Python入门 ￥59.9 (已付款)
```

**逐行解剖**

- `def pay(self):` = 实例方法,self 代表当前对象
- `self.status = "已付款"` = 修改当前对象的属性
- `order.pay()` = 调用实例方法,self 自动传入(不需要手动传)

> **ASCII self 示意图**
> ```
> order.pay()
>    │
>    ▼
> def pay(self):  ← self = order
>     self.status = "已付款"  ← 修改 order.status
> ```

**常见错误**

> 1. **错误现象**:调用实例方法忘记加括号 `order.pay`
>    **原因:**不加括号得到的是方法对象,不是调用。修正:`order.pay()`
> 2. **错误现象**:实例方法不加 `self` 参数
>    **原因:**实例方法必须第一个参数是 self。修正:`def pay(self):`

---

#### 实例属性 vs 类属性 —— "私有"vs"共享"

> **痛点**:你分不清哪些属性属于每个对象,哪些是共享的。
> **类比**:实例属性像"每个人的名字"(各不相同);类属性像"学校的名字"(大家共享)。
> **解释**:实例属性通过 self 定义,每个实例独立;类属性在类里定义,所有实例共享。

```python
class Order:
    platform = "Lec商城"       # 类属性:所有订单共享
    order_count = 0            # 类属性:统计订单总数

    def __init__(self, order_id, product, price):
        self.order_id = order_id   # 实例属性:每个订单独立
        self.product = product
        self.price = price
        Order.order_count += 1     # 修改类属性

order1 = Order("A001", "书", 59.9)
order2 = Order("A002", "笔", 10.0)

# 类属性:共享
print(Order.order_count)       # 2
print(order1.order_count)      # 2(通过实例访问)
print(order2.order_count)      # 2

# 实例属性:独立
print(order1.product)          # 书
print(order2.product)          # 笔
```

**逐行解剖**

- `platform = "Lec商城"` = 类属性,所有实例共享
- `self.order_id = ...` = 实例属性,每个实例独立
- `Order.order_count += 1` = 通过类名修改类属性
- 通过实例访问类属性:先查实例,再查类

> **ASCII 实例属性 vs 类属性图**
> ```
> 类属性(共享):
> Order.platform = "Lec商城"
> Order.order_count = 2
>
> order1 ──▶ 实例属性: order_id="A001", product="书"
> order2 ──▶ 实例属性: order_id="A002", product="笔"
>
> order1.platform → 找不到实例属性 → 找到类属性 "Lec商城"
> ```

**常见错误**

> 1. **错误现象**:通过实例修改类属性
>    **原因:**`self.order_count = 1` 实际创建了实例属性。修正:`Order.order_count = 1`
> 2. **错误现象**:类属性用可变对象(如列表)
>    **原因:**所有实例共享同一个列表。修正:在 __init__ 里创建

---

#### @property —— 属性的"保护伞"

> **痛点**:你想在设置属性时做校验(比如价格不能为负),或直接访问属性不够安全。
> **类比**:@property 像"安检门" —— 设置属性时自动校验,不合格就拒绝。
> **解释**:@property 把方法变成属性访问,可以加校验逻辑。

```python
class Order:
    def __init__(self, order_id, product, price):
        self.order_id = order_id
        self.product = product
        self.price = price          # 调用 setter

    @property
    def price(self):
        """getter:获取价格"""
        return self._price

    @price.setter
    def price(self, value):
        """setter:设置价格(带校验)"""
        if value < 0:
            raise ValueError("价格不能为负")
        self._price = value

# 使用
order = Order("A001", "书", 59.9)
print(order.price)          # 59.9(像访问属性)
order.price = 49.9          # 修改(调用 setter)
# order.price = -10         # ValueError:价格不能为负
```

**逐行解剖**

- `@property` = 把 price 方法变成属性( getter )
- `@price.setter` = 给 price 加 setter,赋值时自动调用
- `self._price` = 内部存储属性(约定用下划线开头)
- `order.price = 49.9` = 像赋值,实际调用 setter 方法

> **ASCII @property 流程图**
> ```
> order.price       ──▶ @property getter ──▶ 返回 self._price
> order.price = 49  ──▶ @price.setter ──▶ 校验 ──▶ 赋值 self._price
> order.price = -10 ──▶ @price.setter ──▶ 校验失败 ──▶ ValueError
> ```

**常见错误**

> 1. **错误现象**:setter 里直接 `self.price = value` 无限递归
> **原因:**`self.price` 又调用 setter。修正:`self._price = value`
> 2. **错误现象**:只写 getter 没写 setter
>    **原因:**只读属性不能赋值。修正:加 `@属性名.setter`

---

#### __str__ 与 __repr__ —— 对象的"自我介绍"

> **痛点**:打印对象显示 `<Order object at 0x...>`,看不懂。
> **类比**:__str__ 像"名片"(给用户看);__repr__ 像"简历"(给开发者看)。
> **解释**:`__str__` 返回友好的字符串;`__repr__` 返回开发者调试信息。

```python
class Order:
    def __init__(self, order_id, product, price):
        self.order_id = order_id
        self.product = product
        self.price = price
        self.status = "待付款"

    def __str__(self):
        """用户友好的字符串(print 时调用)"""
        return f"订单{self.order_id}: {self.product} ￥{self.price}"

    def __repr__(self):
        """开发者调试信息"""
        return f"Order({self.order_id!r}, {self.product!r}, {self.price})"

order = Order("A001", "Python入门", 59.9)
print(order)                   # 订单A001: Python入门 ￥59.9(__str__)
print(str(order))              # 订单A001: Python入门 ￥59.9
print(repr(order))             # Order('A001', 'Python入门', 59.9)
```

**逐行解剖**

- `__str__` = print()/str() 时调用,面向用户
- `__repr__` = repr()/交互式环境 时调用,面向开发者
- 如果只写 __str__,repr 会 fallback 到 __str__
- `{self.order_id!r}` = 用 repr() 格式化(加引号)

> **ASCII __str__ vs __repr__ 图**
> ```
> print(order)  ──▶ __str__  ──▶ "订单A001: Python入门 ￥59.9"
> repr(order)   ──▶ __repr__ ──▶ "Order('A001', 'Python入门', 59.9)"
> ```

**常见错误**

> 1. **错误现象**:忘了 __str__ 要 return 字符串
>    **原因:**__str__ 必须返回字符串。修正:`return "..."`
> 2. **错误现象**:__str__ 里直接 print
>    **原因:**__str__ 应该 return 而不是 print。修正:用 return

---

#### 继承 —— "子承父业"

> **痛点**:你有多个相似的类(普通订单/VIP 订单),想复用代码。
> **类比**:继承像"儿子继承父亲的财产" —— 子类拥有父类的所有属性和方法,还能自己扩展。
> **解释**:`class 子类(父类):` 继承父类,自动拥有父类的属性和方法。

```python
class Order:
    """父类:普通订单"""
    def __init__(self, order_id, product, price):
        self.order_id = order_id
        self.product = product
        self.price = price
        self.status = "待付款"

    def get_final_price(self):
        return self.price

    def __str__(self):
        return f"订单{self.order_id}: {self.product} ￥{self.get_final_price()}"

class VipOrder(Order):
    """子类:VIP 订单(继承 Order)"""
    def __init__(self, order_id, product, price, discount):
        super().__init__(order_id, product, price)  # 调用父类构造
        self.discount = discount                    # VIP 独有属性

    def get_final_price(self):                      # 重写父类方法
        return self.price * self.discount

# 使用
order = VipOrder("V001", "Python入门", 59.9, 0.8)
print(order)               # 订单V001: Python入门 ￥47.92
```

**逐行解剖**

- `class VipOrder(Order):` = VipOrder 继承 Order
- `super().__init__(...)` = 调用父类的构造函数(复用父类代码)
- `discount` = 子类独有的属性
- `get_final_price()` = 重写父类方法(多态!)

> **ASCII 继承关系图**
> ```
> 父类 Order
> ├── order_id, product, price, status
> ├── get_final_price() → return price
> └── __str__()
>       │
>       ▼ 继承
> 子类 VipOrder
> ├── discount(独有)
> └── get_final_price() → return price * discount(重写)
> ```

**常见错误**

> 1. **Error**:子类 __init__ 没调用 super().__init__
>    **原因:**父类属性没初始化。修正:`super().__init__(...)`
> 2. **错误现象**:子类想访问父类的私有属性 `_属性`
>    **原因:**Python 没有真正的私有,但约定 `_` 开头的不要直接访问

---

#### super() —— "请老爸帮忙"

> **痛点**:子类想调用父类的方法,特别是重写后还想用父类的。
> **类比**:super() 像"跟老爸说'帮我一下'" —— 子类请父类帮忙完成一部分工作。
> **解释**:`super()` 返回父类对象,可以调用父类的方法。

```python
class Order:
    def __init__(self, order_id, product, price):
        self.order_id = order_id
        self.product = product
        self.price = price

    def get_info(self):
        return f"{self.order_id}-{self.product}-￥{self.price}"

class VipOrder(Order):
    def __init__(self, order_id, product, price, discount):
        super().__init__(order_id, product, price)  # 调用父类 __init__
        self.discount = discount

    def get_info(self):
        base = super().get_info()                  # 调用父类 get_info()
        return f"{base} (VIP {self.discount*10}折)"

order = VipOrder("V001", "书", 100, 0.8)
print(order.get_info())    # V001-书-￥100 (VIP 8.0折)
```

**逐行解剖**

- `super().__init__(...)` = 调用父类的 __init__,避免重复代码
- `super().get_info()` = 调用父类的 get_info,在其基础上扩展
- super() 本质是返回父类的代理对象

> **ASCII super() 调用图**
> ```
> VipOrder.get_info()
>    │
>    ├── super().get_info() → 调用父类 → "V001-书-￥100"
>    │
>    └── 在后面追加 " (VIP 8.0折)"
>    │
>    ▼
> "V001-书-￥100 (VIP 8.0折)"
> ```

**常见错误**

> 1. **错误现象**:`super()` 在 Python 2 中写法不同
>    **原因:**Python 2 要 `super(子类, self)`。修正:Python 3 直接 `super()`
> 2. **错误现象**:super() 调用父类不存在的方法
>    **原因:**父类没有这个方法。修正:检查父类定义

---

#### 执行过程跟踪

```python
# --- 电商订单系统执行过程 ---

# class Order:
#     platform = "Lec商城"
#   ① 定义 Order 类,platform 是类属性
#
#     def __init__(self, order_id, product, price):
#         self.order_id = order_id
#   ② __init__ 接收参数,赋值给实例属性

# order = Order("A001", "书", 59.9)
#   ① 创建 Order 实例
#   ② 自动调用 __init__(self, "A001", "书", 59.9)
#   ③ self.order_id = "A001", self.product = "书", self.price = 59.9
#   ④ 返回对象,赋值给 order

# order.pay()
#   ① 调用实例方法 pay(self=order)
#   ② self.status = "已付款"(修改 order 的状态)

# class VipOrder(Order):
#   ① VipOrder 继承 Order,拥有 Order 的所有属性和方法
# super().__init__(...) → 调用父类的 __init__
```

---

#### 常见错误汇总

> 1. **错误现象**:忘记写 `self` 参数
>    **原因:**实例方法第一个参数必须是 self。修正:加上 self
> 2. **错误现象**:`AttributeError: 'Order' object has no attribute 'xxx'`
>    **原因:**属性没在 __init__ 里初始化。修正:`self.xxx = ...`
> 3. **错误现象**:子类没调用 `super().__init__()`
>    **原因:**父类属性没初始化。修正:`super().__init__(...)`
> 4. **错误现象**:setter 里直接赋值 `self.price = value` 导致递归
>    **原因:**赋值又调用 setter。修正:`self._price = value`

---

#### 学员代码区

在 VS Code 新建 `day08.py`,补全下面的代码:

```python
class Order:
    """补全下面的电商订单类"""

    # TODO: 定义 __init__(self, order_id, product, price)


    # TODO: 定义 pay(self) 方法,status 改为"已付款"


    # TODO: 定义 __str__(self) 方法,返回订单信息


# TODO: 创建 VipOrder 子类,继承 Order,添加 discount 属性和重写 get_final_price

```

---

#### 参考答案

```python
class Order:
    platform = "Lec商城"

    def __init__(self, order_id, product, price):
        self.order_id = order_id
        self.product = product
        self.price = price
        self.status = "待付款"

    def pay(self):
        self.status = "已付款"

    def __str__(self):
        return f"{self.order_id}: {self.product} ￥{self.price} ({self.status})"

class VipOrder(Order):
    def __init__(self, order_id, product, price, discount):
        super().__init__(order_id, product, price)
        self.discount = discount

    def get_final_price(self):
        return self.price * self.discount
```

---

## 明日衔接

- 明天 Day 09 学什么:**模块与高级**(import/包/生成器/装饰器)
- 今天遗留的概念:今天学了 OOP 基础,还没学如何组织多文件项目
- 脚手架递进预告:Day 9 在 Day 8 基础上,把电商订单系统拆分成模块和包
