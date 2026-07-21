"""
[难度: ⭐⭐⭐]
[所属知识点: __repr__ 调试输出]
[类型: 选做]
[预计完成时间: 20 分钟]

题目描述:
为 Product 类实现 __repr__ 方法,
让 repr(product) 显示关键信息。
格式:Product(sku=..., name=..., price=...)

示例:
    >>> p = Product("A001", "矿泉水", 2.0)
    >>> repr(p)
    "Product(sku='A001', name='矿泉水', price=2.0)"
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Product:
    def __init__(self, sku, name, price):
        self.sku = sku
        self.name = name
        self.price = price
    # 请实现 __repr__

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1:repr(p) 包含 sku
    # 测试 2:repr(p) 包含 name
    # 测试 3:repr(p) 包含 price
    # 测试 4:列表中的 Product 显示 repr
    pass
