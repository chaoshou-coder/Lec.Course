/*
[难度: ★★★]
[所属知识点: 修复 var 泄漏代码]
[预计完成时间: 15 分钟]
[类型: 选做]

题目:修复下面的 var 泄漏代码,让它按预期工作。

预期行为:循环结束后 i 不可访问,每次循环的 item 是独立的。

    function printItems(items) {
        for (var i = 0; i < items.length; i++) {
            console.log(items[i]);
        }
        console.log("Last index:", i);  // 不应该能访问
    }

要求:用 let 修复,让循环结束后 i 不可访问。
*/

if (require.main === module) {
  console.log("修正后:");
  console.log("  function printItems(items) {");
  console.log("      for (let i = 0; i < items.length; i++) {");
  console.log("          console.log(items[i]);");
  console.log("      }");
  console.log("      // console.log(i);  // ❌ ReferenceError: i is not defined");
  console.log("  }");
}
