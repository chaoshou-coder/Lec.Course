"""
[难度: ★★★]
[所属知识点: 卡片内添加链接]
[预计完成时间: 15 分钟]

题目:下面 3 张卡片都没有链接,请按规则为每张卡片加上跳转链接。

规则:
- 把 h3 的标题包上 a 标签(整张卡片可点的感觉)
- href 指向对应详情页,格式: project-1.html / project-2.html / project-3.html
- a 标签必须有 href 属性

原版本(无链接):
    <li>
        <img src="p1.jpg" alt="品牌设计方案" width="280" />
        <h3>品牌设计</h3>
        <p>从 0 到 1 打造品牌。</p>
    </li>
    <li>
        <img src="p2.jpg" alt="App 界面" width="280" />
        <h3>App 界面</h3>
        <p>简洁易用的产品体验。</p>
    </li>
    <li>
        <img src="p3.jpg" alt="包装设计" width="280" />
        <h3>包装设计</h3>
        <p>产品卖相,从包装开始。</p>
    </li>

要求:
1. 每张卡片的 h3 内容用 a 包裹
2. href 为对应的详情页
3. a 标签写在 h3 内部(h3 包住 a,不是 a 包住 h3)
"""

# ======================
# 学员代码区(补全链接后的 li)
# ======================
pass
# 在这里写出三张带链接的 li:


# ======================
# 测试区
# ======================
if __name__ == '__main__':
    print("参考答案:")
    print()
    print('<li>')
    print('    <img src="p1.jpg" alt="品牌设计方案" width="280" />')
    print('    <h3><a href="project-1.html">品牌设计</a></h3>')
    print('    <p>从 0 到 1 打造品牌。</p>')
    print('</li>')
    print('<li>')
    print('    <img src="p2.jpg" alt="App 界面" width="280" />')
    print('    <h3><a href="project-2.html">App 界面</a></h3>')
    print('    <p>简洁易用的产品体验。</p>')
    print('</li>')
    print('<li>')
    print('    <img src="p3.jpg" alt="包装设计" width="280" />')
    print('    <h3><a href="project-3.html">包装设计</a></h3>')
    print('    <p>产品卖相,从包装开始。</p>')
    print('</li>')
    print()
    print("要点:")
    print("  ✓ a 在 h3 内部(h3 > a > 文字)")
    print("  ✓ href 指向具体页面")
    print("  ✓ 文字仍是标题语义(a 不改变 h3 含义)")
