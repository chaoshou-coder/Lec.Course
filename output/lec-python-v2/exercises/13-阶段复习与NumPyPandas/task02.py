"""
[难度: ★★★][所属知识点: NumPy 统计][预计完成时间: 15 分钟]

题目:生成 1000 个 N(50, 10) 正态分布随机数,
1. 计算均值 mean 和标准差 std
2. 计算最大值和最小值
3. 用布尔索引统计 >= 60 的个数

提示:np.random.normal(loc, scale, size)

示例(接近值):
    均值 ≈ 50.x
    标准差 ≈ 10.x
    最大值 ≈ 80.x
    最小值 ≈ 20.x
    >= 60 的个数 ≈ 158
"""

import numpy as np

# TODO: 设置随机种子 np.random.seed(42),生成 1000 个 N(50,10)
# TODO: 计算 mean / std / max / min
# TODO: 统计 >= 60 的个数
pass

if __name__ == '__main__':
    # 参考答案
    np.random.seed(42)
    data = np.random.normal(50, 10, 1000)
    print(f"均值: {data.mean():.2f}")
    print(f"标准差: {data.std():.2f}")
    print(f"最大值: {data.max():.2f}")
    print(f"最小值: {data.min():.2f}")
    print(f">= 60 的个数: {(data >= 60).sum()}")
