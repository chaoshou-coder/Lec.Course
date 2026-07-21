"""
[难度: ★★★][所属知识点: 装饰器与 wraps][预计完成时间: 15 分钟]

题目:定义 log 装饰器,打印函数名和参数,
用 @functools.wraps 保留原函数信息。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('import functools')
    print('def log(func):')
    print('    @functools.wraps(func)')
    print('    def wrapper(*args, **kwargs):')
    print('        print(f"调用 {func.__name__}")')
    print('        return func(*args, **kwargs)')
    print('    return wrapper')
    print()
    print('@log')
    print('def greet(name):')
    print('    return f"你好, {name}"')
