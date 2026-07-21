"""
[难度: ★★][所属知识点: 实例属性 vs 类属性][预计完成时间: 10 分钟]

题目:在 Order 类中添加类属性 platform="Lec商城" 和 order_count=0。
每次创建订单,order_count 加 1。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('class Order:')
    print('    platform = "Lec商城"')
    print('    order_count = 0')
    print('    def __init__(self, order_id, product, price):')
    print('        self.order_id = order_id')
    print('        self.product = product')
    print('        self.price = price')
    print('        Order.order_count += 1')
