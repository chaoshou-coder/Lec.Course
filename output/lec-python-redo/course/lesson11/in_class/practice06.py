"""
[难度: ★★★][所属知识点: reshape + 统计函数][预计完成时间: 15 分钟]

题目:创建 0 到 11 的数组,reshape 成 3 行 4 列,
然后计算:
(1) 全部元素的均值
(2) 全部元素的和
(3) 全部元素的标准差
"""

if __name__ == "__main__":
    print("参考答案:")
    print('import numpy as np')
    print('a = np.arange(12).reshape(3, 4)')
    print('print(a)')
    print('# [[ 0  1  2  3]')
    print('#  [ 4  5  6  7]')
    print('#  [ 8  9 10 11]]')
    print('')
    print('print(np.mean(a))  # 5.5')
    print('print(np.sum(a))   # 66')
    print('print(np.std(a))   # 3.45')
