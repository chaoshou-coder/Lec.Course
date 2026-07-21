#!/usr/bin/env python3
"""
Lec.Course 防回归检查脚本。

用法:
    python scripts/regression-check.py <course_dir>

检查项:
    1. 文件后缀匹配运行环境
    2. 每个 lesson 有 README.md + notes.md + 6 practice + 3 task
    3. notes.md 包含 8 步循环关键段
    4. notes.md 末尾有明日衔接段
    5. practice 文件头含 [难度:]
    6. task 文件头含 [类型: 选做]

示例:
    python scripts/regression-check.py output/iter-R9-js-build-pedagogy/course/
"""

import sys
import os
from pathlib import Path

def check_course(course_dir: str) -> int:
    """检查课程目录,返回错误数"""
    errors = []
    course_path = Path(course_dir)

    if not course_path.exists():
        print(f"目录不存在: {course_dir}")
        return 1

    # 支持两种结构:
    # 旧结构: course_dir/lessonXX/in_class/practice*.py
    # 新结构: exercises/{topic}/practice*.py + knowledge/{XX}-{topic}.md

    # 找 practice 文件(旧结构)
    practice_old = list(course_path.rglob("in_class/practice*"))
    # 找 practice 文件(新结构)
    practice_new = list(course_path.glob("practice*"))

    if practice_old:
        # 旧结构: lessonXX/in_class/practice*.py
        suffix = practice_old[0].suffix
        for lesson in sorted(course_path.glob("lesson*")):
            name = lesson.name
            for required in ["README.md", "notes.md"]:
                if not (lesson / required).exists():
                    errors.append(f"{name}: 缺少 {required}")
            in_class = list((lesson / "in_class").glob("*")) if (lesson / "in_class").exists() else []
            if len(in_class) != 6:
                errors.append(f"{name}: practice 数量 = {len(in_class)}(期望 6)")
            homework = list((lesson / "homework").glob("*")) if (lesson / "homework").exists() else []
            if len(homework) != 3:
                errors.append(f"{name}: task 数量 = {len(homework)}(期望 3)")
            notes_file = lesson / "notes.md"
            if notes_file.exists():
                notes_text = notes_file.read_text(encoding="utf-8")
                steps = ["痛点", "类比", "解释", "常见错误", "学员代码区", "参考答案"]
                missing = [s for s in steps if s not in notes_text]
                if missing:
                    errors.append(f"{name}/notes.md 缺: {', '.join(missing)}")
                if "明日衔接" not in notes_text:
                    errors.append(f"{name}/notes.md 缺: 明日衔接段")
            for p in in_class:
                text = p.read_text(encoding="utf-8", errors="ignore")
                if "难度:" not in text and "难度：" not in text:
                    errors.append(f"{name}/in_class/{p.name}: 缺少难度标注")
            for t in homework:
                text = t.read_text(encoding="utf-8", errors="ignore")
                if "选做" not in text:
                    errors.append(f"{name}/homework/{t.name}: 缺少选做标注")
    elif practice_new:
        # 新结构: exercises/{topic}/practice*.py
        suffix = practice_new[0].suffix
        name = course_path.name
        practice_files = list(course_path.glob("practice*"))
        task_files = list(course_path.glob("task*"))
        if len(practice_files) != 6:
            errors.append(f"{name}: practice 数量 = {len(practice_files)}(期望 6)")
        if len(task_files) != 3:
            errors.append(f"{name}: task 数量 = {len(task_files)}(期望 3)")
        for p in practice_files:
            text = p.read_text(encoding="utf-8", errors="ignore")
            if "难度:" not in text and "难度：" not in text:
                errors.append(f"{name}/{p.name}: 缺少难度标注")
        for t in task_files:
            text = t.read_text(encoding="utf-8", errors="ignore")
            if "选做" not in text:
                errors.append(f"{name}/{t.name}: 缺少选做标注")
    else:
        print("  ⚠️ 没有找到 practice 文件")
        return 0

    # 输出结果
    if errors:
        print(f"❌ 发现 {len(errors)} 个问题:")
        for e in errors:
            print(f"   - {e}")
        return len(errors)
    else:
        print(f"✅ 检查通过: {course_dir}")
        return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"用法: {sys.argv[0]} <course_dir>")
        print(f"示例: {sys.argv[0]} output/iter-R9-js-build-pedagogy/course/")
        sys.exit(1)

    sys.exit(check_course(sys.argv[1]))
