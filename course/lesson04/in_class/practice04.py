"""
[难度: ★★]
[所属知识点: 多行多列表格]
[预计完成时间: 10 分钟]

题目:补全下面的表格,制作一个 3 行 4 列的课程表(含表头)。

    <h1>课程表</h1>
    <table>
        <tr>
            <th>节次</th>
            <th>周一</th>
            <th>周二</th>
            <th>周三</th>
        </tr>
        <tr>
            <td>第 1 节</td>
            <td>???</td>
            <td>???</td>
            <td>???</td>
        </tr>
        <tr>
            <td>第 2 节</td>
            <td>???</td>
            <td>???</td>
            <td>???</td>
        </tr>
    </table>

要求:
1. 第 1 节:周一 = 语文, 周二 = 数学, 周三 = 英语
2. 第 2 节:周一 = 物理, 周二 = 化学, 周三 = 生物
3. 每行 4 个单元格,与表头 4 列对齐
"""

# ======================
# 学员代码区(写出完整表格)
# ======================
pass
# 在这里写出完整课程表:


# ======================
# 测试区
# ======================
if __name__ == '__main__':
    print("参考答案(完整课程表):")
    print()
    print('<h1>课程表</h1>')
    print('<table>')
    print('    <tr>')
    print('        <th>节次</th>')
    print('        <th>周一</th>')
    print('        <th>周二</th>')
    print('        <th>周三</th>')
    print('    </tr>')
    print('    <tr>')
    print('        <td>第 1 节</td>')
    print('        <td>语文</td>')
    print('        <td>数学</td>')
    print('        <td>英语</td>')
    print('    </tr>')
    print('    <tr>')
    print('        <td>第 2 节</td>')
    print('        <td>物理</td>')
    print('        <td>化学</td>')
    print('        <td>生物</td>')
    print('    </tr>')
    print('</table>')
    print()
    print("检查要点:")
    print("  ✓ 表头 4 列:节次/周一/周二/周三")
    print("  ✓ 每行数据 4 个 td,与表头对齐")
    print("  ✓ 嵌套顺序 table → tr → td/th")
