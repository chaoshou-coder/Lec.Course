"""
[难度: ★★★][所属知识点: 逻辑运算综合][预计完成时间: 20 分钟][类型: 选做]

题目:输入一个年份和月份,输出该月天数。这次要考虑闰年:
闰年 2 月 29 天,平年 2 月 28 天。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('year = int(input("年份:")')
    print('month = int(input("月份:")')
    print('is_leap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0')
    print('if month in [1,3,5,7,8,10,12]:')
    print('    print("31 天")')
    print('elif month in [4,6,9,11]:')
    print('    print("30 天")')
    print('elif month == 2:')
    print('    print("29 天" if is_leap else "28 天")')
