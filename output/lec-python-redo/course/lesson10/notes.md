### Day 10 · 阶段复习:购物车项目(consumer_gate 综合实战)

> **痛点**:你学了 9 天 Python,却不知道怎么把它们串成一个完整项目。今天你将独立搭建一个购物车系统 —— 把变量、条件、循环、函数、列表/字典、文件 I/O 全部用一遍。
> **类比**:购物车项目就像"搭积木" —— 每个知识点是一块积木,今天你要搭出一座完整的城堡。
> **解释**:**综合项目 = 用已学的所有知识解决实际问题**。今天:需求设计、函数拆分、JSON 持久化。

---

#### 需求分析与代码框架 —— 先想清楚再动手

> **痛点**:拿到题目就写,写到一半发现缺功能、结构乱,推倒重来。
> **类比**:写代码就像"盖房子" —— 先画图纸再砌墙,否则垒到三楼发现忘了留门。
> **解释**:先列功能清单,再拆函数,最后写代码 —— 永远不要让代码"自发生长"。

```python
# 购物车系统功能清单(写在代码前面的注释里)

# ① 商品库:字典列表,每个商品 = {名称, 价格}
# ② 主菜单:1.浏览商品 2.加入购物车 3.查看购物车 4.结算 0.退出
# ③ 购物车:列表,记录每件商品的名称、价格、数量
# ④ 结算:计算总价,打印购物小票
# ⑤ 持久化:启动时从 products.json 加载商品库,退出时保存
```

**逐行解剖**

- 功能清单 = 把"要做什么"翻译成"要实现什么"
- 数据结构设计 = 商品用 dict(字段名清晰),一组商品用 list
- 菜单循环 = `while True` + 选项分支,直到用户选 0 退出

> **ASCII 项目架构图**
> ```
> ┌─────────────────────────────────┐
> │         购物车系统              │
> ├─────────────┬───────────────────┤
> │ 数据层      │ 商品库(list[dict])│
> │             │ 购物车(list[dict])│
> ├─────────────┼───────────────────┤
> │ 功能层      │ load_products()   │
> │             │ show_menu()       │
> │             │ add_to_cart()     │
> │             │ view_cart()       │
> │             │ checkout()        │
> │             │ save_products()   │
> ├─────────────┼───────────────────┤
> │ 持久层      │ products.json     │
> └─────────────┴───────────────────┘
> ```

**常见错误**

> 1. **错误现象**:所有代码堆在全局,越写越乱
>    **原因:**没拆函数。修正:每个功能一个函数,每函数 ≤ 40 行
> 2. **错误现象**:菜单循环写了一半,发现数据结构不合理
>    **原因:**没先设计。修正:先画架构再写代码

---

#### 商品库与菜单循环 —— 项目的"骨架"

> **痛点**:需要存商品信息,还要能反复显示菜单,怎么做?
> **类比**:商品库就像"超市货架",菜单循环就像"导购员反复问你买什么"。
> **解释**:用 list[dict] 存商品;`while True` + `if-elif` 实现菜单。

```python
import json
import os

# 商品库(列表套字典)
products = [
    {"id": 1, "name": "Python 入门", "price": 39.9},
    {"id": 2, "name": "NumPy 实战", "price": 49.9},
    {"id": 3, "name": "Pandas 精讲", "price": 59.9},
    {"id": 4, "name": "爬虫基础", "price": 29.9},
]

cart = []  # 购物车(空列表,后续追加)

def show_menu():
    """显示主菜单"""
    print("\n=== 购物车系统 ===")
    print("1. 浏览商品")
    print("2. 加入购物车")
    print("3. 查看购物车")
    print("4. 结算")
    print("0. 退出")
    return input("请选择:")

def show_products():
    """浏览商品"""
    print("\n--- 商品列表 ---")
    for p in products:
        print(f"{p['id']}. {p['name']}  ¥{p['price']}")
```

**逐行解剖**

- `products = [{...}, {...}]` = 列表套字典,每个字典是一个商品
- `show_menu()` = 显示菜单,返回用户选择
- `show_products()` = for 循环遍历商品列表,格式化输出
- `input("请选择:")` = 获取用户输入作为选择

> **ASCII 商品库内存图**
> ```
> products = [
>     {"id": 1, "name": "Python 入门", "price": 39.9},
>     {"id": 2, "name": "NumPy 实战",   "price": 49.9},
>     {"id": 3, "name": "Pandas 精讲",  "price": 59.9},
>     {"id": 4, "name": "爬虫基础",     "price": 29.9},
> ]
>
> 索引:   0              1              2              3
> ```

**常见错误**

> 1. **错误现象**:商品字段名写错
>    **原因:**dict 的 key 必须一致。修正:统一用 "id"/"name"/"price"
> 2. **错误现象**:菜单没循环,选完就结束
>    **原因:**没写 `while True`。修正:用 while 循环包裹

---

#### 加入购物车 —— 数据"动起来"

> **痛点**:用户输入商品编号,怎么把它加到购物车里?
> **类比**:购物车就像"购物篮" —— 看到喜欢的商品就拿起来放进去。
> **解释**:根据 id 查找商品,构造购物车条目,追加到 cart 列表。

```python
def add_to_cart():
    """加入购物车"""
    show_products()
    try:
        pid = int(input("输入商品编号:"))
    except ValueError:
        print("请输入数字!")
        return

    # 根据 id 查找商品
    found = None
    for p in products:
        if p["id"] == pid:
            found = p
            break

    if found is None:
        print("商品不存在!")
        return

    try:
        qty = int(input("数量:"))
    except ValueError:
        print("请输入数字!")
        return

    # 加入购物车(字典:商品名/单价/数量)
    item = {
        "name": found["name"],
        "price": found["price"],
        "qty": qty,
    }
    cart.append(item)
    print(f"已添加 {found['name']} x{qty}")

def view_cart():
    """查看购物车"""
    if not cart:
        print("购物车为空")
        return

    print("\n--- 购物车 ---")
    total = 0
    for item in cart:
        subtotal = item["price"] * item["qty"]
        total += subtotal
        print(f"{item['name']} x{item['qty']} = ¥{subtotal:.2f}")
    print(f"合计: ¥{total:.2f}")
```

**逐行解剖**

- `try-except ValueError` = 处理非数字输入,防止崩溃
- `for p in products` + `if p["id"] == pid` = 线性查找商品
- `found is None` = 查不到时提示不存在
- `cart.append(item)` = 把条目追加到购物车列表
- `total += subtotal` = 累加器求总价

> **ASCII 购物车数据结构**
> ```
> cart = [
>     {"name": "Python 入门", "price": 39.9, "qty": 2},
>     {"name": "爬虫基础",    "price": 29.9, "qty": 1},
> ]
>
> 遍历计算:
>   第1项: 39.9 * 2 = 79.8
>   第2项: 29.9 * 1 = 29.9
>   合计:  79.8 + 29.9 = 109.7
> ```

**常见错误**

> 1. **错误现象**:输入字母直接崩溃
>    **原因:**没加 try-except。修正:用 try 包裹 int() 转换
> 2. **错误现象**:重复商品没有合并数量
>    **原因:**每次都 append 新条目。修正:先检查购物车里是否已有该商品

---

#### 结算 —— 项目的"交付"

> **痛点**:购物车有了,怎么计算总价、出示小票?
> **类比**:结算就像"超市收银台" —— 扫一遍所有商品,报总价、打小票。
> **解释**:遍历 cart,累加求和,格式化输出购物小票。

```python
def checkout():
    """结算(核心函数 —— 用结算结果约束设计)"""
    if not cart:
        print("购物车为空,无法结算")
        return

    print("\n=== 购物小票 ===")
    total = 0
    for item in cart:
        subtotal = item["price"] * item["qty"]
        total += subtotal
        print(f"  {item['name']:10s} x{item['qty']}"
              f"  ¥{subtotal:7.2f}")
    print("-" * 30)
    print(f"  总计:           ¥{total:.2f}")
    print("=" * 30)

    cart.clear()  # 清空购物车
    print("结算成功,欢迎下次光临!")
```

**逐行解剖**

- `cart.clear()` = 结算后清空购物车
- `:10s` = 字符串左对齐占 10 格(对齐用)
- `:7.2f` = 浮点数占 7 格,保留 2 位小数
- 结算函数是 consumer_gate 的核心:用它约束所有前置功能

> **ASCII 结算流程图**
> ```
> checkout()
>    │
>    ▼
> 购物车空? ──Yes──▶ 提示"空",返回
>    │
>    No
>    ▼
> 遍历 cart 求总价
>    │
>    ▼
> 格式化打印小票
>    │
>    ▼
> cart.clear()
>    │
>    ▼
> 打印"欢迎下次光临"
> ```

**常见错误**

> 1. **错误现象**:结算后购物车没清空
>    **原因:**忘记 `cart.clear()`。修正:结算后清空
> 2. **错误现象**:小数位数不统一
>    **原因**:没格式化。修正:`{price:.2f}`

---

#### 文件 I/O 持久化 —— 让数据"活得久"

> **痛点**:程序关掉,商品库就丢了;下次启动又要重新输入。
> **类比**:JSON 文件就像"仓库账本" —— 每次开门先读账本,关门时写回账本。
> **解释**:程序启动时 `load_products()`,退出时 `save_products()`。

```python
DATA_FILE = "products.json"

def load_products():
    """启动时加载商品库"""
    global products
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            products = json.load(f)
        print(f"已加载 {len(products)} 个商品")

def save_products():
    """退出时保存商品库"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=2)
    print("商品库已保存")
```

**逐行解剖**

- `os.path.exists()` = 判断文件是否存在(首次运行不存在)
- `with open(...) as f` = 自动关闭文件(推荐写法)
- `json.load(f)` = 从文件读取 JSON,转为 Python 对象
- `json.dump(products, f)` = 把 Python 对象写入 JSON 文件
- `ensure_ascii=False` = 保存中文不转义

> **ASCII 持久化流程图**
> ```
> 启动时:
>    │
>    ▼
> products.json 存在? ──No──▶ 使用默认商品库
>    │
>    Yes
>    ▼
> json.load() → products
>
> 退出时:
>    │
>    ▼
> json.dump(products) → products.json
> ```

**常见错误**

> 1. **错误现象**:`FileNotFoundError`
>    **原因**:文件不存在就读取。修正:先 `os.path.exists()` 判断
> 2. **错误现象**:`json.JSONDecodeError`
>    **原因**:JSON 文件内容损坏。修正:try-except + 备份

---

#### 异常加固 —— 让程序"扛得住"

> **痛点**:用户乱输入、文件损坏,程序动不动就崩溃。
> **类比**:异常处理就像"安全气囊" —— 撞车时自动弹出,保护程序。
> **解释**:所有"可能出错"的代码都用 try-except 包裹。

```python
def safe_input_int(prompt):
    """安全的整数输入(返回整数,非法时返回 None)"""
    try:
        return int(input(prompt))
    except ValueError:
        print("请输入有效的数字!")
        return None

def main():
    """主函数 —— 程序入口"""
    load_products()

    while True:
        choice = show_menu()

        if choice == "1":
            show_products()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            view_cart()
        elif choice == "4":
            checkout()
        elif choice == "0":
            save_products()
            print("再见!")
            break
        else:
            print("无效选择,请重新输入")

if __name__ == "__main__":
    main()
```

**逐行解剖**

- `safe_input_int()` = 封装安全的输入函数,重复利用
- `while True` + `break` = 主循环,退出时保存
- `if-elif-else` = 多分支处理菜单选择
- `if __name__ == "__main__"` = 程序入口(被 import 时不执行)

> **ASCII 异常加固示意图**
> ```
> 正常流程:  用户输入 → 处理 → 继续
>                         │
>                       崩溃?
>                         │
>              ┌──────────┴──────────┐
>              │ Yes                 │ No
>              ▼                     ▼
>         try-except 捕获       继续执行
>         提示用户重试
>              │
>              └──── 继续 ────┘
> ```

**常见错误**

> 1. **错误现象**:所有代码放全局,不可复用
>    **原因:**没写 `main()` 函数。修正:逻辑都放函数里
> 2. **错误现象**:退出时没保存数据
>    **原因:**break 前忘了调用 save。修正:退出前保存

---

#### 函数拆分原则 —— 每函数只做一件事

> **痛点**:函数越写越长,一个函数干了十几件事,改一处漏十处。
> **类比**:函数拆分就像"流水线" —— 每个工位只负责一个动作,坏了只修一个。
> **解释**:每函数 ≤ 40 行,只做一件事,名字要"见名知意"。

```python
# 好的函数拆分示例:
# ① load_products()   —— 只加载
# ② show_menu()       —— 只显示菜单
# ③ add_to_cart()     —— 只加商品
# ④ view_cart()       —— 只查看
# ⑤ checkout()        —— 只结算
# ⑥ save_products()   —— 只保存
# ⑦ main()            —— 只调度

# 反例:把加载、显示、加法全写进一个函数
# → 超过 80 行,根本没法维护
```

> **ASCII 函数拆分原则**
> ```
> 好:
>   main() → show_menu() → add_to_cart()
>                    ↓
>              view_cart()
>
> 坏:
>   everything()  ← 800 行,啥都干
> ```

---

#### 苏格拉底引导

1. 为什么先写功能清单,而不是直接写代码?
2. 商品的数据结构为什么用 list[dict] 而不是 dict[dict]?
3. 结算函数为什么是"消费者门控"?它约束了哪些前置功能?
4. 如果要把"购物车持久化"加进来,需要改哪些函数?
5. 函数超过 40 行怎么办?如何判断"做了一件事还是多件事"?

---

#### 学员代码区

在 VS Code 新建 `day10_shopping_cart.py`,补全下面的框架:

```python
import json
import os

DATA_FILE = "products.json"
products = [...]  # TODO: 至少定义 4 个商品
cart = []

def load_products():
    """加载商品库"""
    pass  # TODO: 实现加载逻辑

def show_menu():
    """显示菜单,返回选择"""
    pass  # TODO: 实现菜单显示

def show_products():
    """浏览商品"""
    pass  # TODO: 遍历并打印商品

def add_to_cart():
    """加入购物车"""
    pass  # TODO: 输入 id + 数量,追加到 cart

def view_cart():
    """查看购物车"""
    pass  # TODO: 遍历 cart,计算总价

def checkout():
    """结算"""
    pass  # TODO: 打印小票,cart.clear()

def save_products():
    """保存商品库"""
    pass  # TODO: 实现保存逻辑

def main():
    """主函数"""
    load_products()
    while True:
        choice = show_menu()
        # TODO: 用 if-elif 处理 5 个选项 + break

if __name__ == "__main__":
    main()
```

---

#### 参考答案

完整代码见课堂演示,核心要点:
- 每个函数 ≤ 40 行
- 所有 input 包裹 try-except
- main() 只负责调度,不写业务逻辑
- 退出前必须 save_products()

---

## 明日衔接

- 明天 Day 11 学什么:**NumPy 基础**(数组/广播/索引)
- 今天遗留的概念:今天是综合复习,没有新语法
- NCDL 预告:Day 11 用 NCDL 教学法,展示"用 for 循环做数值计算"的反模式
