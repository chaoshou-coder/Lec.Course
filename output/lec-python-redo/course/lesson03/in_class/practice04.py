"""
[难度: ★★][所属知识点: 逻辑运算][预计完成时间: 10 分钟]

题目:输入年份和月份,判断该月有多少天(先不考虑闰年)。
提示:1/3/5/7/8/10/12 月 31 天,4/6/9/11 月 30 天,2 月 28 天。
用 and/or 组合条件。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('month = int(input("月份:")')
    print('if month in [1,3,5,7,8,10,12]:')
    print('    print("31 天")')
    print('elif month in [4,6,9,11]:')
    print('    print("30 天")')
    print('elif month == 2:')
    print('    print("28 天")')
    print('else:')
    print('    print("月份无效")')
