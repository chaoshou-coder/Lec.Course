# Day 07 · 文件 I/O + 异常

> 今日节点: d07(open/read/write/with/JSON/try/except)
> 预计时长: 6 小时
> 教学法: NCDL(先感知场景再抽象规则)

## 今日知识点

- open() 与文件模式('r' 读/'w' 写覆盖/'a' 追加)
- read()/readline()/readlines() 三种读取方式
- with 上下文管理(自动 close())
- encoding="utf-8"
- JSON 读写(json.dump/json.load/json.dumps/json.loads)
- ensure_ascii=False 与 indent=2
- 异常处理(try/except/else/finally)
- 常见异常(FileNotFoundError/ValueError/TypeError/KeyError/IndexError/json.JSONDecodeError)

## 当堂练(6 道,必做)

| 题 | 难度 | 知识点 | 预计时间 |
|---|---|---|---|
| practice01.py | ★ | open 与文件模式 | 5 min |
| practice02.py | ★ | 三种读取方式 | 8 min |
| practice03.py | ★★ | with 上下文管理 | 8 min |
| practice04.py | ★★ | JSON 读写 | 10 min |
| practice05.py | ★★★ | try/except 基础 | 12 min |
| practice06.py | ★★★ | 常见异常捕获 | 15 min |

## 课后作业(3 道,选做)

| 题 | 难度 | 知识点 | 预计时间 |
|---|---|---|---|
| task01.py | ★★★ | 文件读写综合 | 15 min |
| task02.py | ★★★ | JSON 数据处理 | 20 min |
| task03.py | ★★★★ | 异常处理综合 | 30 min |

## 验收标准

- [ ] 能用 open() 打开文件,理解 r/w/a 模式区别
- [ ] 能用 read/readline/readlines 读取文件
- [ ] 能用 with 自动管理文件资源
- [ ] 能用 json.dump/load 读写 JSON 文件
- [ ] 能用 try/except 捕获并处理异常
- [ ] 能识别常见异常类型并正确处理
