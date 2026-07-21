### Day 06 · 列表与字典:数据的"容器双雄"

> **痛点**:你有一堆数据(比如全班同学的名字),用单个变量存太麻烦,改一个要找半天。今天你将学会两个"超级容器" —— 列表装有序数据,字典装配对数据。
> **类比**:列表像"排队的人群" —— 有顺序、可重复、能增删;字典像"通讯录" —— 名字对应电话,按键即取。
> **解释**:**列表 = 有序可变序列;字典 = 键值对映射**。今天学:创建、索引、切片、CRUD、排序、遍历。

---

#### 列表创建 —— 有序可变的"数据队伍"

> **痛点**:你想把多个数据"打包"在一起,方便统一管理。
> **类比**:列表就像"一排储物柜" —— 每个柜子有编号(索引),可以放任何东西。
> **解释**:用方括号 `[]` 创建列表,元素用逗号分隔,有序、可变、可重复。

```python
# 创建列表
fruits = ["苹果", "香蕉", "橙子"]      # 字符串列表
numbers = [1, 2, 3, 4, 5]              # 整数列表
mixed = [1, "hello", True, 3.14]       # 混合类型(不推荐但合法)
empty = []                              # 空列表

# 列表可重复
scores = [90, 85, 90, 78, 85]          # 允许重复值

# 查看类型和长度
print(type(fruits))   # <class 'list'>
print(len(fruits))    # 3(元素个数)
```

**逐行解剖**

- `["苹果", "香蕉", "橙子"]` = 创建含 3 个元素的列表
- `mixed` = Python 列表可以混合类型,但实际开发建议统一类型
- `len(fruits)` = 返回列表元素个数(最常用!)

> **ASCII 列表内存图**
> ```
> fruits = ["苹果", "香蕉", "橙子"]
>
> 索引:    0        1        2
> ┌─────┬─────┬─────┐
> │苹果 │香蕉 │橙子 │
> └─────┴─────┴─────┘
> ```

**常见错误**

> 1. **错误现象**:`list = [1, 2, 3]` 后 `list()` 失效
>    **原因:**`list` 是内置函数名,不能做变量名。修正:`my_list = [1, 2, 3]`
> 2. **错误现象**:空列表判断用 `if lst == []`
>    **原因:**Python 风格用 `if not lst:` 判断空列表

---

#### 列表索引与切片 —— 精准"定位"元素

> **痛点**:你想取出列表的某个元素或一段子列表,不知道怎么取。
> **类比**:索引像"座位号" —— 正数从头数,负数从尾数;切片像"切蛋糕" —— 切一段出来。
> **解释**:`lst[i]` 取单个;`lst[start:stop:step]` 取一段,规则同字符串。

```python
fruits = ["苹果", "香蕉", "橙子", "葡萄", "西瓜"]

# 索引(同字符串,从 0 开始)
print(fruits[0])     # 苹果(第一个)
print(fruits[-1])    # 西瓜(最后一个)
print(fruits[2])     # 橙子

# 切片 [start:stop:step](左闭右开)
print(fruits[1:4])   # ['香蕉', '橙子', '葡萄'](不含索引 4)
print(fruits[:3])    # ['苹果', '香蕉', '橙子'](从头开始)
print(fruits[::2])   # ['苹果', '橙子', '西瓜'](步长 2)
print(fruits[::-1])  # ['西瓜', '葡萄', '橙子', '香蕉', '苹果'](逆序!)
```

**逐行解剖**

- `fruits[1:4]` = 从索引 1 到 3(不含 4),左闭右开
- `fruits[:3]` = 省略 start 默认从 0 开始
- `fruits[::2]` = 省略 start/stop 取全部,步长 2 跳着取
- `fruits[::-1]` = 逆序(最常用技巧!)

> **ASCII 索引与切片图**
> ```
> 列表:  苹果  香蕉  橙子  葡萄  西瓜
> 正索引:  0    1    2    3    4
> 负索引: -5   -4   -3   -2   -1
>
> fruits[1:4] → 香蕉 橙子 葡萄
> fruits[::-1] → 西瓜 葡萄 橙子 香蕉 苹果(逆序)
> ```

**常见错误**

> 1. **错误现象**:`IndexError: list index out of range`
>    **原因:**索引超出范围。修正:`len(lst) - 1` 是最大索引
> 2. **错误现象**:以为切片 `lst[1:4]` 包含索引 4
>    **原因:**Python 切片左闭右开 `[start, stop)`。修正:记住"含头不含尾"

---

#### 列表可变性 —— 能"改"的序列

> **痛点**:字符串不能改单个字符,你想知道列表能不能改。
> **类比**:字符串像"刻在石头上的字" —— 不能改;列表像"写在纸上的清单" —— 随时改。
> **解释**:列表是可变类型,可以直接修改、添加、删除元素。

```python
fruits = ["苹果", "香蕉", "橙子"]

# 修改元素(直接赋值)
fruits[1] = "葡萄"           # ['苹果', '葡萄', '橙子']

# 字符串不可变(对比)
# s = "hello"
# s[0] = "H"                # TypeError:字符串不可变

# 判断可变:id 是否变化
print(id(fruits))           # 140234567890
fruits[0] = "西瓜"
print(id(fruits))           # 140234567890(id 不变,原地修改)
```

**逐行解剖**

- `fruits[1] = "葡萄"` = 把索引 1 的元素替换成"葡萄"
- `id(fruits)` = 修改前后 id 不变,说明是"原地修改"
- 字符串 `s[0] = "H"` 会报错,因为字符串不可变

> **ASCII 可变性对比图**
> ```
> 字符串(不可变):
> s = "hello"  →  s[0] = "H"  →  TypeError!
>
> 列表(可变):
> lst = ["苹果", "香蕉"]
> lst[1] = "葡萄"  →  ["苹果", "葡萄"]  ✓
> ```

**常见错误**

> 1. **错误现象**:以为列表赋值给新变量是复制
>    **原因:**`lst2 = lst` 是引用,改 lst2 也会改 lst。修正:`lst2 = lst.copy()`
> 2. **错误现象**:遍历时修改列表导致跳过元素
>    **原因:**遍历时增删会打乱索引。修正:遍历副本或倒序遍历

---

#### 列表 CRUD —— 增删改查"四板斧"

> **痛点**:你想在列表中添加、删除、修改元素,不知道怎么操作。
> **类比**:CRUD 就像"管理名单" —— 加人、删人、改信息、查人。
> **解释**:append/insert/extend 添加;pop/remove/clear 删除。

```python
fruits = ["苹果", "香蕉"]

# 添加元素
fruits.append("橙子")          # 末尾添加:['苹果', '香蕉', '橙子']
fruits.insert(1, "葡萄")       # 指定位置插入:['苹果', '葡萄', '香蕉', '橙子']
fruits.extend(["西瓜", "芒果"]) # 批量添加:合并另一个列表

# 删除元素
fruits.remove("香蕉")          # 按值删除(第一个匹配项)
popped = fruits.pop()          # 删除并返回末尾元素
popped = fruits.pop(0)         # 删除并返回指定索引元素
fruits.clear()                 # 清空列表:[]

# 查询元素
fruits = ["苹果", "香蕉", "橙子", "香蕉"]
print("香蕉" in fruits)        # True(是否存在)
print(fruits.index("香蕉"))    # 1(第一次出现的索引)
print(fruits.count("香蕉"))    # 2(出现次数)
```

**逐行解剖**

- `append(x)` = 末尾添加一个元素
- `insert(i, x)` = 在索引 i 处插入 x,原元素后移
- `extend(lst)` = 把 lst 的所有元素逐个添加(批量)
- `remove(x)` = 删除第一个值为 x 的元素,不存在则报错
- `pop(i)` = 删除索引 i 的元素并返回,默认最后一个
- `in` = 判断元素是否存在,返回布尔值

> **ASCII CRUD 操作图**
> ```
> append("橙"):  [苹果, 香蕉] → [苹果, 香蕉, 橙]
> insert(1,"葡"): [苹果, 香蕉] → [苹果, 葡, 香蕉]
> remove("香蕉"): [苹果, 香蕉, 橙] → [苹果, 橙]
> pop():          [苹果, 橙] → 返回"橙",剩[苹果]
> ```

**常见错误**

> 1. **错误现象**:`ValueError: list.remove(x): x not in list`
>    **原因:**删除不存在的元素。修正:`if x in lst: lst.remove(x)`
> 2. **错误现象**:`pop()` 索引越界
>    **原因:**空列表 pop 会报错。修正:先判断 `if lst:`

---

#### 列表排序与查询 —— 让数据"有序"

> **痛点**:你想把列表排序,或查找某个元素的位置。
> **类比**:排序像"把书按高矮排好";查询像"找某本书在第几个位置"。
> **解释**:`sort()` 原地排序;`index()`/`count()` 查询位置和次数。

```python
nums = [3, 1, 4, 1, 5, 9, 2, 6]

# 排序
nums.sort()                    # 升序:[1, 1, 2, 3, 4, 5, 6, 9]
nums.sort(reverse=True)        # 降序:[9, 6, 5, 4, 3, 2, 1, 1]

# 查询
print(nums.index(5))           # 4(5 的索引,从 0 开始)
print(nums.count(1))           # 2(1 出现 2 次)
print(9 in nums)               # True(是否存在)

# sorted() 返回新列表(不改变原列表)
nums = [3, 1, 4]
new_nums = sorted(nums)        # [1, 3, 4]
print(nums)                    # [3, 1, 4](原列表不变)
```

**逐行解剖**

- `sort()` = 原地排序(修改原列表),无返回值
- `sort(reverse=True)` = 降序排序
- `sorted(lst)` = 返回新列表,原列表不变(非原地)
- `index(x)` = 返回 x 第一次出现的索引,不存在则报错

> **ASCII 排序对比图**
> ```
> sort() vs sorted():
>
> lst = [3, 1, 4]
> lst.sort()       → lst 变为 [1, 3, 4](原地修改)
>
> lst = [3, 1, 4]
> new = sorted(lst) → new = [1, 3, 4], lst 不变
> ```

**常见错误**

> 1. **错误现象**:`x = lst.sort()` 得到 `None`
>    **原因:**`sort()` 是原地操作,返回 None。修正:`lst.sort()` 再 `print(lst)`
> 2. **错误现象**:`index()` 查找不存在的元素报错
>    **原因:**`index()` 找不到会抛 ValueError。修正:先 `if x in lst:`

---

#### 字典创建 —— 键值对的"通讯录"

> **痛点**:你想存"名字→电话"这种配对数据,列表做不到。
> **类比**:字典就像"通讯录" —— 按键(名字)取值(电话),一键即取。
> **解释**:用花括号 `{}` 创建字典,键值对用冒号分隔,键必须唯一。

```python
# 创建字典
phone = {"Alice": "1234", "Bob": "5678", "Charlie": "9012"}
empty = {}                              # 空字典
info = dict(name="Alice", age=25)       # 用 dict() 创建

# 键的类型:不可变类型都可以(字符串/整数/元组)
mixed_keys = {1: "一", "two": 2, (1, 2): "tuple"}

# 值的类型:任意类型
data = {"name": "Alice", "scores": [90, 85, 92], "info": {"age": 25}}

print(type(phone))  # <class 'dict'>
print(len(phone))   # 3(键值对个数)
```

**逐行解剖**

- `{"Alice": "1234"}` = "Alice" 是键,"1234" 是值
- 键必须唯一,重复赋值会覆盖旧值
- 键必须是不可变类型(字符串/整数/元组),值可以是任意类型

> **ASCII 字典结构图**
> ```
> phone = {"Alice": "1234", "Bob": "5678"}
>
> ┌───────┬──────┐
> │ 键     │ 值    │
> ├───────┼──────┤
> │ Alice │ 1234 │
> │ Bob   │ 5678 │
> └───────┴──────┘
> ```

**常见错误**

> 1. **错误现象**:`d = {[1,2]: "list"}` 报错
>    **原因:**列表是可变类型,不能做键。修正:用元组 `(1,2)` 做键
> 2. **错误现象**:以为字典有顺序(Python 3.6 之前)
>    **原因:**Python 3.7+ 字典保持插入顺序,但不要依赖索引访问

---

#### 字典取值 —— 按键"开锁"

> **痛点**:你想取出字典中某个键对应的值,或设置默认值。
> **类比**:取值像"用钥匙开锁" —— `d[key]` 直接开,没有就报错;`d.get(key, 默认)` 没有就返回默认值。
> **解释**:`d[key]` 取值,键不存在报错;`d.get(key, default)` 取值,键不存在返回默认值。

```python
phone = {"Alice": "1234", "Bob": "5678"}

# 直接取值(键不存在会报错)
print(phone["Alice"])          # 1234
# print(phone["Charlie"])      # KeyError: 'Charlie'

# get() 取值(键不存在返回默认值)
print(phone.get("Alice"))      # 1234
print(phone.get("Charlie"))    # None(不报错,返回 None)
print(phone.get("Charlie", "未找到"))  # 未找到(自定义默认值)

# 判断键是否存在
if "Alice" in phone:
    print("找到了")
```

**逐行解剖**

- `d[key]` = 直接取值,键不存在抛 KeyError(危险!)
- `d.get(key)` = 取值,键不存在返回 None(安全!)
- `d.get(key, default)` = 取值,键不存在返回 default(最常用!)
- `in` = 判断键是否存在,返回布尔值

> **ASCII 取值方式对比图**
> ```
> d = {"Alice": "1234"}
>
> d["Alice"]       → "1234"  ✓
> d["Charlie"]     → KeyError ✗
>
> d.get("Alice")   → "1234"  ✓
> d.get("Charlie") → None    ✓(不报错)
> d.get("Charlie", "默认") → "默认"  ✓
> ```

**常见错误**

> 1. **错误现象**:`KeyError: 'xxx'` 程序崩溃
>    **原因:**用 `d[key]` 取值时键不存在。修正:用 `d.get(key, 默认值)`
> 2. **错误现象**:`d.get("key")` 返回 None 但以为有值
>    **原因:**键不存在时 get 返回 None。修正:用 `if d.get("key") is not None:`

---

#### 字典 CRUD —— 增删改查"四板斧"

> **痛点**:你想在字典中添加、修改、删除键值对。
> **类比**:字典 CRUD 就像"管理通讯录" —— 加联系人、改电话、删联系人、查电话。
> **解释**:`d[key] = value` 增/改;`pop()`/`del` 删除。

```python
phone = {"Alice": "1234", "Bob": "5678"}

# 增:添加新键值对
phone["Charlie"] = "9012"      # {'Alice': '1234', 'Bob': '5678', 'Charlie': '9012'}

# 改:键已存在就是修改
phone["Alice"] = "0000"        # Alice 的电话改为 0000

# 删:pop() 删除并返回值
popped = phone.pop("Bob")      # 删除 Bob,返回 "5678"
# phone.pop("David")           # KeyError(不存在)

# pop() 带默认值(不存在返回默认值,不报错)
result = phone.pop("David", "不存在")  # "不存在"

# del 删除
del phone["Alice"]             # 删除 Alice

# 查
print(phone.get("Charlie"))    # 9012
```

**逐行解剖**

- `d[key] = value` = 键不存在则添加,存在则修改(最常用!)
- `d.pop(key)` = 删除键并返回值,键不存在报错
- `d.pop(key, default)` = 删除键,不存在返回 default(安全!)
- `del d[key]` = 删除键值对,键不存在报错

> **ASCII 字典 CRUD 图**
> ```
> d = {"Alice": "1234"}
>
> 增: d["Bob"] = "5678"  → {"Alice": "1234", "Bob": "5678"}
> 改: d["Alice"] = "0000" → {"Alice": "0000", "Bob": "5678"}
> 删: d.pop("Alice")     → 返回 "0000",剩 {"Bob": "5678"}
> ```

**常见错误**

> 1. **错误现象**:`del d["不存在的键"]` 报错
>    **原因:**del 不检查键是否存在。修正:`if key in d: del d[key]`
> 2. **错误现象**:以为 `d.pop()` 和列表一样默认删最后一个
>    **原因:**字典 pop 必须指定键。修正:`d.pop(key)`

---

#### 字典遍历 —— 三种"走法"

> **痛点**:你想遍历字典的所有键、值或键值对,不知道怎么写。
> **类比**:遍历像"翻通讯录" —— 可以只看名字、只看电话、或名字电话一起看。
> **解释**:`keys()` 遍历键;`values()` 遍历值;`items()` 遍历键值对。

```python
phone = {"Alice": "1234", "Bob": "5678", "Charlie": "9012"}

# 遍历键(默认就是遍历键)
for key in phone:
    print(key)                 # Alice Bob Charlie

for key in phone.keys():
    print(key)                 # Alice Bob Charlie

# 遍历值
for value in phone.values():
    print(value)               # 1234 5678 9012

# 遍历键值对(最常用!)
for key, value in phone.items():
    print(f"{key}: {value}")   # Alice: 1234 ...
```

**逐行解剖**

- `for key in phone:` = 默认遍历键,等价于 `phone.keys()`
- `phone.keys()` = 返回所有键的视图
- `phone.values()` = 返回所有值的视图
- `phone.items()` = 返回所有(键, 值)元组,最常用!

> **ASCII 遍历方式图**
> ```
> phone = {"Alice": "1234", "Bob": "5678"}
>
> keys():   Alice       Bob
> values(): 1234        5678
> items():  (Alice,1234)(Bob,5678)
>
> for k, v in phone.items():
>     print(k, v)
> ```

**常见错误**

> 1. **错误现象**:`for key, value in phone:` 报错
>    **原因:**直接遍历字典只得到键。修正:`for key, value in phone.items():`
> 2. **错误现象**:遍历时修改字典大小
>    **原因:**遍历时增删键会报错。修正:遍历 `list(d.keys())` 副本

---

#### 执行过程跟踪

```python
# --- 执行过程 ---

# lst = [1, 2, 3]
#   ① 创建列表 [1, 2, 3]
#   ② 赋值给 lst

# lst.append(4)
#   ① 在列表末尾添加 4
#   ② lst 变为 [1, 2, 3, 4]

# d = {"a": 1}
# d["b"] = 2
#   ① 键 "b" 不存在,添加新键值对
#   ② d 变为 {"a": 1, "b": 2}

# d["a"] = 10
#   ① 键 "a" 已存在,修改值
#   ② d 变为 {"a": 10, "b": 2}

# for k, v in d.items():
#   ① 取出第一个键值对 ("a", 10),k="a", v=10
#   ② 取出第二个键值对 ("b", 2),k="b", v=2
#   ③ 遍历结束
```

---

#### 常见错误汇总

> 1. **错误现象**:`IndexError: list index out of range`
>    **原因:**索引超出范围。修正:最大索引是 `len(lst) - 1`
> 2. **错误现象**:`KeyError: 'xxx'`
>    **原因:**字典键不存在。修正:用 `d.get(key, 默认值)`
> 3. **错误现象**:`ValueError: list.remove(x): x not in list`
>    **原因:**删除不存在的元素。修正:`if x in lst: lst.remove(x)`
> 4. **错误现象**:`AttributeError: 'dict' object has no attribute 'sort'`
>    **原因:**字典没有 sort 方法。修正:用 `sorted(d.items())`

---

#### 学员代码区

在 VS Code 新建 `day06.py`,补全下面的代码:

```python
# TODO: 创建列表 fruits = ["苹果", "香蕉", "橙子"]
fruits =

# TODO: 在末尾添加"葡萄"


# TODO: 删除"香蕉"


# TODO: 创建字典 scores = {"数学": 90, "语文": 85}
scores =

# TODO: 添加 "英语": 88


# TODO: 取出"数学"的值(用 get,默认值 0)


# TODO: 遍历 scores,打印每科成绩
```

---

#### 参考答案

```python
fruits = ["苹果", "香蕉", "橙子"]
fruits.append("葡萄")
fruits.remove("香蕉")
scores = {"数学": 90, "语文": 85}
scores["英语"] = 88
math_score = scores.get("数学", 0)
for subject, score in scores.items():
    print(f"{subject}: {score}")
```

---

## 明日衔接

- 明天 Day 07 学什么:**文件 I/O + 异常**(读写文件、JSON、try/except)
- 今天遗留的概念:今天学了列表和字典的 CRUD,还没学如何持久化存储
- 脚手架递进预告:Day 7 在 Day 6 数据结构基础上,把数据存到文件里
