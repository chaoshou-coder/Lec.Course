"""
[难度: ★★★][所属知识点: @property setter][预计完成时间: 15 分钟]

题目:给 Student 类添加 @property score 和 @score.setter,
保护成绩在 0~100 之间,非法时打印 "成绩必须在 0-100 之间"。
创建学生,尝试赋值为 150,再打印 score。
"""

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score  # 走 setter

    # TODO: 添加 @property score
    # TODO: 添加 @score.setter
    pass

if __name__ == '__main__':
    # 参考答案
    class Student:
        def __init__(self, name, score):
            self.name = name
            self.score = score

        @property
        def score(self):
            return self._score

        @score.setter
        def score(self, value):
            if value < 0 or value > 100:
                print("成绩必须在 0-100 之间")
                return
            self._score = value

    s = Student("小明", 85)
    s.score = 150  # 成绩必须在 0-100 之间
    print(s.score)  # 85(没变)
