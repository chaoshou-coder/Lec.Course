"""
[难度: ★][所属知识点: 自定义模块与包][预计完成时间: 8 分钟]

题目:假设有 mymath.py 定义了 add(a,b) 和 mul(a,b),在 main.py 中导入使用。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('# mymath.py')
    print('def add(a, b): return a + b')
    print('def mul(a, b): return a * b')
    print()
    print('# main.py')
    print('from mymath import add, mul')
    print('print(add(2, 3))   # 5')
    print('print(mul(2, 3))   # 6')
