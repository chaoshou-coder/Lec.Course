/*
[难度: ★]
[所属知识点: var hoisting 认知]
[预计完成时间: 5 分钟]

题目:下面代码的输出是什么?为什么?

    console.log(x);
    var x = 5;
    console.log(x);

边界:如果换成 let,输出会怎样?
*/

if (require.main === module) {
  console.log("var 版本:");
  console.log("  console.log(x) → undefined(hoisting 把声明提升,但赋值没提升)");
  console.log("  var x = 5");
  console.log("  console.log(x) → 5");
  console.log("");
  console.log("let 版本:");
  console.log("  console.log(x) → ReferenceError(TDZ,声明前不可访问)");
  console.log("  let x = 5");
  console.log("  console.log(x) → 5");
}
