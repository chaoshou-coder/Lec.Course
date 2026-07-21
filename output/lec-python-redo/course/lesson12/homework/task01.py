"""
[难度: ★★★][所属知识点: 矩阵运算综合][预计完成时间: 20 分钟][类型: 选做]

题目:给定 a = np.array([[1,2],[3,4]]),
b = np.array([[5,6],[7,8]]),
(1) 计算 a @ b 和 b @ a,它们相等吗?
(2) 计算 a 的逆矩阵,验证 a @ inv(a) = 单位矩阵
(3) 计算 trace(a)(主对角线元素之和)
"""

if __name__ == "__main__":
    print("参考答案:")
    print('import numpy as np')
    print('a = np.array([[1, 2], [3, 4]])')
    print('b = np.array([[5, 6], [7, 8]])')
    print('')
    print('# (1) a @ b != b @ a(矩阵乘法不满足交换律)')
    print('print(a @ b)  # [[19 22] [43 50]]')
    print('print(b @ a)  # [[23 34] [31 46]]')
    print('')
    print('# (2) 逆矩阵验证')
    print('a_inv = np.linalg.inv(a)')
    print('print(a @ a_inv)  # ≈ 单位矩阵')
    print('')
    print('# (3) 主对角线之和 trace')
    print('print(np.trace(a))  # 5(1+4)')
