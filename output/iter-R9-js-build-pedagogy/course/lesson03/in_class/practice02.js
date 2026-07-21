/*
[难度: ★]
[所属知识点: 场景选择(简单)]
[预计完成时间: 5 分钟]

题目:给定以下场景,选择 let/const 并说明理由。

    1. 圆周率 PI = 3.14159
    2. 累加器 sum,每次循环加一个数
    3. 用户列表 users,声明后需要 push 新用户
    4. 循环计数器 i
*/

if (require.main === module) {
  console.log("1. PI → const(永远不变)");
  console.log("2. sum → let(需要重新赋值)");
  console.log("3. users → const(对象本身不变,内容可变)");
  console.log("4. i → let(块级,循环结束后释放)");
}
