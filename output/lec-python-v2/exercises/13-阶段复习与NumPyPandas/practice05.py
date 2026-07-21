"""
[难度: ★★][所属知识点: Pandas DataFrame 创建][预计完成时间: 10 分钟]

题目:从字典创建 DataFrame,包含 "城市" 和 "人口" 两列:
    北京 2189, 上海 2487, 深圳 1768。
1. 打印 DataFrame
2. 打印 shape 和 columns
3. 用 describe() 查看人口统计摘要

示例:
       城市    人口
    0  北京  2189
    1  上海  2487
    2  深圳  1768
    (3, 2)
    Index(['城市', '人口'], dtype='object')
"""

import pandas as pd

# TODO: 从字典创建 DataFrame,打印 shape/columns/describe
pass

if __name__ == '__main__':
    # 参考答案
    data = {"城市": ["北京", "上海", "深圳"],
            "人口": [2189, 2487, 1768]}
    df = pd.DataFrame(data)
    print(df)
    print(df.shape)       # (3, 2)
    print(df.columns)     # Index(['城市', '人口'])
    print(df.describe())
