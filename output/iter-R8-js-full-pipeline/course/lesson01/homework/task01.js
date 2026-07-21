/*
[难度: ★★★]
[所属知识点: 修复错误代码]
[预计完成时间: 15 分钟]
[类型: 选做]

题目:下面这段代码有 3 处错误,你能在不改变变量类型(const→let 或 let→const)的前提下修复?

    const username = "alice";
    const username = "bob";
    console.log(username);

要求:让代码运行输出 "bob",保持 username 仍能被重新赋值。
*/

// 学员作答
const answerCode = `
(在这里写出修正后的代码)
`;

// 测试区
if (require.main === module) {
  console.log("参考答案(改成 let 即可):");
  console.log('  let username = "alice";');
  console.log('  username = "bob";');
  console.log('  console.log(username);');
  console.log("");
  console.log("要点:");
  console.log("  - 把 const 改成 let —— 因为 let 才能重新赋值");
  console.log("  - 移除第二个 const 声明 —— 同一作用域不能重复声明同名字");
}
