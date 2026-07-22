# CLAUDE.md — Lec.Course 工作指南

## 这是什么

Lec.Course 是一个 AI 驱动的课程生产框架。用户描述学习目标,agent 自动扒知识依赖、推理学习路径、并行制课、独立验收。

## 如何使用

用户 clone 仓库后,在 Claude Code 里打开仓库文件夹,告诉 agent 你想学什么。

### 启动课程生产

用户说"我想学 XXX"或"/course-agent"时,agent 进入 DISCOVER 态。

### 工作流程

1. **DISCOVER** —— 多轮问答敲定知识域、目的、深度、验收标准 → 产出 `requirements.json`
2. **PLAN** —— 扒知识依赖 DAG、拓扑排序、推理学习序列 → 产出 `learning-plan.json`
3. **BUILD** —— 按知识点并行制课 → 产出 `knowledge/` + `exercises/`
4. **QA** —— 独立 subagent 验收 → 产出 `qa-report.json`
5. **DONE** —— 交付课程产物

### 产物结构

```
course-name/
├── README.md                      # 入口:知识点地图 + 链接导航
├── knowledge/                     # 每个知识点一个 MD
│   ├── 01-xxx.md
│   ├── 02-xxx.md
│   └── ...
├── exercises/                     # 练习文件
│   ├── 01-xxx/
│   │   ├── practice01-06.py
│   │   └── task01-03.py
│   └── ...
└── solutions/                     # 参考答案(可选)
```

## 关键约定

- **按知识点组织,不按天规划** —— 学员自己决定每天学多少
- **每个知识点 MD 包含** —— 8 步趁热打铁(痛点→类比→解释→ASCII→代码→逐行解剖→常见错误→练习)
- **知识点末尾有导航链接** —— 下一个/上一个知识点 + 返回知识地图
- **ASCII 图用 plain text** —— 不用 box-drawing 字符,确保所有渲染器兼容

## 目录结构

```
Lec.Course/
├── CLAUDE.md                      # 本文件
├── README.md                      # 项目入口
├── methodology/                   # skill 方法论(按阶段组织)
├── schemas/                       # 产物 schema
├── scripts/                       # 校验工具
└── skills/course-agent/           # skill 入口
    ├── SKILL.md                   # agent 执行逻辑
    └── state-machine.md           # 状态机架构
```

## 工具使用

```bash
# schema 校验
python scripts/validate.py schemas/requirements.schema.json path/to/requirements.json

# 内容质量检查(跨语言/跨学科)
python scripts/content-quality-check.py path/to/knowledge/
```
