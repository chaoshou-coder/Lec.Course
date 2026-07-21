"""
[难度: ★★★][所属知识点: 随机数生成][预计完成时间: 12 分钟]

题目:设种子为 0,生成:
(1) 3 个 [0,1) 均匀分布随机数
(2) 2×2 的标准正态分布随机矩阵
(3) 5 个 [1,6) 的整数随机数(模拟掷骰子)
"""

if __name__ == "__main__":
    print("参考答案:")
    print('import numpy as np')
    print('np.random.seed(0)')
    print('')
    print('# (1) 均匀分布')
    print('print(np.random.rand(3))')
    print('')
    print('# (2) 标准正态分布')
    print('print(np.random.randn(2, 2))')
    print('')
    print('# (3) 整数随机')
    print('print(np.random.randint(1, 6, size=5))')
