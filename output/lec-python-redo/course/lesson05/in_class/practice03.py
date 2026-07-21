"""
[难度: ★★][所属知识点: 参数详解][预计完成时间: 10 分钟]

题目:定义函数 power(base, exp=2),计算 base 的 exp 次方,
exp 默认值为 2(即默认平方)。用关键字参数调用 power(exp=3, base=2)。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('def power(base, exp=2):')
    print('    return base ** exp')
    print()
    print('print(power(3))          # 9(平方)')
    print('print(power(2, 3))       # 8')
    print('print(power(exp=3, base=2))  # 8(关键字参数)')
