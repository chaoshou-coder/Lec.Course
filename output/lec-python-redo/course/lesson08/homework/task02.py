"""
[难度: ★★★][所属知识点: VIP 订单继承][预计完成时间: 20 分钟][类型: 选做]

题目:扩展 VipOrder,重写 __str__ 显示折扣价,
添加 is_vip 属性,以及一个类方法 from_order 从普通订单创建 VIP 订单。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('class VipOrder(Order):')
    print('    is_vip = True')
    print('    def __init__(self, order_id, product, price, discount=0.8):')
    print('        super().__init__(order_id, product, price)')
    print('        self.discount = discount')
    print('    def __str__(self):')
    print('        final = self.price * self.discount')
    print('        return f"VIP {self.order_id}: {self.product} ￥{final}"')
    print('    @classmethod')
    print('    def from_order(cls, order, discount=0.8):')
    print('        return cls(order.order_id, order.product, order.price, discount)')
