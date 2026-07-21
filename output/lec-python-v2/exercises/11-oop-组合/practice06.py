"""
[难度: ⭐⭐⭐]
[所属知识点: __hash__ 支持 set 去重]
[预计完成时间: 20 分钟]

题目描述:
基于 practice05 的 Product 类,
添加 __hash__ 方法,让 Product 能放入 set。
要求:相等的对象有相等的哈希值。

示例:
    >>> p1 = Product("A001", "矿泉水", 2.0)
    >>> p2 = Product("A001", "矿泉水", 2.0)
    >>> p3 = Product("B002", "面包", 5.0)
    >>> len({p1, p2, p3})
    2
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Product:
    def __init__(self, sku, name, price):
        self.sku = sku
        self.name = name
        self.price = price

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.sku == other.sku
    # 请实现 __hash__

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1:{p1, p2, p3} 长度为 2
    # 测试 2:hash(p1) == hash(p2)
    # 测试 3:p1 能作为 dict 的键
    pass
