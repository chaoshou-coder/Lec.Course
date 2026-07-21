"""
[难度: ★★][所属知识点: __init__ 构造函数][预计完成时间: 8 分钟]

题目:给 Product 类添加 __init__ 方法,自动绑定 title 和 price,
创建两本书 p1、p2,分别打印它们的 title 和 price。
"""

class Product:
    # TODO: 添加 __init__ 方法
    pass

# TODO: 创建 p1 = Product("Python 入门", 59.8)
# TODO: 创建 p2 = Product("算法图解", 45.0)
# TODO: 打印 p1.title, p1.price

if __name__ == '__main__':
    # 参考答案
    class Product:
        def __init__(self, title, price):
            self.title = title
            self.price = price

    p1 = Product("Python 入门", 59.8)
    p2 = Product("算法图解", 45.0)
    print(p1.title, p1.price)  # Python 入门 59.8
    print(p2.title, p2.price)  # 算法图解 45.0
