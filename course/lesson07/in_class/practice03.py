"""
[难度: ★★]
[所属知识点: 嵌套与可读性]
[预计完成时间: 10 分钟]

题目:下面这段代码缩进混乱,重新格式化它,让嵌套结构清晰。

混乱版本:
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<title>我的网页</title>
</head>
<body>
<header>
<h1>标题</h1>
<p>副标题</p>
</header>
<nav>
<a href="index.html">首页</a>
<a href="about.html">关于</a>
</nav>
<main>
<article>
<h2>文章标题</h2>
<p>文章内容<strong>加粗</strong>和<a href="#">链接</a>。</p>
</article>
</main>
<footer>
<p>© 2026</p>
</footer>
</body>
</html>

要求:
1. 每层嵌套缩进 4 空格
2. 闭标签与开标签对齐
3. 在 head 和 body 之间加空行
4. 在 header/nav/main/footer 之间加空行
"""

# ======================
# 学员代码区(重新格式化)
# ======================
pass
# 在这里写出格式化后的代码:

# ======================
# 测试区
# ======================
if __name__ == '__main__':
    print("参考答案:")
    print()
    print('<!DOCTYPE html>')
    print('<html lang="zh-CN">')
    print('<head>')
    print('    <meta charset="utf-8">')
    print('    <title>我的网页</title>')
    print('</head>')
    print()
    print('<body>')
    print('    <header>')
    print('        <h1>标题</h1>')
    print('        <p>副标题</p>')
    print('    </header>')
    print()
    print('    <nav>')
    print('        <a href="index.html">首页</a>')
    print('        <a href="about.html">关于</a>')
    print('    </nav>')
    print()
    print('    <main>')
    print('        <article>')
    print('            <h2>文章标题</h2>')
    print('            <p>文章内容<strong>加粗</strong>和'
          '<a href="#">链接</a>。</p>')
    print('        </article>')
    print('    </main>')
    print()
    print('    <footer>')
    print('        <p>© 2026</p>')
    print('    </footer>')
    print('</body>')
    print('</html>')
    print()
    print("要点:")
    print("  1. 每深一层,缩进增加 4 空格 ✓")
    print("  2. 闭标签与开标签在同一列 ✓")
    print("  3. 空行分隔逻辑块 ✓")
    print("  4. 内联元素(strong/a)保持在同一行 ✓")
