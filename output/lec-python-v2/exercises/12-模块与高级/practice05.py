"""
[难度: ★★★][所属知识点: 装饰器 @decorator][预计完成时间: 15 分钟]

题目:写一个 @log 装饰器,每次调用被装饰函数时,
打印 "调用 <函数名>,参数=<args>"。
用它装饰 add(a, b) 函数,调用 add(2, 3) 验证。

示例:
    调用 add,参数=(2, 3)
    5
"""

import functools

# TODO: 定义 log 装饰器,用 @functools.wraps 保留元信息
def log(fn):
    pass

# TODO: 用 @log 装饰 add 函数
# def add(a, b):
#     return a + b

if __name__ == '__main__':
    # 参考答案
    # def log(fn):
    #     @functools.wraps(fn)
    #     def wrapper(*args, **kwargs):
    #         print(f"调用 {fn.__name__},参数={args}")
    #         return fn(*args, **kwargs)
    #     return wrapper
    #
    # @log
    # def add(a, b):
    #     return a + b
    print(add(2, 3))    # 先打印日志,再输出 5
