/*
[难度: ★★★★]
[所属知识点: 综合项目]
[预计完成时间: 30 分钟]
[类型: 选做]

题目:编写一个"购物车结算系统",综合运用三种声明方式。

要求:
1. 用 const 声明税率 TAX_RATE(0.1)和折扣配置 DISCOUNT(满 100 打 9 折)
2. 用 let 声明总价 total(因为会重新赋值)
3. 用 const 声明支付方式对象 alipay(有 execute 方法)
4. 用 let 声明循环变量(在 for 循环中)
5. 用消费者函数 checkout(≤4 行)完成结算
*/

if (require.main === module) {
  console.log("参考答案:");
  console.log("  const TAX_RATE = 0.1;");
  console.log("  const DISCOUNT = { threshold: 100, rate: 0.9 };");
  console.log("  const alipay = { execute: (amount) => console.log(`Alipay: ${amount}`) };");
  console.log("");
  console.log("  function checkout(cart, payment) {");
  console.log("      let total = 0;");
  console.log("      for (let i = 0; i < cart.length; i++) {");
  console.log("          total = total + cart[i].price;");
  console.log("      }");
  console.log("      total = total * (1 + TAX_RATE);");
  console.log("      if (total > DISCOUNT.threshold) { total = total * DISCOUNT.rate; }");
  console.log("      return payment.execute(total);");
  console.log("  }");
}
