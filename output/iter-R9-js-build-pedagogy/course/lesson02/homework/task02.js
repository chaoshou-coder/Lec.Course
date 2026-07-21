/*
[难度: ★★★]
[所属知识点: 修复 TDZ 错误]
[预计完成时间: 20 分钟]
[类型: 选做]

题目:下面代码会在第 2 行报错,解释原因并修复。

    function calculate() {
        let result = value * 2;  // ❌ ReferenceError
        let value = 10;
        return result;
    }

要求:修复代码,让 result = 20。
*/

if (require.main === module) {
  console.log("原因:let value 在声明前进入 TDZ,访问会报错(不像 var 会 hoisting 到 undefined)");
  console.log("");
  console.log("修正后:");
  console.log("  function calculate() {");
  console.log("      let value = 10;       // 先声明");
  console.log("      let result = value * 2;  // 后使用");
  console.log("      return result;        // 20");
  console.log("  }");
}
