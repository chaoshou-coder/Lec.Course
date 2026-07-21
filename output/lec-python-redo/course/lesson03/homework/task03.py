"""
[难度: ★★★★][所属知识点: 综合应用][预计完成时间: 30 分钟][类型: 选做]

题目:计算器程序:输入两个数字和一个运算符(+ - * /),输出计算结果。
如果运算符不是这四个,输出"无效运算符"。如果除数为 0,输出"除数不能为 0"。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('a = float(input("第一个数:")')
    print('op = input("运算符:")')
    print('b = float(input("第二个数:")')
    print('if op == "+":')
    print('    print(a + b)')
    print('elif op == "-":')
    print('    print(a - b)')
    print('elif op == "*":')
    print('    print(a * b)')
    print('elif op == "/":')
    print('    if b == 0:')
    print('        print("除数不能为 0")')
    print('    else:')
    print('        print(a / b)')
    print('else:')
    print('    print("无效运算符")')
