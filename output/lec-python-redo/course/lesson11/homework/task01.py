"""
[难度: ★★★][所属知识点: 向量化 vs for 循环][预计完成时间: 15 分钟][类型: 选做]

题目:将下面的 for 循环代码改写成 NumPy 向量化形式。

    nums = list(range(100))
    result = []
    for n in nums:
        result.append(n ** 2 + 2 * n + 1)

要求:创建等价的 NumPy 数组运算。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('import numpy as np')
    print('n = np.arange(100)')
    print('result = n ** 2 + 2 * n + 1')
    print('# 或者完全平方公式:')
    print('result = (n + 1) ** 2')
