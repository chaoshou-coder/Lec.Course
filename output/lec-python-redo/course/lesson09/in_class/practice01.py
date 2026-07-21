"""
[难度: ★][所属知识点: 三种 import][预计完成时间: 5 分钟]

题目:分别用三种方式导入 math 模块的 sqrt 函数,计算 16 的平方根。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('# 方式1')
    print('import math')
    print('print(math.sqrt(16))')
    print()
    print('# 方式2')
    print('from math import sqrt')
    print('print(sqrt(16))')
    print()
    print('# 方式3')
    print('from math import sqrt as my_sqrt')
    print('print(my_sqrt(16))')
