# 07 · 工作日志与流程效率追踪 —— 如何记录、分析、优化课程生产流程

> **归属阶段:** 全流程(DISCOVER → PLAN → BUILD → QA → DONE)
> **用途:** 记录每个阶段的时间消耗、决策、瓶颈,用于持续优化 skill 和流程。
> **适用场景:** 每次课程生产完成后,分析效率短板,指导下一轮迭代。
> **版本:** v1.0(2026-07-29),v1.4 新增

---

## 1. 为什么需要工作日志

**问题:** 没有工作日志,我们无法回答:
- 哪个阶段最慢?是 DISCOVER 的问答轮次太多,还是 BUILD 的 subagent 失败重试?
- 质量问题的根因是什么?是 PLAN 的 pedagogy_notes 不清晰,还是 BUILD subagent 没理解?
- 并行度设置是否合理?3 并发和 5 并发的实际效率差异是多少?

**答案:** 结构化工作日志,记录每个事件的时间戳和上下文。

---

## 2. 工作日志的结构

产出 `output/work-log.json`:

```json
{
  "course_id": "mysql-curl-course",
  "started_at": "2026-07-29T10:00:00Z",
  "completed_at": "2026-07-29T10:25:00Z",
  "total_duration_minutes": 25,
  "parallelism": {
    "build_parallelism": 3,
    "qa_parallelism": 2
  },
  "phases": [
    {
      "phase": "DISCOVER",
      "started_at": "2026-07-29T10:00:00Z",
      "completed_at": "2026-07-29T10:03:00Z",
      "duration_minutes": 3,
      "events": [
        {"time": "10:00", "type": "ask_user", "detail": "知识域确认"},
        {"time": "10:01", "type": "ask_user", "detail": "深度目标确认"},
        {"time": "10:02", "type": "ask_user", "detail": "并发度选择: moderate(3)"},
        {"time": "10:03", "type": "artifact_created", "detail": "requirements.json"}
      ],
      "decisions": [
        {"decision": "研究未落地", "reason": "web_search 不可用", "impact": "reference_courses 未验证"}
      ],
      "bottlenecks": []
    },
    {
      "phase": "PLAN",
      "started_at": "2026-07-29T10:03:00Z",
      "completed_at": "2026-07-29T10:06:00Z",
      "duration_minutes": 3,
      "events": [
        {"time": "10:03", "type": "dag_built", "detail": "22 节点, 38 边"},
        {"time": "10:04", "type": "pruned", "detail": "裁剪 8 个节点"},
        {"time": "10:05", "type": "user_approved", "detail": "用户确认剪枝"}
      ],
      "decisions": [],
      "bottlenecks": []
    },
    {
      "phase": "BUILD",
      "started_at": "2026-07-29T10:06:00Z",
      "completed_at": "2026-07-29T10:18:00Z",
      "duration_minutes": 12,
      "events": [
        {"time": "10:06", "type": "subagent_spawned", "detail": "3 个 build subagent"},
        {"time": "10:10", "type": "subagent_completed", "detail": "subagent-1: 知识点 1-4"},
        {"time": "10:11", "type": "subagent_completed", "detail": "subagent-2: 知识点 5-7"},
        {"time": "10:12", "type": "subagent_failed", "detail": "subagent-3: 知识点 8-10, box_drawing 违规"},
        {"time": "10:14", "type": "subagent_retry", "detail": "subagent-3 重试"},
        {"time": "10:18", "type": "subagent_completed", "detail": "subagent-3 重试成功"}
      ],
      "decisions": [],
      "bottlenecks": [
        {"issue": "subagent-3 失败重试", "cause": "使用了 Unicode box-drawing", "fix_time_minutes": 4}
      ]
    },
    {
      "phase": "QA",
      "started_at": "2026-07-29T10:18:00Z",
      "completed_at": "2026-07-29T10:25:00Z",
      "duration_minutes": 7,
      "events": [
        {"time": "10:18", "type": "subagent_spawned", "detail": "2 个 QA subagent"},
        {"time": "10:22", "type": "subagent_completed", "detail": "结构检查: 通过"},
        {"time": "10:24", "type": "subagent_completed", "detail": "内容正确性: 1 个 minor"}
      ],
      "decisions": [],
      "bottlenecks": []
    }
  ],
  "summary": {
    "total_subagents_spawned": 5,
    "total_subagent_failures": 1,
    "total_retry_count": 1,
    "quality_issues_found": 2,
    "quality_issues_fixed": 1
  }
}
```

---

## 3. 事件类型

| 事件类型 | 触发时机 | 必填字段 |
|----------|----------|----------|
| `ask_user` | 向用户提问 | `detail`(问题摘要) |
| `artifact_created` | 产出硬性产物 | `detail`(产物路径) |
| `dag_built` | PLAN 完成 DAG | `detail`(节点数 + 边数) |
| `pruned` | 剪枝决策 | `detail`(裁剪节点列表) |
| `user_approved` | 用户确认 | `detail`(确认内容) |
| `subagent_spawned` | spawn subagent | `detail`(subagent 职责) |
| `subagent_completed` | subagent 完成 | `detail`(产出摘要) |
| `subagent_failed` | subagent 失败 | `detail`(失败原因) |
| `subagent_retry` | 重试 subagent | `detail`(重试原因) |
| `quality_issue` | 发现质量问题 | `detail`(问题描述 + 位置) |
| `quality_fix` | 修复质量问题 | `detail`(修复方式) |
| `phase_transition` | 阶段转移 | `detail`(从哪到哪) |

---

## 4. 决策记录格式

每个重要决策记录到 `phases[].decisions`:

```json
{"decision": "...", "reason": "...", "impact": "..."}
```

**为什么:** 后续复盘时,能理解决策背景,避免重复犯错。

---

## 5. 瓶颈记录格式

每个瓶颈记录到 `phases[].bottlenecks`:

```json
{"issue": "...", "cause": "...", "fix_time_minutes": N}
```

**为什么:** 瓶颈分析是 skill 迭代的核心输入。

---

## 6. 效率分析(每次课程完成后)

### 6.1 时间分布

```
总耗时 = DISCOVER + PLAN + BUILD + QA
BUILD 占比 > 60% → 考虑提高并行度
QA 占比 > 30% → 考虑提高并行度或简化检查
DISCOVER 占比 > 20% → 问答轮次过多,需要更好的收敛策略
```

### 6.2 失败率分析

```
subagent 失败率 = 失败数 / 总数
> 20% → subagent prompt 需要优化
> 50% → 并行度太高或任务拆分不合理
```

### 6.3 质量瓶颈

```
质量问题最多的阶段 → 重点优化
重复出现的问题 → 加入 checker 自动检测
```

---

## 7. 工作日志的消费方式

### 7.1 QA 阶段

QA 读取 work-log,验证:
- 所有阶段是否按时完成
- 失败是否被正确处理
- 质量问题是否被修复

### 7.2 迭代复盘

每轮迭代结束后,分析 work-log:
- 哪个阶段最慢? → 优化方向
- 哪个问题重复出现? → 加入 checker
- 并行度是否合理? → 调整默认值

### 7.3 skill 改进

work-log 的 `bottlenecks` 和 `decisions` 是 skill 迭代的核心输入:
- 重复的 bottleneck → 加入 methodology 的预防规则
- 重复的 decision → 加入 methodology 的默认策略

---

## 8. 实现指南

### 8.1 主 agent 职责

- 每个阶段开始时记录 `phase_transition`
- 每个事件发生时记录到 `events[]`
- 每个决策记录到 `decisions[]`
- 每个瓶颈记录到 `bottlenecks[]`
- 课程完成后写入 `output/work-log.json`

### 8.2 subagent 职责

- 开始工作时记录 `subagent_spawned`
- 完成工作时记录 `subagent_completed`
- 失败时记录 `subagent_failed`

### 8.3 工具函数

```python
# 伪代码
def log_event(phase, event_type, detail):
    work_log["phases"][-1]["events"].append({
        "time": now(),
        "type": event_type,
        "detail": detail
    })

def log_decision(phase, decision, reason, impact):
    work_log["phases"][-1]["decisions"].append({
        "decision": decision,
        "reason": reason,
        "impact": impact
    })

def log_bottleneck(phase, issue, cause, fix_time_minutes):
    work_log["phases"][-1]["bottlenecks"].append({
        "issue": issue,
        "cause": cause,
        "fix_time_minutes": fix_time_minutes
    })
```

---

## 交叉参考

- **上游:** 所有阶段(DISCOVER/PLAN/BUILD/QA)都产生日志
- **下游:** QA 验证日志完整性,迭代复盘分析日志
- **产物:** `output/work-log.json`
- **分析方法:** `methodology/07-work-logging.md` 第 6 节
