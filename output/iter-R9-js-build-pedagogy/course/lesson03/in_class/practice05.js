/*
[难度: ★★★]
[所属知识点: 综合场景选择]
[预计完成时间: 15 分钟]

题目:给定以下代码,把 var 改成 let/const,并说明每个改动的理由。

    function calculateTotal(items) {
        var total = 0;
        for (var i = 0; i < items.length; i++) {
            var price = items[i].price;
            total = total + price;
        }
        var TAX_RATE = 0.1;
        total = total * (1 + TAX_RATE);
        return total;
    }
*/

if (require.main === module) {
  console.log("修正后:");
  console.log("  function calculateTotal(items) {");
  console.log("      let total = 0;                    // 重新赋值");
  console.log("      for (let i = 0; i < items.length; i++) {  // 块级,不泄漏");
  console.log("          let price = items[i].price;     // 块级,每次循环新变量");
  console.log("          total = total + price;");
  console.log("      }");
  console.log("      const TAX_RATE = 0.1;             // 永远不变");
  console.log("      total = total * (1 + TAX_RATE);");
  console.log("      return total;");
  console.log("  }");
}
