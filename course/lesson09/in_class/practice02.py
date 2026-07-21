"""
[难度: ★★]
[所属知识点: ul/li 嵌套图片与文字]
[预计完成时间: 10 分钟]

题目:下面是一个"损坏"的卡片列表,有 4 处结构错误。找出来并修正。

损坏版本:
    <section>
        <h2>我的项目</h2>
        <ul>
            <img src="p1.jpg" alt="项目1" width="280">
            <li>
                <h3>项目一</h3>
                <p>这是第一个项目</p>
            </li>
            <li>
                <img src="p2.jpg" alt="项目2" width="280">
                <h3>项目二</h3>
            </li>
            <li>
                <h3>项目三</h3>
                <p>这是第三个项目</p>
                <img src="p3.jpg" alt="项目3" width="280">
            </li>
        </ul>
    </section>

要求:
1. 找出全部 4 处错误(提示:img 位置/自闭合/结构一致性)
2. 写出修正后的完整代码
"""

# ======================
# 学员代码区(写出修正后代码)
# ======================
pass
# 在这里写出修正后的完整 section:


# ======================
# 测试区
# ======================
if __name__ == '__main__':
    print("4 处错误及修正:")
    print()
    print("  1. 第一个 img 在 li 外面 → 移到第一个 li 里面")
    print("     原因:img 应该是 li 的子元素,不能直接放 ul 下")
    print()
    print("  2. 所有 img 缺少自闭合斜杠 → 末尾加 />")
    print("     原因:img 是自闭合标签,必须以 /> 结尾")
    print()
    print("  3. 第二个 li 缺少 p 描述 → 补上 p")
    print("     原因:三张卡片结构应一致,每张都有图+标题+描述")
    print()
    print("  4. 第三个 li 的 img 放在 p 后面 → 移到 h3 前面")
    print("     原因:卡片结构应统一为 图→标题→描述,顺序一致")
    print()
    print("修正后完整代码:")
    print('<section>')
    print('    <h2>我的项目</h2>')
    print('    <ul>')
    print('        <li>')
    print('            <img src="p1.jpg" alt="项目1" width="280" />')
    print('            <h3>项目一</h3>')
    print('            <p>这是第一个项目</p>')
    print('        </li>')
    print('        <li>')
    print('            <img src="p2.jpg" alt="项目2" width="280" />')
    print('            <h3>项目二</h3>')
    print('            <p>这是第二个项目</p>')
    print('        </li>')
    print('        <li>')
    print('            <img src="p3.jpg" alt="项目3" width="280" />')
    print('            <h3>项目三</h3>')
    print('            <p>这是第三个项目</p>')
    print('        </li>')
    print('    </ul>')
    print('</section>')
