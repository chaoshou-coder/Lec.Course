/*
[难度: ★★★★]
[所属知识点: 综合应用]
[预计完成时间: 25 分钟]
[类型: 选做]

题目:编写一段"个人名片"代码,演示你对变量声明和值的理解。

要求:
1. 用 const 声明 3 个"不变"信息(如姓名/出生年份/职业),用 let 声明 2 个"会变"信息(如当前城市/心情)
2. 给每个 const 一句简短说明(注释),解释为什么是不变的
3. 给每个 let 一句简短说明,解释为什么会变
4. 最后用 console.log 输出所有 5 个变量的值

进阶挑战:让一个 let 变量的值在代码中变化 2 次(先一个值,console.log,然后改成另一个值,再 console.log),观察输出的变化。
*/

// 学员作答
const answerCode = `
(在这里写出你的个人名片代码)
`;

// 测试区
if (require.main === module) {
  console.log("参考答案(示例):");
  console.log("");
  console.log('  // 不变的信息');
  console.log('  const FULL_NAME = "张三";         // 姓名一般不变');
  console.log('  const BIRTH_YEAR = 1990;         // 出生年份永远不变');
  console.log('  const PROFESSION = "开发者";      // 职业身份相对稳定');
  console.log("");
  console.log('  // 会变的信息');
  console.log('  let currentCity = "北京";         // 可能换城市');
  console.log('  currentCity = "上海";             // 已搬家');
  console.log('  let mood = "happy";              // 心情会变');
  console.log('  mood = "tired";                   // 今天累了');
  console.log("");
  console.log('  console.log(FULL_NAME, BIRTH_YEAR, PROFESSION, currentCity, mood);');
  console.log("");
  console.log("期望输出:");
  console.log("  张三 1990 开发者 上海 tired");
  console.log("");
  console.log("进阶挑战的输出:");
  console.log("  第一次:mood = 'happy' → 输出 'happy ...'");
  console.log("  修改后:mood = 'tired' → 输出 'tired ...'");
}
