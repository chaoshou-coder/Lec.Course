# Day 13 · Pandas 基础

> 今日节点: d13(Series/DataFrame/CSV/属性/查看/列选/行选)
> 预计时长: 6 小时
> 教学法: NCDL(展示"用循环遍历 DataFrame"反模式)

## 今日知识点

- Series(带索引的一维数组)
- DataFrame(二维表格,字典创建)
- 从 CSV 创建(pd.read_csv / df.to_csv)
- 基础属性(shape/dtypes/columns/index)
- 快速查看(head/tail/info/describe)
- 列选择(df["A"] 单列 / df[["A","B"]] 多列)
- 行选择(loc 标签 vs iloc 整数位置)

## 当堂练(6 道,必做)

| 题 | 难度 | 知识点 | 预计时间 |
|---|---|---|---|
| practice01.py | ★ | Series 创建 | 5 min |
| practice02.py | ★ | DataFrame 创建 | 8 min |
| practice03.py | ★★ | CSV 读写 | 10 min |
| practice04.py | ★★ | 基础属性 | 8 min |
| practice05.py | ★★★ | 列选择 | 10 min |
| practice06.py | ★★★ | 行选择(loc/iloc) | 15 min |

## 课后作业(3 道,选做)

| 题 | 难度 | 知识点 | 预计时间 |
|---|---|---|---|
| task01.py | ★★★ | DataFrame 综合 | 20 min |
| task02.py | ★★★ | CSV 数据分析 | 25 min |
| task03.py | ★★★★ | loc/iloc 综合 | 30 min |

## 验收标准

- [ ] 能创建 Series 和 DataFrame
- [ ] 能用 read_csv 读取和 to_csv 保存
- [ ] 能用 shape/dtypes 查看数据属性
- [ ] 能用 head/tail/info 快速了解数据
- [ ] 能区分单列和多列选择
- [ ] 能用 loc(标签)和 iloc(整数)选择行
