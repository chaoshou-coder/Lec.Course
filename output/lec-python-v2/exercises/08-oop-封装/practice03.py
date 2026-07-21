"""
[难度: ★★][所属知识点: self 和实例方法][预计完成时间: 10 分钟]

题目:给 Product 类添加 info(self) 方法,
返回 "商品[XXX] 价格:XX.XX 元"。
创建商品,调用 info()。
"""

class Product:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    # TODO: 添加 info(self) 方法
    pass

if __name__ == '__main__':
    # 参考答案
    class Product:
        def __init__(self, title, price):
            self.title = title
            self.price = price

        def info(self):
            return f"商品[{self.title}] 价格:{self.price:.2f} 元"

    p = Product("Python 入门", 59.8)
    print(p.info())  # 商品[Python 入门] 价格:59.80 元
