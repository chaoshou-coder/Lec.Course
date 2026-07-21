"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 组合设计:订单系统]
[预计完成时间: 35 分钟]

题目描述:
用组合方式设计订单系统:
1. Product:sku、name、price、__eq__、__hash__、__repr__
2. Cart:items 列表、__add__、__len__、__iter__
3. Address:city、detail
4. Order:组合 addr 和 cart,summary() 方法

示例:
    >>> p1 = Product("A001", "书", 59.8)
    >>> p2 = Product("A002", "笔", 5.0)
    >>> cart = Cart([p1, p2])
    >>> addr = Address("北京", "朝阳区")
    >>> order = Order(addr, cart)
    >>> order.summary()
    送到北京(朝阳区),2件商品
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1:Order.summary() 正确
    # 测试 2:len(cart) 返回件数
    # 测试 3:cart1 + cart2 合并
    # 测试 4:同 SKU 产品 == 为 True
    pass
