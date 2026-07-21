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

**ASCII 内存图 —— @property 的调用**

```
class Product:
    @property
    def price_with_tax(self):
        return self.price * 1.13

p.price_with_tax  ← 没有括号!

调用过程:
  ① Python 看到 p.price_with_tax
  ② 发现它是 @property → 自动调用方法
  ③ 方法返回计算结果
  ④ 看起来就像访问属性一样

对比:
  p.price           → 直接读属性
  p.price_with_tax  → 自动调用方法(看起来也是属性)
```

**关键**:`@property` 让**方法**可以像**属性**一样访问,
不需要写括号 `()`。

```python
# 示例 1:@property 把方法伪装成属性
class Product:
    def __init__(self, title, price):  # 构造函数
        self.title = title              # 绑定 title
        self.price = price              # 绑定 price

    @property
    def price_with_tax(self):           # @property 装饰器
        # 像属性一样访问,但背后是计算
        return self.price * 1.13        # 返回含税价格

# --- 执行过程 ---
# 第 1 行 p = Product("Python 入门", 100):
#   ① 分配新内存,创建 Product 实例
#   ② 自动调用 __init__(self=新对象, title="Python 入门", price=100)
#   ③ self.title = "Python 入门" → 新对象的 title = "Python 入门"
#   ④ self.price = 100 → 新对象的 price = 100
#   ⑤ 创建完毕,把对象赋值给变量 p
#
# 第 2 行 print(p.price_with_tax):
#   ① Python 看到 p.price_with_tax
#   ② 发现它是 @property → 自动调用方法 price_with_tax(self=p)
#   ③ 读取 self.price → 100
#   ④ 计算 100 * 1.13 = 113.0
#   ⑤ 返回 113.0
#   ⑥ 输出: 113.0
#   注意:没有写括号!

p = Product("Python 入门", 100)
print(p.price_with_tax)  # 113.0(没有括号)
print(p.price)           # 100(原始价格)
```

**逐行解剖**

① `def __init__(self, title, price):` 定义构造函数,接收 title 和 price
② `self.title = title` 把参数 title 绑到对象
③ `self.price = price` 把参数 price 绑到对象
④ `@property` 装饰器,写在 `def` 上方,把方法变成属性
⑤ `def price_with_tax(self):` 方法名就是属性名
⑥ `return self.price * 1.13` 返回计算结果
⑦ `p.price_with_tax` **没有括号**,像属性一样访问

**要点**:`@property` 是**只读**的,
不能给它赋值(赋值会报错)。

```python
# 示例 2:用 @property 做数据转换
class Student:
    def __init__(self, name, score):  # 构造函数
        self.name = name                # 绑定 name
        self.score = score              # 绑定 score

    @property
    def level(self):                    # @property 装饰器
        # 根据分数返回等级
        if self.score >= 90:            # 90 分及以上
            return "优秀"               # 返回 "优秀"
        elif self.score >= 60:          # 60-89 分
            return "及格"               # 返回 "及格"
        else:                           # 60 分以下
            return "不及格"             # 返回 "不及格"

# --- 执行过程 ---
# 第 1 行 s = Student("小明", 85):
#   ① 分配新内存,创建 Student 实例
#   ② 自动调用 __init__(self=新对象, name="小明", score=85)
#   ③ self.name = "小明" → 新对象的 name = "小明"
#   ④ self.score = 85 → 新对象的 score = 85
#   ⑤ 创建完毕,把对象赋值给变量 s
#
# 第 2 行 print(s.level):
#   ① Python 看到 s.level
#   ② 发现它是 @property → 自动调用方法 level(self=s)
#   ③ 读取 self.score → 85
#   ④ 85 >= 90? → False
#   ⑤ 85 >= 60? → True → 返回 "及格"
#   ⑥ 输出: 及格
#   注意:没有写括号!

s = Student("小明", 85)
print(s.level)  # 及格(没有括号)
```

**逐行解剖**

① `def __init__(self, name, score):` 定义构造函数
② `self.name = name` 把参数 name 绑到对象
③ `self.score = score` 把参数 score 绑到对象
④ `@property` 装饰器,把方法变成属性
⑤ `def level(self):` 方法名就是属性名
⑥ `if self.score >= 90:` 判断是否 90 分及以上
⑦ `return "优秀"` 返回 "优秀"
⑧ `elif self.score >= 60:` 判断是否 60-89 分
⑨ `return "及格"` 返回 "及格"
⑩ `else:` 60 分以下
⑪ `return "不及格"` 返回 "不及格"
⑫ `s.level` **没有括号**,像属性一样访问

---

**NCDL Break It 演示(@property 反模式)**

```python
# ============ BREAK IT 演示 ============
# 错误 1:试图给只读 @property 赋值
class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price_with_tax(self):
        return self.price * 1.13

p = Product(100)
try:
    p.price_with_tax = 200  # ❌ 试图赋值!
except AttributeError as e:
    print(f"报错: {e}")
    # 输出: 报错: can't set attribute

# 错误 2:调用时加了括号
try:
    result = p.price_with_tax()  # ❌ 加了括号!
except TypeError as e:
    print(f"报错: {e}")
    # 输出: 报错: 'float' object is not callable
# ============ END BREAK IT ============
```

**常见错误**

> 1. **错误现象**:`AttributeError: can't set attribute`
>    **原因:**`@property` 是只读的,不能给它赋值。修正:如果需要写入,加 setter(见下一节)
> 2. **错误现象**:`TypeError: 'float' object is not callable`
>    **原因:**`p.price_with_tax()` 加了括号,但 `@property` 返回的是 float 不是函数。修正:`p.price_with_tax`(不加括号)

> **问自己**:
> - `@property` 的方法能不能有参数?
> - 为什么访问 `@property` 不需要写括号?
> - `@property` 和直接定义属性有什么区别?

---

# ============ 学员代码区 ============
# 请定义 Student 类,包含:
# - __init__ 绑定 name 和 score
# - @property level 返回等级
#   (>=90 优秀, >=60 及格, 否则 不及格)
# 创建学生,打印 s.level。
class Student:
    pass  # 请补全

# s = Student("小明", 85)
pass

# ============ 参考答案 ============
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    @property
    def level(self):
        if self.score >= 90:
            return "优秀"
        elif self.score >= 60:
            return "及格"
        else:
            return "不及格"

s = Student("小明", 85)
print(s.level)  # 及格
