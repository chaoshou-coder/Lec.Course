"""
[难度: ⭐⭐]
[所属知识点: super().__init__() 扩展属性]
[预计完成时间: 15 分钟]

题目描述:
定义 Product 基类,属性 name 和 price。
定义 Book 子类继承 Product,新增属性 author。
用 super().__init__() 继承基类属性。
创建 Book 实例,验证所有属性都能正确访问。

示例:
    >>> b = Book("Python 入门", 59.8, "张三")
    >>> b.name
    'Python 入门'
    >>> b.price
    59.8
    >>> b.author
    '张三'
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Book(Product):
    pass  # 请实现 __init__,用 super() 继承 base 属性

# b = Book("Python 入门", 59.8, "张三")
# print(b.name, b.price, b.author)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1:验证 name 属性
    # 测试 2:验证 price 属性
    # 测试 3:验证 author 属性
    pass
