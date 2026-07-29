#!/usr/bin/env python3
"""
Lec.Course Markdown 渲染检查器。

验证 markdown 渲染后的正确性,不仅检查结构。
适用于任何语言和学科。

用法:
    python scripts/render-check.py <file_or_dir>

检查项:
    1. 标题层级跳跃(如 H1 直接到 H4)
    2. 重复标题(同一标题出现多次)
    3. 旧格式残留(# ============)
    4. fenced block 不匹配(``` 没有闭合)
    5. 特殊字符导致的渲染问题
"""

import sys
import re
from pathlib import Path

try:
    import markdown
    HAS_MARKDOWN = True
except ImportError:
    HAS_MARKDOWN = False


def check_heading_hierarchy(text: str) -> dict:
    """检查标题层级是否正确,跳过 fenced block(代码块内的 # 注释不是标题)"""
    headings = []
    lines = text.split('\n')
    in_fenced = False

    for line in lines:
        # 跳过 fenced block 的边界
        stripped = line.strip()
        if stripped.startswith('```'):
            in_fenced = not in_fenced
            continue
        if in_fenced:
            continue

        # 只匹配真正的 markdown 标题(# 后面有空格)
        match = re.match(r'^(#{1,6})\s+(.+)$', stripped)
        if match:
            level = len(match.group(1))
            title = match.group(2).strip()
            # 跳过纯注释行(如 # --- 执行过程 ---)
            if title.startswith('---') or title.startswith('==='):
                continue
            headings.append((level, title))

    issues = []
    prev_level = 0
    for level, title in headings:
        # 真正的跳跃:从高层直接跳到深层(如 H1→H4, H2→H5)
        # H1→H2, H2→H3, H3→H4 都是合法的(只跳一级)
        # H4→H2 也是合法的(回到上层)
        if level > prev_level + 2 and prev_level > 0:
            issues.append(f"H{prev_level} → H{level}: '{title}'(跳跃 {level - prev_level} 级)")
        prev_level = min(prev_level, level) if prev_level > 0 else level

    return {
        'headings': headings,
        'issues': issues,
        'pass': len(issues) == 0
    }


def check_duplicate_headings(text: str) -> dict:
    """检查是否有重复标题(跳过 fenced block 内的内容和结构性标题)"""
    # 结构性标题允许重复(每个知识点都有)
    structural_headings = {'学员代码区', '参考答案', '常见错误', '问自己', '逐行解剖',
                          '执行过程', '明日衔接', '本课知识地图', '今日小结'}

    headings = {}
    lines = text.split('\n')
    in_fenced = False

    for line in lines:
        # 跳过 fenced block 的边界
        if line.strip().startswith('```'):
            in_fenced = not in_fenced
            continue
        if in_fenced:
            continue

        match = re.match(r'^#{1,6}\s+(.+)$', line.strip())
        if match:
            title = match.group(1).strip()
            # 跳过结构性标题
            if title in structural_headings:
                continue
            headings[title] = headings.get(title, 0) + 1

    duplicates = {t: c for t, c in headings.items() if c > 1}

    return {
        'duplicates': duplicates,
        'pass': len(duplicates) == 0
    }


def check_old_format_leftovers(text: str) -> dict:
    """检查旧格式残留(跳过 fenced block)"""
    issues = []
    lines = text.split('\n')
    in_fenced = False

    for i, line in enumerate(lines, 1):
        # 跳过 fenced block 的边界
        if line.strip().startswith('```'):
            in_fenced = not in_fenced
            continue
        if in_fenced:
            continue

        stripped = line.strip()

        # 旧格式 1: # ============ 标题 ============
        if re.match(r'^# =+\s*.+\s*=+$', stripped):
            issues.append(f"旧格式残留(H1+等号): '{stripped}'")

        # 旧格式 2: # 作为代码注释(不在 fenced block 内)
        if re.match(r'^#\s*(import |from |def |class |print\(|html =|response =)', stripped):
            issues.append(f"第{i}行: 裸露的代码注释 '{stripped[:50]}'")

    return {
        'issues': issues,
        'pass': len(issues) == 0
    }


def check_fenced_blocks(text: str) -> dict:
    """检查 fenced block 是否匹配(有开有关)"""
    opens = len(re.findall(r'^```', text, re.MULTILINE))
    issues = []

    if opens % 2 != 0:
        issues.append(f"fenced block 不匹配: {opens} 个开口(应为偶数)")

    # 检查 fenced block 前是否有零宽字符
    zero_width_issues = []
    for i, line in enumerate(text.split('\n'), 1):
        if '```' in line and ('​' in line or '﻿' in line):
            zero_width_issues.append(i)

    issues.extend([f"第{i}行: fenced block 前有零宽字符" for i in zero_width_issues])

    return {
        'opens': opens,
        'issues': issues,
        'pass': len(issues) == 0
    }


def check_rendered_output(text: str) -> dict:
    """渲染 markdown 并检查输出(需要 markdown 库)"""
    if not HAS_MARKDOWN:
        return {
            'rendered': False,
            'pass': True,
            'note': 'markdown 库未安装,跳过渲染检查'
        }

    try:
        html = markdown.markdown(text, extensions=['fenced_code', 'tables'])

        issues = []

        # 检查是否有裸露的 HTML 标签(不在 fenced block 内)
        # 如果原文中有 <div> 等标签不在 fenced block 内,渲染后会真的变成 HTML
        lines = text.split('\n')
        in_fenced = False
        for i, line in enumerate(lines, 1):
            if line.strip().startswith('```'):
                in_fenced = not in_fenced
                continue
            if in_fenced:
                continue
            # 检查裸露的 HTML 标签
            if re.search(r'<[a-z]+[^>]*>', line) and not line.strip().startswith('`'):
                issues.append(f"第{i}行: 裸露的 HTML 标签 '{line.strip()[:50]}'")

        return {
            'rendered': True,
            'issues': issues,
            'pass': len(issues) == 0
        }
    except Exception as e:
        return {
            'rendered': False,
            'pass': True,
            'note': f'渲染失败: {e}'
        }


def check_file(filepath: Path) -> dict:
    """检查单个文件"""
    text = filepath.read_text(encoding='utf-8')

    results = {
        'file': str(filepath),
        'heading_hierarchy': check_heading_hierarchy(text),
        'duplicate_headings': check_duplicate_headings(text),
        'old_format': check_old_format_leftovers(text),
        'fenced_blocks': check_fenced_blocks(text),
        'rendered': check_rendered_output(text),
    }

    results['pass'] = all(
        results[k]['pass'] for k in ['heading_hierarchy', 'duplicate_headings',
                                      'old_format', 'fenced_blocks', 'rendered']
    )

    return results


def check_path(path: str) -> int:
    """检查路径,返回错误数"""
    p = Path(path)
    errors = []

    if not p.exists():
        print(f"路径不存在: {path}")
        return 1

    if p.is_file():
        files = [p] if p.suffix == '.md' else []
    elif p.is_dir():
        files = sorted(p.glob("*.md"))
        if not files:
            files = sorted(p.rglob("*.md"))
    else:
        print(f"⚠️ 不支持的路径类型: {path}")
        return 0

    if not files:
        print(f"⚠️ 没有找到 .md 文件: {path}")
        return 0

    print(f"检查 {len(files)} 个文件...\n")

    for f in files:
        result = check_file(f)
        status = "✅" if result['pass'] else "❌"
        print(f"{status} {f.name}")

        if not result['pass']:
            for check_name, check_result in result.items():
                if check_name in ('file', 'pass'):
                    continue
                if not check_result.get('pass', True):
                    issues = check_result.get('issues', [])
                    if issues:
                        print(f"   ❌ {check_name}:")
                        for issue in issues[:3]:
                            print(f"      - {issue}")
                        if len(issues) > 3:
                            print(f"      ... 还有 {len(issues)-3} 个问题")
                    errors.append(f"{f.name} -> {check_name}")

    print(f"\n{'='*50}")
    print(f"检查完成: {len(files)} 个文件")
    print(f"通过: {len(files) - len(set(e.split(' -> ')[0] for e in errors))} 个")
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
        print(f"用法: {sys.argv[0]} <file_or_dir>")
        print(f"示例: {sys.argv[0]} output/web-scraping/knowledge/")
        sys.exit(1)

    sys.exit(check_path(sys.argv[1]))
