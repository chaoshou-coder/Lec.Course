"""
[难度: ★★★]
[所属知识点: 完整表格页面]
[预计完成时间: 15 分钟]

题目:独立编写一个完整的 HTML5 文档,主题是"员工通讯录"。

要求:
1. 包含完整的文档骨架(DOCTYPE/html/head/body/title/meta)
2. title = "员工通讯录"
3. body 内包含:
   - h1 标题:员工通讯录
   - 一个表格,表头 4 列:工号 / 姓名 / 部门 / 电话
   - 3 行数据(自己编造 3 个员工的信息)
   - 表格前用 p 标签写一行说明:"以下是公司员工通讯录"
4. 表头用 th,数据用 td
5. 每行单元格数量与表头一致(4 列)
"""

# ======================
# 学员代码区(独立编写完整文档)
# ======================
pass
# 在这里写出你的完整 HTML 文档:


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
    print('    <title>员工通讯录</title>')
    print('</head>')
    print('<body>')
    print('    <h1>员工通讯录</h1>')
    print('    <p>以下是公司员工通讯录</p>')
    print('    <table>')
    print('        <tr>')
    print('            <th>工号</th>')
    print('            <th>姓名</th>')
    print('            <th>部门</th>')
    print('            <th>电话</th>')
    print('        </tr>')
    print('        <tr>')
    print('            <td>001</td>')
    print('            <td>张三</td>')
    print('            <td>技术部</td>')
    print('            <td>13800138001</td>')
    print('        </tr>')
    print('        <tr>')
    print('            <td>002</td>')
    print('            <td>李四</td>')
    print('            <td>市场部</td>')
    print('            <td>13800138002</td>')
    print('        </tr>')
    print('        <tr>')
    print('            <td>003</td>')
    print('            <td>王五</td>')
    print('            <td>人事部</td>')
    print('            <td>13800138003</td>')
    print('        </tr>')
    print('    </table>')
    print('</body>')
    print('</html>')
    print()
    print("验收要点:")
    print("  ✓ 文档骨架完整(DOCTYPE/html/head/body)")
    print("  ✓ meta charset 写了")
    print("  ✓ 表头 4 列用 th")
    print("  ✓ 每行数据 4 个 td,与表头对齐")
    print("  ✓ 嵌套顺序 table → tr → td/th")
