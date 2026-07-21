"""
[难度: ⭐⭐]
[所属知识点: 组合 vs 继承]
[预计完成时间: 15 分钟]

题目描述:
用组合方式设计 Order 类:
1. Address 类:city、detail
2. Cart 类:items 列表
3. Order 类:组合 addr 和 cart(不继承)
4. Order 的 summary() 方法返回订单摘要

示例:
    >>> addr = Address("北京", "朝阳区")
    >>> cart = Cart()
    >>> cart.items = ["书", "笔"]
    >>> order = Order(addr, cart)
    >>> order.summary()
    送到北京(朝阳区),2件商品
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Address:
    def __init__(self, city, detail):
        self.city = city
        self.detail = detail

class Cart:
    def __init__(self):
        self.items = []

class Order:
    pass  # 请实现 __init__ 和 summary

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1:Order 能访问 addr.city
    # 测试 2:Order 能访问 cart.items
    # 测试 3:summary() 返回正确字符串
    pass
