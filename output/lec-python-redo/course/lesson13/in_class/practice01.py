"""
[难度: ★][所属知识点: Series 创建][预计完成时间: 5 分钟]

题目:创建以下 Series:
(1) 从列表 [10, 20, 30, 40] 创建(默认索引)
(2) 从列表 [10, 20, 30] 创建,自定义索引 ["a","b","c"]
(3) 从字典 {"北京": 2154, "上海": 2424} 创建
"""

if __name__ == "__main__":
    print("参考答案:")
    print('import pandas as pd')
    print('')
    print('# (1) 默认索引')
    print('s1 = pd.Series([10, 20, 30, 40])')
    print('')
    print('# (2) 自定义索引')
    print('s2 = pd.Series([10, 20, 30], index=["a", "b", "c"])')
    print('')
    print('# (3) 从字典创建')
    print('s3 = pd.Series({"北京": 2154, "上海": 2424})')
