"""
[难度: ⭐⭐⭐⭐⭐]
[所属知识点: 综合项目:动物园模拟器]
[预计完成时间: 45 分钟]

题目描述:
设计一个小型动物园模拟器,练习继承体系:
1. 基类 Animal:name、sound() 方法(返回字符串)
2. 子类 Dog:Cat:Duck,各自重写 sound()
3. 子类 FlyingAnimal(能飞)和 SwimmingAnimal(能游)
4. 用组合或多重继承让 Duck 既会飞又会游(可选)
5. 函数 zoo_sound(animals) 让所有动物发声

示例:
    >>> zoo = [Dog("旺财"), Cat("咪咪"), Duck("唐老鸭")]
    >>> zoo_sound(zoo)
    旺财: 汪汪叫
    咪咪: 喵喵叫
    唐老鸭: 嘎嘎叫
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1:每个 Animal 的 sound() 返回正确叫声
    # 测试 2:zoo_sound(zoo) 输出所有动物叫声
    # 测试 3:isinstance(Dog("x"), Animal) == True
    # 测试 4:zoo_sound([]) 不报错(空列表)
    pass
