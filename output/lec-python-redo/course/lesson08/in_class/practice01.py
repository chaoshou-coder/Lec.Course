"""
[难度: ★][所属知识点: class 定义与 __init__][预计完成时间: 5 分钟]

题目:定义一个 Order 类,包含 __init__(self, order_id, product, price)。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('class Order:')
    print('    def __init__(self, order_id, product, price):')
    print('        self.order_id = order_id')
    print('        self.product = product')
    print('        self.price = price')
    print('order = Order("A001", "书", 59.9)')
