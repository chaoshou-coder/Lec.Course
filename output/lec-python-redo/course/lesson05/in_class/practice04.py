"""
[难度: ★★][所属知识点: return 与多值返回][预计完成时间: 10 分钟]

题目:定义函数 get_stats(numbers),返回一个列表的最小值、最大值、平均值。
用元组解包接收返回值。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('def get_stats(numbers):')
    print('    return min(numbers), max(numbers), sum(numbers)/len(numbers)')
    print()
    print('smallest, largest, avg = get_stats([3,1,4,1,5])')
    print('print(smallest, largest, avg)')
