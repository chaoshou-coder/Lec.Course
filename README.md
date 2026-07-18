# Lec.Course

> 告诉 agent 你想学什么。它扒知识依赖、推理学习路径、并行制课、独立验收。

## 这是什么

一个 AI 驱动的课程生产框架,对标 gstack 的 skill 组合形态,但面向课程生产。

你描述一个学习目标(比如"从零写一个 Web Scraping 工具"),agent 会:

1. **发现** —— 多轮问答敲定知识域、目的、深度、每日时长、验收标准
2. **规划** —— 扒知识依赖 DAG、拓扑排序、推理最小必要学习链
3. **制课** —— 多 subagent 并行产出每课的自学材料
4. **验收** —— 独立 subagent 按验收标准审课(制课者不验收自己的产物)
5. **交付** —— 你拿到一门完整的自学课程产物

## 状态

**v0.1 —— 骨架 + 方法论迁移完成。** 框架正在建设中,尚未有可端到端跑通的管线。详见 [CLAUDE.md](CLAUDE.md)。

## 怎么用

```bash
# 克隆
git clone https://github.com/chaoshou-coder/Lec.Course.git
cd Lec.Course

# 在 Claude Code 里加载 skills 目录,然后告诉 agent 你想学什么
```

(首次端到端用例文档完成 T9 后补充。)

## 项目结构

```
Lec.Course/
├── methodology/        # 课程开发知识底座(按阶段组织)
├── schemas/            # 产物 schema(机器可校验)
├── scripts/            # 校验脚本
├── skills/course-agent/ # 单 agent 宿主 + 状态机
└── examples/           # Lec.Python 60 天课程作为验证样本
```

## 设计文档

完整设计 + 审查报告:[`~/.gstack/projects/chaoshou-coder-Lec.Python/bang-master-design-20260716-214050.md`](需要从 gstack artifacts 读取)

## 不做什么

- 不做 B2B / 机构版(用户 = 个人自学者)
- 不做课堂 / 教师场景(面向自学,不依赖教师)
- 不做通用对话机器人(专用课程生产管线)

## License

(待补充)
