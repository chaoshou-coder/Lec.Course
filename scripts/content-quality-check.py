#!/usr/bin/env python3
"""
Lec.Course 内容质量检查器(v1.2)。

检查知识点的教学质量,不依赖特定文件格式。
适用于任何语言(Python/JS/SQL)和任何学科(数学/物理/通用知识)。

用法:
    python scripts/content-quality-check.py <knowledge_dir>

检查项:
    1. 执行过程跟踪: 是否有编号步骤(①②③④)
    2. NCDL Break It: 标了 teaching_method=ncdl 的节点是否有 Break It 演示
    3. 知识点后练习: 每个主要知识点后是否有学员练习区
    4. 常见错误: 是否包含具体错误信息(如 `Error:` 或 `错误`)
    5. 代码注释密度: 代码块内是否有足够的行注释

示例:
    python scripts/content-quality-check.py output/lec-python-v2/knowledge/
"""

import sys
import os
import re
from pathlib import Path


def check_numbered_steps(text: str) -> dict:
    """检查是否有编号步骤(①②③④)"""
    # 匹配 ① ② ③ ④ 或 1. 2. 3. 等格式
    numbered_pattern = re.compile(r'[①②③④⑤⑥⑦⑧⑨⑩]|\d+\.\s+\S')
    matches = numbered_pattern.findall(text)

    # 检查是否在"执行过程"或"逐行解剖"附近
    execution_keywords = ['执行过程', '逐行解剖', '执行流程', '跟踪']
    has_execution_context = any(kw in text for kw in execution_keywords)

    return {
        'count': len(matches),
        'has_execution_context': has_execution_context,
        'pass': len(matches) >= 4 and has_execution_context
    }


def check_break_it(text: str, teaching_method: str = None) -> dict:
    """检查 NCDL Break It 演示"""
    has_break_it = 'BREAK IT' in text or 'Break It' in text or '反模式' in text

    # 如果标了 ncdl,必须有 Break It
    if teaching_method == 'ncdl':
        return {
            'required': True,
            'present': has_break_it,
            'pass': has_break_it
        }
    else:
        return {
            'required': False,
            'present': has_break_it,
            'pass': True  # 不标 ncdl 的不强制
        }


def check_student_practice(text: str) -> dict:
    """检查每个知识点后是否有学员练习区"""
    # 查找学员代码区/练习区/思考题
    practice_markers = ['学员代码区', '练习区', '思考题', '动手做', '试一试', '学以致用']
    practice_count = sum(text.count(m) for m in practice_markers)

    # 查找知识点小节数量(#### 标题)
    sections = re.findall(r'^####\s+.+', text, re.MULTILINE)
    section_count = len(sections)

    # 每个知识点后应该有练习(允许最后几个综合章节没有)
    expected_min = max(1, section_count - 2)

    return {
        'practice_count': practice_count,
        'section_count': section_count,
        'expected_min': expected_min,
        'pass': practice_count >= expected_min
    }


def check_error_messages(text: str) -> dict:
    """检查常见错误是否包含具体错误信息"""
    # 匹配 Python/JS/Java 等语言的报错格式
    error_patterns = [
        r'[A-Za-z]+Error:',           # Python/JS 报错
        r'[A-Za-z]+Exception:',       # Java 报错
        r'报错[：:]\s*`[^`]+`',       # 中文描述+反引号报错
        r'错误现象[：:]',              # 中文"错误现象"
        r'SyntaxError',               # 常见错误类型
        r'TypeError',
        r'NameError',
        r'ValueError',
        r'AttributeError',
        r'IndexError',
        r'KeyError',
        r'ReferenceError',            # JS
    ]

    error_count = 0
    for pattern in error_patterns:
        matches = re.findall(pattern, text)
        error_count += len(matches)

    # 检查"常见错误"段是否存在
    has_error_section = '常见错误' in text or '常见报错' in text or '易错点' in text

    return {
        'error_message_count': error_count,
        'has_error_section': has_error_section,
        'pass': error_count >= 2 and has_error_section
    }


def check_code_comments(text: str) -> dict:
    """检查代码块内是否有足够的行注释"""
    # 查找代码块(```...``` 或 缩进代码)
    code_blocks = re.findall(r'```[\w]*\n(.*?)```', text, re.DOTALL)

    if not code_blocks:
        # 没有代码块(可能是数学/纯理论),跳过
        return {
            'has_code': False,
            'pass': True,
            'comment_ratio': None
        }

    total_lines = 0
    commented_lines = 0

    for block in code_blocks:
        lines = block.strip().split('\n')
        for line in lines:
            stripped = line.strip()
            if not stripped or stripped.startswith('#') or stripped.startswith('//'):
                continue  # 空行或纯注释行
            total_lines += 1
            # 检查行内注释
            if '#' in stripped or '//' in stripped or '/*' in stripped:
                commented_lines += 1

    if total_lines == 0:
        return {
            'has_code': True,
            'pass': True,
            'comment_ratio': None
        }

    ratio = commented_lines / total_lines if total_lines > 0 else 0

    return {
        'has_code': True,
        'total_code_lines': total_lines,
        'commented_lines': commented_lines,
        'comment_ratio': round(ratio, 2),
        'pass': ratio >= 0.4  # 至少 40% 的代码行有注释(复杂概念可适当降低)
    }


def check_knowledge_file(filepath: Path) -> dict:
    """检查单个知识点文件"""
    text = filepath.read_text(encoding='utf-8')

    # 从文件名或内容推断 teaching_method
    teaching_method = None
    if 'ncdl' in filepath.name.lower() or 'negative' in filepath.name.lower():
        teaching_method = 'ncdl'
    # 也可以从内容推断
    if 'NCDL' in text and 'Break It' in text:
        teaching_method = 'ncdl'

    results = {
        'file': str(filepath),
        'numbered_steps': check_numbered_steps(text),
        'break_it': check_break_it(text, teaching_method),
        'student_practice': check_student_practice(text),
        'error_messages': check_error_messages(text),
        'code_comments': check_code_comments(text),
    }

    # 总体是否通过
    results['pass'] = all(
        results[k]['pass'] for k in ['numbered_steps', 'break_it', 'student_practice',
                                      'error_messages', 'code_comments']
    )

    return results


def check_knowledge_path(knowledge_path: str) -> int:
    """检查知识点目录或文件,返回错误数"""
    errors = []
    path = Path(knowledge_path)

    if not path.exists():
        print(f"路径不存在: {knowledge_path}")
        return 1

    # 支持单个文件或目录
    if path.is_file():
        md_files = [path] if path.suffix == '.md' else []
    elif path.is_dir():
        md_files = sorted(path.glob("*.md"))
        if not md_files:
            md_files = sorted(path.rglob("*.md"))
    else:
        print(f"⚠️ 不支持的路径类型: {knowledge_path}")
        return 0

    if not md_files:
        print(f"⚠️ 没有找到 .md 文件: {knowledge_path}")
        return 0

    print(f"检查 {len(md_files)} 个知识点文件...\n")

    for md_file in md_files:
        result = check_knowledge_file(md_file)
        status = "✅" if result['pass'] else "❌"
        print(f"{status} {md_file.name}")

        if not result['pass']:
            for check_name, check_result in result.items():
                if check_name in ('file', 'pass'):
                    continue
                if not check_result.get('pass', True):
                    detail = ""
                    if check_name == 'numbered_steps':
                        detail = f"(编号步骤数: {check_result['count']}, "
                        detail += f"执行过程上下文: {check_result['has_execution_context']})"
                    elif check_name == 'break_it' and check_result.get('required'):
                        detail = "(标了 teaching_method=ncdl,但缺少 Break It 演示)"
                    elif check_name == 'student_practice':
                        detail = f"(练习数: {check_result['practice_count']}, "
                        detail += f"知识点数: {check_result['section_count']})"
                    elif check_name == 'error_messages':
                        detail = f"(具体错误数: {check_result['error_message_count']}, "
                        detail += f"错误段存在: {check_result['has_error_section']})"
                    elif check_name == 'code_comments' and check_result.get('has_code'):
                        detail = f"(注释覆盖率: {check_result['comment_ratio']*100:.0f}%)"

                    print(f"   ❌ {check_name}: 未通过 {detail}")
                    errors.append(f"{md_file.name} -> {check_name}")

    # 输出总结
    print(f"\n{'='*50}")
    print(f"检查完成: {len(md_files)} 个文件")
    print(f"通过: {len(md_files) - len(set(e.split(' -> ')[0] for e in errors))} 个")
    print(f"未通过: {len(set(e.split(' -> ')[0] for e in errors))} 个")

    if errors:
        print(f"\n需要修复的问题:")
        for e in sorted(set(errors)):
            print(f"  - {e}")
        return len(errors)
    else:
        print("\n✅ 全部通过!")
        return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"用法: {sys.argv[0]} <knowledge_dir>")
        print(f"示例: {sys.argv[0]} output/lec-python-v2/knowledge/")
        sys.exit(1)

    sys.exit(check_knowledge_path(sys.argv[1]))
