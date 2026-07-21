/*
[难度: ★★★]
[所属知识点: 消费者门控实现]
[预计完成时间: 20 分钟]
[类型: 选做]

题目:实现一个"通知系统",用消费者函数门控不同通知方式。

约束:
- sendNotification 函数 ≤4 行,不判断通知类型
- 用 const 声明各个通知对象
- 新增通知方式时不需要改 sendNotification

    // TODO: 实现 sendNotification(≤4 行)
    // TODO: 用 const 声明 emailNotifier(有 send 方法)
    // TODO: 用 const 声明 smsNotifier(有 send 方法)
    // TODO: 调用 sendNotification("Hello", emailNotifier)
*/

if (require.main === module) {
  console.log("参考答案:");
  console.log("  function sendNotification(message, notifier) {");
  console.log("      return notifier.send(message);");
  console.log("  }");
  console.log("  const emailNotifier = {");
  console.log("      send: (msg) => console.log(`[Email] ${msg}`)");
  console.log("  };");
  console.log("  const smsNotifier = {");
  console.log("      send: (msg) => console.log(`[SMS] ${msg}`)");
  console.log("  };");
  console.log("  sendNotification(\"Hello\", emailNotifier);  // [Email] Hello");
  console.log("  sendNotification(\"Hello\", smsNotifier);    // [SMS] Hello");
}
