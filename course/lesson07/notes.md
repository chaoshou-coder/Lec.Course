### Day 07 · 代码结构与多页面网站整合

> **痛点**:你的 HTML 能跑,但代码乱得像一团麻 —— 缩进混乱、没有注释、嵌套三层就找不到标签在哪。更关键的是,你只会做单页面,不会把多个页面连成一个网站。
> **类比**:代码结构就像写文章的段落和标点 —— 缩进是段落首行空两格,注释是给读者的批注,空行是段落之间的间隔。多页面网站就像一本小册子,每页是独立的内容,但通过目录(nav)互相链接。
> **解释**:好的代码结构让人类可读(自己能维护、别人能看懂),HTML 注释让代码能"说话",多页面链接让单页面升级为一个完整的网站。

---

#### 代码可读性 —— 让代码"读起来像文章"

> **痛点**:你写的代码能跑,但过三天自己再看就懵了 —— 标签嵌套三层就找不到闭标签在哪。
> **类比**:没有缩进的代码就像没有段落和标点的文章,读起来令人窒息。
> **解释**:HTML 的缩进、空行、一致的嵌套风格,让代码结构一目了然,自己和别人都能快速读懂。

```html
<!-- 反面教材:没有缩进,读起来像一坨 -->
<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><title>我的网页</title></head><body><h1>标题</h1><p>段落</p></body></html>

<!-- 正面教材:有缩进,结构清晰 -->
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <title>我的网页</title>
</head>
<body>
    <h1>标题</h1>
    <p>段落</p>
</body>
</html>
```

**逐行解剖**

- 每层嵌套缩进 4 个空格(或 1 个 Tab)
- 开标签和闭标签垂直对齐(闭标签和开标签同一列)
- 块级元素(如 `<h1>` `<p>`)独占一行
- 行内元素(如 `<strong>` `<a>`)可以放在一行内
- 空行分隔不同逻辑块(如 head 和 body 之间)

> **ASCII 内存图**
> ```
> 缩进规则(每深一层,缩进 4 空格):
>
> <body>                    ← 第 0 层
>     <header>              ← 第 1 层(4 空格)
>         <h1>标题</h1>     ← 第 2 层(8 空格)
>     </header>             ← 第 1 层(与 header 对齐)
>     <main>                ← 第 1 层
>         <section>         ← 第 2 层
>             <h2>小标题</h2>  ← 第 3 层
>         </section>        ← 第 2 层
>     </main>               ← 第 1 层
> </body>                   ← 第 0 层
> ```

**常见错误**

> 1. **错误现象**:缩进不一致(有的 2 空格,有的 4 空格,有的 Tab)
>    **原因:**混用缩进方式会让嵌套层级混乱,统一用 4 空格或 1 个 Tab
> 2. **错误现象**:开标签和闭标签不对齐
>    **原因:**闭标签应该和开标签在同一列,否则找不到配对
> 3. **错误现象**:所有代码挤在一起,没有空行分隔
>    **原因:**空行分隔逻辑块,让代码有"段落感"

> **问自己:**
> 1. 为什么缩进对 HTML 很重要?
> 2. 闭标签应该和谁对齐?
> 3. 空行在代码中起什么作用?

**学员代码区**

```html
<!-- 下面这段代码缩进混乱,重新格式化它 -->
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<title>我的网页</title>
</head>
<body>
    <h1>标题</h1>
        <p>段落</p>
<main>
<h2>内容</h2>
</main>
</body>
</html>

<!-- TODO: 重新格式化,让缩进一致 -->
```

**参考答案**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <title>我的网页</title>
</head>
<body>
    <h1>标题</h1>
    <p>段落</p>
    <main>
        <h2>内容</h2>
    </main>
</body>
</html>
```

---

#### HTML 注释 —— 让代码"说话"

> **痛点**:你三个月前写的代码,现在完全看不懂当时为什么这么写。
> **类比**:HTML 注释就像课本上的批注 —— 给未来的自己(或别人)解释"为什么这么写"。
> **解释**:HTML 注释用 `<!-- -->` 包裹,浏览器不会渲染,但开发者能看到。用于说明、标记、临时隐藏代码。

```html
<!-- 这是单行注释:说明下面这段代码的作用 -->
<h1>网站标题</h1>

<!-- 
    这是多行注释:
    下面是一个导航栏,
    包含首页/关于/联系三个链接
-->
<nav>
    <a href="index.html">首页</a>
    <a href="about.html">关于</a>
    <a href="contact.html">联系</a>
</nav>

<!-- 临时隐藏某段代码(调试时常用) -->
<!--
<p>这段文字暂时不显示</p>
-->
```

**逐行解剖**

- `<!--` = 注释开始
- `-->` = 注释结束
- 注释可以跨多行
- 注释不能嵌套(`<!-- <!-- --> -->` 会出错)
- 浏览器完全忽略注释内容,不渲染

> **ASCII 内存图**
> ```
> <!-- 注释开始
>      注释内容(浏览器不渲染)
>    注释结束 -->
>
> 常见用途:
>   ① 说明:<!-- 下面是一个导航栏 -->
>   ② 标记:<!-- TODO: 补充内容 -->
>   ③ 临时隐藏:<!-- <p>暂时不显示</p> -->
> ```

**常见错误**

> 1. **错误现象**:`<!-- <!-- 嵌套注释 --> -->`
>    **原因:**HTML 注释不能嵌套,第一个 --> 就结束了注释
> 2. **错误现象**:`<-- 这是注释 -->`(少了一个感叹号)
>    **原因:**正确的开始是 `<!--`,不是 `<--`
> 3. **错误现象**:注释里有 `--`(如 `<!-- 这是 -- 注释 -->`)
>    **原因:**注释内容不能包含 `--` 序列,会导致意外结束

> **问自己:**
> 1. HTML 注释的语法是什么?
> 2. 注释的三种常见用途是什么?
> 3. 注释能嵌套吗?

**学员代码区**

```html
<!-- 下面有 2 处错误,修正它 -->
<-- 这是一个注释 -->
<!-- 这是 <!-- 嵌套注释 --> 错误 -->

<!-- TODO: 写出正确版本 -->
```

**参考答案**

```html
<!-- 错误 1:开始标签应该是 <!--,不是 <-- -->
<!-- 错误 2:注释不能嵌套 -->
<!-- 这是一个注释 -->
<!-- 这是嵌套注释 错误 -->
```

---

#### 多页面链接 —— 网站的"目录"

> **痛点**:你只会做单页面,不知道如何把多个页面连成一个网站。
> **类比**:多页面网站就像一本杂志 —— 每页是独立的内容,但通过目录(nav)互相链接,读者可以从任何一页跳到其他页。
> **解释**:用 `<a href="xxx.html">` 链接到同站点下的其他页面,通过相对路径找到目标文件,实现多页面导航。

```html
<!-- 假设项目目录结构如下:
    my-website/
    ├── index.html      ← 首页
    ├── about.html      ← 关于页
    ├── contact.html    ← 联系页
    └── images/
        └── logo.jpg    ← 图片
-->

<!-- 在 index.html 中链接到其他页面 -->
<nav>
    <a href="index.html">首页</a>
    <a href="about.html">关于</a>
    <a href="contact.html">联系</a>
</nav>

<!-- 在 about.html 中链接回首页 -->
<nav>
    <a href="index.html">首页</a>
    <a href="about.html">关于</a>
    <a href="contact.html">联系</a>
</nav>
```

**逐行解剖**

- `href="index.html"` = 链接到同目录下的 index.html
- `href="about.html"` = 链接到同目录下的 about.html
- `href="images/logo.jpg"` = 链接到子目录 images 下的文件
- `href="../index.html"` = `../` 表示上一级目录
- 每个页面的 nav 应该一致(用户从任何页面都能跳到其他页面)

> **ASCII 内存图**
> ```
> 项目目录:
> my-website/
> ├── index.html      ← href="index.html"
> ├── about.html      ← href="about.html"
> ├── contact.html    ← href="contact.html"
> └── images/
>     └── logo.jpg    ← href="images/logo.jpg"
>
> 页面链接关系:
> index.html ──→ about.html
>      │              │
>      └──→ contact.html ←──┘
>      (每个页面都有 nav,互相链接)
> ```

**常见错误**

> 1. **错误现象**:`<a href="C:\Users\name\about.html">`(用绝对路径)
>    **原因:**绝对路径在你的电脑上能跑,换台电脑就失效,要用相对路径
> 2. **错误现象**:`<a href="About.html">`(大小写不一致)
>    **原因:**Linux 服务器区分大小写,About.html 和 about.html 是两个文件
> 3. **错误现象**:`<a href="about.html">` 但文件实际在子目录里
>    **原因:**相对路径是相对于当前文件的位置,不是相对于项目根目录

> **问自己:**
> 1. 什么是相对路径?什么是绝对路径?
> 2. `../` 在路径中表示什么?
> 3. 为什么每个页面的 nav 应该保持一致?

**学员代码区**

```html
<!-- 假设目录结构:
    site/
    ├── index.html
    ├── products.html
    └── pages/
        └── about.html
-->

<!-- 在 pages/about.html 中,链接到根目录的 index.html -->
<!-- TODO: 写出正确的 href -->

<!-- 在 index.html 中,链接到 pages/about.html -->
<!-- TODO: 写出正确的 href -->
```

**参考答案**

```html
<!-- 在 pages/about.html 中,链接到根目录的 index.html -->
<!-- ../ 表示上一级目录(从 pages/ 回到 site/) -->
<a href="../index.html">首页</a>

<!-- 在 index.html 中,链接到 pages/about.html -->
<!-- pages/ 表示进入子目录 -->
<a href="pages/about.html">关于</a>
```

---

#### 项目目录结构 —— 网站的"文件柜"

> **痛点**:你的项目里 HTML、图片、CSS 全堆在一个目录,找个文件要翻半天。
> **类比**:好的目录结构就像文件柜 —— 每个抽屉贴了标签,文件分类存放,找起来一目了然。
> **解释**:把 HTML 放根目录,图片放 images/,CSS 放 css/,JS 放 js/,让项目结构清晰。

```text
my-website/                     ← 项目根目录
├── index.html                  ← 首页
├── about.html                  ← 关于页
├── contact.html                ← 联系页
├── css/                        ← 样式文件夹
│   └── style.css               ← 样式文件
├── js/                         ← 脚本文件夹
│   └── script.js               ← JavaScript 文件
└── images/                     ← 图片文件夹
    ├── logo.jpg                ← Logo 图片
    ├── banner.jpg              ← 横幅图片
    └── icons/                  ← 图标子文件夹
        └── favicon.ico         ← 网站图标
```

**逐行解剖**

- 根目录放所有 HTML 页面(或按模块分子目录)
- `css/` 放所有 CSS 样式文件
- `js/` 放所有 JavaScript 文件
- `images/` 放所有图片资源
- 子目录可以再嵌套(如 `images/icons/`)
- 文件名用小写 + 短横线(kebab-case),不用中文和空格

> **ASCII 内存图**
> ```
> my-website/                      ← 项目根
>  ├── index.html                  ← 首页
>  ├── about.html                  ← 关于
>  ├── contact.html                ← 联系
>  ├── css/
>  │    └── style.css              ← 样式
>  ├── js/
>  │    └── script.js              ← 脚本
>  └── images/
>       ├── logo.jpg               ← Logo
>       ├── banner.jpg             ← 横幅
>       └── icons/
>           └── favicon.ico        ← 图标
> ```

**常见错误**

> 1. **错误现象**:文件名用中文 `首页.html`
>    **原因:**中文文件名在服务器上可能乱码,用英文小写
> 2. **错误现象**:文件名用空格 `my page.html`
>    **原因:**空格在 URL 里会变成 `%20`,用短横线代替 `my-page.html`
> 3. **错误现象**:所有文件堆在一个目录
>    **原因:**文件多了以后找不到,按类型分目录

> **问自己:**
> 1. 为什么要把图片、CSS、JS 分目录存放?
> 2. 文件名应该用什么命名风格?
> 3. 如果图片很多,怎么组织?

**学员代码区**

```text
<!-- 下面是一个混乱的项目目录,重新组织它 -->
my-site/
├── index.html
├── 关于.html
├── my page.html
├── logo.jpg
├── style.css
├── banner.png
├── script.js
├── about-photo.jpg
└── contact-form.js

<!-- TODO: 重新组织目录结构 -->
```

**参考答案**

```text
my-site/
├── index.html
├── about.html                    ← 改:中文 → 英文
├── contact.html                  ← 改:空格 → 短横线
├── css/
│   └── style.css
├── js/
│   ├── script.js
│   └── contact-form.js
└── images/
    ├── logo.jpg
    ├── banner.png
    └── about-photo.jpg
```

---

#### 综合示例 —— 一个完整的三页面网站

```text
my-blog/                        ← 项目根目录
├── index.html                  ← 首页
├── about.html                  ← 关于页
├── contact.html                ← 联系页
└── images/
    └── logo.jpg                ← Logo 图片
```

**index.html (首页):**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <title>我的博客 - 首页</title>
</head>
<body>
    <!-- 页头 -->
    <header>
        <h1>我的博客</h1>
        <p>记录学习笔记</p>
    </header>

    <!-- 导航栏:链接到所有页面 -->
    <nav>
        <a href="index.html">首页</a>
        <a href="about.html">关于</a>
        <a href="contact.html">联系</a>
    </nav>

    <!-- 主体内容 -->
    <main>
        <article>
            <h2>HTML 学习笔记</h2>
            <p>今天学习了表单和语义化标签...</p>
        </article>
        <article>
            <h2>CSS 入门</h2>
            <p>CSS 是层叠样式表...</p>
        </article>
    </main>

    <!-- 页脚 -->
    <footer>
        <p>© 2026 我的博客</p>
    </footer>
</body>
</html>
```

**about.html (关于页):**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <title>我的博客 - 关于</title>
</head>
<body>
    <!-- 页头(和首页一致) -->
    <header>
        <h1>我的博客</h1>
        <p>记录学习笔记</p>
    </header>

    <!-- 导航栏(和首页一致) -->
    <nav>
        <a href="index.html">首页</a>
        <a href="about.html">关于</a>
        <a href="contact.html">联系</a>
    </nav>

    <!-- 主体内容(不同) -->
    <main>
        <h2>关于我</h2>
        <p>我是一名正在学习 HTML 的初学者。</p>
        <p>这个博客记录了我的学习历程。</p>
    </main>

    <!-- 页脚(和首页一致) -->
    <footer>
        <p>© 2026 我的博客</p>
    </footer>
</body>
</html>
```

**contact.html (联系页):**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <title>我的博客 - 联系</title>
</head>
<body>
    <!-- 页头(和首页一致) -->
    <header>
        <h1>我的博客</h1>
        <p>记录学习笔记</p>
    </header>

    <!-- 导航栏(和首页一致) -->
    <nav>
        <a href="index.html">首页</a>
        <a href="about.html">关于</a>
        <a href="contact.html">联系</a>
    </nav>

    <!-- 主体内容(不同) -->
    <main>
        <h2>联系我</h2>
        <form action="/contact" method="POST">
            <p>
                <label for="name">姓名:</label>
                <input type="text" id="name" name="name" />
            </p>
            <p>
                <label for="email">邮箱:</label>
                <input type="email" id="email" name="email" />
            </p>
            <p>
                <label for="msg">留言:</label>
                <textarea id="msg" name="message"
                    rows="4" cols="30"></textarea>
            </p>
            <p>
                <button type="submit">发送</button>
            </p>
        </form>
    </main>

    <!-- 页脚(和首页一致) -->
    <footer>
        <p>© 2026 我的博客</p>
    </footer>
</body>
</html>
```

**逐行解剖**

- 三个页面有相同的 header、nav、footer(保证网站一致性)
- 每个页面的 main 内容不同(首页=文章列表,关于=自我介绍,联系=表单)
- nav 在所有页面保持一致,用户可以从任何页面跳到其他页面
- 目录结构清晰:HTML 在根目录,图片在 images/

**为什么:**这个三页面网站就像一本三页的小册子 —— 封面(首页)、内页(关于)、回执(联系),每页有相同的页头页脚和导航,但主体内容不同。

> **问自己:**
> 1. 为什么每个页面的 nav 应该一致?
> 2. 相对路径 `href="about.html"` 是相对于什么位置?
> 3. 如果新增一个页面,需要改哪些地方?

---

#### 常见错误汇总

> 1. **错误现象**:缩进混乱,嵌套层级看不清
>    **原因:**统一用 4 空格或 1 个 Tab,闭标签和开标签对齐
> 2. **错误现象**:注释嵌套 `<!-- <!-- --> -->`
>    **原因:**HTML 注释不能嵌套
> 3. **错误现象**:用绝对路径 `C:\Users\...`
>    **原因:**绝对路径换台电脑就失效,用相对路径
> 4. **错误现象**:文件名用中文或空格
>    **原因:**用英文小写 + 短横线命名
> 5. **错误现象**:每个页面的 nav 不一样
>    **原因:**nav 应该保持一致,用户才能从任何页面导航
> 6. **错误现象**:所有文件堆在一个目录
>    **原因:**按类型分目录(css/js/images)

---

#### 学员代码区

新建一个三页面网站,目录结构如下:

```text
my-site/
├── index.html
├── about.html
└── contact.html
```

要求:
1. 三个页面都有相同的 header(h1 + p)、nav(3 个链接)、footer(版权)
2. nav 包含首页/关于/联系三个链接,所有页面一致
3. index.html 的 main 包含两篇 article
4. about.html 的 main 包含自我介绍
5. contact.html 的 main 包含一个表单(姓名/邮箱/留言/提交)
6. 代码缩进一致,有适当的注释

---

#### 参考答案

参见上方"综合示例"部分,那里给出了完整的三页面网站代码。

保存后用浏览器打开 index.html,你应该看到:
- 顶部页头(标题 + 副标题)
- 导航栏(三个链接,点击可跳转到其他页面)
- 主体内容(首页=文章列表)
- 底部页脚(版权信息)

点击导航栏的"关于"链接,跳转到 about.html,看到自我介绍;
点击"联系"链接,跳转到 contact.html,看到联系表单。

**恭喜!你已经掌握了 HTML 的完整技能链,可以独立搭建一个多页面网站。** 🎉
