"""
[难度: ★★★][所属知识点: 上下文管理器][预计完成时间: 12 分钟]

题目:定义 Timer 上下文管理器,用 with 计算代码块执行时间。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('import time')
    print('class Timer:')
    print('    def __enter__(self):')
    print('        self.start = time.time()')
    print('        return self')
    print('    def __exit__(self, *args):')
    print('        print(f"耗时 {time.time()-self.start:.3f}s")')
    print()
    print('with Timer():')
    print('    time.sleep(0.1)')
