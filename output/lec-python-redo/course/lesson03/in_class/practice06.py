"""
[难度: ★★★][所属知识点: 综合(BMI/闰年)][预计完成时间: 15 分钟]

题目:输入一个年份,判断是否为闰年。
闰年规则:能被 4 整除但不能被 100 整除,或者能被 400 整除。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('year = int(input("年份:")')
    print('if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:')
    print('    print(f"{year} 是闰年")')
    print('else:')
    print('    print(f"{year} 是平年")')
