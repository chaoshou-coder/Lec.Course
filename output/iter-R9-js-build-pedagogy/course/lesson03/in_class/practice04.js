/*
[难度: ★★]
[所属知识点: 反模式识别(NCDL)]
[预计完成时间: 10 分钟]

题目:下面代码有 2 个反模式,找出来。

    function checkout(cartTotal, payment) {
        if (payment.type === "alipay") {
            return alipayPay(cartTotal);
        } else if (payment.type === "wechat") {
            return wechatPay(cartTotal);
        }
    }

反模式提示:消费者门控的两个约束
*/

if (require.main === module) {
  console.log("2 个反模式:");
  console.log("  1. 用 if/elif 判断 payment.type → 违反'不能判断类型'约束");
  console.log("  2. 函数体超过 4 行 → 违反'消费者函数 ≤4 行'约束");
  console.log("");
  console.log("修正后:");
  console.log("  function checkout(cartTotal, payment) {");
  console.log("      return payment.execute(cartTotal);  // 多态调用,不判断类型");
  console.log("  }");
}
