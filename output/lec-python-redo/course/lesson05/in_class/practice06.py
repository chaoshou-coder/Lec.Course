"""
[难度: ★★★][所属知识点: 综合(封装)][预计完成时间: 15 分钟]

题目:定义函数 is_even(n),判断 n 是否为偶数,返回 True/False。
再定义函数 filter_even(numbers),用 is_even 过滤列表中的偶数。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('def is_even(n):')
    print('    return n % 2 == 0')
    print()
    print('def filter_even(numbers):')
    print('    result = []')
    print('    for n in numbers:')
    print('        if is_even(n):')
    print('            result.append(n)')
    print('    return result')
    print()
    print('print(filter_even([1,2,3,4,5,6]))  # [2, 4, 6]')
