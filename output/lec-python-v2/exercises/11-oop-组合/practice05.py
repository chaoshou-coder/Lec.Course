"""
[难度: ⭐⭐⭐]
[所属知识点: __eq__ 同款判定]
[预计完成时间: 20 分钟]

题目描述:
为 Product 类实现 __eq__ 方法,
让两个 SKU 相同的产品 == 为 True。
要求:先检查类型,不匹配返回 NotImplemented。

示例:
    >>> p1 = Product("A001", "矿泉水", 2.0)
    >>> p2 = Product("A001", "矿泉水", 2.0)
    >>> p3 = Product("B002", "面包", 5.0)
    >>> p1 == p2
    True
    >>> p1 == p3
    False
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Product:
    def __init__(self, sku, name, price):
        self.sku = sku
        self.name = name
        self.price = price
    # 请实现 __eq__

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1:同 SKU 的 p1 == p2 为 True
    # 测试 2:不同 SKU 的 p1 == p3 为 False
    # 测试 3:p1 == "not a product" 为 False
    # 测试 4:p1 is p2 为 False(不同对象)
    pass
