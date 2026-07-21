"""
[难度: ⭐⭐]
[所属知识点: __len__ 返回件数]
[预计完成时间: 15 分钟]

题目描述:
为 Cart 类实现 __len__ 方法,
让 len(cart) 返回商品件数。

示例:
    >>> c = Cart(["苹果", "香蕉", "牛奶"])
    >>> len(c)
    3
    >>> len(Cart())
    0
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Cart:
    def __init__(self, items=None):
        self.items = items if items else []
    # 请实现 __len__

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1:len(Cart(["a", "b", "c"])) == 3
    # 测试 2:len(Cart()) == 0
    # 测试 3:bool(Cart(["a"])) == True
    # 测试 4:bool(Cart()) == False
    pass
