"""
[难度: ★★★★]
[所属知识点: 综合应用(挑战题)]
[预计完成时间: 20 分钟]
[类型: 挑战题,不强制完成]

题目:下面是一个"损坏"的项目展示页,有 7 处错误。找出来并修正。

损坏版本:
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <header>
            <h2>小李工作室</h2>
            <nav>
                <a href="index.html">首页</a>
                <a href="projects.html">项目</a>
            </nav>
        </header>

        <main>
            <section id="projects">
                <ul>
                    <li>
                        <img src=project1.jpg alt=项目1 width=280 />
                        <h3><a href="#p1">品牌设计</a></h3>
                        <p>完整的品牌方案。</p>
                    </li>
                    <li>
                        <img src="project2.jpg" alt="项目2" width="280">
                        <h4>App 界面</h4>
                        <p>移动端界面设计。</p>
                    </li>
                    <img src="project3.jpg" alt="项目3" width="280" />
                    <li>
                        <h3><a href="#p3">包装设计</a></h3>
                        <p>高端产品的包装。</p>
                    </li>
                </ul>
            </section>
        </main>

        <footer>
            <p>© 2026 小李工作室</p>
        </footer>
    </body>
    </html>

要求:
1. 找出全部 7 处错误
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
    print("7 处错误及修正:")
    print()
    print("  1. <head> 缺少 <title>")
    print("     原因:每个 HTML 文档必须有 title")
    print()
    print("  2. 品牌名用了 <h2>,应改为 <h1>")
    print("     原因:页面主标题应用 h1,h2 级别不够")
    print()
    print("  3. 第一个 img 属性值未加引号")
    print("     原因:src/alt/width 的值必须用引号包裹")
    print()
    print("  4. 第二个 img 缺少自闭合斜杠 />")
    print("     原因:img 是自闭合标签,必须以 /> 结尾")
    print()
    print("  5. 第二个卡片的 h4 应改为 h3")
    print("     原因:三张卡片标题层级应一致,都用 h3")
    print()
    print("  6. 第三个 img 在 li 外面,且第三个 li 缺少 img")
    print("     原因:img 必须放在 li 内,且每张卡片结构应一致")
    print()
    print("  7. footer 缺少 small 标签")
    print("     原因:版权小字应用 small 标签包裹")
    print()
    print("修正后完整文档(关键部分):")
    print('<head>')
    print('    <meta charset="utf-8">')
    print('    <title>小李工作室</title>')
    print('</head>')
    print('<body>')
    print('    <header>')
    print('        <h1>小李工作室</h1>')
    print('        <nav>...</nav>')
    print('    </header>')
    print('    <main>')
    print('        <section id="projects">')
    print('            <h2>精选项目</h2>')
    print('            <ul>')
    print('                <li>')
    print('                    <img src="project1.jpg"')
    print('                         alt="品牌设计方案" width="280" />')
    print('                    <h3><a href="#p1">品牌设计</a></h3>')
    print('                    <p>完整的品牌方案。</p>')
    print('                </li>')
    print('                <li>')
    print('                    <img src="project2.jpg"')
    print('                         alt="App 界面 mockup" width="280" />')
    print('                    <h3><a href="#p2">App 界面</a></h3>')
    print('                    <p>移动端界面设计。</p>')
    print('                </li>')
    print('                <li>')
    print('                    <img src="project3.jpg"')
    print('                         alt="包装设计效果" width="280" />')
    print('                    <h3><a href="#p3">包装设计</a></h3>')
    print('                    <p>高端产品的包装。</p>')
    print('                </li>')
    print('            </ul>')
    print('        </section>')
    print('    </main>')
    print('    <footer>')
    print('        <p><small>© 2026 小李工作室</small></p>')
    print('    </footer>')
    print('</body>')
    print('</html>')
