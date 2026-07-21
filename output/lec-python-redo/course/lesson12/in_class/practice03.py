"""
[难度: ★★][所属知识点: 聚合函数][预计完成时间: 10 分钟]

题目:给定 a = np.array([[1,2,3],[4,5,6]]),
分别计算:
(1) 全部元素的和
(2) 全部元素的均值
(3) 全部元素的最大值
(4) 最大值的索引(argmax)
"""

if __name__ == "__main__":
    print("参考答案:")
    print('import numpy as np')
    print('a = np.array([[1, 2, 3], [4, 5, 6]])')
    print('')
    print('print(np.sum(a))     # 21')
    print('print(np.mean(a))    # 3.5')
    print('print(np.max(a))     # 6')
    print('print(np.argmax(a))  # 5(展平后索引)')
