### Day 02 · 三种声明方式的作用域

> **痛点**:昨天你会用 let/const/var 声明变量了,但写 if 块里的变量时,行为会让你困惑 —— 为什么 if 里声明的 var 在外面也能访问?为什么 let 就不会?今天揭开作用域的面纱。
> **类比**:作用域就像不同级别的容器。`var` 是"函数级盒子" —— 整个函数共享一个大盒子,if 块里声明的变量会"漏"到函数级。`let`/`const` 是"块级盒子" —— 每个 `{}` 是一个独立盒子,里面的变量出不来。
> **解释**:**作用域 = 变量可被访问的范围**。JS 有三种作用域规则,对应三种声明关键字。

---

#### var 的函数作用域与 hoisting

> **痛点**:你在 if 块里声明 var,以为它只在 if 里有效,结果在 if 外面也能访问。更奇怪的是,在声明之前访问它不会报错,只是返回 undefined。
> **类比**:var 就像"提前把盒子标签贴好,但内容后面才放"。无论你在函数哪里声明 var,JS 都会把"标签"提升到函数顶部(hoisting),但赋值留在原地。
> **解释**:`var` 声明的变量作用域是整个函数(函数级),不是块级。且会被"提升"(hoisting)到函数顶部。

```javascript
function example() {
    console.log(name);  // undefined(不是报错!)
    var name = "Alice";
    console.log(name);  // "Alice"

    if (true) {
        var age = 25;    // var 在 if 块里声明
    }
    console.log(age);   // 25 —— if 外面也能访问!
}
example();
```

**逐行解剖**

- `console.log(name)` = 在 var 声明前访问 → undefined(hoisting 把声明提升,但赋值没提升)
- `var name = "Alice"` = 实际赋值位置
- `var age = 25` = 在 if 块里声明,但 var 是函数级 → if 外面也能访问

> **ASCII 内存图**
> ```
> 函数作用域(example)
> ┌──────────────────────────────┐
> │  var name  ← hoisting 提升   │ ← 函数级
> │  var age   ← if 里声明但也漏  │ ← 函数级
> └──────────────────────────────┘
> 块级作用域(if)不存在!
> ```

**常见错误**

> 1. **错误现象**:在 for 循环里用 var 声明循环变量,循环结束后变量还在
>    **原因**:var 是函数级,for 块困不住它
> 2. **错误现象**:在 if 块里声明 var,以为它是"局部变量"
>    **原因**:var 没有块级概念,只有函数级

**NCDL Break It 演示(var hoisting 反模式)**

```javascript
// ============ BREAK IT 演示 ============
function brokenVar() {
    // 你以为这里会报错?不会!
    console.log("Before declaration:", greeting);  // undefined

    if (true) {
        var greeting = "Hello";
    }

    // 你以为 greeting 只在 if 里?不对!
    console.log("Outside if:", greeting);  // "Hello" —— 漏出来了

    // 你以为重复声明会报错?不会!
    var greeting = "World";  // var 允许重复声明
    console.log("Redeclared:", greeting);  // "World"
}
brokenVar();

// 正确做法:用 let 替代 let
function fixedLet() {
    // console.log(greeting);  // ❌ ReferenceError(TDZ)
    let greeting = "Hello";
    if (true) {
        let greeting = "World";  // 块级,不影响外部
        console.log("Inside if:", greeting);  // "World"
    }
    console.log("Outside if:", greeting);  // "Hello"
}
fixedLet();
// ============ END BREAK IT ============
```

> **问自己:**
> 1. `var x = 1; var x = 2;` 会报错吗?为什么?
> 2. 在函数顶部 `console.log(y)` 然后 `var y = 5`,输出是什么?
> 3. 为什么现代 JS 推荐用 let 而不是 var?

---

#### let 的块级作用域

> **痛点**:var 的"漏出"行为导致 bug 难追踪。你需要一种"声明在块里,就只在块里有效"的变量。
> **类比**:let 就像真正的"块级盒子" —— 你在 if 块里声明一个 let,它就被锁在这个盒子里,外面完全看不到。
> **解释**:`let` 声明的变量作用域是最近的 `{}`(块级),且不会被提升(访问会报错,进入 TDZ)。

```javascript
function letExample() {
    if (true) {
        let blockVar = "inside";
        console.log(blockVar);   // "inside"
    }
    // console.log(blockVar);    // ❌ ReferenceError: blockVar is not defined

    let count = 0;
    for (let i = 0; i < 3; i++) {
        console.log(i);          // 0, 1, 2
    }
    // console.log(i);           // ❌ ReferenceError: i is not defined
}
letExample();
```

**逐行解剖**

- `let blockVar = "inside"` = 块级变量,只在 if 块里有效
- `for (let i = 0; ...)` = 每次循环 i 都是新的块级变量(与 var 不同)

> **ASCII 内存图**
> ```
> 函数作用域(letExample)
> ┌──────────────────────────────┐
> │  let count = 0               │
> │  ┌─ if 块 ─────────────────┐ │
> │  │ let blockVar = "inside"  │ │ ← 块级,出不去
> │  └──────────────────────────┘ │
> │  ┌─ for 块 ────────────────┐ │
> │  │ let i = 0, 1, 2         │ │ ← 每次循环新 i
> │  └──────────────────────────┘ │
> └──────────────────────────────┘
> ```

**常见错误**

> 1. **错误现象**:在块外访问 let 变量,报 ReferenceError
>    **原因**:let 是块级,块外不可见
> 2. **错误现象**:在 let 声明前访问,报 ReferenceError(不是 undefined)
>    **原因**:let 不会被提升,进入 TDZ(Temporal Dead Zone)

**NCDL Break It 演示(let TDZ 反模式)**

```javascript
// ============ BREAK IT 演示 ============
function tdzTrap() {
    // 你以为这里输出 undefined(像 var)?报错!
    // console.log(myLet);  // ❌ ReferenceError: Cannot access 'myLet' before initialization

    let myLet = "Hello";    // TDZ 到这里结束
    console.log(myLet);     // "Hello" —— 声明后才能访问

    // 你以为在 for 循环外能访问 i?报错!
    for (let i = 0; i < 3; i++) {
        console.log(i);
    }
    // console.log(i);  // ❌ ReferenceError: i is not defined
}
tdzTrap();

// 对比 var 的"诡异"行为
function varTrap() {
    console.log(myVar);  // undefined(不报错,但也不对)
    var myVar = "Hello";
}
varTrap();
// ============ END BREAK IT ============
```

> **问自己:**
> 1. `let x = 1; let x = 2;` 会报错吗?(对比 var)
> 2. 在 let 声明前访问会报什么错?
> 3. 为什么 for 循环推荐用 let 而不是 var?

---

#### const 的不可重新赋值(≠ 不可变)

> **痛点**:你以为 `const` 是"完全冻结",结果发现 `const arr = []` 后面还能 `arr.push(1)`。const 到底限制什么?
> **类比**:const 就像"密封盒上的锁" —— 你不能换盒子里的东西(重新赋值),但如果里面是个袋子(对象/数组),你可以往袋子里加东西。
> **解释**:`const` = 声明时必须初始化 + 不能重新赋值(绑定不可变)。但对象/数组的内容可以修改(值不可变 ≠ 内容不可变)。

```javascript
const PI = 3.14;
// PI = 3.15;            // ❌ TypeError: Assignment to constant variable

const colors = ["red", "green"];
colors.push("blue");      // ✅ 可以修改内容
// colors = ["yellow"];   // ❌ TypeError: 不能重新赋值
console.log(colors);      // ["red", "green", "blue"]

const person = { name: "Alice" };
person.name = "Bob";      // ✅ 可以修改属性
// person = {};           // ❌ TypeError: 不能重新赋值
```

**逐行解剖**

- `const PI = 3.14` = 声明时必须初始化,之后不能改
- `colors.push("blue")` = 修改数组内容(不是重新赋值) → 允许
- `colors = ["yellow"]` = 重新赋值(指向新数组) → 报错

**常见错误**

> 1. **错误现象**:`const x;` 声明时不赋值,报 SyntaxError
>    **原因**:const 声明时必须初始化
> 2. **错误现象**:以为 const 对象完全不能改
>    **原因**:const 只阻止重新赋值,不阻止修改属性

**NCDL Break It 演示(const 反模式)**

```javascript
// ============ BREAK IT 演示 ============
function constTrap() {
    // 你以为 const 声明可以不初始化?报错!
    // const UNINITIALIZED;  // ❌ SyntaxError: Missing initializer

    // 你以为 const 对象完全冻结?不是!
    const config = { theme: "dark" };
    config.theme = "light";    // ✅ 可以改属性
    console.log(config.theme); // "light"

    // 你以为重新赋值会成功?报错!
    // config = { theme: "blue" };  // ❌ TypeError

    // 你以为 const 数组不能 push?可以!
    const items = [];
    items.push("first");       // ✅ 可以修改内容
    console.log(items);        // ["first"]
}
constTrap();

// 如果你需要真正冻结,用 Object.freeze()
const frozen = Object.freeze({ name: "Alice" });
// frozen.name = "Bob";  // 静默失败(严格模式报错)
// ============ END BREAK IT ============
```

> **问自己:**
> 1. `const arr = []; arr = [1, 2]` 会报错吗?`arr.push(1)` 呢?
> 2. const 和 Object.freeze() 有什么区别?
> 3. 什么时候用 const,什么时候用 let?

---

#### 执行过程跟踪

```javascript
// --- 执行过程 ---
// 第 1 行 function example():
//   ① 创建函数作用域
//
// 第 2 行 console.log(name):
//   ① var name 被 hoisting 到函数顶部
//   ② 此时 name = undefined(赋值还没执行)
//   ③ 输出 undefined
//
// 第 3 行 var name = "Alice":
//   ① 实际赋值位置
//   ② name = "Alice"
//
// 第 6-8 行 if 块:
//   ① var age = 25 在 if 块里声明
//   ② 但 var 是函数级,age 泄漏到函数作用域
//
// 第 9 行 console.log(age):
//   ① if 外面访问 age → 25(因为 var 泄漏)
```

---

#### 常见错误

> 1. **错误现象**:在 for 循环外用 var 声明的循环变量
>    **原因**:var 是函数级,循环结束后变量还在
> 2. **错误现象**:以为 const 声明的对象完全不能改
>  **原因**:const 只阻止重新赋值,不阻止修改属性/内容
> 3. **错误现象**:在 let 声明前访问,以为会像 var 一样返回 undefined
>    **原因**:let 不会被提升,进入 TDZ(访问报错)

---

#### 学员代码区

打开浏览器控制台或 Node.js,补全下面的代码:

```javascript
// TODO: 用 var 声明一个变量 testVar,在 if 块里赋值,在 if 外打印
// TODO: 用 let 声明一个变量 testLet,在 for 循环里用,在循环外尝试打印(观察报错)
// TODO: 用 const 声明一个数组,尝试 push 一个新元素,然后尝试重新赋值(观察哪个成功)
```

---

#### 参考答案

```javascript
// var 泄漏
function testVar() {
    if (true) {
        var testVar = "leaked";
    }
    console.log(testVar);  // "leaked" —— 泄漏到函数级
}
testVar();

// let 块级
function testLet() {
    for (let i = 0; i < 3; i++) {
        console.log(i);    // 0, 1, 2
    }
    // console.log(i);     // ❌ ReferenceError
}
testLet();

// const 内容可变
const arr = [];
arr.push("item");         // ✅ 内容可变
// arr = ["new"];          // ❌ 重新赋值报错
```

---

## 明日衔接

- 明天 Day 03 学什么:**三种声明方式的对比与场景选择**(给定场景,选 let/var/const 之一)
- 今天遗留的概念:今天学了作用域差异,但还没学"给定场景如何选"
- 消费者门控预告(已标 teaching_method=consumer_gate):
  - Day 3 会用消费者函数(≤4 行)约束你必须多态思考
  - 题目形式:"给定一个支付处理函数,要求新增支付方式时不用 if-elif"
