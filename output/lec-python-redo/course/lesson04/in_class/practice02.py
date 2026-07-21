"""
[难度: ★][所属知识点: break 与 continue][预计完成时间: 8 分钟]

题目:用 while 循环打印 1 到 10,但跳过 5(用 continue)。
再用 break 在 7 时退出循环。
"""

if __name__ == "__main__":
    print("参考答案(跳 5):")
    print('i = 0')
    print('while i < 10:')
    print('    i += 1')
    print('    if i == 5:')
    print('        continue')
    print('    print(i)')
    print()
    print("参考答案(到 7 退出):")
    print('i = 0')
    print('while i < 10:')
    print('    i += 1')
    print('    if i == 7:')
    print('        break')
    print('    print(i)')
