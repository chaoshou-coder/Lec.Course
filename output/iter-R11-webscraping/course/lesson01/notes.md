### Day 01 · 爬虫基础:发送请求与解析 HTML

> **痛点**:你想从网站抓取数据,但手动复制粘贴太慢。听说 Python 爬虫很简单,但自己写总是报错 —— 不知道 HTTP 请求是什么,不知道 HTML 怎么解析。今天你将写出人生第一个爬虫 —— 从真实网站抓取数据。
> **类比**:爬虫就像"自动快递站" —— 你给一个地址(URL),它帮你发请求(GET),收到包裹(HTML 响应),然后拆开取出需要的数据。
> **解释**:**爬虫 = 发送 HTTP 请求 → 接收 HTML 响应 → 解析提取数据 → 存储**。今天学前两步。

---

#### 发送 HTTP 请求 —— 用 requests 获取网页

> **痛点**:你在浏览器里输入 URL 就能看到网页,但怎么用 Python 获取同样的内容?
> **类比**:requests.get() 就像"让 Python 帮你打开浏览器",它发一个 HTTP GET 请求,返回网页的 HTML 源码。
> **解释**:**HTTP 请求**是客户端(你的 Python 脚本)向服务器(网站)要数据的过程。requests 库帮你发送这个请求。

```python
import requests

url = "https://books.toscrape.com/"
response = requests.get(url)

print("状态码:", response.status_code)  # 200 = 成功
print("内容长度:", len(response.text))   # HTML 源码长度
print("前 200 字符:", response.text[:200])
```

**逐行解剖**

- `import requests` = 导入 requests 库(需 `pip install requests`)
- `response = requests.get(url)` = 发送 GET 请求,返回 Response 对象
- `response.status_code` = HTTP 状态码(200 成功,404 不存在,429 请求过多)
- `response.text` = HTML 源码(字符串)

> **ASCII 请求流程图**
> ```
> 你的 Python 脚本              网站服务器
> │                              │
> │── GET /index.html ──────────▶│  ← requests.get(url)
> │                              │
%│◀── 200 OK + HTML ─────────────│  ← response.text
> │                              │
> ```

**常见错误**

> 1. **错误现象**:`ModuleNotFoundError: No module named 'requests'`
>    **原因:**没安装 requests 库。修正:`pip install requests`
> 2. **错误现象**:`ConnectionError` 或 `Timeout`
>    **原因:**网络不通或 URL 错误。修正:检查 URL 是否能浏览器打开

---

#### 解析 HTML —— 用 BeautifulSoup 提取数据

> **痛点**:requests 拿到了 HTML 源码,但它是一个大字符串,怎么提取"书名"和"价格"?
> **类比**:BeautifulSoup 就像"HTML 显微镜" —— 把混乱的 HTML 源码变成可查询的文档树,让你用 CSS 选择器精准定位元素。
> **解释**:**HTML 解析**是把 HTML 源码转换成可查询的文档对象模型(DOM),然后用 CSS 选择器或标签名提取内容。

```python
import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 提取页面标题
title = soup.find("h1").text
print("页面标题:", title)

# 提取所有书名
books = soup.find_all("h3")
for book in books[:5]:
    print("书名:", book.find("a")["title"])

# 提取所有价格
prices = soup.find_all("p", class_="price_color")
for price in prices[:5]:
    print("价格:", price.text)
```

**逐行解剖**

- `BeautifulSoup(response.text, "html.parser")` = 解析 HTML 源码,构建文档树
- `soup.find("h1")` = 找到第一个 `<h1>` 标签
- `soup.find_all("h3")` = 找到所有 `<h3>` 标签(返回列表)
- `book.find("a")["title"]` = 找到 `<a>` 标签,读取 `title` 属性
- `class_="price_color"` = CSS 类名选择器(注意 class 后面有下划线,因为 class 是 Python 保留字)

> **ASCII 解析流程图**
> ```
> HTML 源码(字符串)
> │
> ▼
> BeautifulSoup 解析
> │
> ▼
> 文档树(DOM)
> ├── <h1>Books to Scrape</h1>
> ├── <h3><a title="A Light in the Attic">...</a></h3>
> ├── <p class="price_color">£51.77</p>
> └── ...
> ```

**常见错误**

> 1. **错误现象**:`ModuleNotFoundError: No module named 'bs4'`
>    **原因:**没安装 beautifulsoup4。修正:`pip install beautifulsoup4`
> 2. **错误现象**:`AttributeError: 'NoneType' object has no attribute 'text'`
>    **原因:**find() 没找到元素(选择器写错)。修正:检查 CSS 选择器
> 3. **错误现象**:提取的内容是空的
>  **原因:**页面可能是 JavaScript 动态渲染的。修正:这是 Day 5 的内容

---

#### 执行过程跟踪

```python
# --- 执行过程 ---
# 第 1 行 import requests:
#   ① 导入 requests 库
#
# 第 3 行 response = requests.get(url):
#   ① 发送 HTTP GET 请求到 books.toscrape.com
#   ② 服务器返回 200 OK + HTML 源码
#   ③ response.status_code = 200
#   ④ response.text = HTML 源码字符串
#
# 第 7 行 soup = BeautifulSoup(response.text, "html.parser"):
#   ① 把 HTML 源码解析成文档树
#   ② 后续可以用 find/find_all 查询
#
# 第 10 行 title = soup.find("h1").text:
#   ① 找到第一个 <h1> 标签
#   ② 读取其文本内容
#
# 第 13 行 books = soup.find_all("h3"):
#   ① 找到所有 <h3> 标签
#   ② 返回列表,每个元素是一个 <h3> 标签
```

---

#### 常见错误

> 1. **错误现象**:`requests.get(url)` 返回 403
>    **原因:**网站检测到是爬虫(没有 User-Agent)。修正:加 headers(Day 4 详述)
> 2. **错误现象**:`find_all("h3")` 返回空列表
>  **原因:**该页面没有 `<h3>` 标签,或标签名大小写不对。修正:用浏览器开发者工具检查实际标签
> 3. **错误现象**:提取的文本包含多余空格/换行
>  **原因:**HTML 源码中有空白字符。修正:用 `.strip()` 清理

---

#### 学员代码区

在终端运行下面的代码(Day 1 就跑通第一个爬虫):

```python
import requests
from bs4 import BeautifulSoup

# TODO: 用 requests 获取 https://books.toscrape.com/
# TODO: 用 BeautifulSoup 解析 HTML
# TODO: 提取页面标题(<h1> 标签)
# TODO: 提取前 5 个书名(<h3> 标签内的 <a> 标签的 title 属性)
# TODO: 打印每个书名
```

---

#### 参考答案

```python
import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url)
print("状态码:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

title = soup.find("h1").text
print("页面标题:", title)

books = soup.find_all("h3")
for book in books[:5]:
    book_title = book.find("a")["title"]
    print("书名:", book_title)
```

---

## 明日衔接

- 明天 Day 02 学什么:**数据提取**(CSS 选择器 + 正则表达式)
- 今天遗留的概念:今天学了基本 find/find_all,但还没学复杂选择器
- 脚手架递进预告:
  - Day 1:基本 find/find_all
  - Day 2:CSS 选择器(更精准)
  - Day 3:数据存储
  - Day 4:反爬机制(NCDL 节点)
