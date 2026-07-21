"""
[难度: ★★★]
[所属知识点: 综合应用(挑战题)]
[预计完成时间: 15 分钟]
[类型: 挑战题,不强制完成]

题目:下面是一个"损坏"的 HTML 文档,有 5 处语法错误。找出来并修正。

损坏版本:
    <DOCTYPE html>
    <HTML lang="en">
    <head>
        <meta charset=utf-8>
    <body>
        <h1>欢迎来到我的博客</h1>
        <p>这是我的第一篇文章
        <img src="blog.jpg" alt="博客封面">
        <br>
    </head>
    </body>
    </html>

要求:
1. 找出全部 5 处错误
2. 写出修正后的完整文档
3. 每处错误标注原因

提示:错误可能涉及 —— DOCTYPE 写法、标签大小写、属性引号、标签闭合顺序、自闭合标签
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
    print("5 处错误及修正:")
    print()
    print("  1. <DOCTYPE html> → <!DOCTYPE html>")
    print("     原因:DOCTYPE 前面必须是感叹号,不是尖括号")
    print()
    print("  2. <HTML lang=\"en\"> → <html lang=\"zh-CN\">")
    print("     原因:标签名应小写;语言应设为中文 zh-CN")
    print()
    print("  3. <meta charset=utf-8> → <meta charset=\"utf-8\">")
    print("     原因:属性值必须用引号包裹")
    print()
    print("  4. </head> 写在了 <body> 后面")
    print("     原因:head 必须先闭合,body 才能开始")
    print()
    print("  5. <p> 没有闭标签")
    print("     原因:段落内容结束后必须写 </p>")
    print()
    print("修正后完整文档:")
    print('<!DOCTYPE html>')
    print('<html lang="zh-CN">')
    print('<head>')
    print('    <meta charset="utf-8">')
    print('    <title>我的博客</title>')
    print('</head>')
    print('<body>')
    print('    <h1>欢迎来到我的博客</h1>')
    print('    <p>这是我的第一篇文章</p>')
    print('    <img src="blog.jpg" alt="博客封面" />')
    print('    <br />')
    print('</body>')
    print('</html>')
