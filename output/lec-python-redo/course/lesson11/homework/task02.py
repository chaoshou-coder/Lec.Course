"""
[难度: ★★★][所属知识点: 布尔索引应用][预计完成时间: 20 分钟][类型: 选做]

题目:给定数组 scores = np.array([85, 92, 78, 65, 95, 50, 88, 72]),
用布尔索引完成:
(1) 取出所有 >= 60 的及格分数
(2) 取出所有 >= 90 的优秀分数
(3) 统计及格人数和优秀人数
"""

if __name__ == "__main__":
    print("参考答案:")
    print('import numpy as np')
    print('scores = np.array([85, 92, 78, 65, 95, 50, 88, 72])')
    print('')
    print('pass_scores = scores[scores >= 60]')
    print('print(pass_scores)  # [85 92 78 65 95 88 72]')
    print('')
    print('excellent = scores[scores >= 90]')
    print('print(excellent)    # [92 95]')
    print('')
    print('print(len(pass_scores))  # 7')
    print('print(len(excellent))   # 2')
