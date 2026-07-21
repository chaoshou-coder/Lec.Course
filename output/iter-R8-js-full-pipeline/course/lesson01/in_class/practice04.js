/*
[难度: ★★]
[所属知识点: 重新赋值 let]
[预计完成时间: 10 分钟]

题目:下面的代码最后会输出什么?为什么?

    let count = 0;
    count = 5;
    count = count + 1;
    console.log(count);

边界:考虑 count 是否会出错(count 是空、未声明、重新声明等)
*/

// 学员作答
const answer = `
(在这里写出你的预测和理由)
`;

// 测试区
if (require.main === module) {
  console.log("实际运行:");
  console.log("  let count = 0;");
  console.log("  count = 5;");
  console.log("  count = count + 1;");
  console.log("  console.log(count);");
  console.log("");
  console.log("期望输出:6");
  console.log("");
  console.log("解释:");
  console.log("  - 第 1 行:声明 count,值 0");
  console.log("  - 第 2 行:重新赋值 count,值 5(直接 = 表示修改)");
  console.log("  - 第 3 行:count + 1 = 5 + 1 = 6,赋值给 count");
  console.log("  - 第 4 行:打印 6");
  console.log("");
  console.log("边界情况:");
  console.log("  - 如果第 1 行遗漏 'let':count 变成隐式全局变量(老 JS 行为,新规范报错)");
  console.log("  - 如果第 2 行加 'let':Uncaught SyntaxError(重复声明)");
  console.log("  - 如果 count 是 const:第 2-3 行会 TypeError(常量不能改)");
}
