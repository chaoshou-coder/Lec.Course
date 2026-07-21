"""
[难度: ★★][所属知识点: CSV 读写][预计完成时间: 10 分钟]

题目:把下面的 DataFrame 保存为 students.csv,
再读取回来。
df = pd.DataFrame({"姓名":["Alice","Bob"],"成绩":[88,92]})

要求:
- 保存时不保存行索引
- 读取后打印 DataFrame
"""

if __name__ == "__main__":
    print("参考答案:")
    print('import pandas as pd')
    print('df = pd.DataFrame({"姓名": ["Alice", "Bob"],')
    print('                   "成绩": [88, 92]})')
    print('')
    print('# 保存(不保存行索引)')
    print('df.to_csv("students.csv", index=False, encoding="utf-8")')
    print('')
    print('# 读取')
    print('df2 = pd.read_csv("students.csv", encoding="utf-8")')
    print('print(df2)')
