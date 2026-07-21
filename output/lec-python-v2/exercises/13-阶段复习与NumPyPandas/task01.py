"""
[难度: ★★★][所属知识点: 购物车 JSON 持久化][类型: 选做]
[预计完成时间: 20 分钟]

题目:在 Cart 类基础上新增 save 和 load 方法:
- save(path):把购物车写入 JSON 文件(utf-8,ensure_ascii=False)
- load(path):从 JSON 读取,文件不存在返回空列表

用以下流程测试:
    1. 创建 cart,加 2 个苹果 + 1 个香蕉
    2. save("cart.json") 保存
    3. 新建 cart2, load("cart.json") 读取
    4. cart2.view() 应看到同样的内容

示例:
    苹果 x2 = ￥11.00
    香蕉 x1 = ￥3.20
    总价: ￥14.20
"""

import json
import os

# TODO: 定义 Cart 类,包含 add / total / view / save / load
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
    #         t = 0
    #         for item in self.items:
    #             t += item["price"] * item["qty"]
    #         return t
    #
    #     def view(self):
    #         for item in self.items:
    #             sub = item["price"] * item["qty"]
    #             print(f"  {item['name']} x{item['qty']} = ￥{sub:.2f}")
    #         print(f"总价: ￥{self.total():.2f}")
    #
    #     def save(self, path="cart.json"):
    #         with open(path, "w", encoding="utf-8") as f:
    #             json.dump(self.items, f, ensure_ascii=False, indent=2)
    #
    #     def load(self, path="cart.json"):
    #         if not os.path.exists(path):
    #             self.items = []
    #             return
    #         with open(path, "r", encoding="utf-8") as f:
    #             self.items = json.load(f)
    #
    # cart = Cart()
    # cart.add(("苹果", 5.50), 2)
    # cart.add(("香蕉", 3.20), 1)
    # cart.save("cart.json")
    # cart2 = Cart()
    # cart2.load("cart.json")
    # cart2.view()
    pass
