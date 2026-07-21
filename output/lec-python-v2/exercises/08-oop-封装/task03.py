"""
[难度: ★★★★][所属知识点: 综合项目][预计完成时间: 30 分钟][类型: 选做]

题目:设计一个"图书管理系统"的 Book 类:
- __init__(title, author, price, stock)
- @property 保护 price(>0)和 stock(≥0)
- sell(n) 卖 n 本,库存不足时拒绝
- restock(n) 补货 n 本
- __str__ 输出 "Book(title=..., stock=...)"

创建一本书,卖 5 本,补货 10 本,打印状态。
"""

# TODO: 补全
pass

if __name__ == '__main__':
    # 参考答案
    class Book:
        def __init__(self, title, author, price, stock):
            self.title = title
            self.author = author
            self.price = price
            self.stock = stock

        @property
        def price(self):
            return self._price

        @price.setter
        def price(self, value):
            if value <= 0:
                print("价格必须 > 0")
                return
            self._price = value

        @property
        def stock(self):
            return self._stock

        @stock.setter
        def stock(self, value):
            if value < 0:
                print("库存不能为负")
                return
            self._stock = value

        def sell(self, n):
            if n > self._stock:
                print("库存不足")
                return False
            self._stock -= n
            return True

        def restock(self, n):
            self._stock += n
            return self._stock

        def __str__(self):
            return f"Book(title={self.title}, stock={self._stock})"

    book = Book("Python 入门", "张三", 59.8, 10)
    print(book)          # Book(title=Python 入门, stock=10)
    book.sell(5)
    print(book)          # Book(title=Python 入门, stock=5)
    book.restock(10)
    print(book)          # Book(title=Python 入门, stock=15)
