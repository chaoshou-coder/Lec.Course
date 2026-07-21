"""
[难度: ★★★★]
[所属知识点: 综合应用(挑战题)]
[预计完成时间: 20 分钟]
[类型: 挑战题,不强制完成]

题目:下面是一个"损坏"的首页骨架,有 6 处语义化/结构错误。找出来并修正。

损坏版本:
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="utf-8">
        <title>小美的花店</title>
    </head>
    <body>
        <div class="header">
            <h3>小美花屋</h3>
            <div class="nav">
                <a href="#home">首页</a>
                <a href="#about">关于</a>
            </div>
        </div>

        <main>
            <div class="hero">
                <h2>让生活有花相伴</h2>
                <p>每周一束 · 全城配送</p>
            </div>
        </main>

        <main>
            <section>
                <p>我们精选全球鲜花,保证新鲜送达。</p>
            </section>
        </main>

        <div class="footer">
            <p>© 2026 小美花屋</p>
        </div>
    </body>
    </html>

要求:
1. 找出全部 6 处错误(提示:语义标签/div 滥用/重复 main/标题层级/footer)
2. 写出修正后的完整文档
3. 每处错误标注原因
"""

# ======================
# 学员代码区(写出修正后文档)
# ======================
pass
# 在这里写出修正后的完整文档:


# ======================
# 测试区
# ======================
if __name__ == '__main__':
    print("6 处错误及修正:")
    print()
    print("  1. <div class=\"header\"> → <header>")
    print("     原因:应用语义标签 header,不是 div")
    print()
    print("  2. <h3> → <h1>")
    print("     原因:品牌名是页面最重要的标题,应用 h1")
    print()
    print("  3. <div class=\"nav\"> → <nav>")
    print("     原因:导航链接组应用语义标签 nav")
    print()
    print("  4. 第二个 <main> 应删除,内容合并到第一个 <main>")
    print("     原因:一个文档只能有一个 <main>")
    print()
    print("  5. <section> 缺少标题(h2-h6)")
    print("     原因:每个 section 应有自己的标题说明主题")
    print()
    print("  6. <div class=\"footer\"> → <footer>")
    print("     原因:页脚应用语义标签 footer")
    print()
    print("修正后完整文档:")
    print('<!DOCTYPE html>')
    print('<html lang="zh-CN">')
    print('<head>')
    print('    <meta charset="utf-8">')
    print('    <title>小美的花店</title>')
    print('</head>')
    print('<body>')
    print('    <header>')
    print('        <h1>小美花屋</h1>')
    print('        <nav>')
    print('            <a href="#home">首页</a>')
    print('            <a href="#about">关于</a>')
    print('        </nav>')
    print('    </header>')
    print()
    print('    <main>')
    print('        <section id="hero">')
    print('            <h2>让生活有花相伴</h2>')
    print('            <p>每周一束 · 全城配送</p>')
    print('        </section>')
    print()
    print('        <section id="intro">')
    print('            <h2>关于我们</h2>')
    print('            <p>我们精选全球鲜花,保证新鲜送达。</p>')
    print('        </section>')
    print('    </main>')
    print()
    print('    <footer>')
    print('        <p><small>© 2026 小美花屋</small></p>')
    print('    </footer>')
    print('</body>')
    print('</html>')
