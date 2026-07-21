"""
[难度: ★★★][所属知识点: 函数设计][预计完成时间: 15 分钟][类型: 选做]

题目:定义函数 is_prime(n),判断 n 是否为素数,返回 True/False。
素数:大于 1 且只能被 1 和自身整除的数。
测试:is_prime(7) → True, is_prime(10) → False, is_prime(1) → False。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('def is_prime(n):')
    print('    if n < 2:')
    print('        return False')
    print('    for i in range(2, int(n ** 0.5) + 1):')
    print('        if n % i == 0:')
    print('            return False')
    print('    return True')
    print()
    print('print(is_prime(7))   # True')
    print('print(is_prime(10))  # False')
    print('print(is_prime(1))   # False')
