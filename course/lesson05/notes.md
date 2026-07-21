### Day 05 · 表单基础:让页面"接收"用户输入

> **痛点**:你写过文章、放图片、做表格,但页面永远是"死"的 —— 用户只能看,不能输入。今天你将学会让页面"开口问问题"。
> **类比**:表单就像纸质表格的电子版。纸质表格有标题(name)、填写区(输入框)、选择区(打勾)、提交方式(投递到哪个邮箱)。HTML 表单的 form/action/method 一一对应。
> **解释**:HTML 用 `<form>` 定义一个输入区域,`action` 告诉浏览器"提交到哪里",`method` 告诉浏览器"用什么方式提交"。里面放各种输入控件供用户填写。

---

#### 表单容器 form —— 表单的"信封"

> **痛点**:你在页面上放了一堆输入框,但点击"提交"后什么也没发生。
> **类比**:`<form>` 就像信封,输入控件就像信纸。信纸装进信封,写上地址(action),选择平信还是快递(method),才能寄出去。
> **解释**:`<form>` 是一个容器标签,所有要提交的输入控件必须放在里面。`action` 指定数据提交的目标地址(URL),`method` 指定提交方式(GET 或 POST)。

```html
<form action="/login" method="POST">
    <!-- 输入控件放在这里 -->
    <input type="text" name="username" />
    <input type="password" name="password" />
    <button type="submit">登录</button>
</form>
```

**逐行解剖**

- `<form>` = 表单容器,所有要提交的数据必须放在里面
- `action="/login"` = 提交的目标地址,类似信封上的收件地址
- `method="POST"` = 提交方式。POST = 把数据"藏"在请求体里发送(适合密码等敏感信息)
- `method="GET"` = 另一种提交方式,数据拼接在URL后面(适合搜索等公开信息)
- `name="username"` = 输入控件的"名字",提交时服务器靠它识别数据

> **ASCII 内存图**
> ```
> <form action="/login" method="POST">   ← 信封(容器)
>  ├── <input name="username" />         ← 信纸 1(用户名)
>  ├── <input name="password" />         ← 信纸 2(密码)
>  └── <button type="submit">            ← 封蜡(提交按钮)
> ```

**常见错误**

> 1. **错误现象**:输入控件放在 `<form>` 外面
>    **原因:**只有 form 里面的控件数据才会被提交,外面的控件会被忽略
> 2. **错误现象**:`<form action="/login">`(没有 method)
>    **原因:**不写 method 默认是 GET,如果提交密码会暴露在 URL 里,不安全
> 3. **错误现象**:`<form action="login.html">`
>    **原因:**action 应该是一个能处理数据的服务器地址,不是随便一个 HTML 文件

> **问自己:**
> 1. `<form>` 的作用是什么?为什么输入控件要放在里面?
> 2. GET 和 POST 的区别是什么?什么时候用哪个?
> 3. 如果 form 里没有 submit 按钮,表单能提交吗?

**学员代码区**

```html
<!-- 下面这个表单有 2 处错误,修正它 -->
<form action="/register">
    <input type="text" name="email" />
    <input type="password" name="pwd" />
    <button type="submit">注册</button>
</form>

<!-- TODO: 写出正确版本 -->
```

**参考答案**

```html
<!-- 错误 1:提交密码应该用 method="POST",默认 GET 不安全 -->
<!-- 错误 2:action 应该指向能处理注册数据的地址 -->
<form action="/register" method="POST">
    <input type="text" name="email" />
    <input type="password" name="pwd" />
    <button type="submit">注册</button>
</form>
```

---

#### input 控件 —— 表单的"输入框"

> **痛点**:你需要用户输入文字、密码、邮箱、选择性别、勾选爱好,但不知道一个标签怎么实现这么多种输入。
> **类比**:`<input>` 就像变形金刚,`type` 属性决定它变成什么形态 —— type="text" 是文本框,type="password" 是密码框,type="radio" 是单选按钮。
> **解释**:`<input>` 是自闭合标签,通过 `type` 属性切换不同的输入类型,`name` 属性标识提交时的字段名。

```html
<!-- 文本框 -->
<input type="text" name="username" placeholder="请输入用户名" />

<!-- 密码框(输入内容显示为圆点) -->
<input type="password" name="password" />

<!-- 邮箱框(浏览器会验证格式) -->
<input type="email" name="email" />

<!-- 数字框 -->
<input type="number" name="age" min="0" max="150" />

<!-- 单选按钮(多选一,name 相同才能互斥) -->
<input type="radio" name="gender" value="male" /> 男
<input type="radio" name="gender" value="female" /> 女

<!-- 复选框(多选多) -->
<input type="checkbox" name="hobby" value="reading" /> 阅读
<input type="checkbox" name="hobby" value="coding" /> 编程
```

**逐行解剖**

- `type="text"` = 普通文本框,输入内容明文显示
- `type="password"` = 密码框,输入内容显示为圆点(保护隐私)
- `type="email"` = 邮箱框,浏览器会自动验证格式(是否包含 @)
- `type="number"` = 数字框,`min`/`max` 限制范围
- `type="radio"` = 单选按钮,同一组 radio 的 `name` 必须相同才能互斥
- `type="checkbox"` = 复选框,可以同时勾选多个
- `placeholder="..."` = 输入框内的灰色提示文字,用户开始输入后消失

> **ASCII 内存图**
> ```
> <form>
>  ├── <input type="text" name="username">       ← 文本框
>  ├── <input type="password" name="password">   ← 密码框
>  ├── <input type="radio" name="gender" value="male">    ← 单选(男)
>  ├── <input type="radio" name="gender" value="female">  ← 单选(女)
>  └── <input type="checkbox" name="hobby" value="reading"> ← 复选
> ```

**常见错误**

> 1. **错误现象**:单选按钮不能互斥(可以同时选多个)
>    **原因:**同一组 radio 的 `name` 必须相同,name 不同就无法互斥
> 2. **错误现象**:`<input type="text">`(没有 name)
>    **原因:**没有 name 属性,提交时服务器无法识别这个字段
> 3. **错误现象**:`<input type="text"></input>`
>    **原因:**input 是自闭合标签,不能写闭标签

> **问自己:**
> 1. `type="text"` 和 `type="password"` 的区别是什么?
> 2. 为什么同一组 radio 的 name 必须相同?
> 3. radio 和 checkbox 的区别是什么?什么时候用哪个?

**学员代码区**

```html
<!-- 下面有 2 处错误,修正它 -->
<input type="text" placeholder="用户名" />
<input type="radio" name="sex" value="male" /> 男
<input type="radio" name="gender" value="female" /> 女

<!-- TODO: 写出正确版本 -->
```

**参考答案**

```html
<!-- 错误 1:input 没有 name,提交时无法识别 -->
<!-- 错误 2:两个 radio 的 name 不同,无法互斥 -->
<input type="text" name="username" placeholder="用户名" />
<input type="radio" name="gender" value="male" /> 男
<input type="radio" name="gender" value="female" /> 女
```

---

#### select 下拉框 —— 表单的"选择题"

> **痛点**:你想让用户从 10 个城市中选择一个,放 10 个 radio 太占地方。
> **类比**:`<select>` 就像考试的选择题 —— 题目是"选择你的城市",选项是 A/B/C/D,点击展开下拉列表。
> **解释**:`<select>` 是下拉框容器,里面用 `<option>` 定义每个选项,用户点击展开后选择一个。

```html
<select name="city">
    <option value="">--请选择城市--</option>
    <option value="beijing">北京</option>
    <option value="shanghai">上海</option>
    <option value="guangzhou">广州</option>
    <option value="shenzhen">深圳</option>
</select>
```

**逐行解剖**

- `<select name="city">` = 下拉框容器,name 标识提交时的字段名
- `<option value="beijing">北京</option>` = 一个选项,value 是提交给服务器的值,标签内容是用户看到的文字
- `value=""` 的第一个选项通常是"请选择"提示,值为空表示未选择
- 用户看到的是"北京",提交的是 value 的值"beijing"

> **ASCII 内存图**
> ```
> <select name="city">                    ← 下拉框容器
>  ├── <option value="">--请选择城市--</option>  ← 默认提示
>  ├── <option value="beijing">北京</option>    ← 选项 1
>  ├── <option value="shanghai">上海</option>   ← 选项 2
>  ├── <option value="guangzhou">广州</option>  ← 选项 3
>  └── <option value="shenzhen">深圳</option>   ← 选项 4
> ```

**常见错误**

> 1. **错误现象**:`<option>北京</option>`(没有 value)
>    **原因:**没有 value 时,提交的是标签内容(北京),但规范要求写 value
> 2. **错误现象**:`<select>` 里直接放文字而不是 `<option>`
>    **原因:**select 的直接子元素必须是 option,其他内容无效
> 3. **错误现象**:多个 option 同时设置 `selected`
>    **原因:**单选下拉框只能有一个默认选中项,多选时才允许多个

> **问自己:**
> 1. `<select>` 和 `<option>` 的关系是什么?
> 2. option 的 value 和标签内容有什么区别?
> 3. 如何设置默认选中某个选项?

**学员代码区**

```html
<!-- 下面这个下拉框有 2 处错误,修正它 -->
<select name="fruit">
    请选择水果
    <option>苹果</option>
    <option>香蕉</option>
</select>

<!-- TODO: 写出正确版本 -->
```

**参考答案**

```html
<!-- 错误 1:文字不能直接放在 select 里,要用 option -->
<!-- 错误 2:option 没有 value -->
<select name="fruit">
    <option value="">请选择水果</option>
    <option value="apple">苹果</option>
    <option value="banana">香蕉</option>
</select>
```

---

#### textarea 多行文本 —— 表单的"作文题"

> **痛点**:用户要写一段自我介绍,一行文本框装不下。
> **类比**:`<input type="text">` 是"填空题"(一行),`<textarea>` 是"作文题"(多行)。
> **解释**:`<textarea>` 是多行文本输入框,适合输入大段文字,通过 `rows` 和 `cols` 控制大小。

```html
<textarea name="intro" rows="5" cols="40"
    placeholder="请介绍一下你自己..."></textarea>
```

**逐行解剖**

- `<textarea>` = 多行文本输入框,不是自闭合标签,必须写闭标签
- `name="intro"` = 字段名,提交时服务器靠它识别
- `rows="5"` = 显示 5 行(高度)
- `cols="40"` = 显示 40 个字符宽度
- `placeholder="..."` = 灰色提示文字
- 用户输入的内容放在开标签和闭标签之间(不像 input 用 value)

> **ASCII 内存图**
> ```
> <textarea name="intro" rows="5" cols="40">   ← 多行文本框
>  └── (用户输入的内容放在这里)                 ← 内容区
> </textarea>
> ```

**常见错误**

> 1. **错误现象**:`<textarea />`(自闭合写法)
>    **原因:**textarea 不是自闭合标签,必须写成 `<textarea></textarea>`
> 2. **错误现象**:`<textarea value="默认文字"></textarea>`
>    **原因:**textarea 没有 value 属性,默认文字要写在标签之间
> 3. **错误现象**:`<textarea>` 和 `<input type="text">` 混用
>    **原因:**单行用 input,多行用 textarea,不要搞混

> **问自己:**
> 1. `<textarea>` 和 `<input type="text">` 的区别是什么?
> 2. textarea 的默认文字应该写在哪里?
> 3. rows 和 cols 控制的是什么?

**学员代码区**

```html
<!-- 下面这个 textarea 有 2 处错误,修正它 -->
<textarea name="comment" value="请输入评论..." />

<!-- TODO: 写出正确版本 -->
```

**参考答案**

```html
<!-- 错误 1:textarea 不是自闭合标签 -->
<!-- 错误 2:textarea 没有 value 属性,默认文字写在标签之间 -->
<textarea name="comment" rows="4" cols="30">请输入评论...</textarea>
```

---

#### 综合示例 —— 一个完整的注册表单

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
        <p>
            用户名:<input type="text" name="username"
                placeholder="请输入用户名" />
        </p>
        <p>
            密码:<input type="password" name="password"
                placeholder="请输入密码" />
        </p>
        <p>
            邮箱:<input type="email" name="email"
                placeholder="请输入邮箱" />
        </p>
        <p>
            年龄:<input type="number" name="age"
                min="0" max="150" />
        </p>
        <p>
            性别:
            <input type="radio" name="gender" value="male" /> 男
            <input type="radio" name="gender" value="female" /> 女
        </p>
        <p>
            爱好:
            <input type="checkbox" name="hobby" value="reading" /> 阅读
            <input type="checkbox" name="hobby" value="coding" /> 编程
            <input type="checkbox" name="hobby" value="music" /> 音乐
        </p>
        <p>
            城市:
            <select name="city">
                <option value="">--请选择--</option>
                <option value="beijing">北京</option>
                <option value="shanghai">上海</option>
            </select>
        </p>
        <p>
            自我介绍:
            <textarea name="intro" rows="4" cols="30"
                placeholder="介绍一下你自己..."></textarea>
        </p>
        <p>
            <button type="submit">注册</button>
        </p>
    </form>
</body>
</html>
```

**逐行解剖**

- `<form action="/register" method="POST">` = 表单容器,提交到 /register,用 POST 方式
- 每个输入控件都有 `name` 属性,这是提交时服务器识别字段的关键
- `type="radio"` 的 gender 字段 name 相同,保证互斥
- `type="checkbox"` 的 hobby 字段 name 相同,提交时是一个数组
- `<button type="submit">` = 提交按钮,点击后触发表单提交

**为什么:**这个表单就像纸质注册表的电子版 —— 有填空题(input)、单选题(radio)、多选题(checkbox)、下拉选择题(select)、作文题(textarea),最后点提交。

> **问自己:**
> 1. 为什么每个输入控件都要有 name 属性?
> 2. 如果两个 radio 的 name 不同,会发生什么?
> 3. 表单里的数据提交到了哪里?

---

#### 常见错误汇总

> 1. **错误现象**:输入控件放在 `<form>` 外面
>    **原因:**只有 form 里面的控件数据才会被提交
> 2. **错误现象**:`<input>` 没有 name 属性
>    **原因:**没有 name 服务器无法识别提交的数据
> 3. **错误现象**:`<textarea />`(自闭合写法)
>    **原因:**textarea 不是自闭合标签,必须写闭标签
> 4. **错误现象**:同一组 radio 的 name 不同
>    **原因:**name 不同就无法互斥,变成可以多选
> 5. **错误现象**:`<option>` 没有 value
>    **原因:**没有 value 时提交的是标签内容,但规范要求写 value
> 6. **错误现象**:提交密码用 method="GET"
>    **原因:**GET 会把数据暴露在 URL 里,密码应该用 POST

---

#### 学员代码区

新建文件 `signup.html`,编写一个"用户注册"表单,要求:

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <title>用户注册</title>
</head>
<body>
    <h1>用户注册</h1>

    <form action="/signup" method="POST">
        <!-- TODO: 用户名 input type="text" name="username" -->

        <!-- TODO: 密码 input type="password" name="password" -->

        <!-- TODO: 性别 radio 单选(男/女),name="gender" -->

        <!-- TODO: 城市 select + option(北京/上海/广州) -->

        <!-- TODO: 自我介绍 textarea name="intro" -->

        <!-- TODO: 提交按钮 button type="submit" -->

    </form>
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
    <title>用户注册</title>
</head>
<body>
    <h1>用户注册</h1>

    <form action="/signup" method="POST">
        <p>
            用户名:
            <input type="text" name="username" />
        </p>
        <p>
            密码:
            <input type="password" name="password" />
        </p>
        <p>
            性别:
            <input type="radio" name="gender" value="male" /> 男
            <input type="radio" name="gender" value="female" /> 女
        </p>
        <p>
            城市:
            <select name="city">
                <option value="">--请选择--</option>
                <option value="beijing">北京</option>
                <option value="shanghai">上海</option>
                <option value="guangzhou">广州</option>
            </select>
        </p>
        <p>
            自我介绍:
            <textarea name="intro" rows="4" cols="30"></textarea>
        </p>
        <p>
            <button type="submit">注册</button>
        </p>
    </form>
</body>
</html>
```

保存后用浏览器打开,你应该看到:
- 用户名、密码输入框
- 性别单选按钮(只能选一个)
- 城市下拉框(点击展开选项)
- 自我介绍多行文本框
- 注册按钮

**恭喜!你学会了用 HTML 制作用户输入界面。** 🎉
