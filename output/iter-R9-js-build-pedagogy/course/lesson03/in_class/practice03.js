/*
[难度: ★★]
[所属知识点: 消费者函数门控]
[预计完成时间: 10 分钟]

题目:补全下面的消费者函数调用。

约束:
- checkout 函数体不超过 4 行
- 不能用 if/elif 判断支付方式类型
- 支付方式对象用 const 声明

    // 消费者函数(已提供)
    function checkout(cartTotal, payment) {
        return payment.execute(cartTotal);
    }

    // TODO: 用 const 声明 alipay 对象,有 execute 方法
    // TODO: 用 const 声明 wechatPay 对象,有 execute 方法
    // TODO: 调用 checkout(99.0, alipay)
*/

if (require.main === module) {
  console.log("参考答案:");
  console.log("  const alipay = {");
  console.log("      execute: (amount) => console.log(`Alipay: ${amount}`)");
  console.log("  };");
  console.log("  const wechatPay = {");
  console.log("      execute: (amount) => console.log(`WeChat: ${amount}`)");
  console.log("  };");
  console.log("  checkout(99.0, alipay);     // Alipay: 99");
  console.log("  checkout(99.0, wechatPay);  // WeChat: 99");
}
