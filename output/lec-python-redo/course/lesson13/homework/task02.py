"""
[难度: ★★★][所属知识点: CSV 数据分析][预计完成时间: 25 分钟][类型: 选做]

题目:假设已有 sales.csv 文件,列: 日期/产品/金额/城市。
(1) 读取 CSV 到 DataFrame
(2) 查看前 5 行和结构信息
(3) 查看金额的统计摘要(均值/最大/最小)
(4) 只取产品和金额两列
(5) 保存筛选结果到 sales_summary.csv
"""

if __name__ == "__main__":
    print("参考答案:")
    print('import pandas as pd')
    print('')
    print('# (1) 读取')
    print('df = pd.read_csv("sales.csv", encoding="utf-8")')
    print('')
    print('# (2) 查看')
    print('print(df.head())')
    print('print(df.info())')
    print('')
    print('# (3) 金额统计')
    print('print(df["金额"].describe())')
    print('')
    print('# (4) 取两列')
    print('result = df[["产品", "金额"]]')
    print('')
    print('# (5) 保存')
    print('result.to_csv("sales_summary.csv", index=False)')
