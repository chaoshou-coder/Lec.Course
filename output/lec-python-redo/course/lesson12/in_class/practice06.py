"""
[难度: ★★★][所属知识点: 文件读写][预计完成时间: 15 分钟]

题目:给定 a = np.array([[1,2,3],[4,5,6]]),
(1) 保存为 a.npy,然后加载回来
(2) 保存为 a.txt(逗号分隔,整数格式),然后加载回来
"""

if __name__ == "__main__":
    print("参考答案:")
    print('import numpy as np')
    print('a = np.array([[1, 2, 3], [4, 5, 6]])')
    print('')
    print('# (1) 二进制读写')
    print('np.save("a.npy", a)')
    print('b = np.load("a.npy")')
    print('print(b.shape)  # (2, 3)')
    print('')
    print('# (2) 文本读写')
    print('np.savetxt("a.txt", a, fmt="%d", delimiter=",")')
    print('c = np.loadtxt("a.txt", delimiter=",")')
    print('print(c)')
    print('# [[1. 2. 3.]')
    print('#  [4. 5. 6.]]')
