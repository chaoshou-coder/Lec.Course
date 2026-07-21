### Day 10 · OOP 多态契约 (L3)

> **叙事锚点**:电商支付系统 —— 从 if-elif 到多态

今天进入 OOP 最强大的武器:**多态**与**契约**。
你会学会:用同一接口处理不同对象、用 abc 强制子类履约。

---

**本课知识地图**

| 知识点 | 解决什么问题 |
| --- | --- |
| 痛点:if-elif 灾难 | 每新增一种支付都要改核心函数 |
| 鸭子类型 | 不写继承也能多态,看"有没有这个方法" |
| Break It:鸭子类型的代价 | 漏写方法不会提前报错 |
| abc.ABC 抽象基类 | 把"必须实现"写进契约 |
| @abstractmethod | 标记必须实现的方法,否则实例化报错 |
| 接口概念 | 团队协作的契约,Python 用 ABC 模拟 |
| 鸭子类型 vs abc.ABC | 灵活 vs 安全,根据项目规模选择 |
| 综合:Payment 支付系统 | 把全部知识点串成一个真实系统 |

---

#### 痛点:if-elif 灾难

> **痛点**

假设你要写一个支付函数,
支持支付宝/微信/银行卡。
如果用 if-elif 类型分发,代码每加一种支付
都要改核心函数,越来越长,越来越难维护。

> **类比**

交通检查站:每过一辆车就检查一次"车型",
是货车? 是客车? 是摩托车?
检查流程越来越长,车队越堵越长。

> **解释**

类型和逻辑耦合在一起,函数越来越长,
阅读/维护成本指数上升。

```python
# 示例 1:120 行 if-elif 的灾难
def pay(payment_type, amount):
    if payment_type == "alipay":
        # 30 行支付宝逻辑
        print(f"支付宝支付 {amount} 元")
    elif payment_type == "wechat":
        # 30 行微信逻辑
        print(f"微信支付 {amount} 元")
    elif payment_type == "bank":
        # 30 行银行卡逻辑
        print(f"银行卡支付 {amount} 元")
    else:
        raise ValueError("未知支付类型")

pay("alipay", 99.0)
pay("wechat", 50.0)
```

**逐行解剖**

① if-elif 链:每新增一种支付都要**改这个函数**
② 函数越来越长,阅读/维护成本指数上升
③ 测试要覆盖所有分支,新增一种就要加测试
④ **核心问题**:类型和逻辑耦合在一起

**3 个致命问题**:
1. **新增 = 改核心**:加一种支付方式必须动 `pay` 函数
2. **函数膨胀**:120 行 if-else,改一行可能引入 3 个 bug
3. **测试爆炸**:N 种支付 × M 种场景 = N×M 个用例

**今天的目标**:`pay` 函数缩小到 4 行,
新增支付方式只需**加文件**。

```python
# 示例 2:重构思路 —— 把每种支付抽取成类
class Alipay:
    def execute(self, amount):
        return f"支付宝支付 {amount} 元"

class WeChatPay:
    def execute(self, amount):
        return f"微信支付 {amount} 元"

class BankPay:
    def execute(self, amount):
        return f"银行卡支付 {amount} 元"

# 调用时直接 execute,不判断类型
alipay = Alipay()
wechat = WeChatPay()
bank = BankPay()
print(alipay.execute(99.0))   # 支付宝支付 99.0 元
print(wechat.execute(50.0))   # 微信支付 50.0 元
print(bank.execute(200.0))    # 银行卡支付 200.0 元
```

**逐行解剖**

① 三个类**没有继承同一个父类**
② 但它们都有 `execute` 方法 → 这就是多态的基础
③ 调用时直接 `obj.execute()`,不需要 if-elif
④ 新增一种支付?再加一个类即可,**原有代码零修改**

**要点**:核心洞察是"每种支付都有共同行为",
与其用 if-elif 判断类型,
不如让每种支付**自己知道怎么支付**。

**常见错误**

> 1. **错误现象**:以为多态必须继承
>    **原因:**Python 的多态基于鸭子类型,不强制继承。有同名方法就行
> 2. **错误现象**:方法名不一致
>    **原因:**有人写 `execute`,有人写 `pay`。约定好方法名

> **问自己**(先思考,再看下面的参考答案):
> - if-elif 方案的核心问题是什么?
> - 重构后,新增一种支付要改哪些代码?
> - 三个类没有继承同一个父类,为什么还能多态?

---

#### 鸭子类型 (Duck Typing) —— 不写继承也能多态

> **痛点**

鸭子类型的致命弱点:**漏写方法不会提前报错**。
代码能创建对象,能调用函数,
直到**运行到那一行**才爆炸。

> **类比**

"像鸭子就是鸭子":走路像鸭子、叫声像鸭子,
它就是鸭子,不管它**继承自谁**。
Python 只看"有没有这个方法"。

> **解释**

Python 不关注对象是哪个类的实例,
只关心"**有没有这个方法**"。
只要对象有 `execute` 方法,就能传给 `checkout`。

**ASCII 内存图 —— 鸭子类型调用链**

```
checkout(99.0, Alipay())
    │
    ▼
payment = Alipay 实例
    │
    ▼
payment.execute(99.0)
    │
    ▼
Alipay.execute(self=实例, amount=99.0)
    │
    ▼
返回 "支付宝支付 99.0 元"

关键:checkout 不关心 payment 是哪个类
只要它有 execute 方法就行 → 鸭子类型
```

**关键**:调用方只调用 `execute`,不判断类型,
传入任何有 `execute` 的对象都能工作。

```python
# 示例 1:鸭子类型 —— checkout 不判断类型
class Alipay:
    def execute(self, amount):
        return f"支付宝支付 {amount} 元"

class WeChatPay:
    def execute(self, amount):
        return f"微信支付 {amount} 元"

def checkout(cart_total, payment):
    # payment 可以是任何有 execute 方法的对象
    return payment.execute(cart_total)

print(checkout(99.0, Alipay()))     # 支付宝支付 99.0 元
print(checkout(50.0, WeChatPay()))  # 微信支付 50.0 元
```

**逐行解剖**

① `checkout` 函数**不判断类型**,只调用 `payment.execute`
② 传入 `Alipay()` → 执行支付宝逻辑
③ 传入 `WeChatPay()` → 执行微信逻辑
④ **完全去掉 if-elif**!新增支付方式无需修改 `checkout`

```python
# 示例 2:甚至可以是"临时"的类 —— 鸭子类型的灵活性
class CreditCard:
    def execute(self, amount):
        return f"信用卡支付 {amount} 元"

class Bitcoin:
    def execute(self, amount):
        return f"比特币支付 {amount} 元"

def checkout(cart_total, payment):
    result = payment.execute(cart_total)
    print(f"支付结果: {result}")
    return result

for p in [CreditCard(), Bitcoin()]:
    checkout(100.0, p)
```

**逐行解剖**

① CreditCard 和 Bitcoin 都是"临时"写的类
② 不继承任何父类,但都有 execute 方法
③ checkout 来者不拒,照单全收
④ 灵活性极高,但也**失去了保护**

**要点**:鸭子类型的优势是灵活,
劣势是不安全 —— 漏写方法不会提前报错。

**常见错误**

> 1. **错误现象**:拼写错误 `execte` vs `execute`
>    **原因:**不报错,运行才炸。修正:仔细检查方法名
> 2. **错误现象**:参数不一致
>    **原因:**`execute(self, amount, currency)` 调用时参数不匹配。修正:统一签名

> **问自己**:
> - 鸭子类型在什么场景下会变成"坑"?
> - 如果团队 10 个人写支付类,怎么保证每个人都写了 execute?
> - 能不能在创建对象时就检查,而不是等到调用时才报错?

---

#### Break It:鸭子类型的代价 —— 漏写方法不报错

> **NCDL 负案例演示**

鸭子类型的致命弱点:**漏写方法不会提前报错**。
代码能创建对象,能调用函数,
直到**运行到那一行**才爆炸。

```python
# ============ BREAK IT 演示 ============
class BrokenAlipay:
    # 注意:execute 方法被漏写了!
    pass

def checkout(total, payment):
    return payment.execute(total)

alipay = BrokenAlipay()
print("创建成功,一切看似正常...")
try:
    checkout(99.0, alipay)
except AttributeError as e:
    print(f"报错: {e}")
    print("错误在运行中才暴露,难以追溯!")
# ============ END BREAK IT ============
```

**逐行解剖**

① `BrokenAlipay` 没有 `execute` 方法 → 但**创建不报错**
② `alipay = BrokenAlipay()` 成功 → 看起来一切正常
③ `checkout(99.0, alipay)` → 调用 `payment.execute`
④ `AttributeError` → 此时才暴露问题
⑤ **问题**:bug 在**运行时**才出现,可能藏很久

**结论**:个人脚本用鸭子类型 OK,
但团队项目需要**更强的保护**。

**常见错误**

> 1. **错误现象**:漏写方法,创建成功,调用才失败
>    **原因:**鸭子类型没有强制检查。修正:用 abc.ABC
> 2. **错误现象**:方法名拼写错误,运行时报 AttributeError
>    **原因:**Python 不检查方法名。修正:用 abc 强制

> **问自己**:
> - 为什么漏写方法不会提前报错?
> - 这种"运行时才暴露"的问题有什么危害?
> - 能不能在实例化时就检查?

---

#### abc.ABC 抽象基类 —— 把"必须实现"写进契约

> **痛点**

鸭子类型灵活但不安全,团队项目需要
"漏写方法就提前报错"的保护机制。

> **类比**

国家发布 USB-C 接口规范:
每个厂商的设备必须有 type-c 口。
不符合规范 → 不准上市。

> **解释**

- `abc.ABC` 作为父类 → 类成为**抽象基类**
- `@abstractmethod` 装饰的方法 → 子类**必须实现**
- 漏写 → **实例化时报 TypeError**,而不是运行时

**ASCII 内存图 —— 抽象基类**

```
Payment(abc.ABC)
    │
    ├── execute (抽象方法,未实现)
    │
    └── 不能直接实例化!
        │
        ▼
    TypeError: Can't instantiate abstract class
               Payment with abstract method execute

子类必须实现 execute 才能实例化
```

**关键**:抽象基类是"图纸",不能直接用,
必须通过子类实现所有抽象方法后才能用。

```python
# 示例 1:abc.ABC 基本用法
import abc

class Payment(abc.ABC):
    @abc.abstractmethod
    def execute(self, amount):
        ...

try:
    p = Payment()
except TypeError as e:
    print(f"报错: {e}")
```

**逐行解剖**

① `class Payment(abc.ABC)` → 继承 abc.ABC,成为抽象基类
② `@abc.abstractmethod` → 标记 execute 为抽象方法
③ `Payment()` → 尝试实例化 → TypeError
④ 错误信息明确告诉你:哪些方法没实现

```python
# 示例 2:子类实现抽象方法后才能实例化
import abc

class Payment(abc.ABC):
    @abc.abstractmethod
    def execute(self, amount):
        ...

class Alipay(Payment):
    def execute(self, amount):
        return f"支付宝支付 {amount} 元"

class WeChatPay(Payment):
    def execute(self, amount):
        return f"微信支付 {amount} 元"

alipay = Alipay()
wechat = WeChatPay()
print(alipay.execute(99.0))   # 支付宝支付 99.0 元
print(wechat.execute(50.0))   # 微信支付 50.0 元
```

**逐行解剖**

① `Alipay(Payment)` 继承抽象基类 → 必须实现 execute
② `def execute(self, amount)` → 提供实现 → 契约满足
③ `Alipay()` → 检查通过 → 实例化成功
④ `alipay.execute(99.0)` → 调用子类实现

**要点**:`@abstractmethod` 是 Python 的"契约标记",
标记后该方法**只有签名,没有实现**,
子类**必须**提供实现,否则实例化时报错。

**常见错误**

> 1. **错误现象**:忘记继承 abc.ABC
>    **原因:**`@abstractmethod` 单独使用无效。修正:`class Payment(abc.ABC)`
> 2. **错误现象**:子类漏写方法,实例化时报 TypeError
>    **原因:**这是**正确行为**!错误信息会告诉你缺哪个方法

> **问自己**:
> - 为什么单独用 `@abstractmethod` 没有效果?
> - abc.ABC 在背后做了什么检查?
> - 如果团队有人忘了继承 abc.ABC,怎么发现?

---

#### Break It:@abstractmethod 必须配合 abc.ABC

> **NCDL 负案例演示**

你用了 `@abstractmethod`,但忘了继承 abc.ABC。
"能跑",但漏写 execute 不报错 →
鸭子类型的弱点又回来了!

```python
# ============ BREAK IT 演示 ============
import abc

class BrokenPayment:  # 没有 abc.ABC! BREAK IT!
    @abc.abstractmethod
    def execute(self, amount):
        ...

class Alipay(BrokenPayment):
    pass  # 漏写 execute!

alipay = Alipay()  # 竟然不报错!
print("没报错!但 execute 不存在,运行时才爆炸")
try:
    alipay.execute(99)
except AttributeError as e:
    print(f"运行时报错: {e}")
# ============ END BREAK IT ============
```

**逐行解剖**

① `class BrokenPayment:` 没有继承 abc.ABC → 不是抽象基类
② `@abstractmethod` 装饰器**单独使用无效**
③ `Alipay(BrokenPayment)` → 没有强制检查
④ `Alipay()` → 实例化成功 → 看起来正常
⑤ `alipay.execute(99)` → AttributeError → 运行时才暴露

**关键结论**:
`@abstractmethod` + `abc.ABC` **必须一起用**!
- 只有 `@abstractmethod` → 装饰器空操作,无强制力
- 只有 `abc.ABC` → 没有抽象方法,类可以实例化
- 两者结合 → 真正的契约保护

> **问自己**:
> - 为什么单独用 `@abstractmethod` 没有效果?
> - abc.ABC 在背后做了什么检查?
> - 如果团队有人忘了继承 abc.ABC,怎么发现?

---

#### 接口概念 —— 团队协作的契约

> **痛点**

多人协作时,需要明确"每个类必须实现哪些方法",
否则各自为政,集成时才发现对不上。

> **类比**

接口 = 合同条款,实现类 = 签约方。
合同只写"乙方必须做什么",不管"怎么做"。

> **解释**

- **接口** = 只包含抽象方法的抽象类
- Python 用"全抽象方法的 ABC"模拟接口
- 接口**不实现任何方法**,只定义"必须做什么"
- 子类**实现接口**,提供具体行为

**ASCII 内存图 —— 接口定义**

```
Notifier(abc.ABC)  ← 接口(全部抽象)
    │
    ├── send (抽象) ── 子类必须实现
    └── channel (抽象) ── 子类必须实现

不能实例化!只能被实现。
```

**关键**:接口是"纯契约",不包含任何实现,
所有方法都是抽象的,子类必须全部实现。

```python
# 示例 1:定义接口
import abc

class Notifier(abc.ABC):
    @abc.abstractmethod
    def send(self, msg):
        ...

    @abc.abstractmethod
    def channel(self):
        ...

try:
    n = Notifier()
except TypeError as e:
    print(f"接口不能实例化: {e}")
```

**逐行解剖**

① `Notifier(abc.ABC)` → 抽象基类
② 所有方法都标记 `@abstractmethod` → 这就是**接口**
③ `Notifier()` → 不能实例化 → 错误信息列出所有抽象方法
④ 子类必须实现 `send` 和 `channel` 才能实例化

```python
# 示例 2:实现接口
import abc

class Notifier(abc.ABC):
    @abc.abstractmethod
    def send(self, msg):
        ...

    @abc.abstractmethod
    def channel(self):
        ...

class EmailNotifier(Notifier):
    def send(self, msg):
        return f"邮件: {msg}"

    def channel(self):
        return "email"

class SMSNotifier(Notifier):
    def send(self, msg):
        return f"短信: {msg}"

    def channel(self):
        return "sms"

for n in [EmailNotifier(), SMSNotifier()]:
    print(f"[{n.channel()}] {n.send('订单已发货')}")
# [email] 邮件: 订单已发货
# [sms] 短信: 订单已发货
```

**逐行解剖**

① `EmailNotifier` 实现 `send` 和 `channel` → 契约满足
② `SMSNotifier` 同样实现 → 契约满足
③ `for n in [...]` → 多态:同一调用,不同行为
④ `n.channel()` → 各自返回自己的渠道名

**要点**:接口让团队协作有了"合同",
每个人按合同实现,集成时不会出错。

**常见错误**

> 1. **错误现象**:接口里写了实现代码
>    **原因:**接口应该全部抽象。修正:把实现移到子类
> 2. **错误现象**:子类只实现部分方法
>    **原因:**实例化时报 TypeError,列出缺失方法。修正:实现全部抽象方法

> **问自己**:
> - 接口和抽象基类有什么区别?
> - 为什么接口不能实例化?
> - Python 中没有 interface 关键字,怎么模拟接口?

---

#### 鸭子类型 vs abc.ABC —— 什么时候用哪个?

> **痛点**

不清楚什么时候用鸭子类型,
什么时候用 abc.ABC。

> **类比**

鸭子类型 = 口头约定("你应该有这个方法")
abc.ABC = 合同("你必须实现这个方法,否则不准上线")

> **解释**

| 维度 | 鸭子类型 | abc.ABC |
| --- | --- | --- |
| 灵活性 | 高 | 中 |
| 安全性 | 低(运行时才报错) | 高(实例化时报错) |
| 代码量 | 少 | 稍多 |
| 团队协作 | 容易出错 | 强制契约 |
| 适用场景 | 个人脚本 | 团队项目 |

**经验法则**:
超过 3 个人的项目,用 abc.ABC。
个人脚本/原型,用鸭子类型。

```python
# 示例:鸭子类型版本 vs abc.ABC 版本
# --- 鸭子类型版本 —— 灵活但不安全 ---
class Alipay:
    def execute(self, amount):
        return f"支付宝 {amount} 元"

def checkout(total, payment):
    return payment.execute(total)

print(checkout(99.0, Alipay()))
# 优点:简单,无需 import abc
# 缺点:漏写 execute 不报错

# --- abc.ABC 版本 —— 安全但稍繁琐 ---
import abc

class Payment(abc.ABC):
    @abc.abstractmethod
    def execute(self, amount):
        ...

class Alipay(Payment):
    def execute(self, amount):
        return f"支付宝 {amount} 元"

def checkout(total, payment):
    return payment.execute(total)

print(checkout(99.0, Alipay()))
# 优点:漏写 execute 实例化时报错
# 缺点:需要 import abc,多写几行
```

**要点**:根据项目规模选择,
不要教条地只用一种。

**常见错误**

> 1. **错误现象**:小项目过度使用 abc.ABC
>    **原因:**增加不必要的复杂度。修正:个人脚本用鸭子类型
> 2. **错误现象**:大项目全用鸭子类型
>    **原因:**团队协作容易出错。修正:用 abc.ABC 强制契约

> **问自己**:
> - 你的项目有几个人?
> - 如果漏写方法,什么时候发现最合适?
> - 鸭子类型和 abc.ABC 能混用吗?

---

#### 综合练习 —— Payment 支付系统

现在把**鸭子类型、abc.ABC、接口、多态**
串成一个真实业务系统。

**需求清单**:
1. `Payment(abc.ABC)` 定义 execute 抽象方法
2. `Alipay(Payment)` 实现 execute
3. `WeChatPay(Payment)` 实现 execute
4. `checkout(cart_total, payment)` 不判断类型,直接调用
5. 漏写 execute 时在实例化阶段就报 TypeError
6. 新增支付方式只需**添加一个文件**

```python
# 示例:Payment 支付系统完整实现
import abc

class Payment(abc.ABC):
    @abc.abstractmethod
    def execute(self, amount):
        ...

class Alipay(Payment):
    def execute(self, amount):
        return f"支付宝支付 {amount:.2f} 元"

class WeChatPay(Payment):
    def execute(self, amount):
        return f"微信支付 {amount:.2f} 元"

def checkout(cart_total, payment):
    return payment.execute(cart_total)

# 测试
print(checkout(99.0, Alipay()))     # 支付宝支付 99.00 元
print(checkout(50.0, WeChatPay()))  # 微信支付 50.00 元

# 验证:漏写 execute 会报错
class BrokenPay(Payment):
    pass

try:
    broken = BrokenPay()
except TypeError as e:
    print(f"契约保护: {e}")
```

**逐行解剖**

① `Payment(abc.ABC)` → 抽象基类,定义契约
② `@abc.abstractmethod` → execute 是必须实现的方法
③ `Alipay(Payment)` → 继承并实现 execute → 契约满足
④ `checkout` → 不判断类型,直接调用 execute
⑤ `BrokenPay(Payment)` → 没实现 execute → 实例化时报错

**要点**:这个案例综合了 abc.ABC / @abstractmethod /
多态 / 接口 全部知识点,是 OOP L3 的"最小完整案例"。

**扩展思考 —— 新增支付方式**

```python
# 新增一种支付方式 —— 只需加一个类!
class ApplePay(Payment):
    def execute(self, amount):
        return f"Apple Pay 支付 {amount:.2f} 元"

print(checkout(120.0, ApplePay()))
# checkout 函数完全没有修改!
# 这就是"开闭原则":对扩展开放,对修改关闭
```

> **问自己**(综合练习前先思考):
> - 这道题要用到今天学的哪个知识点?
> - 抽象基类应该定义哪些抽象方法?
> - checkout 函数应该怎么写才不包含 if-elif?
> - 如果运行报错,检查:继承 abc.ABC 了吗? 实现了所有抽象方法吗?

---

#### 练习指导

完成下面的练习,巩固今天学的知识点。

**当堂练**(必做):
- 打开 `exercises/10-oop-多态契约/practice01.py` —— 鸭子类型基本用法
- 打开 `exercises/10-oop-多态契约/practice02.py` —— checkout 多态函数
- 打开 `exercises/10-oop-多态契约/practice03.py` —— abc.ABC 抽象基类
- 打开 `exercises/10-oop-多态契约/practice04.py` —— @abstractmethod 强制契约
- 打开 `exercises/10-oop-多态契约/practice05.py` —— 接口:Notifier
- 打开 `exercises/10-oop-多态契约/practice06.py` —— Payment 支付系统综合

**课后作业**(选做):
- 打开 `exercises/10-oop-多态契约/task01.py` —— 鸭子类型:序列化器
- 打开 `exercises/10-oop-多态契约/task02.py` —— abc.ABC:日志系统
- 打开 `exercises/10-oop-多态契约/task03.py` —— 综合项目:通知中心

**参考答案**:在 `solutions/10-oop-多态契约/` 下找到对应答案。

---

#### 今日小结

| 概念 | 解决的痛点 | 适用场景 |
| --- | --- | --- |
| 鸭子类型 | 不写继承也能多态 | 个人脚本、原型 |
| abc.ABC 抽象基类 | 漏实现立即报错 | 团队项目、公共库 |
| @abstractmethod | 标记必须实现的方法 | 配合 abc.ABC 使用 |
| 接口 | 团队协作契约 | 多人协作、API 设计 |
| NCDL 负案例 | 通过踩坑加深理解 | 所有抽象概念 |

**核心洞察**:
多态 = 同一接口,不同实现。
契约 = 强制子类实现接口。
鸭子类型灵活但不安全,abc.ABC 安全但稍繁琐。
**根据项目规模选择**。

---

[← 上一个:Python 知识](../knowledge/09-oop-继承.md) | [返回目录](../README.md) | [下一个:OOP 组合 L4 →](../knowledge/11-oop-组合.md)
