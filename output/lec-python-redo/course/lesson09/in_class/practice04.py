"""
[难度: ★★][所属知识点: yield from][预计完成时间: 10 分钟]

题目:用 yield from 定义一个生成器,合并 range(3) 和 "abc"。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('def merge():')
    print('    yield from range(3)')
    print('    yield from "abc"')
    print()
    print('print(list(merge()))  # [0, 1, 2, "a", "b", "c"]')
