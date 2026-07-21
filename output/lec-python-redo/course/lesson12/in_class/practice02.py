"""
[难度: ★★][所属知识点: 线性代数(转置/行列式/逆)][预计完成时间: 10 分钟]

题目:给定 a = np.array([[1,2],[3,4]]),
(1) 计算 a 的转置
(2) 计算 a 的行列式
(3) 计算 a 的逆矩阵
"""

if __name__ == "__main__":
    print("参考答案:")
    print('import numpy as np')
    print('a = np.array([[1, 2], [3, 4]])')
    print('')
    print('# (1) 转置')
    print('print(a.T)')
    print('# [[1 3]')
    print('#  [2 4]]')
    print('')
    print('# (2) 行列式')
    print('print(np.linalg.det(a))  # -2.0')
    print('')
    print('# (3) 逆矩阵')
    print('print(np.linalg.inv(a))')
    print('# [[-2.   1. ]')
    print('#  [ 1.5 -0.5]]')
