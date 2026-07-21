"""
[难度: ⭐⭐]
[所属知识点: MRO 方法解析顺序]
[预计完成时间: 15 分钟]

题目描述:
定义三层继承体系 Animal → Mammal → Dog。
查看 Dog 的 __mro__,验证查找顺序。
创建 Dog 实例,验证 isinstance 判断结果。

示例:
    >>> print(Dog.__mro__)
    (<class '__main__.Dog'>, <class '__main__.Mammal'>,
     <class '__main__.Animal'>, <class 'object'>)
    >>> dog = Dog()
    >>> isinstance(dog, Animal)
    True
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Animal:
    pass

class Mammal(Animal):
    pass

class Dog(Mammal):
    pass

# print(Dog.__mro__)
# dog = Dog()
# print(isinstance(dog, Animal))
# print(isinstance(dog, Mammal))
# print(isinstance(dog, object))

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1:Dog.__mro__ 长度为 4
    # 测试 2:isinstance(Dog(), Animal) == True
    # 测试 3:isinstance(Dog(), str) == False
    pass
