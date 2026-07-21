### Day 01 · JavaScript 变量入门

> **痛点**:你刚学 HTML 能写静态网页,但网页还是死的 —— 它不会记住用户点击了什么、看不到你输入的名字。这一切需要 JavaScript,而 JavaScript 的第一步是**变量**。今天你将理解变量是什么,并能用三种关键字声明变量。
> **类比**:变量就像贴了标签的盒子。`name = "张三"` 就像一个标着 "name" 的盒子,里面装了"张三"。后面你随时可以读这个盒子(`console.log(name)`)或换内容(`name = "李四"`)。
> **解释**:JavaScript 中,**变量**是一个存储数据的命名容器,用 `let`、`const`、`var` 三个关键字之一声明。今天先学概念和基本声明。

---

#### 变量是什么 —— 数据的"贴标签盒子"

> **痛点**:你可能听过"变量",但说不出它和直接写值的区别。比如 `console.log(3.14)` 和 `let pi = 3.14; console.log(pi)` 都能打印 3.14,但只有后者把 3.14 "存起来"了。
> **类比**:一篇文章里直接出现的数字 vs. 文章引用了某个数据来源。`f = ma` 这个公式里的 f,不是直接写出来的值,而是"代表某个力的符号"。
> **解释**:**变量 = 名字 + 可变/不可变 + 存储的值**。三件事绑在一起就构成了变量。

```javascript
let age = 25;        // 声明一个名为 age 的变量,初值 25
console.log(age);    // 25 —— 读出变量里的值

age = 26;            // 修改变量的值(重新赋值)
console.log(age);    // 26
```

**逐行解剖**

- `let age = 25` = 创建变量:`let` 声明关键字,`age` 是变量名,`=` 是赋值,`25` 是初值
- `console.log(age)` = 读出变量:`console.log` 是个函数,传入变量名 `age`,打印它装的值
- `age = 26` = 重新赋值:直接写 `变量名 = 新值`,不加 `let`(加了就报错"重复声明")

> **ASCII 内存图**
> ```
> 变量表(内存)
> ┌──────────┬──────┐
> │  名字    │ 值   │
> ├──────────┼──────┤
> │  age     │  25  │ ← 初始状态
> └──────────┴──────┘
> 重新赋值后:
> ┌──────────┬──────┐
> │  age     │  26  │ ← age = 26 后
> └──────────┴──────┘
> ```

> **问自己:**
> 1. `let x = 5` 和 `let x = 10` —— 第二次声明会报错还是覆盖?
> 2. 变量名能以数字开头吗(比如 `let 2name`)?
> 3. 一个变量能装不同类型的值吗(先装数字再装字符串)?

---

#### 变量声明关键字:let / const / var 三种写法

> **痛点**:JavaScript 提供三种声明关键字,但网络上常有人说"别用 var",又有人说"实际项目主要是 const"。哪种该用?
> **类比**:三种关键字就像三种不同的"盒子设计":
> - `var` = 老式纸盒:松散,可以重写标签,作用域按函数划分
> - `let` = 现代塑料盒:严格按区块划分,可以重新赋值
> - `const` = 密封盒:按区块划分,装进去就不能换内容(重新赋值会报错)
> **解释**:三种声明**写法类似,但语义和作用域不同**。Day 2 详述作用域差异,今天先学"如何写"。

```javascript
// 三种声明的写法
let userName = "Alice";      // 1. let:可重新赋值
const PI = 3.14;            // 2. const:不可重新赋值
var legacy = "old way";     // 3. var:旧式声明(新代码少用)

// 重新赋值 let ✅
userName = "Bob";           // OK
console.log(userName);      // Bob

// 重新赋值 const ❌
// PI = 3.15;               // TypeError: Assignment to constant variable.
```

**逐行解剖**

- `let userName = "Alice"` = `let` 声明,初值 "Alice"。`userName` 是标识符(identifier),命名规范是首词小写后续词首字母大写(camelCase)
- `const PI = 3.14` = `const` 声明,初值 3.14。`PI` 用大写,因为它是"逻辑常量"(虽然 JS 的 const 不阻止对象内部修改)
- `var legacy = "old way"` = `var` 声明,用于兼容老代码。新项目优先用 `let` 或 `const`

> **问自己:**
> 1. `const x = 5; x = 10;` 会发生什么?
> 2. 同样是声明变量,`let`、`const`、`var` 在写法上有什么共同点?
> 3. 现代 JavaScript 推荐用哪一个?为什么?

---

#### 执行过程跟踪

```javascript
// --- 执行过程 ---
// 第 1 行 let userName = "Alice":
//   ① 创建变量 userName
//   ② 把 "Alice" 赋值给 userName
//   ③ 当前内存: {userName: "Alice"}
//
// 第 2 行 console.log(userName):
//   ① 调用 console.log 函数
//   ② 传入变量名 userName
//   ③ 读取 userName 的值 "Alice"
//   ④ 打印到控制台 → 显示 "Alice"
//
// 第 4 行 const PI = 3.14:
//   ① 创建常量 PI
//   ② 把 3.14 赋值给 PI
//   ③ 标记为常量(重新赋值会报错)
//
// 第 6 行 var legacy = "old way":
//   ① 创建变量 legacy
//   ② 把 "old way" 赋值
//   ③ 与 let 区别:作用域为函数级(明天详述)
//
// 第 9 行 userName = "Bob":
//   ① 不使用 let/const/var —— 直接赋值表示"修改现有变量"
//   ② 把 "Bob" 赋值给 userName
//   ③ 当前内存: {userName: "Bob", PI: 3.14, legacy: "old way"}
//
// 第 10 行 console.log(userName):
//   ① 读取并打印 → 显示 "Bob"
```

---

#### 常见错误

> 1. **错误现象**:`Uncaught SyntaxError: Identifier 'X' has already been declared`
>    **原因**:在同一个作用域里,用 `let`/`const`/`var` 重复声明同一个变量名。会报错。
> 2. **错误现象**:`Uncaught TypeError: Assignment to constant variable.`
>    **原因**:对 `const` 声明的常量重新赋值。常量一旦声明,内容不能再换(对象内部属性可改)。
> 3. **错误现象**:变量名写错大小写导致 `undefined`
>    **原因**:JavaScript 区分大小写。`userName` 和 `username` 是两个不同的变量。

---

#### 学员代码区

打开浏览器控制台(F12 → Console)或 Node.js,补全下面的代码:

```javascript
// TODO: 声明一个变量,名为 myName,初值是你的名字
// TODO: 声明一个常量,名为 BIRTH_YEAR,初值是 1990(用你的实际出生年)
// TODO: 修改 myName 为另一个名字(比如加上"同学")
// TODO: 用 console.log 输出两个变量的值
```

---

#### 参考答案

```javascript
let myName = "张三";
const BIRTH_YEAR = 1990;

myName = "张三同学";           // ✅ let 可以重新赋值
// BIRTH_YEAR = 2000;          // ❌ TypeError,const 不能

console.log(myName);           // "张三同学"
console.log(BIRTH_YEAR);       // 1990
```

**注意:** `const BIRTH_YEAR` 用大写+下划线命名是约定,表示"逻辑常量",但 JS 不会强制,只是惯例。

---

## 明日衔接

- 明天 Day 02 学什么:**三种声明方式的作用域差异**(`var` 函数级 / `let` 块级 / `const` 不可重新赋值)
- 今天遗留的概念:今天只学了"声明",还没学"作用域"和"hoisting"
- 可以预告的 NCDL 反模式(已标 teaching_method=ncdl):
  - `var` 在 `if` 块里声明会被"提升"(hoisting)到外面 —— 看着像块级,实际不是
  - `const` 对象声明后修改内部属性不算"重新赋值" —— 新手会误以为 `const` 完全冻结
