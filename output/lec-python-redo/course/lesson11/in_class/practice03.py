"""
[难度: ★★][所属知识点: 向量化运算][预计完成时间: 10 分钟]

题目:给定 a = np.array([1,2,3,4,5]),
用向量化运算完成以下操作(不要用 for 循环):
(1) 每个元素加 10
(2) 每个元素平方
(3) 求每个元素的平方根
"""

if __name__ == "__main__":
    print("参考答案:")
    print('import numpy as np')
    print('a = np.array([1, 2, 3, 4, 5])')
    print('print(a + 10)        # [11 12 13 14 15]')
    print('print(a ** 2)        # [ 1  4  9 16 25]')
    print('print(np.sqrt(a))    # [1.   1.41 1.73 2.   2.24]')
