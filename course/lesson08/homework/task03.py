"""
[难度: ★★★★]
[所属知识点: 多页面站点导航]
[预计完成时间: 30 分钟]
[类型: 选做]

题目:你已经写好了一个首页 index.html(参考 task02),现在需要新增两个页面:
projects.html(作品展示) 和 contact.html(联系表单)。
三个页面共享同一套导航,用户从一个页面点导航能跳到另一个页面的对应位置。

要求:
1. 在下面补全三个页面的导航结构:
   - 每个页面的 <header> 里都有一套完整导航
   - 每个页面的导航都指向:
     index.html#hero → 首页
     index.html#travel → 游记(在首页)
     projects.html → 作品展示页
     contact.html → 联系页
2. 三个页面的 title 不同(首页/作品展示/联系)
3. 三个页面的 main 结构符合各自的页面定位

题目:补全下面 projects.html 的导航部分和 main 骨架。

    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="utf-8">
        <!-- TODO: title = "作品展示 - 小林 Wanderlust" -->
    </head>
    <body>
        <!-- TODO: header + nav(4 个链接) -->
        <!-- TODO: main 内含一个 section,标题 h2 "我的作品" -->
        <!--     和 ul 列出 3 个作品项(每项含 a 链接) -->
        <!-- TODO: footer 版权 -->
    </body>
    </html>
"""

# ======================
# 学员代码区(补全 projects.html)
# ======================
pass
# 在这里写出完整的 projects.html:


# ======================
# 测试区
# ======================
if __name__ == '__main__':
    print("参考答案(projects.html):")
    print()
    print('<!DOCTYPE html>')
    print('<html lang="zh-CN">')
    print('<head>')
    print('    <meta charset="utf-8">')
    print('    <title>作品展示 - 小林 Wanderlust</title>')
    print('</head>')
    print('<body>')
    print('    <header>')
    print('        <h1>小林 Wanderlust</h1>')
    print('        <nav>')
    print('            <a href="index.html#hero">首页</a>')
    print('            <a href="index.html#travel">游记</a>')
    print('            <a href="projects.html">作品</a>')
    print('            <a href="contact.html">联系</a>')
    print('        </nav>')
    print('    </header>')
    print()
    print('    <main>')
    print('        <section>')
    print('            <h2>我的作品</h2>')
    print('            <ul>')
    print('                <li><a href="#photo">摄影集</a></li>')
    print('                <li><a href="#video">旅拍视频</a></li>')
    print('                <li><a href="#article">专栏文章</a></li>')
    print('            </ul>')
    print('        </section>')
    print('    </main>')
    print()
    print('    <footer>')
    print('        <p><small>© 2026 小林 Wanderlust. 保留所有权利。</small></p>')
    print('    </footer>')
    print('</body>')
    print('</html>')
    print()
    print("要点:")
    print("  ✓ 跨页面导航用相对路径文件名(index.html)")
    print("  ✓ 页面内锚点用 #id")
    print("  ✓ 导航在三个页面保持一致性")
    print("  ✓ title 包含页面名 + 品牌名")
