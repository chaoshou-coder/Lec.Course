"""
[难度: ★★★]
[所属知识点: 制作课程表]
[预计完成时间: 20 分钟]
[类型: 选做]

题目:用 HTML 表格制作一张"一周课程表"。

下面是一周课程安排,请用合适的 HTML 表格标签重新组织:

    节次      周一    周二    周三    周四    周五
    第 1 节   语文    数学    英语    物理    化学
    第 2 节   数学    英语    语文    化学    生物
    第 3 节   英语    物理    数学    生物    历史
    第 4 节   体育    化学    历史    地理    政治

要求:
1. 用 h1 做标题:课程表
2. 表头行 6 列:节次 / 周一 / 周二 / 周三 / 周四 / 周五
3. 4 行数据,每行 6 个单元格
4. 完整文档骨架
5. 表头用 th,数据用 td
"""

# ======================
# 学员代码区
# ======================
pass
# 在这里写出课程表 HTML 文档:


# ======================
# 测试区
# ======================
if __name__ == '__main__':
    print("参考答案(示例):")
    print()
    print('<!DOCTYPE html>')
    print('<html lang="zh-CN">')
    print('<head>')
    print('    <meta charset="utf-8">')
    print('    <title>课程表</title>')
    print('</head>')
    print('<body>')
    print('    <h1>课程表</h1>')
    print('    <table>')
    print('        <tr>')
    print('            <th>节次</th>')
    print('            <th>周一</th>')
    print('            <th>周二</th>')
    print('            <th>周三</th>')
    print('            <th>周四</th>')
    print('            <th>周五</th>')
    print('        </tr>')
    print('        <tr>')
    print('            <td>第 1 节</td>')
    print('            <td>语文</td>')
    print('            <td>数学</td>')
    print('            <td>英语</td>')
    print('            <td>物理</td>')
    print('            <td>化学</td>')
    print('        </tr>')
    print('        <tr>')
    print('            <td>第 2 节</td>')
    print('            <td>数学</td>')
    print('            <td>英语</td>')
    print('            <td>语文</td>')
    print('            <td>化学</td>')
    print('            <td>生物</td>')
    print('        </tr>')
    print('        <tr>')
    print('            <td>第 3 节</td>')
    print('            <td>英语</td>')
    print('            <td>物理</td>')
    print('            <td>数学</td>')
    print('            <td>生物</td>')
    print('            <td>历史</td>')
    print('        </tr>')
    print('        <tr>')
    print('            <td>第 4 节</td>')
    print('            <td>体育</td>')
    print('            <td>化学</td>')
    print('            <td>历史</td>')
    print('            <td>地理</td>')
    print('            <td>政治</td>')
    print('        </tr>')
    print('    </table>')
    print('</body>')
    print('</html>')
    print()
    print("要点:")
    print("  ✓ 表头 6 列,每行数据 6 个单元格")
    print("  ✓ 嵌套顺序 table → tr → th/td")
    print("  ✓ 结构清晰,行数 = 列数规律明显")
