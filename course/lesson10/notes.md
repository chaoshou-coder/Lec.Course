### Day 10 · 综合项目 —— 联系表单页 + 站点整合 + 部署上线

> **痛点**:你学会了展示内容(标题、图片、列表、卡片),但做不出"能跟用户互动"的东西——让访客填写信息、提交留言。做完整个站点却发现只有自己电脑上能看,朋友打不开。从"写页面"到"做真正的网站",差的就是表单 + 部署这两步。
> **类比**:表单就像前台的访客登记表,form 是表格封面,name/email/message 是各个填字栏,button 是"提交"按钮。部署就像把你的作品从卧室搬到商场橱窗里——全世界都能看到。
> **解释**:HTML 表单(`<form>`)是用户与网站交互的核心载体,由各类 `<input>`(文本/邮箱/电话等)、`<textarea>`(多行文本)、`<button>`(提交)组成。GitHub Pages 是 GitHub 提供的免费静态托管服务,把 HTML 文件 push 到仓库,就能获得一个 `用户名.github.io` 的公网地址。

---

#### form 标签是什么 —— 访客登记表

**逐行解剖**

form 是表单的外壳,定义"哪些字段要发给服务端、怎么发":

```html
<form action="#" method="post">
    <!-- 表单控件都写在这里 -->
</form>
```

- `action="#"`:提交到哪里。`#` 表示提交到当前页面(占位,后续课程会接后端)。
- `method="post"`:发送方式。post = 把数据"打包"发送(适合表单)。
- 所有需要用户填写的控件(input/textarea)都**必须放在 form 里**,否则提交时收集不到。

**为什么:**form 就像一个信封——action 是寄到哪里,method 是平信还是挂号信,里面的 input 控件是你填写的信纸。

> **问自己:**
> 1. input 能放在 form 外面吗?提交时会怎样?
> 2. action="#" 是什么意思?什么时候需要改成真实地址?
> 3. method="get" 和 method="post" 有什么区别?

---

#### input 标签 —— 万能输入框

**ASCII 内存图**

```
<input> 类型一览(通过 type 属性区分)
├── type="text"        ← 单行文本(默认值)
├── type="email"       ← 邮箱(带格式校验)
├── type="tel"         ← 电话号码
├── type="url"         ← 网址
├── type="number"      ← 数字
├── type="password"    ← 密码(掩码显示)
├── type="search"      ← 搜索框
└── type="hidden"      ← 隐藏输入(用户看不到)
```

**代码示例**

```html
<!-- 单行文本输入 -->
<input type="text" name="username" placeholder="请输入姓名" />

<!-- 邮箱输入(浏览器会校验 @ 符号) -->
<input type="email" name="email" placeholder="your@email.com" />

<!-- 电话输入 -->
<input type="tel" name="phone" placeholder="13800138000" />
```

**逐行解剖**

- `type="text"`:最基本的文本框,一行,单行输入。
- `name="username"`:字段名,提交时后台靠这个 key 识别"这是用户名"。**必须有 name**。
- `placeholder="请输入姓名"`:占位提示,用户一开始能看到,输入后消失。不是默认值!

**常见错误**

> 1. **错误现象**:input 没有 name 属性
>    **原因**:提交表单时,name 是后台识别字段的 key,没 name = 数据丢失
> 2. **错误现象**:用 placeholder 代替 label
>    **原因**:placeholder 是辅助提示,不是标题;用户一开始输入就消失,容易忘记要填啥
> 3. **错误现象**:`<input type="text"></input>`(写了闭标签)
>    **原因**:input 是自闭合标签,没有内容,不能有闭标签

> **问自己:**
> 1. placeholder 和 value 有什么区别?哪个会被提交?
> 2. type="email" 比 type="text" 多了什么功能?
> 3. 为什么 password 类型会把字符变成 • ?

---

#### textarea 与 button —— 多行文本 + 提交

**代码示例**

```html
<!-- 多行文本输入 -->
<textarea name="message" rows="5" cols="30"
          placeholder="请输入您的留言"></textarea>

<!-- 提交按钮 -->
<button type="submit">发送留言</button>
```

**逐行解剖**

- `<textarea>`:多行文本块。`rows="5"` 显示 5 行高度,`cols="30"` 显示约 30 字宽度。
- `</textarea>`:textarea **不是**自闭合!必须有闭标签,标签之间的内容是默认值。
- `<button type="submit">`:提交按钮,点击后触发表单提交。type="submit" 是默认值,也可以省略。

**为什么:textarea 和 input 的区别** —— input 单行,textarea 多行。选错会导致用户没法换行(比如留言本用 input 会挤成一行)。

> **问自己:**
> 1. 想要一个"性别单选"用 input 还是 textarea?type 应该是什么?
> 2. button 里如果不写 type,默认是什么?
> 3. textarea 之间的文字会被提交吗?

---

#### label 与表单无障碍 —— 每个输入都配标题

**代码示例**

```html
<!-- 推荐:用 for/id 关联 label 和 input -->
<label for="name">姓名</label>
<input type="text" id="name" name="name" />

<!-- 也可以把 input 包在 label 里 -->
<label>
    邮箱
    <input type="email" name="email" />
</label>
```

**逐行解剖**

- `for="name"`:label 的 for 属性 = input 的 id,两者关联。点击"姓名"文本时,光标自动聚焦到输入框。
- `id="name"`:input 的 id(唯一标识),供 label 的 for 引用。
- 读屏软件会朗读 label 文本,让视障用户知道这个输入框要填什么。

**为什么:**label 不只是视觉标题——它是表单无障碍的核心。没有 label 的输入框 = 读屏软件只听到"编辑框",不知道要填什么。点击 label 聚焦输入框也是重要的桌面端体验。

> **问自己:**
> 1. label 的 for 必须和 input 的什么属性匹配?
> 2. 一个页面两个 input 能共用同一个 id 吗?
> 3. 没有 label 的表单能通过无障碍审查吗?

---

#### 完整联系表单 —— 姓名+邮箱+留言

**代码示例**

```html
<section id="contact">
    <h2>联系我</h2>
    <form action="#" method="post">
        <p>
            <label for="name">姓名</label>
            <input type="text" id="name" name="name"
                   placeholder="请输入姓名" required />
        </p>
        <p>
            <label for="email">邮箱</label>
            <input type="email" id="email" name="email"
                   placeholder="your@email.com" required />
        </p>
        <p>
            <label for="message">留言</label>
            <textarea id="message" name="message" rows="5"
                      cols="30" placeholder="请输入您的留言"
                      required></textarea>
        </p>
        <button type="submit">发送留言</button>
    </form>
</section>
```

> **ASCII 内存图**
> ```
> <section id="contact">
> ├── <h2>联系我</h2>
> └── <form action="#" method="post">
>      ├── <p>  ← 每组 label+input 包一个 p
>      │    ├── <label for="name">
>      │    └── <input id="name" name="name" type="text">
>      ├── <p>
>      │    ├── <label for="email">
>      │    └── <input id="email" name="email" type="email">
>      ├── <p>
>      │    ├── <label for="message">
>      │    └── <textarea id="message" name="message">
>      └── <button type="submit">
> ```

**逐行解剖**

- `required`:必填字段,空着时浏览器阻止提交并提示"请填写此字段"。
- 每个 label+input 用一个 `<p>` 分组,视觉上形成一行一个字段。
- form 整体放在 section 里,符合语义化结构。

**执行过程跟踪(关键)**

```html
<!-- --- 浏览器渲染联系表单的过程 --- -->

<!-- h2 "联系我":渲染大标题 -->

<!-- form:创建表单上下文 -->

<!-- 第一个 p: -->
<!--   ① label "姓名" for="name" → 关联到 id="name" 的 input -->
<!--   ② input type="text" → 渲染单行输入框,placeholder 显示"请输入姓名" -->
<!--   ③ required → 标记为必填 -->

<!-- 第二个 p: -->
<!--   ① label "邮箱" for="email" -->
<!--   ② input type="email" → 邮箱输入,浏览器会校验 @ -->

<!-- 第三个 p: -->
<!--   ① label "message" for="message" -->
<!--   ② textarea rows=5 → 五行高的多行输入框 -->

<!-- button type="submit":提交按钮 -->

<!-- 最终:用户看到一个三行表单(姓名/邮箱/留言 + 发送按钮) -->
<!-- 点击"发送" → form 尝试提交到 action="#" (当前页) -->
```

---

#### 站点整合 —— 多页面文件组织

**代码示例**

一个完整的小型官网应该有如下文件结构:

```
my-portfolio/
├── index.html          ← 首页(导航 + Hero + 关于 + 联系)
├── projects.html       ← 项目展示页(卡片列表)
├── contact.html        ← 联系表单页
└── images/             ← 所有图片放在一个文件夹
    ├── avatar.jpg
    ├── project1.jpg
    └── project2.jpg
```

**逐行解剖**

- 三个页面共享同一套 `<header>`(品牌名 + 导航)和 `<footer>`(版权)。
- 导航链接跳转:首页 → 作品集 → 联系页,构成闭环。
- 图片统一放 images 文件夹,src 写 `images/avatar.jpg`。

**为什么:**文件分离让每页职责清晰——改首页不影响项目页。这也是真实项目的标准做法。

> **问自己:**
> 1. 为什么三个页面要共享同一个 header?改一处和改三处哪个更好?
> 2. 图片文件夹的好处是什么?
> 3. 如果新增一个"博客"页面,需要改哪些文件?

---

#### 部署上线 —— GitHub Pages 静态托管

**逐行解剖**

GitHub Pages 把静态 HTML 文件免费托管到公网,步骤:

```
1. 在 GitHub 创建一个新仓库(仓库名 = 你的用户名.github.io)
2. 把本地的 index.html、projects.html、contact.html push 到仓库
3. 进入仓库 Settings → Pages → Source 选 main 分支 → Save
4. 等 1-2 分钟,访问 https://用户名.github.io
   即能看到你的站点正式上线!
```

**为什么:**GitHub Pages 完全免费,支持自定义域名,是静态站点的最佳入门托管方案。你的 HTML 课程项目上线后,把链接发给朋友就能访问,是作品集的第一块基石。

**常见错误**

> 1. **错误现象**:访问 404
>    **原因**:仓库首页文件名必须是 index.html,不能叫 homepage.html
> 2. **错误现象**:页面能打开,但图片全部裂开
>    **原因**:图片路径用了绝对路径(C:/Users/...),应改用相对路径(images/...)
> 3. **错误现象**:CSS/JS 加载失败
>    **原因**:路径区分大小写,images/A.jpg 和 images/a.jpg 是不同的文件

> **问自己:**
> 1. 为什么 index.html 是默认首页?能改成其他名字吗?
> 2. 相对路径和绝对路径在部署时有什么差异?
> 3. GitHub Pages 能托管带后端的网站吗?

---

#### 学员代码区

打开编辑器,新建 `contact.html`,补全下面的联系表单:

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <title>联系我 - 小红 Design</title>
</head>
<body>
    <!-- 共享 header(...参考 Day_08) -->

    <main>
        <section id="contact">
            <h2>联系我</h2>
            <form action="#" method="post">
                <!-- TODO: 姓名 label + input(text) -->

                <!-- TODO: 邮箱 label + input(email) -->

                <!-- TODO: 留言 label + textarea -->

                <!-- TODO: 发送按钮 -->
            </form>
        </section>
    </main>

    <!-- 共享 footer -->
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
    <title>联系我 - 小红 Design</title>
</head>
<body>
    <header>
        <h1>小红 Design</h1>
        <nav>
            <a href="index.html">首页</a>
            <a href="projects.html">作品集</a>
            <a href="contact.html">联系我</a>
        </nav>
    </header>

    <main>
        <section id="contact">
            <h2>联系我</h2>
            <form action="#" method="post">
                <p>
                    <label for="name">姓名</label>
                    <input type="text" id="name" name="name"
                           placeholder="请输入您的姓名" required />
                </p>
                <p>
                    <label for="email">邮箱</label>
                    <input type="email" id="email" name="email"
                           placeholder="your@email.com" required />
                </p>
                <p>
                    <label for="message">留言</label>
                    <textarea id="message" name="message"
                              rows="5" cols="30"
                              placeholder="请输入您的留言"
                              required></textarea>
                </p>
                <button type="submit">发送留言</button>
            </form>
        </section>
    </main>

    <footer>
        <p><small>© 2026 小红 Design. 保留所有权利。</small></p>
    </footer>
</body>
</html>
```

保存后用浏览器打开,你应该看到:
- 顶部与首页一致的导航
- 三行表单:姓名(单行输入) + 邮箱(带校验) + 留言(多行文本) + 发送按钮
- 空字段点提交时浏览器弹出"请填写此字段"
- 与首页、作品集页导航互通

**恭喜!你已经完成了整个官网的三页站点,并能部署上线。** 🎉

把三个文件 push 到 GitHub Pages,把链接写进简历 ——
你的第一个作品集网站就正式诞生了!
