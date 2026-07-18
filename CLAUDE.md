# CLAUDE.md — Lec.Course 仓库工作指南

## What this repo is

Lec.Course 是一个 **AI 驱动的课程生产框架**。用户描述想学什么,agent 自动扒知识依赖关系、推理学习路径、多 subagent 并行制课、独立 subagent 验收。

这不是一个软件应用 —— 这是一套 **Claude Code skill + 方法论参考**。仓库的"可运行产物"是 skills 目录里的 SKILL.md 文件,不是可执行二进制。

## 核心设计决策(已评审锁定)

- **单 agent + 工具调用**架构(不是 4 个独立 skill 的 Pipeline)
- **7 态状态机**: IDLE → DISCOVER → PLAN → BUILD → QA → AWAIT_CONFIRM → DONE
- **软关卡 + 硬验收**: 中间关卡由 agent 主动调 `ask_user` 确认;只有 QA 验收是硬性关卡
- **面向自学,不依赖教师**: 核心产物 = self-study notes + 练习 + 验收证据
- **独立 subagent 验收**: build subagent 绝不能验收自己的产出

完整设计文档:`~/.gstack/projects/chaoshou-coder-Lec.Python/bang-master-design-20260716-214050.md`

## 目录结构

```
Lec.Course/
├── CLAUDE.md              # 本文件 —— Claude Code 工作指南
├── README.md              # 对外入口:这是什么、怎么用、用例
├── methodology/           # 知识底座 —— 按课程开发阶段组织的方法论文档
│   ├── 01-discover-target-domain.md
│   ├── 02-build-knowledge-dag.md
│   ├── 03-design-learning-sequence.md
│   ├── 04-design-assessments.md
│   ├── 05-production-standards.md
│   └── 06-subject-specific-patterns.md
├── schemas/               # 产物 schema(机器可校验)
│   ├── requirements.schema.json
│   ├── learning-plan.schema.json
│   └── qa-report.schema.json
├── scripts/
│   └── validate.py        # schema 校验脚本
├── skills/
│   └── course-agent/      # 单 agent 宿主(待实施 T8)
│       ├── SKILL.md
│       └── state-machine.md
└── examples/
    └── python-60day/      # 从 Lec.Python 复制的验证样本(待实施 T3)
```

## 阶段 → 方法论映射

| 阶段 | 状态机态 | 方法论文档 | 核心工具 |
|------|---------|-----------|---------|
| 需求问答 + 研究 | DISCOVER | 01-discover-target-domain.md | web_search, ask_user |
| DAG + 学习路径 | PLAN | 02-build-knowledge-dag.md, 03-design-learning-sequence.md | build_dag, topological_sort, prune |
| 并行制课 | BUILD | 04-design-assessments.md, 05-production-standards.md | spawn_build_subagent, validate_schema |
| 独立验收 | QA | (对照 requirements.md acceptance_criteria) | spawn_qa_subagent |

## 产物 schema(硬性关卡)

每个阶段的产出必须通过 schema 校验:

| 产物 | schema | 产出态 |
|------|--------|--------|
| `requirements.md` | requirements.schema.json | DISCOVER |
| `learning-plan.md` | learning-plan.schema.json | PLAN |
| `qa-report.md` | qa-report.schema.json | QA |

```bash
python scripts/validate.py schemas/requirements.schema.json path/to/requirements.md.json
```

## 实施顺序(关键路径)

```
T1(骨架) ✅ ─▶ T2(方法论迁移) ✅ ─▶ T4(schema) ✅ ─▶ T5(discover skill) ─▶ T6(plan) ─▶ T7(build+qa) ─▶ T8(状态机harness) ─▶ T9(README)
       │                                      ▲
       └──▶ T3(验证样本) ──────────────────────┘
```

T10(CI) 可在 T4 之后的任意时间做。

**下一步 = T3(复制 Lec.Python 60 课为 examples)或直接 T5(搭 discover skill)。**
T3 和 T5 无依赖关系,可并行。建议先 T5(核心代码路径),T3 作为验证样本后补。

## 不改这些

- Lec.Python 仓库的内容 —— 那是 Lec.Course 的验证样本,不是 Lec.Course 本身
- schema 字段定义(视为 breaking change,变更需更新消费方)
- 实施任务清单见设计文档的 Implementation Tasks 节
