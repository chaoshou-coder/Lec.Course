"""
[难度: ★★★]
[所属知识点: 修复错误表格]
[预计完成时间: 15 分钟]
[类型: 选做]

题目:你收到一份"损坏"的 HTML 表格,本应显示"图书馆藏书目录",但渲染出错。

损坏版本:
    <table>
        <td>Python 编程</td>
        <td>张三</td>
        <td>2020</td>
        <tr>
            <th>书名</th>
            <th>作者</th>
            <th>出版年份</th>
        </tr>
        <tr>
            <td>算法导论</td>
            <td>李四</td>
        <tr>
            <td>深入理解计算机系统</td>
            <td>王五</td>
            <td>2016</td>
    </table>

要求:
1. 找出全部 6 处错误(提示:td 缺 tr/表头位置/单元格数不等/tr 未闭合/th 与 td 混淆/table 未闭合)
2. 写出修正后的完整文档
3. 保存为 library.html,用浏览器打开验证
"""

# ======================
# 学员代码区
# ======================
pass
# 在这里写出修正后的完整文档:


# ======================
# 测试区
# ======================
if __name__ == '__main__':
    print("6 处错误:")
    print("  1. 第一行 3 个 td 没有 tr 包裹")
    print("  2. 表头行(<th>)写在了数据行后面(应在第一行)")
    print("  3. 表头用的是 th,但数据行 1 用的是 td(这没错,但表头行本身位置错)")
    print("  4. 算法导论那行只有 2 个 td(缺出版年份)")
    print("  5. 算法导论那行的 tr 没有闭合标签 </tr>")
    print("  6. </table> 缺失")
    print()
    print("修正后完整文档(示例):")
    print('<table>')
    print('    <tr>')
    print('        <th>书名</th>')
    print('        <th>作者</th>')
    print('        <th>出版年份</th>')
    print('    </tr>')
    print('    <tr>')
    print('        <td>Python 编程</td>')
    print('        <td>张三</td>')
    print('        <td>2020</td>')
    print('    </tr>')
    print('    <tr>')
    print('        <td>算法导论</td>')
    print('        <td>李四</td>')
    print('        <td>2009</td>')
    print('    </tr>')
    print('    <tr>')
    print('        <td>深入理解计算机系统</td>')
    print('        <td>王五</td>')
    print('        <td>2016</td>')
    print('    </tr>')
    print('</table>')
