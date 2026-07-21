/*
[难度: ★★]
[所属知识点: const 限制]
[预计完成时间: 8 分钟]

题目:下面哪些操作会报错?为什么?

    const arr = [1, 2, 3];
    arr.push(4);          // ( )
    arr = [5, 6, 7];     // ( )

    const obj = { name: "Alice" };
    obj.name = "Bob";     // ( )
    obj = { name: "Carol" }; // ( )

    const x;              // ( )
*/

if (require.main === module) {
  console.log("arr.push(4) → ✅ 不报错(修改内容,不是重新赋值)");
  console.log("arr = [5, 6, 7] → ❌ TypeError(重新赋值)");
  console.log("obj.name = 'Bob' → ✅ 不报错(修改属性)");
  console.log("obj = { name: 'Carol' } → ❌ TypeError(重新赋值)");
  console.log("const x; → ❌ SyntaxError(const 声明时必须初始化)");
  console.log("");
  console.log("要点:const 阻止重新赋值,不阻止修改内容/属性");
}
