"""
[难度: ★★★][所属知识点: DataFrame 综合][预计完成时间: 20 分钟][类型: 选做]

题目:创建一个学生成绩 DataFrame(5 行 4 列):
列: 姓名/语文/数学/英语,5 个学生。
(1) 查看前 3 行
(2) 查看 info 结构
(3) 查看 describe 统计
(4) 只取姓名和语文两列
(5) 取第 2 行(用 iloc)
"""

if __name__ == "__main__":
    print("参考答案:")
    print('import pandas as pd')
    print('df = pd.DataFrame({')
    print('    "姓名": ["张三", "李四", "王五", "赵六", "孙七"],')
    print('    "语文": [85, 92, 78, 65, 95],')
    print('    "数学": [90, 88, 82, 70, 98],')
    print('    "英语": [80, 95, 70, 60, 92],')
    print('})')
    print('')
    print('print(df.head(3))         # (1)')
    print('print(df.info())          # (2)')
    print('print(df.describe())      # (3)')
    print('print(df[["姓名", "语文"]])# (4)')
    print('print(df.iloc[1])         # (5)')
