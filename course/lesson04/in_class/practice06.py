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
        <title>成绩单</title>
    <body>
        <h1>期末成绩</h1>
        <table>
            <td>张三</td>
            <td>90</td>
            <td>85</td>
        <tr>
            <th>姓名</th>
            <th>语文</th>
            <th>数学</th>
        </tr>
        <tr>
            <td>李四</td>
            <td>88</td>
        <tr>
            <td>王五</td>
            <td>82</td>
            <td>78</td>
        </tr>
    </body>
    </html>

要求:
1. 找出全部 6 处错误
2. 写出修正后的完整文档
3. 每处错误标注原因

提示:错误可能涉及 —— head 闭合/td 缺 tr/表头位置/行单元格数不等/tr 未闭合/table 未闭合
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
    print("  2. 第一行的 3 个 td 没有 tr 包裹")
    print("     原因:td 必须放在 tr 里")
    print()
    print("  3. 表头行(<th>)写在了数据行后面")
    print("     原因:表头行应该放在表格第一行")
    print()
    print("  4. 李四那行只有 2 个 td(缺数学成绩)")
    print("     原因:每行单元格数量应与表头 3 列一致")
    print()
    print("  5. 李四那行的 tr 没有闭合标签 </tr>")
    print("     原因:tr 必须闭合")
    print()
    print("  6. </table> 缺失")
    print("     原因:table 必须闭合")
    print()
    print("修正后完整文档:")
    print('<!DOCTYPE html>')
    print('<html lang="zh-CN">')
    print('<head>')
    print('    <meta charset="utf-8">')
    print('    <title>成绩单</title>')
    print('</head>')
    print('<body>')
    print('    <h1>期末成绩</h1>')
    print('    <table>')
    print('        <tr>')
    print('            <th>姓名</th>')
    print('            <th>语文</th>')
    print('            <th>数学</th>')
    print('        </tr>')
    print('        <tr>')
    print('            <td>张三</td>')
    print('            <td>90</td>')
    print('            <td>85</td>')
    print('        </tr>')
    print('        <tr>')
    print('            <td>李四</td>')
    print('            <td>88</td>')
    print('            <td>(缺考)</td>')
    print('        </tr>')
    print('        <tr>')
    print('            <td>王五</td>')
    print('            <td>82</td>')
    print('            <td>78</td>')
    print('        </tr>')
    print('    </table>')
    print('</body>')
    print('</html>')
