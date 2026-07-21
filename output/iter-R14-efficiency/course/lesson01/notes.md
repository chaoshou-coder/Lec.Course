### Day 01 · 正则基础语法

> **痛点**:你需要从文本中提取所有手机号,但 str.replace() 只能处理固定字符串。正则表达式是"通配符搜索"的超级版,今天你将学会基础语法。
> **类比**:正则就像"文件搜索的 *.txt" —— 但更强大。`.` 匹配任意字符,`*` 匹配 0 次或多次,`+` 匹配 1 次或多次。
> **解释**:**正则表达式 = 描述文本模式的语言**。今天学:字符类 + 量词 + 锚点。

---

#### 字符类 —— 匹配"某一类字符"

```python
import re

# 匹配单个字符
re.findall(r'[abc]', 'abc abc')     # ['a', 'b', 'c', 'a', 'b', 'c']
re.findall(r'[a-z]', 'Hello 123')   # ['e', 'l', 'l', 'o']
re.findall(r'[0-9]', 'Age: 25')     # ['2', '5']
re.findall(r'[^abc]', 'abc def')    # [' ', 'd', 'e', 'f'](取反)

# 常用简写
re.findall(r'\d', 'Age: 25')        # ['2', '5'](数字)
re.findall(r'\w', 'Hello_world')    # ['H', 'e', 'l', 'l', 'o', '_', 'w', ...](单词字符)
re.findall(r'\s', 'Hello world')    # [' '](空白字符)
```

**逐行解剖**

- `[abc]` = 匹配 a 或 b 或 c
- `[a-z]` = 匹配任意小写字母
- `[^abc]` = 匹配除了 a/b/c 之外的字符
- `\d` = [0-9], `\w` = [a-zA-Z0-9_], `\s` = 空白

---

#### 量词 —— 匹配"重复次数"

```python
# 量词
re.findall(r'a*', 'aaa baa')   # ['aaa', '', 'aa', ''](0 次或多次)
re.findall(r'a+', 'aaa baa')   # ['aaa', 'aa'](1 次或多次)
re.findall(r'a?', 'aaa baa')   # ['a', 'a', 'a', '', 'a', 'a', ''](0 次或 1 次)
re.findall(r'a{2,3}', 'aaa aaa a')  # ['aaa', 'aa'](2-3 次)

# 贪婪 vs 非贪婪
re.findall(r'a.*a', 'abaca')   # ['abaca'](贪婪:尽可能多)
re.findall(r'a.*?a', 'abaca')  # ['aba', 'aca'](非贪婪:尽可能少)
```

---

#### 锚点 —— 匹配"位置"

```python
re.findall(r'^Hello', 'Hello world')  # ['Hello'](行首)
re.findall(r'world$', 'Hello world')  # ['world'](行尾)
re.findall(r'\bword\b', 'a word here')  # ['word'](单词边界)
```

---

#### 执行过程跟踪

```python
# --- 执行过程 ---
# re.findall(r'[abc]', 'abc abc'):
#   ① 遍历 'abc abc' 的每个字符
#   ② 检查字符是否在 [abc] 中
#   ③ 匹配的加入结果列表
#   ④ 返回 ['a', 'b', 'c', 'a', 'b', 'c']
#
# re.findall(r'a*', 'aaa baa'):
#   ① 贪婪匹配:尽可能多的 a
#   ② 'aaa' 匹配 'aaa', '' 匹配 '', 'baa' 匹配 'aa', '' 匹配 ''
```

---

#### 常见错误

> 1. **错误现象**:忘记写 r 前缀,`\d` 被 Python 转义
>    **原因:**r'\d' 是原始字符串,不加 r 会变成转义字符
> 2. **错误现象**:贪婪匹配 `.*` 匹配了太多内容
>    **原因:**`*` 默认贪婪。修正:用 `*?` 非贪婪

---

#### 学员代码区

```python
import re

# TODO: 提取字符串 'My phone is 13812345678' 中的所有数字
# TODO: 匹配 'aaa' 中的 a(用 + 量词)
# TODO: 匹配 'Hello world' 中的单词(用 \w+)
```

---

#### 参考答案

```python
import re

text = 'My phone is 13812345678'
print(re.findall(r'\d+', text))        # ['13812345678']
print(re.findall(r'a+', 'aaa'))        # ['aaa']
print(re.findall(r'\w+', 'Hello world'))  # ['Hello', 'world']
```

---

## 明日衔接

- 明天 Day 02 学什么:**常用模式**(邮箱/手机号/URL)
- 今天遗留的概念:今天学了基础语法,但还没学如何组合成常用模式
- 脚手架递进预告:Day 2 在 Day 1 基础上组合邮箱/手机号正则
