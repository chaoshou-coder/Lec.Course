### Day 11 · OOP 组合 (L4)

> **叙事锚点**:电商订单系统 v2 —— 从继承到组合,像内置类型一样自然

今天让自定义对象**像内置类型一样自然**。
你会学会:组合优于继承、运算符重载、迭代协议、
让 `len(obj)`、`obj1 + obj2`、`for x in obj` 全部可用。

---

**本课知识地图**

| 知识点 | 解决什么问题 |
| --- | --- |
| 组合 vs 继承 | has-a vs is-a,避免强耦合 |
| 继承的三个坏味道 | 什么时候不该用继承 |
| 组合设计 | 复杂对象由简单对象组合而成 |
| 运算符重载本质 | 运算符就是方法的语法糖 |
| __add__ | 让 obj1 + obj2 可用 |
| __len__ | 让 len(obj) 可用 |
| __iter__ | 让 for item in obj 可用 |
| __eq__ | == 比较属性而非地址 |
| __hash__ | 支持放入 set 和 dict |
| __repr__ vs __str__ | 面向开发者 vs 面向用户 |
| 综合练习 | 电商订单系统 v2 |

---

#### 组合 vs 继承 —— is-a 还是 has-a?

> **痛点**

继承用多了,改一处崩一片。
子类和父类**强耦合**,
父类加个参数,所有子类都要跟着改。

> **类比**

- **is-a**:苹果 **是** 一种水果 → 用继承
- **has-a**:订单 **有** 一个购物车 + 收货地址 → 用组合

**判断口诀**:把两个类放进"X 是 Y"和"X 有 Y"各读一遍,
通顺的就是正确关系。

**ASCII 内存图 —— 组合 vs 继承**

```
继承(强耦合):              组合(松耦合):
┌─────────────┐           ┌──────────┐
│ Order       │           │ Order    │
│  └─ 继承 Cart│           │  └─ cart ──→ ┌──────┐
│     └─ items │           │              │ Cart │
└─────────────┘           │  └─ addr ──→ │ Addr │
改 Cart 影响 Order        └──────────┘   └──────┘
                          改 Cart 不影响 Order
```

**关键**:继承时"改底层影响上层",
组合时"改组件不影响容器"。

```python
# 示例 1:继承写法(不推荐)
class Cart:
    def __init__(self):
        self.items = []

class Order(Cart):        # Order is-a Cart? 不通顺!
    def __init__(self, addr):
        super().__init__()
        self.addr = addr

o = Order("北京")
print(o.items)   # []
print(o.addr)    # 北京
```

**逐行解剖**

① `class Order(Cart)` 让 Order 继承 Cart 的全部
② `super().__init__()` 调用父类构造函数
③ 问题:Order 不是 Cart,强行继承导致语义混乱
④ 一旦 Cart 改了构造参数,Order 必须跟着改

```python
# 示例 2:组合写法(推荐)
class Cart:
    def __init__(self):
        self.items = []

class Address:
    def __init__(self, city):
        self.city = city

class Order:
    def __init__(self, addr, cart):
        self.addr = addr    # has-a Address
        self.cart = cart    # has-a Cart

addr = Address("北京")
cart = Cart()
order = Order(addr, cart)
print(order.addr.city)   # 北京
print(order.cart.items)  # []
```

**逐行解剖**

① Order **持有引用** addr 和 cart
② 不复制数据,只引用(省内存)
③ 改 addr.city 会影响 order.addr.city(共享)
④ 这就是组合:**持有引用**,不是**复制数据**

**要点**:组合 = "has-a"关系,
每个类只负责一件事,
复杂对象由简单对象**组合**而成。

**常见错误**

> 1. **错误现象**:`class Order(Cart)` 读作"订单是购物车"
>    **原因:**逻辑不通,应该用组合。修正:`Order` 里组合 `Cart`
> 2. **错误现象**:为了复用两行代码就继承一个大类
>    **原因:**子类拿到一堆不需要的方法。修正:用组合

> **问自己**:
> - "订单"和"购物车"是"是一个"还是"有一个"关系?
> - 如果购物车加了一个 discount 属性,订单类需要跟着改吗?
> - 组合的话,订单怎么访问购物车的商品?

---

#### 继承的三个坏味道 —— 该用组合时用了继承

> **痛点**

看到两个类有相似代码,第一反应就继承。
结果类层次越来越深,改底层崩上层。

> **类比**

继承像"血缘关系"——不能改;
组合像"合作关系"——随时换人。

**三个坏味道**:
1. 子类只用了父类**一小部分**方法
2. 子类**重写**了父类大部分方法
3. 继承层次**超过两层**

```python
# 示例 1:坏味道 1 —— 子类只用父类一小部分
class Animal:
    def eat(self): print("吃")
    def fly(self): print("飞")
    def swim(self): print("游")

class Dog(Animal):
    def fly(self):
        raise NotImplementedError  # 狗不会飞!

d = Dog()
d.eat()   # 吃
# d.fly()  # 报错! 继承了不该继承的
```

**逐行解剖**

① Dog 继承 Animal,拿到 eat/fly/swim 三个方法
② 但狗不会飞,fly 只能抛异常
③ 这说明 Dog 不该继承 Animal,应该拆分
④ 正确做法:把 fly 拆成独立类,组合注入

```python
# 示例 2:坏味道 2 —— 子类重写父类大部分方法
class Report:
    def header(self): return "=== 报告 ==="
    def body(self): return "内容"
    def footer(self): return "=== 结束 ==="

class PDFReport(Report):
    def header(self): return "<pdf header>"   # 重写
    def body(self): return "<pdf body>"       # 重写
    def footer(self): return "<pdf footer>"   # 全重写了!
```

**逐行解剖**

① 三个方法全重写,继承毫无意义
② 应该用组合:Report has-a Renderer
③ 继承只为重写,不如用组合

```python
# 示例 3:坏味道 3 —— 继承层次超过两层
class Animal: pass
class Mammal(Animal): pass
class Dog(Mammal): pass
class SmartDog(Dog): pass    # 已经第四层!
class RobotDog(SmartDog): pass  # 越来越深!
```

**要点**:继承超过两层,改底层时
不知道影响谁,调试地狱。
正确做法:超过两层就该考虑组合。

**常见错误**

> 1. **错误现象**:为了省几行代码就继承
>    **原因:**耦合代价远超复用收益。修正:用组合
> 2. **错误现象**:"未来可能用到"就先继承
>    **原因:**结果"以后"永远不来。修正:需要时再加

> **问自己**:
> - 如果子类只用了父类的 20% 方法,继承合适吗?
> - 重写超过一半方法,是不是该用组合?
> - 继承超过两层,改底层时你能确定影响范围吗?

---

#### 组合设计 —— Order has-a Cart + Payment + Address

> **类比**

订单像一份快递单:它**有**一个地址、**有**一个包裹、
**有**一个付款方式,
但订单本身不是地址也不是包裹。

**设计原则**:每个类只负责一件事,
复杂对象由简单对象**组合**而成。

**ASCII 内存图**

```
order ──→ ┌─────────────────┐
          │ Order           │
          │  addr ──────→ ┌──────────┐
          │  pay  ──────→ │ Address  │
          │  cart ──────→ │ city="北京"│
          └─────────────────┘ └──────────┘
              │
              ├──────→ ┌──────────┐
              │        │ Payment  │
              │        │ method="微信"│
              │        └──────────┘
              └──────→ ┌──────────┐
                       │ Cart     │
                       │ items=[] │
                       └──────────┘
```

**关键**:Order 不复制 addr/pay/cart,
只持有它们的引用(共享,省内存)。

```python
# 示例:组合设计完整实现
class Address:
    def __init__(self, city, detail):
        self.city = city
        self.detail = detail

class Payment:
    def __init__(self, method):
        self.method = method  # "微信"/"支付宝"

class Cart:
    def __init__(self):
        self.items = []

class Order:
    def __init__(self, addr, pay, cart):
        self.addr = addr      # has-a Address
        self.pay = pay        # has-a Payment
        self.cart = cart      # has-a Cart

    def summary(self):
        n = len(self.cart.items)
        return (f"送到{self.addr.city}"
                f"({self.addr.detail}),"
                f"{n}件商品,支付方式{self.pay.method}")

addr = Address("上海", "浦东新区")
pay = Payment("支付宝")
cart = Cart()
cart.items = ["书", "笔"]
order = Order(addr, pay, cart)
print(order.summary())
# 送到上海(浦东新区),2件商品,支付方式支付宝
```

**逐行解剖**

① `self.addr = addr` 把 Address 实例绑到 Order 上
② Order 不复制 addr,只是**引用**它(省内存)
③ `summary()` 通过 self.addr.city 访问地址
④ 通过 self.cart.items 访问商品列表
⑤ 每个类只负责一件事,职责清晰

**要点**:组合让代码松耦合,
改 Address 不需要改 Order,
改 Payment 不需要改 Order,
改 Cart 不需要改 Order。

**常见错误**

> 1. **错误现象**:在 Order 里复制 addr 的数据
>    **原因:**没必要,直接持有引用即可。修正:`self.addr = addr`
> 2. **错误现象**:Order 的太多逻辑直接操作 cart.items
>    **原因:**违反封装。修正:在 Cart 里加方法,Order 调用

> **问自己**:
> - Order 能继承 Address 吗? "订单是地址"通顺吗?
> - 如果支付方式要支持"信用卡",改哪里?
> - 组合后,Order 怎么访问购物车的商品?

---

#### 运算符重载本质 —— 运算符就是方法的语法糖

> **痛点**

`cart1 + cart2` 直接报 TypeError,
因为 Python 不知道两个自定义对象怎么"加"。

> **类比**

`+` 不是魔法,它只是调用 `__add__` 方法的**快捷方式**。
`a + b` 等价于 `a.__add__(b)`。

**核心认知**:所有运算符背后都是**双下划线方法**(魔术方法)。
你想支持什么操作,就实现对应的协议方法。

```python
# 示例:验证运算符就是方法
a = [1, 2]
b = [3, 4]

# 两种写法完全等价
r1 = a + b          # 语法糖
r2 = a.__add__(b)   # 实际调用

print(r1)  # [1, 2, 3, 4]
print(r2)  # [1, 2, 3, 4]
print(r1 == r2)  # True
```

**逐行解剖**

① `a + b` 是**语法糖**,实际调用 `a.__add__(b)`
② 列表的 `__add__` 返回**新列表**,不修改原列表
③ 自定义类没有 `__add__`,所以 `obj1 + obj2` 报错
④ 实现 `__add__` 后,`+` 就自动可用

**要点**:运算符重载的关键是**返回新对象**,
而不是修改原对象(符合不可变语义)。

**常见错误**

> 1. **错误现象**:以为 `+` 会修改原对象
>    **原因:**`a + b` 返回新对象,a 本身不变。修正:返回新对象
> 2. **错误现象**:忘记返回结果
>    **原因:**`__add__` 里没 return,拿到 None。修正:return 新对象

> **问自己**:
> - `a + b` 和 `a.__add__(b)` 完全等价吗?
> - `__add__` 应该返回新对象还是修改 self?
> - 如果 other 不是同类对象,应该怎么处理?

---

#### __add__ —— 合并两辆购物车

> **痛点**

想把两辆购物车的商品合并,只能手动 `extend`。
如果 `cart1 + cart2` 就能合并,代码会自然很多。

> **类比**

`+` 就像把两个购物车的商品**倒在一起**,
返回一辆**新**购物车,两辆原车不变。

> **解释**

实现 `__add__` 方法,定义 `+` 的行为。

**ASCII 内存图**

```
c1 ──→ ┌──────┐      c2 ──→ ┌──────┐
       │ Cart │             │ Cart │
       │items │             │items │
       │ ↓    │             │ ↓    │
       │[苹果,│             │[牛奶] │
       │ 香蕉]│             └──────┘
       └──────┘
              │
              │ c1 + c2 → 调用 __add__
              ↓
       c3 ──→ ┌──────┐
              │ Cart │
              │items │
              │ ↓    │
              │[苹果,│
              │ 香蕉,│
              │ 牛奶]│
              └──────┘
```

**关键**:`__add__` 返回新对象,不修改 self 和 other。

```python
# 示例:__add__ 合并购物车
class Cart:
    def __init__(self, items=None):
        # 默认参数不用可变对象(常见坑)
        self.items = items if items else []

    def __add__(self, other):
        """合并两辆购物车,返回新购物车"""
        if not isinstance(other, Cart):
            return NotImplemented
        # 创建新列表,不修改原对象
        new_items = self.items + other.items
        return Cart(new_items)

c1 = Cart(["苹果", "香蕉"])
c2 = Cart(["牛奶"])
c3 = c1 + c2
print(c1.items)  # ['苹果', '香蕉']  ← 不变!
print(c2.items)  # ['牛奶']          ← 不变!
print(c3.items)  # ['苹果', '香蕉', '牛奶']
```

**逐行解剖**

① `def __add__(self, other)` 定义 `+` 行为
② `isinstance` 检查类型,不匹配返回 NotImplemented
③ `self.items + other.items` 调用列表的 `__add__`
④ `return Cart(new_items)` 返回**新**购物车
⑤ 不修改 self 和 other,符合**不可变语义**

**要点**:`__add__` 的核心是**返回新对象**,
让 `+` 的行为和内置类型一致。

**常见错误**

> 1. **错误现象**:修改原对象
>    **原因:**`self.items.extend(other.items)` 然后 return self —— 这修改了 c1。修正:返回新对象
> 2. **错误现象**:忘记返回
>    **原因:**`__add__` 里只合并没 return,c3 拿到 None。修正:return Cart(new_items)
> 3. **错误现象**:共享引用
>    **原因:**`new_items = self.items` 然后 extend,修改 new_items 会影响原购物车。修正:创建新列表

> **问自己**:
> - `__add__` 应该返回新对象还是修改 self?
> - 为什么 `self.items + other.items` 不会修改原列表?
> - 如果 other 不是 Cart 实例,应该怎么报错?

---

#### __len__ —— 让 len(cart) 返回件数

> **痛点**

`len(cart)` 报错,因为 Python 不知道自定义对象
的"长度"是什么。必须 `len(cart.items)` 才行。

> **类比**

`len()` 像问"这箱苹果有几个?",
实现 `__len__` 就是告诉 Python 怎么数。

> **解释**

实现 `__len__` 方法,返回对象的"长度"。

```python
# 示例:__len__ 让 len(cart) 可用
class Cart:
    def __init__(self, items=None):
        self.items = items if items else []

    def __len__(self):
        """返回商品件数"""
        return len(self.items)

c = Cart(["苹果", "香蕉", "牛奶"])
print(len(c))       # 3
print(c.__len__())  # 3 (等价写法)
```

**逐行解剖**

① `def __len__(self)` 必须返回**整数**
② `len(c)` 等价于 `c.__len__()`
③ 返回 0 表示空对象,Python 视其为**假值**
④ `if cart:` 等价于 `if len(cart) > 0:`

**要点**:有了 `__len__`,对象就能用于
`len()`、`bool()`、`if obj:` 等场景。

**常见错误**

> 1. **错误现象**:返回非整数
>    **原因:**`return self.items` 返回列表,len() 报 TypeError。修正:`return len(self.items)`
> 2. **错误现象**:返回负数
>    **原因:**`__len__` 返回负数会报 ValueError。修正:确保非负

> **问自己**:
> - `__len__` 必须返回什么类型?
> - `if cart:` 背后调用的是什么方法?
> - 空购物车 `len(cart)` 应该返回几?

---

#### __iter__ —— 让 for item in cart 遍历

> **痛点**

`for item in cart` 报错,因为 Python 不知道
怎么"逐个取出"自定义对象的元素。

> **类比**

`__iter__` 像给 Python 一个**迭代器**,
告诉它"每次取一个,取完为止"。

> **解释**

实现 `__iter__` 方法,让对象可迭代。

**两种实现方式**:
1. **yield 生成器**(简单):`__iter__` 里 yield 每个元素
2. **返回迭代器对象**(标准):`__iter__` 返回带 `__next__` 的对象

```python
# 示例 1:__iter__ 用 yield 实现
class Cart:
    def __init__(self, items=None):
        self.items = items if items else []

    def __iter__(self):
        """用 yield 逐个返回元素"""
        for item in self.items:
            yield item

c = Cart(["苹果", "香蕉", "牛奶"])
for item in c:
    print(item)
# 苹果
# 香蕉
# 牛奶
```

**逐行解剖**

① `yield item` 把 `__iter__` 变成**生成器函数**
② `for x in obj` 等价于 `for x in obj.__iter__()`
③ 没有元素时抛出 StopIteration,循环结束
④ 有了 `__iter__`,也自动支持 `list(cart)`、`tuple(cart)`

```python
# 示例 2:__iter__ 返回迭代器(更简洁)
class Cart:
    def __init__(self, items=None):
        self.items = items if items else []

    def __iter__(self):
        """直接委托给列表的 __iter__"""
        return iter(self.items)

c = Cart(["苹果", "香蕉"])
it = iter(c)       # 等价于 c.__iter__()
print(next(it))    # 苹果
print(next(it))    # 香蕉
```

**要点**:`return iter(self.items)` 是最简洁的写法,
直接委托给列表的迭代器。

**常见错误**

> 1. **错误现象**:返回列表而非迭代器
>    **原因:**`return self.items` 不报错,但语义不对。修正:`return iter(self.items)`
> 2. **错误现象**:忘记 yield
>    **原因:**`__iter__` 里写 `return item`,只返回一个元素就结束。修正:用 yield

> **问自己**:
> - `for x in obj` 背后调用的是什么方法?
> - yield 和 return 在 `__iter__` 里有什么区别?
> - 为什么 `return iter(self.items)` 比 `return self.items` 好?

---

#### __eq__ —— 同款判定(购物车去重)

> **痛点**

两个商品属性完全相同,`==` 仍返回 False。
因为默认 `==` 比较的是**内存地址**(is),不是属性值。

> **类比**

超市里两瓶同款矿泉水,**不是同一瓶**(is 不同),
但**是同款**(== 应该 True)。

> **解释**

实现 `__eq__` 方法,定义 `==` 的行为。

```python
# 示例:__eq__ 让 == 比较 SKU
class Product:
    def __init__(self, sku, name, price):
        self.sku = sku      # 货号:唯一标识
        self.name = name
        self.price = price

    def __eq__(self, other):
        """SKU 相同 = 同款"""
        if not isinstance(other, Product):
            return NotImplemented
        return self.sku == other.sku

p1 = Product("A001", "矿泉水", 2.0)
p2 = Product("A001", "矿泉水", 2.0)
p3 = Product("B002", "面包", 5.0)

print(p1 == p2)   # True  (同款)
print(p1 == p3)   # False (不同款)
print(p1 is p2)   # False (不是同一个对象)
```

**逐行解剖**

① `def __eq__(self, other)` 定义 `==` 行为
② `isinstance` 检查类型,不同类型返回 NotImplemented
③ `return self.sku == other.sku` 只比较 SKU
④ `is` 永远比较地址,不受 `__eq__` 影响

**要点**:`__eq__` 的核心是**类型检查** + **属性比较**,
类型不匹配时返回 NotImplemented 而不是 False。

**常见错误**

> 1. **错误现象**:忘记类型检查
>    **原因:**`return self.sku == other.sku`,当 other 不是 Product 时,访问 other.sku 会 AttributeError。修正:先 isinstance 检查
> 2. **错误现象**:返回 NotImplemented 而非 False
>    **原因:**类型不匹配时返回 NotImplemented,让 Python 尝试反向调用。这是正确做法

> **问自己**:
> - `==` 和 `is` 有什么区别?
> - 为什么 `__eq__` 里要先检查类型?
> - 如果两个商品价格不同但 SKU 相同,算同款吗?

---

#### __hash__ —— 支持放入 set 和 dict

> **痛点**

实现了 `__eq__` 后,对象能比较了,
但放入 `set` 报错:unhashable type。

> **类比**

`__hash__` 像给对象一个"身份证号",
set/dict 用它快速查找。
同款商品应该有**相同**的身份证号。

> **解释**

实现 `__hash__` 方法,让对象可哈希。

**黄金法则**:如果 `a == b`,那么 `hash(a) == hash(b)`。

**ASCII 内存图 —— set 去重原理**

```
set 内部结构:
┌─────────────────────────────┐
│ 哈希桶                       │
│  hash("A001") → [p1, p2]   │  ← __eq__ 判定重复
│  hash("B002") → [p3]       │
└─────────────────────────────┘

添加 p2 时:
  ① hash("A001") 找到桶 [p1]
  ② p1 == p2? → True → 不添加
```

**关键**:相等的对象必须有相等的哈希值(契约!)。

```python
# 示例:__hash__ 让 Product 支持 set 去重
class Product:
    def __init__(self, sku, name):
        self.sku = sku
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.sku == other.sku

    def __hash__(self):
        """用 SKU 的哈希值作为对象的哈希值"""
        return hash(self.sku)

p1 = Product("A001", "矿泉水")
p2 = Product("A001", "矿泉水")
p3 = Product("B002", "面包")

products = {p1, p2, p3}
print(len(products))  # 2 (p1 和 p2 同款,去重)
```

**逐行解剖**

① `def __hash__(self)` 必须返回整数
② `hash(self.sku)` 复用字符串的哈希函数
③ 相等的对象必须有相等的哈希值(契约!)
④ 只实现 `__eq__` 不实现 `__hash__`,对象不可哈希

**要点**:`__eq__` 和 `__hash__** 必须同时实现,
否则对象不能放入 set 或作为 dict 的键。

**常见错误**

> 1. **错误现象**:只实现 `__eq__` 不实现 `__hash__`
>    **原因:**Python 自动把 `__hash__` 设为 None,对象不可哈希。修正:同时实现 __hash__
> 2. **错误现象**:哈希值依赖可变属性
>    **原因:**用 `hash(self.price)`,改了 price 后哈希值变了,set 里找不到它。修正:用不可变属性

> **问自己**:
> - 为什么 `__eq__` 和 `__hash__` 必须同时实现?
> - 如果两个对象相等,它们的哈希值必须满足什么条件?
> - 为什么不能用列表(可变)做哈希的依据?

---

#### __repr__ vs __str__ —— 面向开发者 vs 面向用户

> **痛点**

`print(对象)` 打印 `<__main__.Product at 0x...>`,
调试时完全看不出对象里装了什么。

> **类比**

- `__repr__` = 开发者的"X 光片":精确、无歧义
- `__str__` = 用户的"商品标签":友好、可读

> **解释**

- `repr(obj)` → 调用 `__repr__`,给开发者看
- `str(obj)` / `print(obj)` → 调用 `__str__`,给用户看
- 如果只实现 `__repr__`,`__str__` 默认用它

```python
# 示例:__repr__ vs __str__
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        """面向开发者:精确、能还原对象"""
        return f"Product(name={self.name!r}, price={self.price})"

    def __str__(self):
        """面向用户:友好可读"""
        return f"{self.name} ￥{self.price:.2f}"

p = Product("苹果", 5.0)
print(p)          # 苹果 ￥5.00  (调用 __str__)
print(repr(p))    # Product(name='苹果', price=5.0)
```

**逐行解剖**

① `__repr__` 返回**能还原对象**的字符串(给开发者)
② `__str__` 返回**用户友好**的字符串(给终端用户)
③ `!r` 在 f-string 里调用 `repr(self.name)`,加引号
④ 列表/字典显示元素时用 `__repr__`,不是 `__str__`

**要点**:建议**至少实现 `__repr__`**,
因为它是调试时最常用的。

**常见错误**

> 1. **错误现象**:只实现 `__str__` 不实现 `__repr__`
>    **原因:**`repr(obj)` 仍显示默认地址,调试时不方便。修正:至少实现 __repr__
> 2. **错误现象**:返回非字符串
>    **原因:**`return self.price` 会 TypeError。修正:返回 str

> **问自己**:
> - `print(obj)` 和 `repr(obj)` 分别调用什么方法?
> - 为什么建议至少实现 `__repr__`?
> - `__repr__` 的理想格式是什么?

---

#### 协议总结 —— 想支持什么操作就实现什么协议

> **核心认知**

Python 的"魔法"都是**协议**。
运算符、内置函数、语法糖,
背后都在查找对应的**双下划线方法**。

**常用协议速查表**:

| 你想支持 | 实现方法 | 触发方式 |
| --- | --- | --- |
| `a + b` | `__add__` | 加法运算 |
| `a == b` | `__eq__` | 相等比较 |
| `len(obj)` | `__len__` | 求长度 |
| `for x in obj` | `__iter__` | 迭代遍历 |
| `obj[k]` | `__getitem__` | 索引访问 |
| `print(obj)` | `__str__` | 用户输出 |
| `repr(obj)` | `__repr__` | 开发者输出 |
| `hash(obj)` | `__hash__` | set/dict 键 |
| `bool(obj)` | `__bool__` | 真假判断 |
| `a < b` | `__lt__` | 小于比较 |

**协议之间的关系**

```
┌─────────────────────────────────────────┐
│           让对象像内置类型一样自然         │
├─────────────┬───────────────────────────┤
│ 容器协议     │ __len__ + __iter__        │
│             │ → len() 和 for 循环        │
├─────────────┼───────────────────────────┤
│ 比较协议     │ __eq__ + __hash__         │
│             │ → == 和 set 去重           │
├─────────────┼───────────────────────────┤
│ 数值协议     │ __add__ / __sub__         │
│             │ → + / - 运算符             │
├─────────────┼───────────────────────────┤
│ 字符串协议   │ __str__ / __repr__        │
│             │ → print() / repr()         │
└─────────────┴───────────────────────────┘
```

**设计口诀**:先想"用户会怎么用这个对象",
再决定实现哪些协议。

> **问自己**:
> - 如果想让 `obj[key]` 可用,要实现什么方法?
> - 如果想让对象能排序,要实现什么方法?
> - 为什么实现了 `__iter__` 就能用 `list(obj)`?

---

#### 综合练习 —— 电商订单系统 v2

现在把**组合、运算符重载、迭代协议、比较协议**
串成一个真实业务系统。

**需求清单**:
1. `Product` 用 `@property` 保护 price
2. `Book` / `Food` 继承 `Product`(Day09)
3. `describe()` 方法多态(Day10)
4. `Cart` 组合多个 `Product`
5. `__add__` 合并购物车
6. `__len__` 返回件数
7. `__iter__` 遍历商品
8. `__eq__` 同款判定
9. `__repr__` 调试输出
10. `__hash__` 支持 set 去重

```python
# 示例:电商订单系统 v2 完整实现
import abc

class Product(abc.ABC):
    """抽象基类"""
    def __init__(self, sku, name, price):
        self.sku = sku
        self.name = name
        self.price = price  # 触发 setter

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("价格不能为负")
        self._price = value

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.sku == other.sku

    def __hash__(self):
        return hash(self.sku)

    def __repr__(self):
        return (f"{type(self).__name__}"
                f"(sku={self.sku!r}, name={self.name!r}, "
                f"price={self.price})")

    @abc.abstractmethod
    def describe(self):
        pass

class Book(Product):
    def describe(self):
        return f"图书《{self.name}》￥{self.price}"

class Food(Product):
    def describe(self):
        return f"食品[{self.name}] ￥{self.price}"

class Cart:
    def __init__(self, items=None):
        self.items = list(items) if items else []

    def __add__(self, other):
        if not isinstance(other, Cart):
            return NotImplemented
        return Cart(self.items + other.items)

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    def __repr__(self):
        return f"Cart({self.items!r})"

# 测试
b = Book("B001", "Python 入门", 59.9)
f = Food("F001", "面包", 8.5)
c1 = Cart([b, f])
c2 = Cart([b])
c3 = c1 + c2
print(f"共 {len(c3)} 件")
for item in c3:
    print(item.describe())
print(repr(c3))
```

**逐行解剖**

① Product 用 @property 保护 price
② Book/Food 继承 Product,实现 describe()
③ Cart 组合多个 Product
④ `__add__` 合并购物车,返回新对象
⑤ `__len__` 返回件数
⑥ `__iter__` 遍历商品
⑦ `__eq__` + `__hash__` 同款判定 + set 去重
⑧ `__repr__` 调试输出

**要点**:这个案例综合了 Day08-11 全部知识,
是 OOP L1-L4 的"最小完整案例"。

> **问自己**(综合练习前先思考):
> - 这个类用到了今天学的哪些知识点?
> - 为什么 __add__ 要返回新对象?
> - __eq__ 和 __hash__ 为什么必须同时实现?
> - 如果想让 Cart 支持 obj[key],要实现什么方法?

---

#### 练习指导

完成下面的练习,巩固今天学的知识点。

**当堂练**(必做):
- 打开 `exercises/11-oop-组合/practice01.py` —— 组合 vs 继承
- 打开 `exercises/11-oop-组合/practice02.py` —— __add__ 合并购物车
- 打开 `exercises/11-oop-组合/practice03.py` —— __len__ 返回件数
- 打开 `exercises/11-oop-组合/practice04.py` —— __iter__ 遍历商品
- 打开 `exercises/11-oop-组合/practice05.py` —— __eq__ 同款判定
- 打开 `exercises/11-oop-组合/practice06.py` —— __hash__ 支持 set 去重

**课后作业**(选做):
- 打开 `exercises/11-oop-组合/task01.py` —— __repr__ 调试输出
- 打开 `exercises/11-oop-组合/task02.py` —— 组合设计:订单系统
- 打开 `exercises/11-oop-组合/task03.py` —— 综合项目:电商订单系统 v2

**参考答案**:在 `solutions/11-oop-组合/` 下找到对应答案。

---

#### 今日小结

| 概念 | 解决的痛点 | 关键方法 |
| --- | --- | --- |
| 组合 vs 继承 | has-a 不用继承 | 持有引用 |
| 继承三个坏味道 | 避免错误继承 | is-a 判断 |
| 组合设计 | 复杂对象拆简单 | 注入实例 |
| 运算符重载本质 | 运算符是语法糖 | `__add__` 等 |
| `__add__` | 合并两个对象 | 返回新对象 |
| `__len__` | len(obj) 可用 | 返回整数 |
| `__iter__` | for x in obj | yield/返回迭代器 |
| `__eq__` | == 比较属性 | 类型检查 |
| `__hash__` | 支持 set/dict | 与 __eq__ 一致 |
| `__repr__` vs `__str__` | 调试 vs 显示 | 至少实现 repr |
| 协议总结 | 统一认知 | 查表实现 |

---

[← 上一个:Python 知识](../knowledge/10-oop-多态契约.md) | [返回目录](../README.md) | [下一个:Day 12 →](../knowledge/12-模块与包.md)
