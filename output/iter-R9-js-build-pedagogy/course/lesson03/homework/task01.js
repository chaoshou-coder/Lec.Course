/*
[难度: ★★★]
[所属知识点: 修复错误声明]
[预计完成时间: 15 分钟]
[类型: 选做]

题目:修复下面的声明错误。

    var PI = 3.14;           // 应该用 const
    let config = {}; config = {};  // 第二次赋值应该用 let,但第一次用 const 更好
    for (var i = 0; i < 10; i++) {  // var 泄漏
        console.log(i);
    }
*/

if (require.main === module) {
  console.log("修正后:");
  console.log("  const PI = 3.14;");
  console.log("  const config = {};  // 如果不重新赋值");
  console.log("  // 或 let config = {};  // 如果后续需要重新赋值");
  console.log("  for (let i = 0; i < 10; i++) {");
  console.log("      console.log(i);");
  console.log("  }");
}
