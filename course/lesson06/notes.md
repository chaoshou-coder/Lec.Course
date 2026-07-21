### Day 06 · 表单进阶与语义化标签

> **痛点**:你的表单能用了,但看起来很粗糙 —— 点击文字不会聚焦输入框,按钮不知道是提交还是重置,页面全是用 div 堆的,像个纸箱做的房子。
> **类比**:label 就像电灯开关的标签,你按"灯"字就能开灯,不需要精准按开关;fieldset 就像档案袋,把相关材料装在一个袋子上写个总标题;语义化标签就像给每个房间贴上门牌 —— "厨房"、"卧室"、"客厅",而不是"房间1"、"房间2"。
> **解释**:HTML 提供了 label 关联输入控件、fieldset 分组表单字段、以及 header/nav/main/section/article/footer 等语义化标签,让页面从"能用"升级到"专业"。

---

#### button 标签 —— 表单的"触发器"

> **痛点**:你用了 `<input type="submit">` 当按钮,但想加个图标或换文字就不方便。
> **类比**:`<input type="submit">` 就像固定印章,只能盖一个章;`<button>` 就像万能按钮,里面可以放文字、图标、甚至其他标签。
> **解释**:`<button>` 是一个容器标签,type 属性决定它的行为:submit(提交,默认)、button(普通按钮)、reset(重置)。

```html
<!-- 提交按钮:点击后提交表单 -->
<button type="submit">提交</button>

<!-- 普通按钮:点击后不提交,通常配合 JavaScript -->
<button type="button">点击我(不提交)</button>

<!-- 重置按钮:点击后清空表单所有输入 -->
<button type="reset">重置</button>
```

**逐行解剖**

- `type="submit"` = 提交按钮,点击后触发表单提交(这是默认值)
- `type="button"` = 普通按钮,点击后什么都不做(需要 JS 绑定事件)
- `type="reset"` = 重置按钮,点击后把表单所有输入恢复默认值
- `<button>` 是容器标签,里面可以放文字、`<img>`、`<strong>` 等
- 和 `<input type="submit" value="提交">` 相比,button 更灵活

> **ASCII 内存图**
> ```
> <form>
>  ├── <button type="submit">提交</button>     ← 提交(默认)
>  ├── <button type="button">点击我</button>   ← 普通(JS 控制)
>  └── <button type="reset">重置</button>      ← 清空表单
> ```

**常见错误**

> 1. **错误现象**:form 里放了多个 submit 按钮,点了都提交
>    **原因:**多个 submit 按钮会分别提交,通常一个表单只需一个
> 2. **错误现象**:`<button>点击</button>`(没写 type)
>    **原因:**button 默认 type="submit",如果不想提交要显式写 type="button"
> 3. **错误现象**:想重置表单但用了 `<button type="reset">` 放在 form 外面
>    **原因:**reset 按钮必须放在 form 里才能控制该表单

> **问自己:**
> 1. button 的三种 type 分别有什么效果?
> 2. 为什么 form 里应该避免多个 submit 按钮?
> 3. button 和 input type="submit" 有什么区别?

**学员代码区**

```html
<!-- 下面有 2 处错误,修正它 -->
<form action="/search" method="GET">
    <input type="text" name="q" />
    <button type="button">搜索</button>
    <button type="submit">搜索</button>
</form>

<!-- TODO: 写出正确版本(只需要一个搜索按钮) -->
```

**参考答案**

```html
<!-- 错误 1:type="button" 不会提交,应该用 submit -->
<!-- 错误 2:两个 submit 按钮重复了 -->
<form action="/search" method="GET">
    <input type="text" name="q" />
    <button type="submit">搜索</button>
</form>
```

---

#### label 标签 —— 表单的"关联标签"

> **痛点**:用户要点输入框旁边的那几个小字才能聚焦输入框,体验很差。
> **类比**:label 就像电灯开关上的"灯"字 —— 你点"灯"字等于按开关,不需要精准按开关本身。
> **解释**:`<label>` 通过 `for` 属性关联 input 的 `id`,点击 label 就等于点击 input,既提升可访问性(读屏软件),又提升点击体验。

```html
<!-- 方式 1:for 属性关联 input 的 id -->
<label for="username">用户名:</label>
<input type="text" id="username" name="username" />

<!-- 方式 2:label 直接包裹 input(隐式关联) -->
<label>
    密码:
    <input type="password" name="password" />
</label>
```

**逐行解剖**

- `<label for="username">` = for 属性的值 = 目标 input 的 id
- `<input id="username">` = id 必须与 label 的 for 一致
- 点击"用户名:"文字时,光标自动聚焦到输入框
- 方式 2 是隐式关联,label 包裹 input 时不需要 for/id
- 一个 label 只能关联一个 input,一个 input 可以被多个 label 关联

> **ASCII 内存图**
> ```
> <label for="username">用户名:</label>
>              │
>              ↓ (关联)
> <input type="text" id="username" name="username" />
>
> 点击"用户名:" → 光标定位到输入框
> ```

**常见错误**

> 1. **错误现象**:`<label for="username">` 但 input 没有 id="username"
>    **原因:**for 找不到对应的 id,关联失效,点击 label 没反应
> 2. **错误现象**:input 的 id 有两个值 `id="username password"`
>    **原因:**id 只能是一个值,不能有空格(空格表示两个 id-class 混淆)
> 3. **错误现象**:用纯文字 `<span>` 代替 label
>    **原因:**span 无法关联输入框,读屏软件也无法知道这段文字对应哪个输入框

> **问自己:**
> 1. label 的 for 属性和 input 的 id 有什么关系?
> 2. 显式关联(for/id)和隐式关联(包裹)哪种更好?
> 3. 为什么 label 能提升可访问性?

**学员代码区**

```html
<!-- 下面有 2 处错误,修正它 -->
<label for="email">邮箱</label>
<input type="email" id="user-email" name="email" />

<label for="agree">
    <input type="checkbox" id="agree" name="agree" />
</label>

<!-- TODO: 写出正确版本 -->
```

**参考答案**

```html
<!-- 错误 1:label for="email" 但 input id="user-email",不一致 -->
<!-- 错误 2:隐式关联不需要 for,写了反而混乱 -->
<label for="email">邮箱:</label>
<input type="email" id="email" name="email" />

<label>
    <input type="checkbox" name="agree" />
    我同意条款
</label>
```

---

#### fieldset/legend —— 表单的"分组夹"

> **痛点**:表单字段太多,用户不知道哪些是"基本信息"哪些是"联系信息"。
> **类比**:fieldset 就像档案夹,把相关的材料夹在一起;legend 就是档案夹上的总标题。
> **解释**:`<fieldset>` 把相关字段包起来(默认有边框),`<legend>` 是 fieldset 的标题,显示在边框上。

```html
<form action="/register" method="POST">
    <fieldset>
        <legend>基本信息</legend>
        <p>姓名:<input type="text" name="name" /></p>
        <p>年龄:<input type="number" name="age" /></p>
    </fieldset>

    <fieldset>
        <legend>账号信息</legend>
        <p>用户名:<input type="text" name="username" /></p>
        <p>密码:<input type="password" name="password" /></p>
    </fieldset>
</form>
```

**逐行解剖**

- `<fieldset>` = 分组容器,默认渲染为一个带边框的盒子
- `<legend>` = fieldset 的标题,显示在边框的左上角
- 一个 form 可以有多个 fieldset,每个 fieldset 有一个 legend
- legend 必须是 fieldset 的第一个子元素(否则显示位置不对)

> **ASCII 内存图**
> ```
> <form>
>  ├── <fieldset>                    ← 分组 1(带边框)
>  │    ├── <legend>基本信息</legend>  ← 标题(左上角)
>  │    ├── 姓名: <input />
>  │    └── 年龄: <input />
>  └── <fieldset>                    ← 分组 2(带边框)
>       ├── <legend>账号信息</legend>  ← 标题(左上角)
>       ├── 用户名: <input />
>       └── 密码: <input />
> ```

**常见错误**

> 1. **错误现象**:`<legend>` 没有作为 fieldset 的第一个子元素
>    **原因:**legend 不是第一个子元素时,显示位置会错乱
> 2. **错误现象**:`<fieldset>` 里没有 `<legend>`
>    **原因:**没有 legend 的 fieldset 只有边框没有标题,意义不完整
> 3. **错误现象**:legend 放在 fieldset 外面
>    **原因:**legend 必须是 fieldset 的子元素,放在外面就没有标题效果

> **问自己:**
> 1. fieldset 和 legend 的关系是什么?
> 2. 为什么表单字段要分组?
> 3. legend 在 fieldset 中的位置有什么要求?

**学员代码区**

```html
<!-- 下面有 2 处错误,修正它 -->
<form action="/signup" method="POST">
    <fieldset>
        <p>姓名:<input type="text" name="name" /></p>
        <legend>基本信息</legend>
    </fieldset>
</form>

<!-- TODO: 写出正确版本 -->
```

**参考答案**

```html
<!-- 错误 1:legend 不是 fieldset 的第一个子元素 -->
<form action="/signup" method="POST">
    <fieldset>
        <legend>基本信息</legend>
        <p>姓名:<input type="text" name="name" /></p>
    </fieldset>
</form>
```

---

#### 综合示例 —— 带分组的注册表单

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <title>用户注册</title>
</head>
<body>
    <h1>用户注册</h1>

    <form action="/register" method="POST">
        <fieldset>
            <legend>基本信息</legend>
            <p>
                <label for="name">姓名:</label>
                <input type="text" id="name" name="name" />
            </p>
            <p>
                <label for="age">年龄:</label>
                <input type="number" id="age" name="age" />
            </p>
        </fieldset>

        <fieldset>
            <legend>账号信息</legend>
            <p>
                <label for="user">用户名:</label>
                <input type="text" id="user" name="username" />
            </p>
            <p>
                <label for="pwd">密码:</label>
                <input type="password" id="pwd" name="password" />
            </p>
            <p>
                <label for="email">邮箱:</label>
                <input type="email" id="email" name="email" />
            </p>
        </fieldset>

        <p>
            <button type="submit">注册</button>
            <button type="reset">重置</button>
        </p>
    </form>
</body>
</html>
```

**逐行解剖**

- 两个 `<fieldset>` 把表单分成"基本信息"和"账号信息"
- 每个 fieldset 的第一个子元素是 `<legend>`(标题)
- 所有 input 都用 `<label for="...">` 关联
- 底部两个 button:一个 submit 提交,一个 reset 重置

**为什么:**这个表单就像一本分两章的登记表 —— 第一章"基本信息",第二章"账号信息",每章有标题,每个输入项有清晰的标签。用户填写时一目了然。

> **问自己:**
> 1. 为什么每个 legend 都是 fieldset 的第一个子元素?
> 2. label 和 input 的关联关系是怎么建立的?
> 3. submit 和 reset 按钮有什么区别?

---

#### 语义化标签 header/nav/main/section/article/footer —— 页面的"骨架"

> **痛点**:你的页面全是用 `<div>` 堆的 —— `<div id="header">`,`<div id="nav">`,`<div id="main">` —— div 没有语义,浏览器和搜索引擎不知道每个 div 是干什么的。
> **类比**:`<div>` 是"箱子",语义化标签是"贴着标签的箱子" —— `<header>` 贴着"页头"标签,`<nav>` 贴着"导航"标签,`<main>` 贴着"主体"标签。
> **解释**:HTML5 引入语义化标签,用有意义的标签名替代 div,让浏览器、搜索引擎、读屏软件都能理解页面结构。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <title>我的网站</title>
</head>
<body>
    <header>
        <h1>网站标题</h1>
        <p>网站副标题</p>
    </header>

    <nav>
        <a href="index.html">首页</a>
        <a href="about.html">关于</a>
        <a href="contact.html">联系</a>
    </nav>

    <main>
        <section>
            <h2>第一章节</h2>
            <p>章节内容...</p>
        </section>

        <section>
            <h2>第二章节</h2>
            <p>章节内容...</p>
        </section>
    </main>

    <footer>
        <p>© 2026 我的网站</p>
    </footer>
</body>
</html>
```

**逐行解剖**

- `<header>` = 页头,通常包含 logo、标题、副标题。一个页面可以有多个 header
- `<nav>` = 导航栏,包含一组链接(主导航)
- `<main>` = 页面主体内容,一个页面只能有一个 main
- `<section>` = 章节,把主体内容分成几个独立的部分
- `<article>` = 独立的文章/帖子/评论(完整、独立、可复用)
- `<footer>` = 页脚,通常包含版权信息、联系方式

> **ASCII 内存图**
> ```
> <body>
>  ├── <header>           ← 页头(标题/logo)
>  │    ├── <h1>网站标题</h1>
>  │    └── <p>副标题</p>
>  ├── <nav>              ← 导航栏(一组链接)
>  │    ├── <a>首页</a>
>  │    ├── <a>关于</a>
>  │    └── <a>联系</a>
>  ├── <main>             ← 主体内容(唯一)
>  │    ├── <section>     ← 章节 1
>  │    │    └── ...
>  │    └── <section>     ← 章节 2
>  │         └── ...
>  └── <footer>           ← 页脚(版权/联系方式)
>       └── <p>© 2026</p>
> ```

**常见错误**

> 1. **错误现象**:一个页面有多个 `<main>`
>    **原因:**main 代表页面的主体内容,一个页面只能有一个
> 2. **错误现象**:`<nav>` 包了一堆不相关的链接
> │   **原因:**nav 应该只放主导航,页脚的链接组不需要 nav
> 3. **错误现象**:`<section>` 里没有标题标签(h2/h3)
>    **原因:**section 是一个有主题的部分,应该有标题说明主题
> 4. **错误现象**:`<article>` 用在不是独立内容的地方
>    **原因:**article 必须是独立可复用的内容(如博客文章、评论)

> **问自己:**
> 1. `<header>` 和 `<h1>` 的区别是什么?
> 2. `<section>` 和 `<article>` 的区别是什么?
> 3. 为什么一个页面只能有一个 `<main>`?

**学员代码区**

```html
<!-- 下面有 3 处错误,修正它 -->
<body>
    <main>
        <h1>文章标题</h1>
        <p>文章内容...</p>
    </main>
    <main>
        <h2>侧边栏</h2>
        <p>侧边内容...</p>
    </main>
    <nav>
        <p>这不是导航,是版权声明</p>
    </nav>
</body>

<!-- TODO: 写出正确版本 -->
```

**参考答案**

```html
<!-- 错误 1:两个 main -->
<!-- 错误 2:nav 里放了非导航内容 -->
<body>
    <main>
        <h1>文章标题</h1>
        <p>文章内容...</p>
        <aside>
            <h2>侧边栏</h2>
            <p>侧边内容...</p>
        </aside>
    </main>
    <footer>
        <p>© 2026 版权声明</p>
    </footer>
</body>
```

---

#### 综合示例 —— 语义化结构的博客页面

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <title>我的博客</title>
</head>
<body>
    <header>
        <h1>我的博客</h1>
        <p>记录学习笔记和生活感悟</p>
    </header>

    <nav>
        <a href="index.html">首页</a>
        <a href="articles.html">文章</a>
        <a href="about.html">关于</a>
    </nav>

    <main>
        <article>
            <h2>HTML 语义化标签学习笔记</h2>
            <p>今天学习了 header、nav、main、section、
            article、footer 这 6 个语义化标签...</p>
            <section>
                <h3>什么是语义化</h3>
                <p>语义化就是用有意义的标签名...</p>
            </section>
            <section>
                <h3>语义化的好处</h3>
                <p>1. 搜索引擎更容易理解页面...</p>
            </section>
        </article>

        <article>
            <h2>CSS 入门笔记</h2>
            <p>CSS 是层叠样式表,用于控制页面外观...</p>
        </article>
    </main>

    <footer>
        <p>© 2026 我的博客 | 联系我们</p>
    </footer>
</body>
</html>
```

**逐行解剖**

- `<header>` = 页头,包含博客标题和副标题
- `<nav>` = 导航栏,包含首页/文章/关于三个链接
- `<main>` = 主体,包含两篇独立的文章
- `<article>` = 每篇文章独立,可复用(单独看也有意义)
- `<article>` 里的 `<section>` = 文章内的章节
- `<footer>` = 页脚,声明版权

**为什么:**这个结构就像一本杂志 —— 封面(header)、目录目录(nav)、正文(main)分为多篇文章(article),每篇文章内有小节(section),最后是版权页(footer)。

> **问自己:**
> 1. 为什么 `<article>` 里面还能有 `<section>`?
> 2. `<nav>` 里的链接跳转到哪里?
> 3. 如果不写语义化标签,用 div 代替,会有什么影响?

---

#### 常见错误汇总

> 1. **错误现象**:`<button>点击</button>` 在 form 里点击后提交了
>    **原因:**button 默认 type="submit",不写 type 就会提交
> 2. **错误现象**:label 的 for 和 input 的 id 不一致
>    **原因:**关联失效,点击 label 无反应
> 3. **错误现象**:legend 不是 fieldset 的第一个子元素
>    **原因:**legend 显示位置会错乱
> 4. **错误现象**:一个页面多个 `<main>`
>    **原因:**main 代表主体,一个页面只能有一个
> 5. **错误现象**:`<section>` 没有标题标签
>    **原因:**section 应该有标题说明主题
> 6. **错误现象**:`<nav>` 包了非导航的链接组
>    **原因:**nav 只用于主导航,页脚链接不需要 nav

---

#### 学员代码区

新建文件 `blog.html`,用语义化标签搭建一个博客首页,要求:

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <title>我的博客</title>
</head>
<body>
    <!-- TODO: header 包含 h1 标题 + p 副标题 -->

    <!-- TODO: nav 包含 3 个链接(首页/文章/关于) -->

    <!-- TODO: main 包含两篇 article,每篇有 h2 + p -->

    <!-- TODO: footer 包含版权信息 -->

</body>
</html>
```

---

#### 参考答案

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <title>我的博客</title>
</head>
<body>
    <header>
        <h1>我的博客</h1>
        <p>记录学习笔记</p>
    </header>

    <nav>
        <a href="index.html">首页</a>
        <a href="articles.html">文章</a>
        <a href="about.html">关于</a>
    </nav>

    <main>
        <article>
            <h2>HTML 学习笔记</h2>
            <p>今天学习了表单和语义化标签...</p>
        </article>

        <article>
            <h2>CSS 入门</h2>
            <p>CSS 用于控制页面的视觉样式...</p>
        </article>
    </main>

    <footer>
        <p>© 2026 我的博客</p>
    </footer>
</body>
</html>
```

保存后用浏览器打开,你应该看到:
- 顶部页头(标题 + 副标题)
- 导航栏(三个链接)
- 主体部分(两篇文章)
- 底部页脚(版权信息)

**恭喜!你学会了表单进阶和语义化标签,页面从"能用"升级到"专业"。** 🎉
