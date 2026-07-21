"""
[难度: ⭐⭐⭐]
[所属知识点: __iter__ 遍历商品]
[预计完成时间: 20 分钟]

题目描述:
为 Cart 类实现 __iter__ 方法,
让 for item in cart 能遍历商品。
使用 return iter(self.items) 方式。

示例:
    >>> c = Cart(["苹果", "香蕉"])
    >>> for item in c:
    ...     print(item)
    苹果
    香蕉
    >>> list(c)
    ['苹果', '香蕉']
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Cart:
    def __init__(self, items=None):
        self.items = items if items else []
    # 请实现 __iter__

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1:for item in cart 能遍历
    # 测试 2:list(cart) 返回 items 列表
    # 测试 3:空购物车遍历不报错
    pass
