"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 员工薪资系统综合]
[预计完成时间: 30 分钟]

题目描述:
综合本课全部知识点,实现员工薪资系统:
1. 基类 Employee:name、base_salary、pay()
2. 子类 Sales:新增 commission,重写 pay()
3. 子类 Manager:新增 bonus,重写 pay()
4. 用 super().__init__() 和 super().pay()

示例:
    >>> staff = [Employee("张三", 5000),
    ...          Sales("李四", 5000, 2000),
    ...          Manager("王五", 8000, 3000)]
    >>> [e.pay() for e in staff]
    [5000, 7000, 11000]
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    def pay(self):
        return self.base_salary

class Sales(Employee):
    pass  # 请实现

class Manager(Employee):
    pass  # 请实现

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1:Employee("张三", 5000).pay() == 5000
    # 测试 2:Sales("李四", 5000, 2000).pay() == 7000
    # 测试 3:Manager("王五", 8000, 3000).pay() == 11000
    # 测试 4:[e.pay() for e in staff] == [5000, 7000, 11000]
    pass
