### Day 03 · 场景选择:给变量选对"盒子"

> **痛点**:昨天你理解了三种声明方式的作用域差异,但遇到实际场景时还是犹豫 —— "这个变量该用 let 还是 const?"今天给你一个决策框架,让你在任何场景下都能快速选对。
> **类比**:三种声明方式就像三种不同用途的容器 —— const 是"密封标签"(贴上去就不能换),let 是"可擦写标签"(可以改但不能漏出),var 是"共享标签"(整个函数共享,容易搞混)。选容器 = 选声明方式。
> **解释**:**场景选择 = 根据变量的"变"与"不变"和"作用域需求"选择声明方式**。

---

#### 决策框架:三问选声明

> **痛点**:记不住 let/const/var 的 10 条规则,每次都要想很久。
> **类比**:不需要记 10 条规则,只需要问自己 3 个问题。
> **解释**:三问决策框架 —— 回答 3 个问题就能确定声明方式。

```javascript
// 三问决策框架:
// Q1: 这个变量需要重新赋值吗?
//   → 不能:const
//   → 能: 进入 Q2
// Q2: 这个变量需要在块外访问吗?
//   → 不能:let(块级)
// → 能:let(函数级,但推荐)
// Q3: 这个变量是"逻辑常量"吗?(值不变但非技术常量)
//   → 是:const(命名用大写)
//   → 否:let
```

**逐行解剖**

- Q1 区分 const vs let/var:const 不能重新赋值,let/var 可以
- Q2 区分 let vs var:let 块级(不泄漏),var 函数级(泄漏)
- Q3 是风格约定:逻辑常量用 const + 大写命名

> **ASCII 决策图**
> ```
> 变量声明选择
> │
> ├─ 需要重新赋值?
> │   ├─ 否 → const ✅
> │   └─ 是 → 进入 Q2
> │
> ├─ 需要在块外访问?
> │   ├─ 否 → let ✅(块级)
> │   └─ 是 → let ✅(函数级,但推荐)
> │
> └─ 是逻辑常量?
>     ├─ 是 → const + 大写命名
>     └─ 否 → let
> ```

**常见错误**

> 1. **错误现象**:所有变量都用 let,因为"保险"
>    **原因**:失去了 const 的语义表达(告诉读者"这个值不变")
> 2. **错误现象**:以为 const 完全冻结,不敢用
>    **原因**:const 只阻止重新赋值,不阻止修改内容

---

#### 消费者函数即门控(Consumer-Function Gate)

> **痛点**:你背了三问框架,但遇到"消费者函数"场景时还是会犹豫 —— 函数要求你的变量必须是"可多态的"。
> **类比**:消费者函数就像"自动售货机" —— 你投入不同币种(变量),它都能处理。如果你的变量选错了声明方式,机器不认。
> **解释**:消费者函数 = 一个短函数(≤4 行),它要求你的变量必须满足某种约束。通过实现正确的声明方式,让消费者的调用成功。

```javascript
// === 消费者函数(教师提供,不可修改) ===
// 这个函数要求:payment 变量必须能被不同"支付方式"使用
// 且新增支付方式时,不能改这个函数
function checkout(cartTotal, payment) {
    // 约束:本函数体不超过 4 行
    // 约束:不能使用 if/elif/isinstance 判断类型
    return payment.execute(cartTotal);
}

// === 学员代码区 ===
// TODO: 用 const 声明 Alipay 支付方式(因为支付方式对象不变)
// TODO: 用 const 声明 WeChatPay 支付方式
// TODO: 调用 checkout(99.0, alipay) 和 checkout(99.0, wechatPay)
```

**逐行解剖**

- `checkout(cartTotal, payment)` = 消费者函数,≤4 行,不判断类型
- `payment.execute(cartTotal)` = 多态调用:payment 必须有 execute 方法
- 学员必须用 const 声明支付方式对象(因为对象本身不变,只是被传入)

**NCDL Break It 演示(消费者门控反模式)**

```javascript
// ============ BREAK IT 演示 ============
// 错误 1:用 let 声明支付方式(语义不对,支付方式对象不变)
let alipay = { execute: (amount) => console.log(`Alipay: ${amount}`) };

// 错误 2:支付方式没有 execute 方法
const wechatPay = { pay: (amount) => console.log(`WeChat: ${amount}`) };
// checkout(99.0, wechatPay);  // ❌ TypeError: wechatPay.execute is not a function

// 错误 3:试图在 checkout 里用 if 判断类型
function brokenCheckout(cartTotal, payment) {
    if (payment.type === "alipay") {  // ❌ 违反消费者门控约束
        // ...
    }
}

// 正确做法:
const alipayFixed = { execute: (amount) => console.log(`Alipay: ${amount}`) };
const wechatPayFixed = { execute: (amount) => console.log(`WeChat: ${amount}`) };
console.log(checkout(99.0, alipayFixed));   // ✅
console.log(checkout(99.0, wechatPayFixed)); // ✅
// ============ END BREAK IT ============
```

> **问自己:**
> 1. 为什么消费者函数要求"不能 if/elif 判断类型"?
> 2. 为什么支付方式对象用 const 而不是 let?
> 3. 如果新增 ApplePay,需要改 checkout 函数吗?

---

#### 执行过程跟踪

```javascript
// --- 执行过程 ---
// 第 1 行 const alipay = { execute: ... }:
//   ① 创建常量 alipay
//   ② 把 { execute: ... } 赋值给 alipay
//   ③ 标记为常量(不能重新赋值,但可修改属性)
//
// 第 2 行 checkout(99.0, alipay):
//   ① 调用 checkout 函数
//   ② 传入 cartTotal = 99.0, payment = alipay
//   ③ 执行 payment.execute(cartTotal)
//   ④ 即 alipay.execute(99.0)
//   ⑤ 输出 "Alipay: 99"
```

---

#### 常见错误

> 1. **错误现象**:在消费者函数里用 if 判断类型
>    **原因**:违反消费者门控约束,应该用多态调用
> 2. **错误现象**:支付方式对象用 let 声明
>    **原因**:语义不对,支付方式对象本身不变,应该用 const
> 3. **错误现象**:支付方式没有 execute 方法
>    **原因**:消费者函数要求 payment 必须有 execute 方法

---

#### 学员代码区

```javascript
// TODO: 用 const 声明两个支付方式对象(alipay 和 wechatPay)
//   要求:每个对象有 execute(amount) 方法
// TODO: 调用 checkout(99.0, alipay) 和 checkout(99.0, wechatPay)
// TODO: 新增 ApplePay,不需要改 checkout 函数
```

---

#### 参考答案

```javascript
const alipay = { execute: (amount) => console.log(`Alipay: ${amount}`) };
const wechatPay = { execute: (amount) => console.log(`WeChat: ${amount}`) };
const applePay = { execute: (amount) => console.log(`ApplePay: ${amount}`) };

checkout(99.0, alipay);     // "Alipay: 99"
checkout(99.0, wechatPay);  // "WeChat: 99"
checkout(99.0, applePay);   // "ApplePay: 99"
```

---

## 明日衔接

- 明天:课程结束,综合项目(用三问框架完成一个完整的小项目)
- 今天遗留的概念:今天学了场景选择,但还没在完整项目中实践
- 综合项目预告:
  - 用 const 声明配置项和支付方式
  - 用 let 声明累加器和循环变量
  - 用消费者函数门控场景选择
