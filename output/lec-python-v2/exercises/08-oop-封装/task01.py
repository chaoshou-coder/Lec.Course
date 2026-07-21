"""
[难度: ★★★][所属知识点: __str__ 魔术方法][预计完成时间: 15 分钟][类型: 选做]

题目:为 Student 类添加 __str__ 方法,
返回 "Student(name=XXX, score=XXX)"。
创建学生,用 print 打印它。
"""

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # TODO: 补全 __str__
    pass

if __name__ == '__main__':
    # 参考答案
    class Student:
        def __init__(self, name, score):
            self.name = name
            self.score = score

        def __str__(self):
            return f"Student(name={self.name}, score={self.score})"

    s = Student("小明", 85)
    print(s)  # Student(name=小明, score=85)
