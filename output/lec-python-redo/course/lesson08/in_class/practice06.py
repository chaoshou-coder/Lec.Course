"""
[难度: ★★★][所属知识点: 继承与 super()][预计完成时间: 15 分钟]

题目:定义 VipOrder 子类继承 Order,添加 discount 属性,
用 super() 调用父类 __init__。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('class VipOrder(Order):')
    print('    def __init__(self, order_id, product, price, discount):')
    print('        super().__init__(order_id, product, price)')
    print('        self.discount = discount')
    print('    def get_final_price(self):')
    print('        return self.price * self.discount')
