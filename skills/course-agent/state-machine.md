# 单 Agent 状态机

> 本文档定义 course-agent 的状态、状态转移规则和工具映射。SKILL.md 是入口,本文档是架构骨架。

## 状态定义

| 状态 | 职责 | 可调工具 |
|---|---|---|
| `IDLE` | agent 已加载,无活跃任务 | `ask_user`(启动) |
| `DISCOVER` | 需求问答 + 研究目标域 | `web_search`, `ask_user`, `read_reference` |
| `PLAN` | 扒知识依赖 DAG + 推理学习路径 | `build_dag`, `topological_sort`, `research_dependencies`, `prune` |
| `BUILD` | 并行 spawn subagent 制课 | `spawn_build_subagent`, `write_file`, `validate_schema` |
| `QA` | 独立 subagent 验收 | `spawn_qa_subagent`, `read_qa_report` |
| `AWAIT_CONFIRM` | 软关卡:等待用户确认转移 | `ask_user`(approve / reject / revise) |
| `DONE` | 全部通过,课程产出完成 | 无(终态) |

## 状态转移图

```
                    ┌─────────────────────────────────────────────┐
                    │                                             │
                    ▼                                             │
                 ┌──────┐   用户提供目标     ┌──────────┐         │
  启动────────▶│ IDLE │ ──────────────▶│ DISCOVER │         │
                 └──────┘                    └────┬─────┘         │
                      ▲                           │               │
                      │                           │ requirements  │
                      │                           │ 完成           │
                      │                           ▼               │
                      │                     ┌──────────┐         │
                      │   用户修订需求       │ AWAIT    │         │
                      │◀───────────────────│ CONFIRM  │         │
                      │                     └────┬─────┘         │
                      │                          │ approve        │
                      │                          ▼               │
                      │    plan 被拒         ┌──────────┐         │
                      │◀───────────────────│  PLAN    │         │
                      │                     └────┬─────┘         │
                      │                          │ learning-plan  │
                      │                          │ 完成 + 用户确认  │
                      │                          ▼               │
                      │    rebuild 失败课       ┌──────────┐     │
                      │◀───────────────────│  BUILD   │         │
                      │                     └────┬─────┘         │
                      │                          │ 所有 lesson    │
                      │                          │ schema 通过    │
                      │                          ▼               │
                      │    plan 级失败        ┌──────────┐       │
                      │◀───────────────────│   QA     │         │
                      │                     └────┬─────┘         │
                      │          ┌───────────────┼───────────┐   │
                      │          │               │           │   │
                      │          ▼               ▼           ▼   │
                      │     replan          rebuild      pass   │
                      │     (PLAN)         (BUILD)     (DONE)  │
                      │                                         │
                      └─────────────────────────────────────────┘
                                                           │
                                                           ▼
                                                      ┌────────┐
                                                      │  DONE  │
                                                        └────────┘
```

## 转移规则(防非法转移)

- **只有 `AWAIT_CONFIRM` 能接收用户 approve。** 其他状态不直接接受 approve,必须经过软关卡显式征求。
- **`QA → DISCOVER` 只在 requirements 级 root cause 时触发。** agent 必须在 `qa-report.md` 里写明"为什么是 requirements 的问题"才允许跨级回退,否则只能回退一级(QA→BUILD)。
- **每个状态有超时:** DISCOVER/PLAN 超过 N 轮 ask_user 还没收敛 → 主动进 AWAIT_CONFIRM 让用户决定方向。BUILD 单 lesson 超过时间预算 → 标记失败,不阻塞其他 lesson。
- **`DONE` 是终态,不接受任何工具调用,** 只能由用户显式启动新课程(IDLE)。

## 软关卡实现

`AWAIT_CONFIRM` 状态 = 软关卡的物理实现。agent 进入此状态时:
1. 写 `.gate-pending/{stage}.json`(产物 + 状态 + 选项)
2. 向用户展示当前阶段产物摘要 + 请用户 approve / reject / revise
3. 用户回复后,agent 读取回复 → 决定下一状态

## 阶段 → 方法论参考

| 阶段 | 状态机态 | 方法论文档 |
|------|---------|-----------|
| 需求问答 + 研究 | DISCOVER | `methodology/01-discover-target-domain.md` |
| DAG + 学习路径 | PLAN | `methodology/02-build-knowledge-dag.md`, `methodology/03-design-learning-sequence.md` |
| 并行制课 | BUILD | `methodology/04-design-assessments.md`, `methodology/05-production-standards.md` |
| 独立验收 | QA | 对照 `requirements.md` acceptance_criteria |
