"""
[难度: ★★★★][所属知识点: 自定义上下文管理器][预计完成时间: 20 分钟]

题目:写一个 Timer 类作为上下文管理器,
统计 with 代码块的执行时间。
要求:__enter__ 记录开始时间,__exit__ 计算并打印耗时。

用法:
    with Timer():
        total = sum(range(1000000))

输出:
    代码块耗时 0.0123 秒
"""

import time

# TODO: 定义 Timer 类,实现 __enter__ 和 __exit__
class Timer:
    pass

if __name__ == '__main__':
    # 参考答案
    # class Timer:
    #     def __enter__(self):
    #         self.start = time.time()
    #         return self
    #
    #     def __exit__(self, exc_type, exc_val, exc_tb):
    #         elapsed = time.time() - self.start
    #         print(f"代码块耗时 {elapsed:.4f} 秒")
    #         return False  # 不吞掉异常
    with Timer():
        total = sum(range(1000000))
        print(f"计算结果: {total}")
