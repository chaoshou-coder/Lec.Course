"""
[难度: ★★][所属知识点: NumPy 数组创建][预计完成时间: 10 分钟]

题目:用 np.arange 创建 0~11 的一维数组,
reshape 为 3×4 的二维数组,
打印它的 shape、dtype 和 ndim。

示例:
    [[ 0  1  2  3]
     [ 4  5  6  7]
     [ 8  9 10 11]]
    (3, 4)
    int64
    2
"""

import numpy as np

# TODO: 创建 0~11 的一维数组,reshape 为 3×4
# TODO: 打印数组、shape、dtype、ndim
pass

if __name__ == '__main__':
    # 参考答案
    a = np.arange(12)
    b = a.reshape(3, 4)
    print(b)
    print(b.shape)    # (3, 4)
    print(b.dtype)    # int64
    print(b.ndim)     # 2
