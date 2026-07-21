"""
[难度: ★★★★][所属知识点: 电商订单系统模块化][预计完成时间: 30 分钟][类型: 选做]

题目:把 Day 8 的电商订单系统拆分成包结构:
shop/__init__.py, shop/order.py, shop/vip_order.py, main.py。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('# shop/order.py')
    print('class Order:')
    print('    platform = "Lec商城"')
    print('    def __init__(self, oid, product, price):')
    print('        self.oid = oid; self.product = product')
    print('        self.price = price; self.status = "待付款"')
    print('    def pay(self): self.status = "已付款"')
    print('    def __str__(self):')
    print('        return f"{self.oid}: {self.product} ￥{self.price}"')
    print()
    print('# shop/vip_order.py')
    print('from .order import Order')
    print('class VipOrder(Order):')
    print('    def __init__(self, oid, product, price, discount=0.8):')
    print('        super().__init__(oid, product, price)')
    print('        self.discount = discount')
    print('    def get_final_price(self):')
    print('        return self.price * self.discount')
    print()
    print('# main.py')
    print('from shop.order import Order')
    print('from shop.vip_order import VipOrder')
    print('order = VipOrder("V001", "书", 100)')
    print('print(order.get_final_price())')
