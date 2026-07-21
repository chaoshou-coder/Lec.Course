"""
[难度: ★★★][所属知识点: 列选择][预计完成时间: 10 分钟]

题目:给定 DataFrame df(列: 姓名/年龄/成绩,3 条记录),
(1) 取出"姓名"列(返回 Series)
(2) 取出"姓名"和"成绩"两列(返回 DataFrame)
(3) 查看(1)和(2)的类型,确认区别
"""

if __name__ == "__main__":
    print("参考答案:")
    print('import pandas as pd')
    print('df = pd.DataFrame({')
    print('    "姓名": ["Alice", "Bob", "Charlie"],')
    print('    "年龄": [25, 30, 35],')
    print('    "成绩": [88.5, 92.0, 78.5],')
    print('})')
    print('')
    print('# (1) 单列(返回 Series)')
    print('print(df["姓名"])')
    print('print(type(df["姓名"]))  # <class Series>')
    print('')
    print('# (2) 多列(返回 DataFrame)')
    print('print(df[["姓名", "成绩"]])')
    print('print(type(df[["姓名", "成绩"]]))  # <class DataFrame>')
