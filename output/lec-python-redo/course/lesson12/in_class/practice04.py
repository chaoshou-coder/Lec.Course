"""
[难度: ★★★][所属知识点: axis 参数][预计完成时间: 12 分钟]

题目:给定 a = np.array([[1,2,3],[4,5,6]]),
分别计算:
(1) 沿 axis=0 求和(跨行,结果按列)
(2) 沿 axis=1 求和(跨列,结果按行)
(3) 沿 axis=0 求最大值
(4) 沿 axis=1 求均值
"""

if __name__ == "__main__":
    print("参考答案:")
    print('import numpy as np')
    print('a = np.array([[1, 2, 3], [4, 5, 6]])')
    print('')
    print('print(np.sum(a, axis=0))   # [5, 7, 9]')
    print('print(np.sum(a, axis=1))   # [6, 15]')
    print('print(np.max(a, axis=0))   # [4, 5, 6]')
    print('print(np.mean(a, axis=1))  # [2.0, 5.0]')
