"""
[难度: ★★★]
[所属知识点: 目录结构设计]
[预计完成时间: 15 分钟]

题目:为一个"个人作品集"网站设计目录结构,并用 HTML 写出首页的框架。

要求:
1. 设计合理的目录结构(用 ASCII 文本图)
2. 包含以下页面:首页(index.html)、作品gallery.html、关于about.html、联系contact.html
3. 包含资源:css/style.css、js/main.js、images/ 下有 logo.jpg 和 作品图片
4. 在首页中正确使用相对路径引用 css 和 images
5. 首页包含语义化标签 header/nav/main/footer
"""

# ======================
# 学员代码区
# ======================

# 第一部分:设计目录结构
pass
# 在这里写出你的目录结构:

# 第二部分:写 index.html 框架
pass
# 在这里写出 index.html 代码:

# ======================
# 测试区
# ======================
if __name__ == '__main__':
    print("参考答案:")
    print()
    print("目录结构:")
    print("portfolio/")
    print("├── index.html")
    print("├── gallery.html")
    print("├── about.html")
    print("├── contact.html")
    print("├── css/")
    print("│   └── style.css")
    print("├── js/")
    print("│   └── main.js")
    print("└── images/")
    print("    ├── logo.jpg")
    print("    └── gallery/")
    print("        ├── project1.jpg")
    print("        └── project2.jpg")
    print()
    print("index.html:")
    print('<!DOCTYPE html>')
    print('<html lang="zh-CN">')
    print('<head>')
    print('    <meta charset="utf-8">')
    print('    <title>我的作品集</title>')
    print('    <link rel="stylesheet" href="css/style.css" />')
    print('</head>')
    print('<body>')
    print('    <header>')
    print('        <img src="images/logo.jpg" alt="Logo" />')
    print('        <h1>我的作品集</h1>')
    print('    </header>')
    print('    <nav>')
    print('        <a href="index.html">首页</a>')
    print('        <a href="gallery.html">作品</a>')
    print('        <a href="about.html">关于</a>')
    print('        <a href="contact.html">联系</a>')
    print('    </nav>')
    print('    <main>')
    print('        <!-- 作品展示 -->')
    print('    </main>')
    print('    <footer>')
    print('        <p>© 2026 我的作品集</p>')
    print('    </footer>')
    print('    <script src="js/main.js"></script>')
    print('</body>')
    print('</html>')
    print()
    print("验收要点:")
    print("  ✓ HTML 在根目录,css/js/images 分目录")
    print("  ✓ 图片作品放在 images/gallery/ 子目录")
    print("  ✓ 相对路径:href=\"css/style.css\" ✓")
    print("  ✓ 相对路径:src=\"images/logo.jpg\" ✓")
    print("  ✓ 语义化标签齐全")
