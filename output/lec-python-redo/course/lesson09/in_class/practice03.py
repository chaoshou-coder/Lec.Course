"""
[难度: ★★][所属知识点: 生成器 yield][预计完成时间: 10 分钟]

题目:定义一个生成器 gen_counter(n),从 1 到 n 依次产生数字。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('def gen_counter(n):')
    print('    for i in range(1, n + 1):')
    print('        yield i')
    print()
    print('for num in gen_counter(5):')
    print('    print(num)  # 1 2 3 4 5')
