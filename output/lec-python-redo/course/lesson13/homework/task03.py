"""
[难度: ★★★★][所属知识点: loc/iloc 综合][预计完成时间: 30 分钟][类型: 选做]

题目:给定 DataFrame df(列: 姓名/年龄/成绩,索引 a/b/c/d/e),
完成:
(1) 用 loc 取 "b" 到 "d" 的行
(2) 用 iloc 取第 1 到第 3 的行
(3) 用 loc 取 "a" 到 "c" 的行,但只取"姓名"和"成绩"列
(4) 用 iloc 取第 0 到第 2 的行,但只取第 0 和第 2 列
"""

if __name__ == "__main__":
    print("参考答案:")
    print('import pandas as pd')
    print('df = pd.DataFrame({')
    print('    "姓名": ["Alice", "Bob", "Charlie", "David", "Eve"],')
    print('    "年龄": [25, 30, 35, 28, 22],')
    print('    "成绩": [88.5, 92.0, 78.5, 95.0, 85.0],')
    print('}, index=["a", "b", "c", "d", "e"])')
    print('')
    print('# (1) loc 取 "b" 到 "d"(含末尾)')
    print('print(df.loc["b":"d"])')
    print('')
    print('# (2) iloc 取第 1 到第 3(不含 3)')
    print('print(df.iloc[1:3])')
    print('')
    print('# (3) loc 行 + 列')
    print('print(df.loc["a":"c", ["姓名", "成绩"]])')
    print('')
    print('# (4) iloc 行 + 列')
    print('print(df.iloc[0:2, [0, 2]])')
