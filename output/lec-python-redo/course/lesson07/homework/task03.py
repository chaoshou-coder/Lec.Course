"""
[难度: ★★★★][所属知识点: 异常处理综合][预计完成时间: 30 分钟][类型: 选做]

题目:实现一个安全的数字计算器,能连续运行,
捕获 ValueError/ZeroDivisionError/文件读取错误。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('while True:')
    print('    try:')
    print('        expr = input("输入表达式(quit=退出):")')
    print('        if expr == "quit": break')
    print('        a, op, b = expr.split()')
    print('        a, b = float(a), float(b)')
    print('        result = eval(f"{a}{op}{b}")')
    print('        print(f"结果: {result}")')
    print('    except ValueError:')
    print('        print("输入格式错误")')
    print('    except ZeroDivisionError:')
    print('        print("除数不能为 0")')
    print('    except Exception as e:')
    print('        print(f"未知错误: {e}")')
