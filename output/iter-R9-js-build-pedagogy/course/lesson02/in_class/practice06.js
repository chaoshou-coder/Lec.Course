/*
[难度: ★★★]
[所属知识点: 综合(挑战题)]
[预计完成时间: 15 分钟]
[类型: 挑战题,不强制完成]

题目:下面的"购物车"代码有 4 处反模式,找出来并修正。

    function checkout(cart) {
        var total = 0;
        for (var i = 0; i < cart.length; i++) {
            var price = cart[i].price;
            var tax = price * 0.1;
            total = total + price + tax;
        }

        var DISCOUNT = 0.9;
        if (total > 100) {
            DISCOUNT = 0.8;
        }
        total = total * DISCOUNT;

        return total;
    }

反模式提示:var 泄漏 / const 误用 / 作用域 / 命名规范
*/

if (require.main === module) {
  console.log("4 处反模式:");
  console.log("  1. var i 在 for 循环外泄漏 → 修正:let i");
  console.log("  2. var price/tax 在 for 块外泄漏 → 修正:let price/let tax");
  console.log("  3. var DISCOUNT 重新赋值 → 修正:let DISCOUNT(因为会变)");
  console.log("     (或 const + 三元运算符)");
  console.log("  4. var total 可以,const 不行(因为重新赋值) → 保持 let");
  console.log("");
  console.log("修正后:");
  console.log("  function checkout(cart) {");
  console.log("      let total = 0;");
  console.log("      for (let i = 0; i < cart.length; i++) {");
  console.log("          let price = cart[i].price;");
  console.log("          let tax = price * 0.1;");
  console.log("          total = total + price + tax;");
  console.log("      }");
  console.log("      let DISCOUNT = total > 100 ? 0.8 : 0.9;");
  console.log("      total = total * DISCOUNT;");
  console.log("      return total;");
  console.log("  }");
}
