"""
[难度: ★★★][所属知识点: 类属性 vs 实例属性][预计完成时间: 20 分钟][类型: 选做]

题目:定义 Product 类:
- 类属性 tax_rate = 0.13
- 实例属性 name 和 price
- 方法 price_with_tax() 返回含税价格
创建两个商品,改 Product.tax_rate = 0.09,
观察两个商品是否都跟着变。
"""

# TODO: 补全
pass

if __name__ == '__main__':
    # 参考答案
    class Product:
        tax_rate = 0.13

        def __init__(self, name, price):
            self.name = name
            self.price = price

        def price_with_tax(self):
            return self.price * (1 + Product.tax_rate)

    p1 = Product("Python 入门", 100)
    p2 = Product("算法图解", 200)
    print(p1.price_with_tax())  # 113.0
    print(p2.price_with_tax())  # 226.0
    Product.tax_rate = 0.09
    print(p1.price_with_tax())  # 109.0
    print(p2.price_with_tax())  # 218.0
