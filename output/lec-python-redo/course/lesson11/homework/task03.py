"""
[难度: ★★★★][所属知识点: 综合(数组处理)][预计完成时间: 30 分钟][类型: 选做]

题目:模拟 3 个学生 4 门课的成绩(随机生成 0-100 整数),
存成 3×4 的数组,完成以下分析:
(1) 计算每个学生的平均分
(2) 计算每门课的平均分
(3) 找出最高分和最低分
(4) 统计 >= 80 分的个数
"""

if __name__ == "__main__":
    print("参考答案:")
    print('import numpy as np')
    print('np.random.seed(42)')
    print('scores = np.random.randint(0, 101, size=(3, 4))')
    print('')
    print('# (1) 每个学生的平均分(沿列求均值)')
    print('print(np.mean(scores, axis=1))')
    print('')
    print('# (2) 每门课的平均分(沿行求均值)')
    print('print(np.mean(scores, axis=0))')
    print('')
    print('# (3) 最高分和最低分')
    print('print(np.max(scores), np.min(scores))')
    print('')
    print('# (4) >= 80 分的个数')
    print('print(np.sum(scores >= 80))')
