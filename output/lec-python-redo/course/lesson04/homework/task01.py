"""
[难度: ★★★][所属知识点: 循环综合][预计完成时间: 15 分钟][类型: 选做]

题目:输入一个正整数,计算它是几位数,并输出各位数字之和。
如输入 1234,输出"4 位数,各位之和 = 10"。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('n = input("请输入正整数:")')
    print('print(f"{len(n)} 位数,各位之和 = {sum(int(d) for d in n)}")')
    print()
    print("或者用循环:")
    print('n = int(input("请输入正整数:")')
    print('count = 0; total = 0')
    print('while n > 0:')
    print('    total += n % 10')
    print('    n //= 10')
    print('    count += 1')
    print('print(f"{count} 位数,各位之和 = {total}")')
