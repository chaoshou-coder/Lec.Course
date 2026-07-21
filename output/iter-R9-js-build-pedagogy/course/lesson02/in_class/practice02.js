/*
[难度: ★]
[所属知识点: let TDZ 认知]
[预计完成时间: 5 分钟]

题目:下面代码的输出是什么?为什么?

    function test() {
        console.log(y);
        let y = 10;
        console.log(y);
    }
    test();

边界:对比 var 的行为。
*/

if (require.main === module) {
  console.log("let 版本:");
  console.log("  console.log(y) → ReferenceError: Cannot access 'y' before initialization");
  console.log("  原因:let 不会被提升,在声明前进入 TDZ(Temporal Dead Zone)");
  console.log("");
  console.log("var 版本:");
  console.log("  console.log(y) → undefined(hoisting)");
  console.log("  原因:var 被提升,声明在顶部,但赋值留在原地");
}
