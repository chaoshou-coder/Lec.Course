"""
[难度: ★★★]
[所属知识点: 综合应用(挑战题)]
[预计完成时间: 15 分钟]

题目:下面是一个"损坏"的多页面网站首页,有 5 处错误,找出来并写出正确版本。

损坏版本:
    <!DOCTYPE html>
    <html>
    <head>
    <title>我的网站</title>
    </head>
    <body>
    <header>
    <h1>我的网站</h1>
    </header>
    <nav>
    <a href="index.html">首页</a>
    <a href="About.html">关于</a>
    <a href="pages/contact.html">联系</a>
    </nav>
    <main>
    <article>
    <h2>文章标题</h2>
    <p>文章<img src="C:\Users\me\images\photo.jpg" alt="照片">内容</p>
    </article>
    </main>
    <footer>
    <p>© 2026</p>
    </footer>
    </body>
    </html>

要求:找出全部 5 处错误(提示:涉及 meta/缩进/路径/大小写/注释)
"""

# ======================
# 学员代码区(写出修正后的完整页面)
# ======================
pass
# 在这里写出修正后的完整 HTML 页面:

# ======================
# 测试区
# ======================
if __name__ == '__main__':
    print("5 处错误:")
    print()
    print("  1. 缺少 <meta charset=\"utf-8\">")
    print("     原因:没有 charset 中文可能乱码")
    print()
    print("  2. 代码完全没有缩进")
    print("     原因:应该每层缩进 4 空格,让结构清晰")
    print()
    print("  3. href=\"About.html\" 大小写不一致")
    print("     原因:建议统一小写 about.html,避免服务器上找不到")
    print()
    print("  4. href=\"pages/contact.html\" 但其他链接没有 pages/")
    print("     原因:如果 contact 在 pages/ 里,about 也应该在 pages/ 里")
    print()
    print("  5. img 的 src 用了绝对路径 C:\\Users\\...")
    print("     原因:绝对路径换台电脑就失效,应该用相对路径")
    print()
    print("修正后完整版本:")
    print()
    print('<!DOCTYPE html>')
    print('<html lang="zh-CN">')
    print('<head>')
    print('    <meta charset="utf-8">')
    print('    <title>我的网站</title>')
    print('</head>')
    print('<body>')
    print('    <header>')
    print('        <h1>我的网站</h1>')
    print('    </header>')
    print('    <nav>')
    print('        <a href="index.html">首页</a>')
    print('        <a href="about.html">关于</a>')
    print('        <a href="contact.html">联系</a>')
    print('    </nav>')
    print('    <main>')
    print('        <article>')
    print('            <h2>文章标题</h2>')
    print('            <p>文章<img src="images/photo.jpg" '
          'alt="照片" />内容</p>')
    print('        </article>')
    print('    </main>')
    print('    <footer>')
    print('        <p>© 2026</p>')
    print('    </footer>')
    print('</body>')
    print('</html>')
    print()
    print("边界测试(考考自己):")
    print("  - 如果 contact.html 确实在 pages/ 里,但 about.html 不在,怎么办?")
    print("    答:统一目录结构,要么都放根目录,要么都放 pages/")
    print("  - 注释 <!-- 临时隐藏 --> 里的代码会被浏览器渲染吗?")
    print("    答:不会,注释内容完全被浏览器忽略")
