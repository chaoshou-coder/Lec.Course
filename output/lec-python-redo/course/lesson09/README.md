# Day 09 · 模块与高级

> 今日节点: d09(import/包/生成器/上下文管理器/装饰器)
> 预计时长: 6 小时
> 教学法: default(理论+示例+实战)

## 今日知识点

- 三种 import(import 模块/from ... import .../as 别名)
- 自定义模块(同目录 .py 文件 import)
- 包(Package)= 模块的文件夹 + __init__.py
- 生成器 yield(惰性计算)
- yield from
- 上下文管理器(__enter__/__exit__)
- 装饰器(接收函数→返回新函数,@decorator 语法糖)
- functools.wraps

## 当堂练(6 道,必做)

| 题 | 难度 | 知识点 | 预计时间 |
|---|---|---|---|
| practice01.py | ★ | 三种 import | 5 min |
| practice02.py | ★ | 自定义模块与包 | 8 min |
| practice03.py | ★★ | 生成器 yield | 10 min |
| practice04.py | ★★ | yield from | 10 min |
| practice05.py | ★★★ | 上下文管理器 | 12 min |
| practice06.py | ★★★ | 装饰器与 wraps | 15 min |

## 课后作业(3 道,选做)

| 题 | 难度 | 知识点 | 预计时间 |
|---|---|---|---|
| task01.py | ★★★ | 生成器综合 | 15 min |
| task02.py | ★★★ | 装饰器综合 | 20 min |
| task03.py | ★★★★ | 电商订单系统模块化 | 30 min |

## 验收标准

- [ ] 能用三种方式 import,理解区别
- [ ] 能创建自定义模块,组织成包
- [ ] 能用 yield 创建生成器,理解惰性计算
- [ ] 能用 yield from 简化生成器委托
- [ ] 能实现 __enter__/__exit__ 自定义上下文管理器
- [ ] 能定义装饰器,用 @wraps 保留函数元信息
