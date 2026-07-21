"""
[难度: ★★]
[所属知识点: 多页面链接]
[预计完成时间: 10 分钟]

题目:根据下面的目录结构,补全相对路径。

目录结构:
    my-site/
    ├── index.html
    ├── products.html
    ├── css/
    │   └── style.css
    └── pages/
        ├── about.html
        └── contact.html

要求:填写下面的 href 值:
"""

# ======================
# 学员代码区(填写 href 值)
# ======================
pass
# 1. 在 index.html 中链接到 products.html:
#    <a href="____">产品</a>

# 2. 在 index.html 中链接到 pages/about.html:
#    <a href="____">关于</a>

# 3. 在 pages/about.html 中链接回 index.html:
#    <a href="____">首页</a>

# 4. 在 pages/about.html 中链接到 pages/contact.html:
#    <a href="____">联系</a>

# 5. 在 pages/contact.html 中链接到 css/style.css:
#    <link rel="stylesheet" href="____" />

# ======================
# 测试区
# ======================
if __name__ == '__main__':
    print("参考答案:")
    print()
    print("1. <a href=\"products.html\">产品</a>")
    print("   解释:同目录,直接写文件名")
    print()
    print("2. <a href=\"pages/about.html\">关于</a>")
    print("   解释:进入 pages 子目录找 about.html")
    print()
    print("3. <a href=\"../index.html\">首页</a>")
    print("   解释:../ 回到上级目录,再找 index.html")
    print()
    print("4. <a href=\"contact.html\">联系</a>")
    print("   解释:同目录(pages/),直接写文件名")
    print()
    print("5. <link rel=\"stylesheet\" href=\"../css/style.css\" />")
    print("   解释:../ 回到上级,再进 css 目录找 style.css")
    print()
    print("路径规则总结:")
    print("  - 同目录:直接写文件名")
    print("  - 子目录:目录名/文件名")
    print("  - 上级目录:../文件名")
