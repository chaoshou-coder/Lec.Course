"""
[难度: ⭐⭐⭐⭐⭐]
[所属知识点: 综合项目:电商订单系统 v2]
[预计完成时间: 50 分钟]

题目描述:
整合 Day08-11 全部知识,实现电商订单系统 v2:
1. Product(abc.ABC):sku、name、price(@property)、describe()
2. Book/Food 继承 Product,实现 describe()
3. Cart:组合多个 Product,__add__/__len__/__iter__
4. Product 支持 __eq__/__hash__/__repr__
5. Order:组合 addr 和 cart,summary() 方法

示例:
    >>> b = Book("B001", "Python 入门", 59.9)
    >>> f = Food("F001", "面包", 8.5)
    >>> c1 = Cart([b, f])
    >>> c2 = Cart([b])
    >>> c3 = c1 + c2
    >>> len(c3)
    3
    >>> for item in c3:
    ...     print(item.describe())
    图书《Python 入门》￥59.9
    食品[面包] ￥8.5
    图书《Python 入门》￥59.9
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import abc

class Product(abc.ABC):
    """抽象基类"""
    # 请实现 __init__、@property、__eq__、__hash__、__repr__
    # 请实现 describe() 抽象方法
    pass

class Book(Product):
    """图书"""
    # 请实现 describe()
    pass

class Food(Product):
    """食品"""
    # 请实现 describe()
    pass

class Cart:
    """购物车"""
    # 请实现 __init__、__add__、__len__、__iter__、__repr__
    pass

class Address:
    """收货地址"""
    def __init__(self, city, detail):
        self.city = city
        self.detail = detail

class Order:
    """订单"""
    # 请实现 __init__、summary()
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1:Book 和 Food 能正常实例化
    # 测试 2:price 为负时报错
    # 测试 3:cart1 + cart2 合并正确
    # 测试 4:len(cart) 返回件数
    # 测试 5:for item in cart 遍历
    # 测试 6:同 SKU 产品 == 为 True
    # 测试 7:set 去重正确
    # 测试 8:Order.summary() 正确
    pass
