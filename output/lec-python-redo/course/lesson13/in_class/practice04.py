"""
[难度: ★★][所属知识点: 基础属性][预计完成时间: 8 分钟]

题目:给定 DataFrame df(列: 姓名/年龄/成绩,3 条记录),
输出:
(1) shape —— 行列数
(2) dtypes —— 列类型
(3) columns —— 列名列表
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
    print('print(df.shape)     # (3, 3)')
    print('print(df.dtypes)')
    print('# 姓名     object')
    print('# 年龄      int64')
    print('# 成绩    float64')
    print('print(df.columns)   # Index(["姓名","年龄","成绩"])')
