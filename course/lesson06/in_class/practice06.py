"""
[难度: ★★★]
[所属知识点: 综合应用(挑战题)]
[预计完成时间: 15 分钟]

题目:下面是一个"损坏"的页面,有 5 处错误,找出来并写出正确版本。

损坏版本:
    <!DOCTYPE html>
    <html>
    <head>
        <title>我的博客</title>
    </head>
    <body>
        <main>
            <h1>博客标题</h1>
            <nav>
                <a href="index.html">首页</a>
            </nav>
        </main>
        <main>
            <article>
                <h2>文章标题</h2>
                <p>文章内容...</p>
            </article>
        </main>
        <header>
            <p>© 2026 我的博客</p>
        </header>
    </body>
    </html>

要求:找出全部 5 处错误(提示:涉及 meta/main/header/nav/语义位置)
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
    print("  2. 有两个 <main>")
    print("     原因:一个页面只能有一个 main")
    print()
    print("  3. <header> 放在了 body 最后面")
    print("     原因:header 是页头,应该放在最前面")
    print()
    print("  4. <nav> 放在了 <main> 里面")
    print("     原因:nav 是独立导航,应该和 main 同级")
    print()
    print("  5. 最后一个 <header> 应该是 <footer>")
    print("     原因:版权信息放在 footer,不是 header")
    print()
    print("修正后完整版本:")
    print()
    print('<!DOCTYPE html>')
    print('<html lang="zh-CN">')
    print('<head>')
    print('    <meta charset="utf-8">')
    print('    <title>我的博客</title>')
    print('</head>')
    print('<body>')
    print('    <header>')
    print('        <h1>博客标题</h1>')
    print('    </header>')
    print('    <nav>')
    print('        <a href="index.html">首页</a>')
    print('    </nav>')
    print('    <main>')
    print('        <article>')
    print('            <h2>文章标题</h2>')
    print('            <p>文章内容...</p>')
    print('        </article>')
    print('    </main>')
    print('    <footer>')
    print('        <p>© 2026 我的博客</p>')
    print('    </footer>')
    print('</body>')
    print('</html>')
    print()
    print("边界测试(考考自己):")
    print("  - 如果 header 里不放 h1 可以吗?")
    print("    答:可以,header 不强制包含 h1")
    print("  - section 和 article 可以互相嵌套吗?")
    print("    答:可以,article 里可以有 section,section 里也可以有 article")
