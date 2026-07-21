"""
[难度: ★][所属知识点: 函数四种形式][预计完成时间: 8 分钟]

题目:分别写一个:(1) 无参无返:打印 5 行星号
(2) 有参无返:打印 n 行星号 (3) 无参有返:返回随机数 1-10
(4) 有参有返:返回两数之和。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('def print_stars():')
    print('    print("*" * 5)')
    print()
    print('def print_n_stars(n):')
    print('    print("*" * n)')
    print()
    print('import random')
    print('def get_random():')
    print('    return random.randint(1, 10)')
    print()
    print('def add(a, b):')
    print('    return a + b')
