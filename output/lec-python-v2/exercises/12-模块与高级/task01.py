"""
[难度: ★★★][所属知识点: 装饰器 计时器][类型: 选做]
[预计完成时间: 15 分钟]

题目:写一个 @timer 装饰器,统计被装饰函数的执行时间,
打印 "<函数名> 耗时 x.xxxx 秒"。
用它装饰一个计算 1~n 整数和的函数,验证计时效果。

示例:
    slow_sum 耗时 0.0456 秒
    50000005000000
"""

import time
import functools

# TODO: 定义 timer 装饰器,用 @functools.wraps 保留元信息
# 提示: time.time() 获取当前时间
def timer(fn):
    pass

# TODO: 用 @timer 装饰 slow_sum 函数
# def slow_sum(n):
#     total = 0
#     for i in range(n + 1):
#         total += i
#     return total

if __name__ == '__main__':
    # 参考答案
    # def timer(fn):
    #     @functools.wraps(fn)
    #     def wrapper(*args, **kwargs):
    #         start = time.time()
    #         result = fn(*args, **kwargs)
    #         elapsed = time.time() - start
    #         print(f"{fn.__name__} 耗时 {elapsed:.4f} 秒")
    #         return result
    #     return wrapper
    #
    # @timer
    # def slow_sum(n):
    #     total = 0
    #     for i in range(n + 1):
    #         total += i
    #     return total
    print(slow_sum(10_000_000))
