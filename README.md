# Lec.Course

> 告诉 agent 你想学什么。它扒知识依赖、推理学习路径、并行制课、独立验收。

## 这是什么

一个 AI 驱动的课程生产框架,对标 gstack 的 skill 组合形态,但面向课程生产。

你描述一个学习目标(比如"从零写一个 Web Scraping 工具"),agent 会:

1. **发现(DISCOVER)** —— 多轮问答敲定知识域、目的、深度、验收标准
2. **规划(PLAN)** —— 扒知识依赖 DAG、拓扑排序、推理最小必要学习链
3. **制课(BUILD)** —— 多 subagent 并行产出每个知识点的自学材料 + 练习
4. **验收(QA)** —— 独立 subagent 按验收标准审课(制课者不验收自己的产物)
5. **交付(DONE)** —— 你拿到一门完整的自学课程产物

## 核心理念

**按知识点组织,不按天规划。** 每个知识点是一个独立的 Markdown 文件,学员打开一个入口 MD,通过链接在不同知识点之间跳转。学员自己决定每天学多少 —— 框架不强制日程。

## 怎么用

```bash
# 克隆
git clone https://github.com/chaoshou-coder/Lec.Course.git
cd Lec.Course

# 在 Claude Code 里加载 skills 目录,然后告诉 agent 你想学什么
```

## 项目结构

```
Lec.Course/
├── CLAUDE.md                      # Claude Code 工作指南
├── README.md                      # 本文件
├── lessons-learned.md             # 迭代铁律(10 条)
├── .github/workflows/validate.yml # CI(schema + 结构检查)
├── methodology/                   # skill 方法论(按阶段组织)
│   ├── 01-discover-target-domain.md
│   ├── 02-build-knowledge-dag.md
│   ├── 03-design-learning-sequence.md
│   ├── 04-design-assessments.md
│   ├── 05-production-standards.md
│   └── 06-subject-specific-patterns.md
├── schemas/                       # 产物 schema(机器可校验)
│   ├── requirements.schema.json
│   ├── learning-plan.schema.json
│   └── qa-report.schema.json
├── scripts/
│   ├── validate.py                # schema 校验
│   ├── regression-check.py        # 格式一致性检查
│   └── content-quality-check.py   # 内容质量检查(跨语言/跨学科)
└── skills/
    └── course-agent/              # skill 入口
        ├── SKILL.md               # agent 执行逻辑(状态机)
        └── state-machine.md       # 状态机架构(7 态 + 转移规则)
```

## 产出结构(示例)

框架产出的课程结构如下(以 Python Day 1-13 为例):

```
course-name/
├── README.md                      # 入口:知识点地图 + 链接导航
├── knowledge/                     # 每个知识点一个 MD
│   ├── 01-python-入门.md
│   ├── 02-字符串与格式化.md
│   ├── 03-条件分支.md
│   ├── ...
│   └── 13-阶段复习与NumPyPandas.md
├── exercises/                     # 练习文件
│   ├── 01-python-入门/
│   │   ├── practice01-06.py       # 6 道当堂练
│   │   └── task01-03.py           # 3 道课后作业(选做)
│   ├── ...
│   └── 13-阶段复习与NumPyPandas/
└── solutions/                     # 参考答案(可选)
```

**特点:**
- 每个知识点 MD 包含完整的 8 步趁热打铁循环(痛点→类比→解释→ASCII→代码→逐行解剖→常见错误→练习)
- 知识点末尾有"下一个/上一个"链接,学员按自己节奏跳转
- 没有"Day 1/Day 2"的强制日程

## 不做什么

- 不做 B2B / 机构版(用户 = 个人自学家)
- 不做课堂 / 教师场景(面向自学,不依赖教师)
- 不做通用对话机器人(专用课程生产管线)
- 不强制每日学习进度(学员自主决定)

## License

(待补充)
