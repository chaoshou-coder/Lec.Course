/*
[难度: ★★]
[所属知识点: 三种声明方式对比]
[预计完成时间: 10 分钟]

题目:给定以下场景,选择 let/var/const 并说明理由。

    1. 循环计数器,循环结束后不再需要
    2. 配置项(API_KEY),声明后永远不变
    3. 累加器,每次循环需要重新赋值
    4. 对象字面量,声明后需要添加属性
*/

if (require.main === module) {
  console.log("1. 循环计数器 → let");
  console.log("   理由:块级作用域,循环结束后自动释放");
  console.log("");
  console.log("2. 配置项(API_KEY) → const");
  console.log("   理由:永远不变,const 阻止重新赋值");
  console.log("");
  console.log("3. 累加器 → let");
  console.log("   理由:需要重新赋值,const 不允许");
  console.log("");
  console.log("4. 对象字面量 → const");
  console.log("   理由:const 允许修改属性(添加属性),只是不能重新赋值");
}
