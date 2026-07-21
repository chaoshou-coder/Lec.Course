"""
[难度: ★★★★][所属知识点: 综合(线性方程组)][预计完成时间: 30 分钟][类型: 选做]

题目:用 NumPy 解二元一次方程组:
    2x + y = 5
    x + 3y = 10

方法:写成矩阵形式 AX = B,则 X = inv(A) @ B
(1) 构造系数矩阵 A 和常数向量 B
(2) 计算 A 的逆矩阵
(3) 求解 X
(4) 验证 A @ X = B
"""

if __name__ == "__main__":
    print("参考答案:")
    print('import numpy as np')
    print('A = np.array([[2, 1],')
    print('              [1, 3]])')
    print('B = np.array([5, 10])')
    print('')
    print('# (2) 逆矩阵')
    print('A_inv = np.linalg.inv(A)')
    print('')
    print('# (3) 求解')
    print('X = A_inv @ B')
    print('print(X)  # [1. 3.] → x=1, y=3')
    print('')
    print('# (4) 验证')
    print('print(A @ X)  # [5. 10.]')
    print('(等价:np.linalg.solve(A, B)更稳定)')
