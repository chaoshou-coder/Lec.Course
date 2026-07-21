"""
[难度: ★★★][所属知识点: loc/iloc 选择][预计完成时间: 15 分钟]

题目:创建 DataFrame:
    name  age
a   Amy   25
b   Bob   30
c   Cal   35

1. 用 loc 选取 index="b" 的 name
2. 用 iloc 选取第 0 到第 1 行(含第 1 行,不含第 2 行)
3. 用 loc 选取 "a" 到 "c" 行的 name 列(注意含右端)

示例:
    Bob
      name  age
    a  Amy   25
    b  Bob   30
    a    Amy
    b    Bob
    c    Cal
"""

import pandas as pd

# TODO: 创建 DataFrame
df = None

if __name__ == '__main__':
    # 参考答案
    df = pd.DataFrame({"name": ["Amy", "Bob", "Cal"],
                       "age": [25, 30, 35]},
                      index=["a", "b", "c"])
    print(df.loc["b", "name"])       # Bob
    print(df.iloc[0:2])              # Amy, Bob(不含第 2 行)
    print(df.loc["a":"c", "name"])   # Amy, Bob, Cal(含右端)
