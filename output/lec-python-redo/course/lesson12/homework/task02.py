"""
[难度: ★★★][所属知识点: 随机数应用][预计完成时间: 20 分钟][类型: 选做]

题目:用蒙特卡洛方法估算 π 值。
原理:在单位正方形内随机投点,落在单位圆内的比例 ≈ π/4。
步骤:
(1) 生成 10000 个 [0,1) 的随机点(x,y)
(2) 计算每个点到原点的距离
(3) 统计距离 <= 1 的点数
(4) π ≈ 4 * (圆内点数 / 总点数)
"""

if __name__ == "__main__":
    print("参考答案:")
    print('import numpy as np')
    print('np.random.seed(42)')
    print('n = 10000')
    print('x = np.random.rand(n)')
    print('y = np.random.rand(n)')
    print('dist = np.sqrt(x ** 2 + y ** 2)')
    print('inside = np.sum(dist <= 1)')
    print('pi = 4 * inside / n')
    print('print(f"π ≈ {pi:.4f}")  # ≈ 3.14')
