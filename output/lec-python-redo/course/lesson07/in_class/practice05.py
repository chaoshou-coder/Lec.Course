"""
[难度: ★★★][所属知识点: try/except 基础][预计完成时间: 12 分钟]

题目:输入两个整数,计算商。用 try/except 处理除零错误和输入错误。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('try:')
    print('    a = int(input("被除数:"))')
    print('    b = int(input("除数:"))')
    print('    print(a / b)')
    print('except ValueError:')
    print('    print("请输入整数")')
    print('except ZeroDivisionError:')
    print('    print("除数不能为 0")')
