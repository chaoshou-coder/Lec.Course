"""
[难度: ★★][所属知识点: 生成器表达式][预计完成时间: 10 分钟]

题目:用生成器表达式计算 1~20 所有奇数的平方和,
打印结果。

示例:
    >>> 参见参考答案输出
"""

import sys

# TODO: 用生成器表达式计算奇数的平方和
# 提示: sum(x*x for x in range(1, 21) if ...)
pass

if __name__ == '__main__':
    # 参考答案
    total = sum(x * x for x in range(1, 21) if x % 2 == 1)
    print(total)         # 1330

    # 对比内存:生成器 vs 列表推导
    gen = (x * x for x in range(1000))
    lst = [x * x for x in range(1000)]
    print(sys.getsizeof(gen))   # 约 200 字节
    print(sys.getsizeof(lst))   # 约 8856 字节
