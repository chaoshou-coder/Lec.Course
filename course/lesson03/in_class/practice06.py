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
        <title>我的收藏</title>
    <body>
        <h1>我的收藏</h1>
        <h2>收藏的图片</h2>
        <img src="photo1.jpg">
        <img src="photo2.jpg" alt="照片2" />
        <h2>收藏的网站</h2>
        <ul>
            <p>https://www.example.com</p>
            <li><a "https://www.github.com">GitHub</a></li>
        </ul>
        <ol>
            <li>第一名</li>
            <li>第二名</li>
            第三名
        </ol>
    </body>
    </html>

要求:
1. 找出全部 6 处错误
2. 写出修正后的完整文档
3. 每处错误标注原因

提示:错误可能涉及 —— head 闭合/img alt/a href/ul 内放 p/ol 中缺 li/缺少 h2
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
    print("  2. <img src=\"photo1.jpg\"> 缺少 alt 属性")
    print("     原因:alt 是 img 的必填属性")
    print()
    print("  3. <p>...</p> 直接放在 ul 内")
    print("     原因:ul 的直接子元素必须是 li,不能是 p")
    print()
    print("  4. <a \"https://www.github.com\"> 缺少 href 属性名")
    print("     原因:href 是属性名,不能省略不写")
    print()
    print("  5. '第三名' 没有 li 标签包裹")
    print("     原因:ol 内的每一项都必须用 li 标签包裹")
    print()
    print("  6. <ol> 前面缺少 <h2> 标题")
    print("     原因:收藏排行没有对应的结构化标题(语义不完整)")
    print()
    print("修正后完整文档:")
    print('<!DOCTYPE html>')
    print('<html lang="zh-CN">')
    print('<head>')
    print('    <meta charset="utf-8">')
    print('    <title>我的收藏</title>')
    print('</head>')
    print('<body>')
    print('    <h1>我的收藏</h1>')
    print('    <h2>收藏的图片</h2>')
    print('    <img src="photo1.jpg" alt="照片1" />')
    print('    <img src="photo2.jpg" alt="照片2" />')
    print('    <h2>收藏的网站</h2>')
    print('    <ul>')
    print('        <li><a href="https://www.example.com">示例网站</a></li>')
    print('        <li><a href="https://www.github.com">GitHub</a></li>')
    print('    </ul>')
    print('    <h2>收藏排行</h2>')
    print('    <ol>')
    print('        <li>第一名</li>')
    print('        <li>第二名</li>')
    print('        <li>第三名</li>')
    print('    </ol>')
    print('</body>')
    print('</html>')
