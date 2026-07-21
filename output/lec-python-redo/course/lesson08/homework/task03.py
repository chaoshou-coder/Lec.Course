"""
[难度: ★★★★][所属知识点: 完整订单系统][预计完成时间: 30 分钟][类型: 选做]

题目:实现电商订单系统,包含 Order/VipOrder 类,
支持创建订单、付款、取消、显示信息。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('class Order:')
    print('    platform = "Lec商城"')
    print('    def __init__(self, oid, product, price):')
    print('        self.oid = oid; self.product = product')
    print('        self.price = price; self.status = "待付款"')
    print('    def pay(self): self.status = "已付款"')
    print('    def cancel(self): self.status = "已取消"')
    print('    def __str__(self):')
    print('        return f"{self.oid}: {self.product} ￥{self.price} ({self.status})"')
    print()
    print('class VipOrder(Order):')
    print('    def __init__(self, oid, product, price, discount=0.8):')
    print('        super().__init__(oid, product, price)')
    print('        self.discount = discount')
    print('    def get_final_price(self):')
    print('        return self.price * self.discount')
    print('    def __str__(self):')
    print('        return f"VIP {super().__str__()} {self.discount*10}折"')
