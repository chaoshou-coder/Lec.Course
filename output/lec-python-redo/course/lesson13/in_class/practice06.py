"""
[难度: ★★★][所属知识点: 行选择(loc/iloc)][预计完成时间: 15 分钟]

题目:给定 DataFrame df(列: 姓名/年龄/成绩,索引 a/b/c),
(1) 用 loc 取索引为 "b" 的行
(2) 用 iloc 取第 2 行
(3) 用 loc 取 "a" 到 "b" 的行切片
(4) 用 iloc 取第 0 到第 1 的行切片
"""

if __name__ == "__main__":
    print("参考答案:")
    print('import pandas as pd')
    print('df = pd.DataFrame({')
    print('    "姓名": ["Alice", "Bob", "Charlie"],')
    print('    "年龄": [25, 30, 35],')
    print('    "成绩": [88.5, 92.0, 78.5],')
    print('}, index=["a", "b", "c"])')
    print('')
    print('# (1) loc 取索引 "b"')
    print('print(df.loc["b"])')
    print('')
    print('# (2) iloc 取第 2 行')
    print('print(df.iloc[1])')
    print('')
    print('# (3) loc 切片(含末尾)')
    print('print(df.loc["a":"b"])')
    print('')
    print('# (4) iloc 切片(不含末尾)')
    print('print(df.iloc[0:2])')
