"""
[难度: ★★★][所属知识点: __str__ 与 __repr__][预计完成时间: 12 分钟]

题目:在 Order 类中添加 __str__ 和 __repr__。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('class Order:')
    print('    def __str__(self):')
    print('        return f"订单{self.order_id}: {self.product} ￥{self.price}"')
    print('    def __repr__(self):')
    print('        return f"Order({self.order_id!r}, {self.product!r}, {self.price})"')
