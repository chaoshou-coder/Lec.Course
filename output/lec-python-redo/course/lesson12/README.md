# Day 12 · NumPy 进阶

> 今日节点: d12(矩阵乘法/线性代数/聚合/随机数/文件读写)
> 预计时长: 6 小时
> 教学法: 脚手架递进(在 Day 11 数组基础上进阶)

## 今日知识点

- 矩阵乘法(@ / np.dot)vs 逐元素乘法(*)
- 线性代数(a.T / np.linalg.det / np.linalg.inv)
- 聚合函数(sum/mean/std/max/min/argmax)
- axis 参数(axis=0 跨行 / axis=1 跨列)
- 随机数生成(seed/rand/randn/randint/choice)
- 文件读写(np.save/np.load/savetxt/loadtxt)

## 当堂练(6 道,必做)

| 题 | 难度 | 知识点 | 预计时间 |
|---|---|---|---|
| practice01.py | ★★ | 矩阵乘法 | 8 min |
| practice02.py | ★★ | 线性代数(转置/行列式/逆) | 10 min |
| practice03.py | ★★ | 聚合函数 | 10 min |
| practice04.py | ★★★ | axis 参数 | 12 min |
| practice05.py | ★★★ | 随机数生成 | 12 min |
| practice06.py | ★★★ | 文件读写 | 15 min |

## 课后作业(3 道,选做)

| 题 | 难度 | 知识点 | 预计时间 |
|---|---|---|---|
| task01.py | ★★★ | 矩阵运算综合 | 20 min |
| task02.py | ★★★ | 随机数应用 | 20 min |
| task03.py | ★★★★ | 综合(线性方程组) | 30 min |

## 验收标准

- [ ] 能区分逐元素乘法(*)和矩阵乘法(@)
- [ ] 能计算转置、行列式、逆矩阵
- [ ] 能用聚合函数沿指定 axis 计算
- [ ] 理解 axis=0 跨行、axis=1 跨列
- [ ] 能用 seed 控制随机数可复现
- [ ] 能用 save/load 和 savetxt/loadtxt 读写数组
