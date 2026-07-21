### Day 07 · 文件 I/O + 异常:让数据"永存"且"安全"

> **痛点**:你写的程序运行完数据就丢了,下次打开又要重新输入。今天你将学会把数据存到文件里,下次直接读取 —— 还要学会处理各种"意外情况",让程序不崩溃。
> **类比**:文件 I/O 像"存档/读档" —— 游戏存档到硬盘,下次读档继续;异常处理像"安全气囊" —— 出事故时保护程序不崩溃。
> **解释**:**文件 I/O = 程序与文件的数据交换;异常处理 = 应对运行时错误**。今天学:open/read/write、with、JSON、try/except。

---

#### open() 与文件模式 —— 打开文件的"钥匙"

> **痛点**:你想让程序读取或写入一个文件,不知道怎么打开。
> **类比**:open() 像"开门" —— 不同模式就像不同钥匙:读钥匙、写钥匙、追加钥匙。
> **解释**:`open(文件路径, 模式)` 打开文件,模式决定读/写/追加。

```python
# 文件模式
# 'r' = 读(read,默认),文件不存在报错
# 'w' = 写(write),文件不存在创建,存在则覆盖!
# 'a' = 追加(append),文件不存在创建,存在则末尾追加
# 'r+' = 读写(文件必须存在)

# 写文件
f = open("test.txt", "w", encoding="utf-8")
f.write("Hello\n")
f.write("World")
f.close()                       # 必须手动关闭!

# 读文件
f = open("test.txt", "r", encoding="utf-8")
content = f.read()
f.close()
print(content)
```

**逐行解剖**

- `open("test.txt", "w")` = 以写模式打开 test.txt
- `encoding="utf-8"` = 指定编码(中文文件必须加!)
- `f.write("Hello\n")` = 写入字符串(不会自动加换行)
- `f.close()` = 关闭文件(释放资源,必须关闭!)

> **ASCII 文件模式图**
> ```
> 'r' 读:  文件必须存在 ──▶ 读取内容
> 'w' 写:  不存在则创建 ──▶ 覆盖写入(危险!)
> 'a' 追加: 不存在则创建 ──▶ 末尾追加(安全)
> ```

**常见错误**

> 1. **错误现象**:`FileNotFoundError: [Errno 2] No such file or directory`
>    **原因:**读模式打开不存在的文件。修正:先判断文件是否存在,或改用 'w'/'a'
> 2. **错误现象**:中文文件乱码
>    **原因:**没指定 encoding="utf-8"。修正:始终加 encoding="utf-8"

---

#### 三种读取方式 —— 文件的"吃法"

> **痛点**:文件内容有多行,你想一次性读、逐行读、或读成列表。
> **类比**:读取像"吃面条" —— read 一口吃全部;readline 一根一根吃;readlines 按份吃。
> **解释**:`read()` 读全部;`readline()` 读一行;`readlines()` 读成列表。

```python
# 假设 test.txt 内容:
# 第一行
# 第二行
# 第三行

# read():一次性读取全部内容
f = open("test.txt", "r", encoding="utf-8")
content = f.read()              # "第一行\n第二行\n第三行"
f.close()

# readline():逐行读取
f = open("test.txt", "r", encoding="utf-8")
line1 = f.readline()             # "第一行\n"(包含换行符)
line2 = f.readline()             # "第二行\n"
f.close()

# readlines():读取所有行,返回列表
f = open("test.txt", "r", encoding="utf-8")
lines = f.readlines()            # ["第一行\n", "第二行\n", "第三行\n"]
f.close()

# 最常用:直接遍历文件对象(逐行读取,省内存)
f = open("test.txt", "r", encoding="utf-8")
for line in f:                   # 每次读一行
    print(line.strip())          # strip() 去掉换行符
f.close()
```

**逐行解剖**

- `read()` = 返回整个文件内容(字符串),大文件慎用
- `readline()` = 返回一行(包含末尾 `\n`)
- `readlines()` = 返回每行组成的列表
- `for line in f:` = 逐行遍历,最省内存(推荐!)

> **ASCII 三种读取方式图**
> ```
> 文件内容: 第一行\n第二行\n第三行
>
> read()     → "第一行\n第二行\n第三行"(一个字符串)
> readline() → "第一行\n"(每次读一行)
> readlines()→ ["第一行\n", "第二行\n", "第三行\n"](列表)
> ```

**常见错误**

> 1. **错误现象**:`read()` 返回空字符串
>    **原因:**文件指针已在末尾(之前读过)。修正:重新打开或 `f.seek(0)`
> 2. **错误现象**:行尾有空白
>    **原因:**`readline()` 保留换行符。修正:`line.strip()` 去掉

---

#### with 上下文管理 —— 自动"关门"

> **痛点**:你经常忘记 `f.close()`,导致文件资源泄漏。
> **类比**:with 像"自动门" —— 进去后自动开门,出来时自动关门,不用操心。
> **解释**:`with open() as f:` 自动管理文件,代码块结束自动关闭。

```python
# 传统写法(容易忘记 close)
f = open("test.txt", "r", encoding="utf-8")
content = f.read()
f.close()                       # 容易忘记!

# with 写法(推荐!)
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
# 这里 f 自动关闭,无需手动 close

# with 写文件
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("Hello\n")
    f.write("World")
# 自动关闭,即使写代码时出错也会关闭
```

**逐行解剖**

- `with open(...) as f:` = 打开文件,赋值给 f
- 缩进代码块 = 在 with 内部使用 f
- 代码块结束 = 自动调用 f.close(),即使出错也关闭

> **ASCII with 自动关闭图**
> ```
> with open("f.txt") as f:
>     data = f.read()    ← 在 with 内,f 是打开的
>                        ← 离开 with,自动 close
>
> 即使 f.read() 报错,也会自动 close ✓
> ```

**常见错误**

> 1. **错误现象**:在 with 外部使用 f
>    **原因:**with 结束后文件已关闭。修正:在 with 内部操作
> 2. **错误现象**:忘记写 `as f`
>    **原因:**`with open(...) ` 没赋值无法操作。修正:`as f`

---

#### JSON 读写 —— 数据的"通用语言"

> **痛点**:你想把 Python 的列表/字典存到文件,下次直接读回来。
> **类比**:JSON 像"国际通用语言" —— Python 的字典转成 JSON 字符串,存到文件,其他语言也能读。
> **解释**:`json.dump()` 写入;`json.load()` 读取;dumps/loads 操作字符串。

```python
import json

# Python 数据
data = {
    "name": "Alice",
    "age": 25,
    "scores": [90, 85, 92]
}

# 写入 JSON 文件
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    # ensure_ascii=False:中文不转义
    # indent=2:格式化缩进(好看)

# 读取 JSON 文件
with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)       # 直接转回 Python 字典
print(loaded["name"])           # Alice

# json.dumps():Python 对象 → JSON 字符串
json_str = json.dumps(data, ensure_ascii=False)
print(json_str)                 # '{"name": "Alice", ...}'

# json.loads():JSON 字符串 → Python 对象
data2 = json.loads(json_str)
```

**逐行解剖**

- `json.dump(data, f)` = 把 data 写入文件 f
- `ensure_ascii=False` = 中文不转成 `\uXXXX`(必须加!)
- `indent=2` = 格式化缩进 2 格(好看)
- `json.load(f)` = 从文件读取并转回 Python 对象
- `dumps/loads` = 操作字符串(不带文件)

> **ASCII JSON 读写图**
> ```
> Python 对象 ──json.dump()──▶ 文件
> 文件      ──json.load()──▶ Python 对象
>
> Python 对象 ──json.dumps()──▶ JSON 字符串
> JSON 字符串 ──json.loads()──▶ Python 对象
> ```

**常见错误**

> 1. **错误现象**:JSON 文件中文显示为 `\uXXXX`
>    **原因:**没加 `ensure_ascii=False`。修正:始终加
> 2. **错误现象**:`json.loads()` 解析失败
>    **原因:**JSON 格式错误(如单引号)。修正:JSON 必须用双引号

---

#### 异常处理 —— 程序的"安全气囊"

> **痛点**:程序运行时出错就崩溃,用户体验很差。
> **类比**:try/except 像"安全气囊" —— 出事故时保护乘客,程序继续运行。
> **解释**:`try` 放可能出错的代码;`except` 捕获错误并处理。

```python
# 基本异常处理
try:
    num = int(input("请输入整数:"))
    print(f"你输入的是 {num}")
except ValueError:
    print("输入错误!请输入整数")

# 多个 except(捕获不同类型错误)
try:
    a = int(input("被除数:"))
    b = int(input("除数:"))
    print(a / b)
except ValueError:
    print("请输入整数")
except ZeroDivisionError:
    print("除数不能为 0")

# try/except/else/finally
try:
    f = open("test.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("文件不存在")
else:
    print("文件打开成功")
    f.close()
finally:
    print("无论成功失败都执行")
```

**逐行解剖**

- `try:` = 放可能出错的代码
- `except ValueError:` = 捕获 ValueError,执行处理代码
- `else:` = 没有异常时执行(可选)
- `finally:` = 无论有无异常都执行(可选,常用于清理)

> **ASCII 异常处理流程图**
> ```
> try:
>     可能出错的代码
>    │
>    ├── 正常 ──▶ else ──▶ finally
>    │
>    └── 异常 ──▶ except ──▶ finally
> ```

**常见错误**

> 1. **错误现象**:`except:` 捕获所有异常(裸 except)
>    **原因:**捕获太广,隐藏真正错误。修正:指定异常类型
> 2. **错误现象**:except 顺序错误
>    **原因:**父类异常放前面会覆盖子类。修正:子类放前面

---

#### 常见异常类型 —— "错误百科全书"

> **痛点**:你遇到报错不知道是什么类型,不知道怎么处理。
> **类比**:异常类型像"疾病分类" —— 知道什么病,才能开什么药。
> **解释**:常见异常:FileNotFoundError/ValueError/TypeError/KeyError/IndexError。

```python
# FileNotFoundError:文件不存在
# open("不存在的文件.txt", "r")  # FileNotFoundError

# ValueError:值错误(类型对但值不对)
# int("abc")                      # ValueError

# TypeError:类型错误
# "hello" + 123                    # TypeError

# KeyError:字典键不存在
# d = {}; d["不存在的键"]          # KeyError

# IndexError:索引超出范围
# lst = [1, 2]; lst[10]           # IndexError

# json.JSONDecodeError:JSON 格式错误
import json
# json.loads("{invalid}")          # json.JSONDecodeError

# 捕获多个异常
try:
    # 可能出错的代码
    pass
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"文件错误: {e}")         # e 是错误信息
```

**逐行解剖**

- `as e` = 把错误对象赋值给 e,可以打印错误信息
- `(Type1, Type2)` = 元组形式捕获多个异常
- 常见异常要记住,遇到报错先看类型

> **ASCII 异常类型图**
> ```
> Exception(所有异常的基类)
> ├── FileNotFoundError(文件不存在)
> ├── ValueError(值错误)
> ├── TypeError(类型错误)
> ├── KeyError(键不存在)
> ├── IndexError(索引越界)
> └── json.JSONDecodeError(JSON 格式错误)
> ```

**常见错误**

> 1. **错误现象**:`except Exception as e:` 捕获所有异常
>    **原因:**捕获太广,可能隐藏 bug。修正:尽量指定具体类型
> 2. **错误现象**:捕获了异常但没处理(空 except)
>    **原因:**`pass` 会隐藏错误。修正:至少打印错误信息

---

#### 执行过程跟踪

```python
# --- 执行过程 ---

# with open("data.json", "w", encoding="utf-8") as f:
#     json.dump(data, f, ensure_ascii=False, indent=2)
#   ① 打开 data.json,写模式
#   ② 把 data 转成 JSON 字符串
#   ③ 写入文件(中文不转义,缩进 2 格)
#   ④ 离开 with,自动关闭文件

# with open("data.json", "r", encoding="utf-8") as f:
#     loaded = json.load(f)
#   ① 打开 data.json,读模式
#   ② 读取文件内容
#   ③ 把 JSON 字符串转回 Python 对象
#   ④ 赋值给 loaded

# try:
#     num = int(input("请输入整数:"))
# except ValueError:
#     print("输入错误")
#   ① 等待用户输入
#   ② 尝试转整数
#   ③ 失败则捕获 ValueError,打印提示
```

---

#### 常见错误汇总

> 1. **错误现象**:`FileNotFoundError`
>    **原因:**读模式打开不存在的文件。修正:先判断或改用 'w'/'a'
> 2. **错误现象**:`json.JSONDecodeError`
>    **原因:**JSON 格式错误。修正:检查 JSON 语法(双引号)
> 3. **错误现象**:`UnicodeDecodeError`(中文乱码)
>    **原因:**没指定 encoding="utf-8"。修正:始终加
> 4. **错误现象**:忘记 `f.close()`
>    **原因:**资源泄漏。修正:用 with 自动关闭

---

#### 学员代码区

在 VS Code 新建 `day07.py`,补全下面的代码:

```python
import json

# TODO: 把 data = {"name": "Alice", "age": 25} 写入 data.json
data = {"name": "Alice", "age": 25}


# TODO: 从 data.json 读取内容,赋值给 loaded


# TODO: 用 try/except 处理用户输入整数,输入错误时提示"请输入整数"


```

---

#### 参考答案

```python
import json

data = {"name": "Alice", "age": 25}
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

try:
    num = int(input("请输入整数:"))
except ValueError:
    print("请输入整数")
```

---

## 明日衔接

- 明天 Day 08 学什么:**OOP 基础**(类/对象/继承/封装)
- 今天遗留的概念:今天学了文件存储和异常处理,还没学如何组织复杂代码
- 脚手架递进预告:Day 8 在 Day 7 基础上,用类封装电商订单系统
