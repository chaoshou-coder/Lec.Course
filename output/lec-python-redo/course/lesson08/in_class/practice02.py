"""
[难度: ★][所属知识点: 实例方法(self)][预计完成时间: 8 分钟]

题目:在 Order 类中添加 pay(self) 方法,将 status 改为"已付款"。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('class Order:')
    print('    def __init__(self, order_id, product, price):')
    print('        self.order_id = order_id')
    print('        self.product = product')
    print('        self.price = price')
    print('        self.status = "待付款"')
    print('    def pay(self):')
    print('        self.status = "已付款"')
