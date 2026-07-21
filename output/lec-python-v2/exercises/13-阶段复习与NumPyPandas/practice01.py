"""
[难度: ★★][所属知识点: 购物车 OOP 版][预计完成时间: 15 分钟]

题目:定义 Cart 类,包含 add / total / view 方法。
- add(product, qty):添加商品,有则加数量,无则新增
- total():返回总价(累加器在循环外!)
- view():打印购物车内容和总价

用以下数据测试:
    p1 = ("苹果", 5.50)
    p2 = ("香蕉", 3.20)
    加 2 个苹果,1 个香蕉,打印购物车。

示例:
    苹果 x2 = ￥11.00
    香蕉 x1 = ￥3.20
    总价: ￥14.20
"""

# TODO: 定义 Cart 类,实现 add / total / view
class Cart:
    pass

if __name__ == '__main__':
    # 参考答案
    # class Cart:
    #     def __init__(self):
    #         self.items = []
    #
    #     def add(self, product, qty=1):
    #         name, price = product
    #         for item in self.items:
    #             if item["name"] == name:
    #                 item["qty"] += qty
    #                 return
    #         self.items.append({"name": name, "price": price, "qty": qty})
    #
    #     def total(self):
    #         t = 0  # 累加器在循环外!
    #         for item in self.items:
    #             t += item["price"] * item["qty"]
    #         return t
    #
    #     def view(self):
    #         for item in self.items:
    #             sub = item["price"] * item["qty"]
    #             print(f"  {item['name']} x{item['qty']} = ￥{sub:.2f}")
    #         print(f"总价: ￥{self.total():.2f}")
    cart = Cart()
    cart.add(("苹果", 5.50), 2)
    cart.add(("香蕉", 3.20), 1)
    cart.view()
