"""
[难度: ★★★]
[所属知识点: 修复卡片结构错误]
[预计完成时间: 15 分钟]
[类型: 选做]

题目:你收到一份"卡片结构混乱"的项目展示 HTML,有 5 处错误。找出来并修正。

损坏版本:
    <section id="projects">
        <h2>作品</h2>
        <li>
            <img src="p1.jpg" alt="p1.jpg" width="280" />
            <h3>项目一</h3>
            <p>第一个项目。</p>
        </li>
        <ul>
            <li>
                <h3>项目二</h3>
                <p>第二个项目。</p>
                <img src="p2.jpg" alt="项目2图片" width=280 />
            </li>
        </ul>
        <ul>
            <li>
                <img src="p3.jpg" alt="项目3" width="280" />
                <h2>项目三</h2>
                <p>第三个项目。</p>
            </li>
        </ul>
    </section>

要求:
1. 找出全部 5 处错误(提示:ul/li 嵌套/img 位置/alt/标题层级/重复 ul)
2. 写出修正后的完整 section
3. 所有卡片结构统一为 图 → 标题 → 描述
"""

# ======================
# 学员代码区(写出修正后 section)
# ======================
pass
# 在这里写出修正后的完整 section:


# ======================
# 测试区
# ======================
if __name__ == '__main__':
    print("5 处错误及修正:")
    print()
    print("  1. 第一个 li 在 ul 外面 → 移到 ul 里")
    print("     原因:li 必须被 ul 包裹")
    print()
    print("  2. alt=\"p1.jpg\" 改为 alt=\"项目一的内容描述\"")
    print("     原因:alt 应该是图片视觉内容,不是文件名")
    print()
    print("  3. 第二个 li 的 img 应在 h3 前面")
    print("     原因:卡片结构应统一为 图→标题→描述")
    print()
    print("  4. width=280 应改为 width=\"280\"(加引号)")
    print("     原因:属性值必须用引号包裹")
    print()
    print("  5. 第三个卡片的 h2 应改为 h3(与另两张一致)")
    print("     原因:三张卡片标题层级应一致,用 h3")
    print()
    print("修正后完整 section:")
    print('<section id="projects">')
    print('    <h2>作品</h2>')
    print('    <ul>')
    print('        <li>')
    print('            <img src="p1.jpg"')
    print('                 alt="项目一的具体内容" width="280" />')
    print('            <h3>项目一</h3>')
    print('            <p>第一个项目。</p>')
    print('        </li>')
    print('        <li>')
    print('            <img src="p2.jpg"')
    print('                 alt="项目二的具体内容" width="280" />')
    print('            <h3>项目二</h3>')
    print('            <p>第二个项目。</p>')
    print('        </li>')
    print('        <li>')
    print('            <img src="p3.jpg"')
    print('                 alt="项目三的具体内容" width="280" />')
    print('            <h3>项目三</h3>')
    print('            <p>第三个项目。</p>')
    print('        </li>')
    print('    </ul>')
    print('</section>')
    print()
    print("要点:三张卡片应在一个 ul 里,结构完全一致")
