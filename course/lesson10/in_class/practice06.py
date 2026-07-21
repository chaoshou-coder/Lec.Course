"""
[难度: ★★★★]
[所属知识点: 综合应用(挑战题)]
[预计完成时间: 20 分钟]
[类型: 挑战题,不强制完成]

题目:下面是一个"损坏"的联系表单页,有 7 处错误。找出来并修正。

损坏版本:
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <header>
            <h1>小张工作室</h1>
            <nav>
                <a href="index.html">首页</a>
                <a href="projects.html">作品</a>
                <a href="contact.html">联系</a>
            </nav>
        </header>

        <main>
            <section id="contact">
                <h2>联系我</h2>
                <form action="#" method="get">
                    <p>
                        <label for="name">姓名</label>
                        <input type="text" id="name" />
                    </p>
                    <p>
                        <label for="mail">邮箱</label>
                        <input type="text" id="mail" name="mail" />
                    </p>
                    <p>
                        <label for="msg">留言</label>
                        <input id="msg" name="msg" rows="5" />
                    </p>
                    <button>提交</button>
                </form>
            </section>
        </main>

        <footer>
            <p>© 2026 小张工作室</p>
        </footer>
    </body>
    </html>

要求:
1. 找出全部 7 处错误(提示:title/name 缺失/类型错误/textarea/label 关联等)
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
    print("  2. 姓名 input 缺少 name 属性")
    print("     原因:name 是提交时的字段名,没 name 数据丢失")
    print()
    print("  3. 邮箱 input type=\"text\" 应改为 type=\"email\"")
    print("     原因:邮箱字段应用 email 类型,带格式校验")
    print()
    print("  4. 留言用了 input,应改为 textarea")
    print("     原因:留言是多行文本,input 只能单行")
    print()
    print("  5. textarea 的 rows 属性不能用在 input 上")
    print("     原因:input 没有 rows 属性,只有 textarea 有")
    print()
    print("  6. button 缺少 type=\"submit\"")
    print("     原因:在 form 中 button 默认 type 是 submit,")
    print("          但显式声明更清晰可靠")
    print()
    print("  7. footer 缺少 small 标签")
    print("     原因:版权小字应用 small 标签包裹")
    print()
    print("修正后完整文档(关键部分):")
    print('<head>')
    print('    <meta charset="utf-8">')
    print('    <title>联系我 - 小张工作室</title>')
    print('</head>')
    print('<body>')
    print('    ...')
    print('    <form action="#" method="post">')
    print('        <p>')
    print('            <label for="name">姓名</label>')
    print('            <input type="text" id="name" name="name" />')
    print('        </p>')
    print('        <p>')
    print('            <label for="mail">邮箱</label>')
    print('            <input type="email" id="mail" name="mail" />')
    print('        </p>')
    print('        <p>')
    print('            <label for="msg">留言</label>')
    print('            <textarea id="msg" name="msg"')
    print('                      rows="5" cols="30"></textarea>')
    print('        </p>')
    print('        <button type="submit">提交</button>')
    print('    </form>')
    print('    ...')
    print('    <footer>')
    print('        <p><small>© 2026 小张工作室</small></p>')
    print('    </footer>')
    print('</body>')
    print('</html>')
