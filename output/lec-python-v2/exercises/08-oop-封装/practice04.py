"""
[难度: ★★][所属知识点: @property getter][预计完成时间: 10 分钟]

题目:给 Product 类添加 @property price_with_tax,
返回含税价格(税率 13%)。
创建商品,访问 p.price_with_tax(注意:不加括号!)。
"""

class Product:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    # TODO: 添加 @property price_with_tax
    pass

if __name__ == '__main__':
    # 参考答案
    class Product:
        def __init__(self, title, price):
            self.title = title
            self.price = price

        @property
        def price_with_tax(self):
            return self.price * 1.13

    p = Product("Python 入门", 100)
    print(p.price_with_tax)  # 113.0(没有括号)
