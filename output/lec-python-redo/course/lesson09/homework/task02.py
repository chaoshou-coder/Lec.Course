"""
[难度: ★★★][所属知识点: 装饰器综合][预计完成时间: 20 分钟][类型: 选做]

题目:定义 retry 装饰器,函数失败时自动重试 3 次,
每次间隔 1 秒(用 time.sleep)。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('import time')
    print('import functools')
    print('def retry(times=3, delay=1):')
    print('    def decorator(func):')
    print('        @functools.wraps(func)')
    print('        def wrapper(*args, **kwargs):')
    print('            for i in range(times):')
    print('                try: return func(*args, **kwargs)')
    print('                except Exception as e:')
    print('                    if i == times-1: raise')
    print('                    time.sleep(delay)')
    print('        return wrapper')
    print('    return decorator')
