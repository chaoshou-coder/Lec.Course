"""
[难度: ★★★][所属知识点: 电商订单系统设计][预计完成时间: 15 分钟][类型: 选做]

题目:设计 Product 类,包含 name/price/stock 属性,
和 reduce_stock(self, qty) 方法(减少库存)。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('class Product:')
    print('    def __init__(self, name, price, stock):')
    print('        self.name = name')
    print('        self.price = price')
    print('        self.stock = stock')
    print('    def reduce_stock(self, qty):')
    print('        if self.stock >= qty:')
    print('            self.stock -= qty')
    print('            return True')
    print('        return False')
