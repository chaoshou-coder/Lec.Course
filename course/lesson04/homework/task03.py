"""
[难度: ★★★★]
[所属知识点: 综合数据报表]
[预计完成时间: 30 分钟]
[类型: 选做]

题目:综合运用 Day 01~Day 04 所有知识,编写一个"公司季度销售报表"HTML 页面。

要求:
1. 完整文档骨架(DOCTYPE/html/head/body/title/meta charset)
2. 页面内容包含:
   - h1:2026 年 Q1 销售报表
   - p 说明文字:一段介绍报表的话
   - h2 "销售数据":一个表格,表头 5 列(月份/产品A/产品B/产品C/合计)
     3 行数据(1月/2月/3月,数据自己编造)
   - hr 分隔线
   - h2 "销售冠军":ol/li 有序列表,列出前 3 名销售员
   - h2 "数据来源":a 标签链接到 https://www.example.com,target="_blank"
3. 表格表头用 th,数据用 td
4. 每行单元格数量与表头一致(5 列)
5. 保存为 report.html,用浏览器打开验证

进阶挑战(可选):
- 在表格下方加一行"总计",用 td 计算每列的总和
- 在页面底部加一行小字"© 2026 公司财报",用 <small> 标签
- 给表格加一个 h2 标题"季度汇总",用 hr 与其他部分分隔
"""

# ======================
# 学员代码区(独立编写完整页面)
# ======================
pass
# 在这里写出你的销售报表页面:


# ======================
# 测试区
# ======================
if __name__ == '__main__':
    print("参考答案(示例结构):")
    print()
    print('<!DOCTYPE html>')
    print('<html lang="zh-CN">')
    print('<head>')
    print('    <meta charset="utf-8">')
    print('    <title>2026 年 Q1 销售报表</title>')
    print('</head>')
    print('<body>')
    print('    <h1>2026 年 Q1 销售报表</h1>')
    print('    <p>以下是公司 2026 年第一季度的销售数据汇总。</p>')
    print('    <h2>销售数据</h2>')
    print('    <table>')
    print('        <tr>')
    print('            <th>月份</th>')
    print('            <th>产品A</th>')
    print('            <th>产品B</th>')
    print('            <th>产品C</th>')
    print('            <th>合计</th>')
    print('        </tr>')
    print('        <tr>')
    print('            <td>1 月</td>')
    print('            <td>120 万</td>')
    print('            <td>85 万</td>')
    print('            <td>95 万</td>')
    print('            <td>300 万</td>')
    print('        </tr>')
    print('        <tr>')
    print('            <td>2 月</td>')
    print('            <td>135 万</td>')
    print('            <td>90 万</td>')
    print('            <td>100 万</td>')
    print('            <td>325 万</td>')
    print('        </tr>')
    print('        <tr>')
    print('            <td>3 月</td>')
    print('            <td>150 万</td>')
    print('            <td>110 万</td>')
    print('            <td>115 万</td>')
    print('            <td>375 万</td>')
    print('        </tr>')
    print('    </table>')
    print('    <hr>')
    print('    <h2>销售冠军</h2>')
    print('    <ol>')
    print('        <li>张三 —— 450 万</li>')
    print('        <li>李四 —— 380 万</li>')
    print('        <li>王五 —— 320 万</li>')
    print('    </ol>')
    print('    <h2>数据来源</h2>')
    print('    <p>')
    print('        <a href="https://www.example.com" target="_blank">')
    print('            访问公司官网')
    print('        </a>')
    print('    </p>')
    print('    <small>© 2026 公司财报</small>')
    print('</body>')
    print('</html>')
    print()
    print("验收要点:")
    print("  ✓ 文档骨架完整")
    print("  ✓ 表格表头 5 列,每行数据 5 个单元格")
    print("  ✓ th 用于表头,td 用于数据")
    print("  ✓ ol/li 列表正确")
    print("  ✓ a 标签有 href + target + 链接文字")
