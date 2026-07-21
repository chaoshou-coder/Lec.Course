"""
[难度: ⭐⭐⭐]
[所属知识点: super().方法() 保留并扩展]
[预计完成时间: 20 分钟]

题目描述:
定义 Employee 基类,属性 name 和 base,
方法 pay() 返回 base。
子类 Manager 新增 bonus 属性,
重写 pay(),用 super().pay() 保留父类逻辑,
再加上 bonus。

示例:
    >>> m = Manager("李四", 8000, 3000)
    >>> m.pay()
    11000
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Employee:
    def __init__(self, name, base):
        self.name = name
        self.base = base
    def pay(self):
        return self.base

class Manager(Employee):
    pass  # 请实现 __init__ 和 pay(用 super().pay() + bonus)

# m = Manager("李四", 8000, 3000)
# print(m.pay())  # 期望 11000

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1:Manager("李四", 8000, 3000).pay() == 11000
    # 测试 2:Manager("a", 0, 0).pay() == 0 (边界)
    # 测试 3:普通 Employee("a", 5000).pay() == 5000
    pass
