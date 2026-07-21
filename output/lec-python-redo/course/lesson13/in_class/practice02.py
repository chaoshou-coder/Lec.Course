"""
[难度: ★][所属知识点: DataFrame 创建][预计完成时间: 8 分钟]

题目:从字典创建 DataFrame,数据如下:
姓名/年龄/城市三列,3 条记录:
Alice 25 北京
Bob   30 上海
Charlie 35 广州
"""

if __name__ == "__main__":
    print("参考答案:")
    print('import pandas as pd')
    print('data = {')
    print('    "姓名": ["Alice", "Bob", "Charlie"],')
    print('    "年龄": [25, 30, 35],')
    print('    "城市": ["北京", "上海", "广州"],')
    print('}')
    print('df = pd.DataFrame(data)')
    print('print(df)')
