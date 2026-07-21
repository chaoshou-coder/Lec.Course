"""
[难度: ★★★][所属知识点: 字典遍历][预计完成时间: 15 分钟]

题目:给定 scores = {"数学": 90, "语文": 85, "英语": 88},
用 items() 遍历打印每科成绩,并计算总分。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('scores = {"数学": 90, "语文": 85, "英语": 88}')
    print('total = 0')
    print('for subject, score in scores.items():')
    print('    print(f"{subject}: {score}")')
    print('    total += score')
    print('print(f"总分: {total}")')
