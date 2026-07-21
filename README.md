# Lec.Course

> 告诉 agent 你想学什么。它扒知识依赖、推理学习路径、并行制课、独立验收。

## 这是什么

一个 AI 驱动的课程生产框架,对标 gstack 的 skill 组合形态,但面向课程生产。

你描述一个学习目标(比如"从零写一个 Web Scraping 工具"),agent 会:

1. **发现(DISCOVER)** —— 多轮问答敲定知识域、目的、深度、每日时长、验收标准
2. **规划(PLAN)** —— 扒知识依赖 DAG、拓扑排序、推理最小必要学习链
3. **制课(BUILD)** —— 多 subagent 并行产出每天的自学材料 + 练习
4. **验收(QA)** —— 独立 subagent 按验收标准审课(制课者不验收自己的产物)
5. **交付(DONE)** —— 你拿到一门完整的自学课程产物

## 状态

**v1.0 —— 首个端到端验证完成。** 用"HTML 基础知识"作为首个验证案例,产出了完整的 10 天课程。框架结构已就绪,可用任意知识域跑全流程。

## 怎么用

```bash
# 克隆
git clone https://github.com/chaoshou-coder/Lec.Course.git
cd Lec.Course

# 在 Claude Code 里加载 skills 目录,然后告诉 agent 你想学什么
```

### 快速体验(无需写代码)

仓库已包含一个完整的端到端验证案例 —— **HTML 基础知识 → 个人作品集网站**:

```bash
# 查看 DISCOVER 产出(课程需求)
cat output/requirements.json

# 查看 PLAN 产出(学习计划 + DAG)
cat output/learning-plan.json

# 查看完整课程(10 天)
ls course/lesson01/  # Day 1: 你的第一个 HTML 文档
ls course/lesson10/  # Day 10: 联系表单 + 部署上线

# schema 校验
python3 scripts/validate.py schemas/requirements.schema.json output/requirements.json
```

## 项目结构

```
Lec.Course/
├── CLAUDE.md                      # Claude Code 工作指南
├── README.md                      # 本文件
├── methodology/                   # 课程开发知识底座(按阶段组织)
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
│   └── validate.py                # schema 校验脚本
├── skills/
│   └── course-agent/              # 单 agent 宿主
│       ├── SKILL.md               # agent 入口(状态机执行逻辑)
│       └── state-machine.md       # 状态机架构(7 态 + 转移规则)
├── output/                        # 验证案例的 DISCOVER/PLAN 产物
│   ├── requirements.json
│   └── learning-plan.json
└── course/                        # 验证案例的完整课程(10 天)
    ├── lesson01/ ~ lesson10/
    │   ├── README.md              # 当天入口
    │   ├── notes.md               # 自学笔记(8 步趁热打铁)
    │   ├── in_class/              # 6 道当堂练(practice01-06.py)
    │   ├── homework/              # 3 道课后作业(task01-03.py)
    │   └── mini_project/          # 迷你项目(待扩展)
    └── ...
```

## 端到端案例:HTML 基础知识

作为框架的首个验证,我们选了"HTML 基础知识 → 个人作品集网站"作为目标域。

### 输入(DISCOVER 产出)

```json
{
  "target_capability": "独立编写一个个人作品集网站(首页/项目展示/联系表单)",
  "current_level": "零编程基础",
  "daily_hours": 2,
  "depth_goal": "能写",
  "acceptance_criteria": [
    "给定内容大纲,能独立写出结构正确的 HTML 文档",
    "给定设计稿,能用语义化标签搭建完整的多页面作品集网站",
    "给定联系需求,能写出带 form/input/textarea/button 的完整表单"
  ]
}
```

### 规划(PLAN 产出)

- **17 个知识节点**,25 条依赖边,6 层拓扑
- **10 天**课表,每天 2 小时
- **倒推法**:从"作品集网站"反推 → 文档结构 → 标签语法
- **工具先行**:Day 1 先写能渲染的文档,Day 8-10 做综合项目
- **剪枝**:canvas/svg/iframe/class/id/SEO meta(从终点不可达)

### 课程产出(BUILD)

10 天 × (笔记 + 6 练习 + 3 作业) = **110 个文件**

| 天 | 主题 | 知识点 |
|---|---|---|
| 01 | 你的第一个 HTML 文档 | 标签语法 + 文档骨架 |
| 02 | 文本元素 | h1-h6 / p / br / hr |
| 03 | 链接、图片与列表 | a / img / ul / ol / li |
| 04 | 表格 | table / tr / td / th |
| 05 | 表单基础 | form / action / method / input / select / textarea |
| 06 | 表单进阶与语义化 | button / label / header / nav / main / section / article / footer |
| 07 | 代码结构与多页面整合 | 缩进/注释 + 跨页导航 |
| 08 | 综合项目:首页 | 语义化结构 + Hero 区 |
| 09 | 综合项目:项目展示页 | 卡片列表(ul/li + img) |
| 10 | 综合项目:联系表单 + 部署 | 完整表单 + GitHub Pages |

### 下一步

- 跑 QA 验收(`output/qa-report.json`)
- 用新知识域(如 Web Scraping / RAG)验证框架通用性
- 完善 mini_project 和 weekly_projects

## 设计文档

完整设计 + CEO 评审报告:see `~/.gstack/projects/chaoshou-coder-Lec.Python/bang-master-design-20260716-214050.md`

核心决策(已评审锁定):
- **单 agent + 工具调用**(从 Pipeline 翻转)
- **7 态状态机**: IDLE → DISCOVER → PLAN → BUILD → QA → AWAIT_CONFIRM → DONE
- **软关卡 + 硬验收**: 中间关卡由 agent 主动确认;只有 QA 验收是硬性关卡
- **面向自学,不依赖教师**
- **独立 subagent 验收**: build subagent 绝不能验收自己的产物

## 不做什么

- 不做 B2B / 机构版(用户 = 个人自学家)
- 不做课堂 / 教师场景(面向自学,不依赖教师)
- 不做通用对话机器人(专用课程生产管线)

## License

(待补充)
