# Day 02 · 三种声明方式的作用域

> 今日节点: v3(var hoisting) + v4(let TDZ) + v5(const 不可变)
> 预计时长: 1.5 小时
> 教学法: NCDL(3 个 Break It 演示段)

## 今日知识点

1. **var 的函数作用域与 hoisting** —— var 泄漏 + 声明提升
2. **let 的块级作用域** —— 块级 + TDZ
3. **const 的不可重新赋值** ≠ 不可变 —— 内容可变 + 重新赋值报错

## NCDL 反模式预览

今天的 3 个 Break It 演示段:
- var hoisting:在 if 块里声明 var,外面也能访问
- let TDZ:在 let 声明前访问会报错(不是 undefined)
- const 反以为:const 对象完全冻结(实际不是)

## 当堂练(6 道,必做)

| 题 | 难度 | 知识点 | 预计时间 |
|---|---|---|---|
| practice01.js | ★ | var hoisting 认知 | 5 min |
| practice02.js | ★ | let TDZ 认知 | 5 min |
| practice03.js | ★★ | const 限制 | 8 min |
| practice04.js | ★★ | 三种声明方式对比 | 10 min |
| practice05.js | ★★★ | 反模式识别(NCDL) | 15 min |
| practice06.js | ★★★ | 综合(挑战题) | 15 min |

## 课后作业(3 道,选做)

| 题 | 难度 | 知识点 | 预计时间 |
|---|---|---|---|
| task01.js | ★★★ | 修复 var 泄漏代码 | 15 min |
| task02.js | ★★★ | 修复 TDZ 错误 | 20 min |
| task03.js | ★★★★ | 综合应用(选做) | 25 min |

## 验收标准

- [ ] 能解释 var 为什么会在 if 块外泄漏
- [ ] 能解释 let 的 TDZ 行为(声明前访问报错)
- [ ] 能区分 const 的"不可重新赋值"和"内容可变"
- [ ] 能识别至少 3 种声明方式的反模式
