"""
[难度: ★][所属知识点: 类与对象][预计完成时间: 5 分钟]

题目:定义 Product 类(暂时用 pass),创建两个对象 p1、p2,
分别给它们绑定 title 和 price,然后打印两个商品的 title。
"""

class Product:
    pass

# TODO: 创建 p1,绑定 title 和 price
# TODO: 创建 p2,绑定 title 和 price
# TODO: 打印 p1.title 和 p2.title
pass

if __name__ == '__main__':
    # 参考答案
    class Product:
        pass

    p1 = Product()
    p1.title = "Python 入门"
    p1.price = 59.8

    p2 = Product()
    p2.title = "算法图解"
    p2.price = 45.0

    print(p1.title)  # Python 入门
    print(p2.title)  # 算法图解
