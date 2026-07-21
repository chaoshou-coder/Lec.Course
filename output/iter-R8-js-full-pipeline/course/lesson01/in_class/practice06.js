/*
[难度: ★★★]
[所属知识点: 综合应用(挑战题)]
[预计完成时间: 15 分钟]
[类型: 挑战题,不强制完成]

题目:下面是一段损坏的 JS 代码,运行会报错,需要你:
1. 找出 4 处错误
2. 说出报错原因
3. 写出修正后版本

损坏代码:
    const Name = "张三";
    Name = "李四";
    const age = 25;
    let Age;
    Age = 30;
    console.log(NAME, Age);

提示:错误可能涉及 —— 重复声明、大小写、const 重新赋值
*/

// 学员作答
const errorsFound = `
1. (你的分析)
2. (你的分析)
3. (你的分析)
4. (你的分析)
`;

// 测试区
if (require.main === module) {
  console.log("4 处错误:");
  console.log("  1. const Name = ... 然后 Name = ... : const 不能重新赋值");
  console.log("  2. const name 已声明后,又声明 Age(不同名): 在同一个作用域里 const 不能重复声明(这里是 const name,然后 let Age 是不同的变量名,这条不算错误)");
  console.log("");
  console.log("实际上:");
  console.log("  - Name = 李四 : TypeError(改名没用,const 仍然不能改)");
  console.log("  - console.log(NAME, Age) : NAGE 未定义(大小写不对)");
  console.log("");
  console.log("3 处主要错误:");
  console.log("  1. Name = '李四' 尝试重新赋值 const(报错)");
  console.log("  2. console.log(NAME): NAME 未定义(没这个变量,有 Name)");
  console.log("  3. 即使上面都修了,代码意图混乱(变量名不规范)");
  console.log("");
  console.log("修正版本:");
  console.log('  let name = "张三";');              // 用 let 不是 const
  console.log('  name = "李四";');                  // 改为 let 后可以重新赋值
  console.log('  const age = 25;')                  ; // age 不变(无需 let)
  console.log('  let Age = age + 5;');              // Age 可变(假设要做年龄计算)
  console.log('  console.log(name, Age);');         // 修正大小写
}
