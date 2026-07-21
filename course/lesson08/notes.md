### Day 08 · 综合项目 —— 首页结构与 Hero 区

> **痛点**:你已经学了 7 天 HTML 标签,能写单个段落、列表、图片,但面对一张真实网站的首页设计稿,不知道从哪里下手——标签砌成一"坨",结构混乱,看不懂也改不动。
> **类比**:写 HTML 就像建房子。之前你学会了烧砖(标签)、拧钢筋(属性),今天要真正建一栋有门有窗有房间的房子——每个房间有明确的用途,访客一进门就知道哪里是客厅、哪里是卧室。
> **解释**:**语义化标签**(Semantic HTML)是 HTML5 引入的一类标签,名字本身就说明了它的用途(header=头部、nav=导航、main=主体、footer=页脚),让代码"自解释",也让搜索引擎和读屏软件更好理解页面结构。

---

#### 语义化标签是什么 —— 给代码"贴名牌"

**逐行解剖**

HTML5 新增了一批语义标签,每个标签的名字 = 它的用途:

```html
<header>   ← 页面或区块的"头部"(放 logo、标题、导航)
<nav>      ← 导航链接的专区
<main>     ← 页面唯一的主体内容(每个页面只有一个)
<section>  ← 一个独立的"主题区块"
<article>  ← 一篇独立可分发的内容(文章、博客)
<aside>    ← 侧边栏、附加内容
<footer>   ← 页面或区块的"脚部"(放版权、联系方式)
```

**为什么:**以前开发者用 `<div class="header">` 代替 `<header>`,class 名字自己取的,浏览器不知道它是啥。语义标签直接告诉浏览器:"我就是头部!"——搜索引擎优先收录结构清晰的页面,读屏软件能直接跳到 `<main>` 阅读主体。

> **问自己:**
> 1. `<div class="header">` 和 `<header>` 在视觉上有区别吗?为什么还要用语义标签?
> 2. 一个页面可以有几个 `<main>`?
> 3. `<section>` 和 `<article>` 怎么选?有什么判断标准?

---

#### 语义标签 vs div —— 什么时候用哪个

**ASCII 内存图**

```
传统写法(全部用 div)           语义化写法
├── <div class="header">       ├── <header>
│    ├── <div class="logo">    │    ├── <h1>(logo)
│    └── <div class="nav">     │    └── <nav>
├── <div class="main">         ├── <main>
│    ├── <div class="hero">    │    ├── <section>(hero)
│    └── <div class="content"> │    └── <section>(内容)
└── <div class="footer">       └── <footer>
```

**逐行解剖**

- 左边:所有容器都是 `<div>`,靠 class 区分。浏览器、搜索引擎、读屏软件看不出结构。
- 右边:标签本身就是结构说明。打开代码,扫一眼就知道哪段是头部、哪里是主体。

**为什么:**语义化代码 = 给未来和自己写说明书。三个月后回头看,`<footer>` 一眼就认,`<div class="bottom-stuff-last">` 啥意思?

> **问自己:**
> 1. 如果整个页面全用 `<div>`,会导致什么问题?
> 2. `<div>` 是完全没用的标签吗?什么时候仍然需要用它?
> 3. 搜索引擎怎么利用语义标签做排名?

---

#### 首页的典型骨架 —— 上中下三段式

**代码示例**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <title>设计师小红的个人官网</title>
</head>
<body>
    <!-- ===== 顶部导航 ===== -->
    <header>
        <h1>小红 Design</h1>
        <nav>
            <a href="#home">首页</a>
            <a href="#projects">作品集</a>
            <a href="#contact">联系我</a>
        </nav>
    </header>

    <!-- ===== 主体内容 ===== -->
    <main>
        <section id="home">
            <h2>你好,我是小红</h2>
            <p>独立 UI 设计师,专注品牌视觉</p>
            <a href="#projects">查看我的作品 →</a>
        </section>

        <section id="projects">
            <h2>精选作品</h2>
            <!-- 项目卡片稍后填充 -->
        </section>
    </main>

    <!-- ===== 页脚 ===== -->
    <footer>
        <p><small>© 2026 小红 Design. 保留所有权利。</small></p>
    </footer>
</body>
</html>
```

> **ASCII 内存图**
> ```
> <body>
> ├── <header>              ← 顶部(logo + 导航)
> │    ├── <h1>             ← 品牌名/logo
> │    └── <nav>            ← 导航链接容器
> │         ├── <a>
> │         ├── <a>
> │         └── <a>
> ├── <main>                ← 主体(唯一)
> │    ├── <section id="home">    ← Hero 区
> │    │    ├── <h2>
> │    │    ├── <p>
> │    │    └── <a>(行动按钮)
> │    └── <section id="projects"> ← 作品区
> │         └── <h2>
> └── <footer>              ← 页脚(版权)
>      └── <p><small>
> ```

**逐行解剖**

- `<header>`:页面级头部,放 logo/品牌名 + 导航。每个页面一个(也可在 section 里用)。
- `<nav>`:专门包裹一组导航链接。告诉浏览器"这些是导航"。
- `<main>`:页面的核心内容,每个文档只能有一个,且不能嵌套在 header/nav/footer 里。
- `<section>`:一个有主题的内容块,通常带一个标题(h2-h6)。
- `<footer>`:页面尾部,放版权、联系方式、备案信息等。
- `<a href="#home">`:锚点链接,点击跳转到页面内 id="home" 的元素,页面内跳转不刷新。

> **注意:**`<header>` / `<footer>` 可以在一个页面中出现多次(比如每个 `<article>` 也有自己的 header/footer),但 `<main>` 只能出现**一次**。

---

#### Hero 区 —— 首页的"黄金广告位"

**逐行解剖**

Hero 区(Hero Section)是打开首页时最先看到的区域,通常包含三部分:

```html
<section id="hero">
    <!-- 主标题 -->
    <h2>让设计有温度</h2>

    <!-- 副标题/口号 -->
    <p>独立品牌设计师 · 服务过 50+ 品牌 · 5 年经验</p>

    <!-- 行动按钮(Call to Action) -->
    <a href="#contact">立即咨询</a>
</section>
```

- 主标题:一句话说清楚"我是谁、做什么",字号最大,视觉焦点。
- 副标题:补充细节,建立信任(经验/数据/差异化)。
- 行动按钮:告诉访客下一步做什么(联系/查看作品/下单)。

**为什么:**Hero 区决定访客 3 秒内去留。好 Hero = 清晰身份 + 明确价值 + 清晰行动。

> **问自己:**
> 1. 为什么 Hero 区通常放最大的标题?如果小小的会怎样?
> 2. 如果 Hero 区没有行动按钮,访客可能做什么?
> 3. Hero 区应该放在 `<main>` 里面还是外面?

---

#### 执行过程跟踪(关键)

```html
<!-- --- 浏览器解析首页骨架的过程 --- -->

<!-- 第 1 行 <!DOCTYPE html>: -->
<!--   ① 识别为 HTML5,按标准模式渲染 -->

<!-- 第 2 行 <html lang="zh-CN">: -->
<!--   ① 创建根元素,语言 = 中文 -->

<!-- 第 3-7 行 <head>: -->
<!--   ① meta charset:启用 UTF-8 中文支持 -->
<!--   ② title:标签页显示"设计师小红的个人官网" -->

<!-- 第 9-16 行 <header>: -->
<!--   ① 渲染品牌名"小红 Design" -->
<!--   ② 渲染三个导航链接(默认横排,未加 CSS 时是普通行内) -->

<!-- 第 19-28 行 <main>: -->
<!--   ① section#home:渲染 Hero 区(h2 + p + a) -->
<!--   ② section#projects:渲染作品区(只有 h2 标题占位) -->

<!-- 第 31-33 行 <footer>: -->
<!--   ① 渲染版权小字 -->

<!-- 最终:用户看到一个从上到下三段式的首页 -->
<!-- 顶部导航 → Hero 主视觉 → 作品区 → 版权页脚 -->
```

---

#### 常见错误

> 1. **错误现象**:`<main>` 里套了另一个 `<main>`
>    **原因:**`<main>` 在整份文档中只能出现一次,重复会违反规范
> 2. **错误现象**:`<nav>` 里没放链接,放了一段文字
>    **原因:**`<nav>` 专门用于包裹导航链接组,普通文字不应放在里面
> 3. **错误现象**:`<section>` 里没有任何标题,光秃秃几个 p
>    **原因:**每个 `<section>` 应该有自己的主题,至少有一个 h2-h6 标题说明它是什么
> 4. **错误现象**:整个页面全用 `<div>`,没有 header/nav/main/footer
>    **原因:**虽然浏览器能渲染,但结构不明,不利于 SEO 和可读性

---

#### 学员代码区

打开编辑器,新建 `index.html`,补全下面的首页骨架:

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <title>我的个人官网</title>
</head>
<body>
    <!-- TODO: 添加 header,里面包含 h1(你的名字/品牌) -->
    <!--     和 nav,nav 里放三个 a 链接 -->

    <!-- TODO: 添加 main,里面包含一个 section(id="home") -->
    <!--     作为 Hero 区: h2 主标题 + p 副标题 + a 行动按钮 -->

    <!-- TODO: 添加 footer,里面放版权小字 -->

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
    <title>王小明的个人官网</title>
</head>
<body>
    <header>
        <h1>王小明 Design</h1>
        <nav>
            <a href="#home">首页</a>
            <a href="#projects">作品集</a>
            <a href="#contact">联系我</a>
        </nav>
    </header>

    <main>
        <section id="home">
            <h2>用设计解决问题</h2>
            <p>专注品牌视觉与 UI 设计 · 6 年经验</p>
            <a href="#contact">一起聊聊 →</a>
        </section>

        <section id="projects">
            <h2>精选作品</h2>
        </section>
    </main>

    <footer>
        <p><small>© 2026 王小明 Design. 保留所有权利。</small></p>
    </footer>
</body>
</html>
```

保存后用浏览器打开,你应该看到:
- 顶部:品牌名 + 导航链接
- Hero 区:大标题 + 副标题 + 行动按钮
- 作品区:一个占位标题
- 底部:版权小字

**恭喜!你已经搭出了真实官网的首页骨架。** 🎉

如果没有 CSS,页面会比较"朴素",但结构已经完整。后续课程会给它加上样式,让它变美。
