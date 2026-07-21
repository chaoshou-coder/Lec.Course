/*
[难度: ★★★]
[所属知识点: 消费者门控(挑战题)]
[预计完成时间: 15 分钟]
[类型: 挑战题,不强制完成]

题目:实现一个"日志系统",用消费者函数门控日志级别的输出。

约束:
- Logger 消费者函数 ≤4 行,不判断 logger 类型
- 用 const 声明各个 logger 对象
- 新增 logger 时不需要改 Logger 函数

    // TODO: 实现 Logger 消费者函数(≤4 行)
    // TODO: 用 const 声明 consoleLogger(有 log 方法)
    // TODO: 用 const 声明 fileLogger(有 log 方法,输出到文件)
    // TODO: 调用 Logger("Hello", consoleLogger) 和 Logger("Hello", fileLogger)
*/

if (require.main === module) {
  console.log("参考答案:");
  console.log("  function Logger(message, logger) {");
  console.log("      return logger.log(message);  // 多态调用");
  console.log("  }");
  console.log("  const consoleLogger = {");
  console.log("      log: (msg) => console.log(`[Console] ${msg}`)");
  console.log("  };");
  console.log("  const fileLogger = {");
  console.log("      log: (msg) => console.log(`[File] ${msg}`)");
  console.log("  };");
  console.log("  Logger(\"Hello\", consoleLogger);  // [Console] Hello");
  console.log("  Logger(\"Hello\", fileLogger);     // [File] Hello");
}
