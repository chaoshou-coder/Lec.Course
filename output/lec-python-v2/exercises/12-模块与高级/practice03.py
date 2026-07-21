"""
[难度: ★★][所属知识点: 生成器 yield][预计完成时间: 10 分钟]

题目:写一个生成器函数 count_up_to(n),
从 1 开始逐个产出整数,直到 n(包含 n)。
用 for 循环遍历打印每个值。

示例:
    >>> for v in count_up_to(5):
    ...     print(v)
    1
    2
    3
    4
    5
"""

# TODO: 定义生成器函数 count_up_to(n),用 yield 产出
def count_up_to(n):
    pass

if __name__ == '__main__':
    # 参考答案
    # def count_up_to(n):
    #     i = 1
    #     while i <= n:
    #         yield i
    #         i += 1
    for v in count_up_to(5):
        print(v)        # 1 2 3 4 5
