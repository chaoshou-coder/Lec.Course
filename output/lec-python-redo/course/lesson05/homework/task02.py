"""
[难度: ★★★][所属知识点: 递归入门][预计完成时间: 20 分钟][类型: 选做]

题目:定义递归函数 factorial(n),计算 n 的阶乘。
阶乘:n! = n × (n-1) × ... × 1, 0! = 1。
提示:递归 = 函数调用自己,必须有终止条件。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('def factorial(n):')
    print('    if n <= 1:')
    print('        return 1')
    print('    return n * factorial(n - 1)')
    print()
    print('print(factorial(5))  # 120')
    print('print(factorial(0))  # 1')
    print()
    print("递归思路:")
    print("  5! = 5 × 4!")
    print("  4! = 4 × 3!")
    print("  ...")
    print("  1! = 1(终止条件)")
