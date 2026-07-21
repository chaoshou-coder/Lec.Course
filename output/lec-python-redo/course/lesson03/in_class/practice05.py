"""
[难度: ★★★][所属知识点: 三元表达式与嵌套][预计完成时间: 12 分钟]

题目:输入一个整数,用三元表达式判断奇偶性,输出"奇数"或"偶数"。
再用 if 嵌套判断这个数是否为正数。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('n = int(input("请输入整数:")')
    print('print("奇数" if n % 2 != 0 else "偶数")')
    print('if n > 0:')
    print('    if n % 2 == 0:')
    print('        print("正偶数")')
    print('    else:')
    print('        print("正奇数")')
