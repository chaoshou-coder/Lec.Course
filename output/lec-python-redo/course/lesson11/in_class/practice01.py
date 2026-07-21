"""
[难度: ★][所属知识点: 数组创建][预计完成时间: 5 分钟]

题目:用 NumPy 创建以下数组:
(1) 一维数组 [10, 20, 30, 40]
(2) 长度为 5 的全零数组
(3) 0 到 8 步长为 2 的等差数列
(4) 0 到 1 之间均匀取 4 个点
"""

if __name__ == "__main__":
    print("参考答案:")
    print('import numpy as np')
    print('a = np.array([10, 20, 30, 40])')
    print('z = np.zeros(5)')
    print('r = np.arange(0, 10, 2)')
    print('l = np.linspace(0, 1, 4)')
