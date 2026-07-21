"""
[难度: ⭐⭐]
[所属知识点: 方法重写 override]
[预计完成时间: 15 分钟]

题目描述:
定义 Product 基类,方法 shipping_cost() 返回 0。
子类 PhysicalProduct 新增 weight 属性,
重写 shipping_cost() = weight * 8。
子类 DigitalProduct 不重写,继承基类版本。
各创建一个实例,验证运费不同。

示例:
    >>> p = PhysicalProduct(10)
    >>> p.shipping_cost()
    80
    >>> d = DigitalProduct()
    >>> d.shipping_cost()
    0
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Product:
    def shipping_cost(self):
        return 0

class PhysicalProduct(Product):
    pass  # 请实现 __init__ 和重写 shipping_cost

# pp = PhysicalProduct(10)
# print(pp.shipping_cost())  # 期望 80
# dp = DigitalProduct()
# print(dp.shipping_cost())  # 期望 0

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1:PhysicalProduct(10).shipping_cost() == 80
    # 测试 2:DigitalProduct().shipping_cost() == 0
    # 测试 3:PhysicalProduct(0).shipping_cost() == 0 (边界)
    pass
