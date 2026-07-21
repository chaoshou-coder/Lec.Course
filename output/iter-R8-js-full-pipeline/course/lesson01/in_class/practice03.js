/*
[难度: ★★]
[所属知识点: 三种关键字写法]
[预计完成时间: 8 分钟]

题目:同时声明三个变量:
- 用 let 声明 score,值 85
- 用 const 声明 MAX,值 100
- 用 var 声明 legacy,值 "old"

要求:
1. 三种关键字各用一次
2. 三个 console.log 分别输出它们的值
*/

// 学员代码区
// 在这里写出代码:


// 测试区
if (require.main === module) {
  console.log("参考答案:");
  console.log('  let score = 85;');
  console.log('  const MAX = 100;');
  console.log('  var legacy = "old";');
  console.log('  console.log(score, MAX, legacy);');
  console.log("");
  console.log("期望输出:85 100 old");
}
