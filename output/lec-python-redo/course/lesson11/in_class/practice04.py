"""
[难度: ★★][所属知识点: 广播][预计完成时间: 10 分钟]

题目:给定二维数组 a = np.array([[1,2,3],[4,5,6]]),
用广播完成:
(1) 每个元素加 100(标量广播)
(2) 每列分别加 [10, 20, 30](一维广播到二维)
"""

if __name__ == "__main__":
    print("参考答案:")
    print('import numpy as np')
    print('a = np.array([[1, 2, 3],')
    print('              [4, 5, 6]])')
    print('')
    print('# (1) 标量广播')
    print('print(a + 100)')
    print('# [[101 102 103]')
    print('#  [104 105 106]]')
    print('')
    print('# (2) 一维广播')
    print('b = np.array([10, 20, 30])')
    print('print(a + b)')
    print('# [[11 22 33]')
    print('#  [14 25 36]]')
