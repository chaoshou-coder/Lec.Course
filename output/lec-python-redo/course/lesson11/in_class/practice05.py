"""
[难度: ★★★][所属知识点: 布尔索引][预计完成时间: 12 分钟]

题目:给定 a = np.array([3, 8, 1, 6, 9, 2, 7]),
用布尔索引完成:
(1) 取出所有大于 5 的元素
(2) 取出所有偶数
(3) 取出 3 到 7 之间(含)的元素
"""

if __name__ == "__main__":
    print("参考答案:")
    print('import numpy as np')
    print('a = np.array([3, 8, 1, 6, 9, 2, 7])')
    print('')
    print('# (1) 大于 5')
    print('print(a[a > 5])  # [8 6 9 7]')
    print('')
    print('# (2) 偶数')
    print('print(a[a % 2 == 0])  # [8 6 2]')
    print('')
    print('# (3) 3 到 7 之间')
    print('print(a[(a >= 3) & (a <= 7)])  # [3 6 7]')
