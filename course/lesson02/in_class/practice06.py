"""
[难度: ★★★]
[所属知识点: 综合应用(挑战题)]
[预计完成时间: 15 分钟]
[类型: 挑战题,不强制完成]

题目:下面是一个"损坏"的 HTML 文档,有 6 处语法错误。找出来并修正。

损坏版本:
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="utf-8">
        <title>我的旅行日记</title>
    <body>
        <h1>云南之旅</h1>
        <h3>第一天:昆明</h3>
        <p>昆明四季如春,被称为春城。
        <h3>第二天:大理</h3>
        <p>大理的洱海很美。</p>
        <hr></hr>
        <h2>第三天:丽江</h2>
        <p>丽江古城很有味道。<br></br>
        <h6>旅行感悟</h6>
        <p>读万卷书,行万里路。
    </body>
    </html>

要求:
1. 找出全部 6 处错误
2. 写出修正后的完整文档
3. 每处错误标注原因

提示:错误可能涉及 —— 标题跳级、标签未闭合、br/hr 误用、p 标签未闭合
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
    print("  1. </head> 缺失")
    print("     原因:head 必须在 body 之前闭合")
    print()
    print("  2. <h3>第一天</h3> 前面没有 <h2>")
    print("     原因:标题不能从 h1 跳到 h3,中间必须有 h2")
    print()
    print("  3. <p>昆明四季如春...</p> 没有闭标签")
    print("     原因:p 标签必须闭合")
    print()
    print("  4. <hr></hr> → <hr>")
    print("     原因:hr 是自闭合标签,不能加闭标签")
    print()
    print("  5. <br></br> → <br>")
    print("     原因:br 是自闭合标签,不能加闭标签")
    print()
    print("  6. <p>读万卷书...</p> 没有闭标签")
    print("     原因:p 标签必须闭合")
    print()
    print("修正后完整文档:")
    print('<!DOCTYPE html>')
    print('<html lang="zh-CN">')
    print('<head>')
    print('    <meta charset="utf-8">')
    print('    <title>我的旅行日记</title>')
    print('</head>')
    print('<body>')
    print('    <h1>云南之旅</h1>')
    print('    <h2>行程安排</h2>')
    print('    <h3>第一天:昆明</h3>')
    print('    <p>昆明四季如春,被称为春城。</p>')
    print('    <h3>第二天:大理</h3>')
    print('    <p>大理的洱海很美。</p>')
    print('    <hr>')
    print('    <h2>第三天:丽江</h2>')
    print('    <p>丽江古城很有味道。<br>')
    print('    <h2>旅行感悟</h2>')
    print('    <p>读万卷书,行万里路。</p>')
    print('</body>')
    print('</html>')
