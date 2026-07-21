/*
[难度: ★★★★]
[所属知识点: 综合应用]
[预计完成时间: 25 分钟]
[类型: 选做]

题目:编写一个"温度转换器",演示你对三种声明方式的理解。

要求:
1. 用 const 声明转换系数(华氏→摄氏的系数 5/9)
2. 用 let 声明输入温度和输出温度(因为会重新赋值)
3. 用 const 声明一个配置对象(包含单位名称),然后尝试修改属性
4. 在 for 循环中用 let 声明循环变量,验证循环结束后不可访问
*/

if (require.main === module) {
  console.log("参考答案:");
  console.log("  const FACTOR = 5 / 9;           // 转换系数(不变)");
  console.log("  let fahrenheit = 100;            // 输入温度(会变)");
  console.log("  let celsius = 0;                 // 输出温度(会变)");
  console.log("  celsius = (fahrenheit - 32) * FACTOR;");
  console.log("  console.log(celsius);            // 37.78");
  console.log("");
  console.log("  const config = { from: 'F', to: 'C' };");
  console.log("  config.from = 'K';               // ✅ 可以修改属性");
  console.log("  // config = {};                   // ❌ 不能重新赋值");
  console.log("");
  console.log("  for (let i = 0; i < 3; i++) {");
  console.log("      console.log(i);");
  console.log("  }");
  console.log("  // console.log(i);                // ❌ ReferenceError");
}
