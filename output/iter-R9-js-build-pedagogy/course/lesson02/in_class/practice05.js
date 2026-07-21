/*
[难度: ★★★]
[所属知识点: 反模式识别(NCDL)]
[预计完成时间: 15 分钟]

题目:下面代码有 3 个反模式(常见错误),找出来并修正。

    function processItems(items) {
        for (var i = 0; i < items.length; i++) {
            console.log(items[i]);
        }
        console.log("Total:", i);

        var result;
        if (items.length > 0) {
            result = items[0];
        }
        console.log(result);

        var MAX_SIZE = 100;
        if (items.length > MAX_SIZE) {
            MAX_SIZE = 200;
        }
    }

反模式提示:var 泄漏 / var hoisting / const 误用
*/

if (require.main === module) {
  console.log("3 个反模式:");
  console.log("  1. for 循环用 var 声明 i → 循环结束后 i 还在(泄漏)");
  console.log("     修正:for (let i = 0; ...)");
  console.log("");
  console.log("  2. var result 在 if 块外访问 → 可能 undefined(hoisting)");
  console.log("     修正:let result = null(初始值明确)");
  console.log("");
  console.log("  3. var MAX_SIZE 声明后重新赋值 → 应该用 const");
  console.log("     修正:const MAX_SIZE = 100(如果不变)或 let(如果变)");
  console.log("");
  console.log("修正后:");
  console.log("  function processItems(items) {");
  console.log("      for (let i = 0; i < items.length; i++) {");
  console.log("          console.log(items[i]);");
  console.log("      }");
  console.log("      let result = null;");
  console.log("      if (items.length > 0) {");
  console.log("          result = items[0];");
  console.log("      }");
  console.log("      const MAX_SIZE = 100;");
  console.log("  }");
}
