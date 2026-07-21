"""
[难度: ★]
[所属知识点: 表格结构认知]
[预计完成时间: 5 分钟]

题目:下面哪些是合法的 HTML 表格结构?在合法的后面打 ✓,非法的后面打 ✗。

    1. <table><tr><td>数据</td></tr></table>       (  )
    2. <table><td>数据</td></table>                  (  )
    3. <table><tr><th>表头</th></tr></table>          (  )
    4. <table><tr>文字</tr></table>                 (  )
    5. <table><tr><td>A</td><td>B</td></tr></table>     (  )
    6. <tr><td>数据</td></tr>                         (  )
    7. <table><tr><th>名称</th><td>数据</td></tr></table> (  )
    8. <td>数据</td>                                  (  )

提示:嵌套顺序必须是 table → tr → td/th,数据必须放在 td/th 里。
"""

# 学员不需要写代码,在纸上作答即可。
# 参考答案见下方测试区。

if __name__ == '__main__':
    # 参考答案
    answers = {
        1: "✓ 合法:table → tr → td,结构正确",
        2: "✗ 非法:td 不能直接放在 table 里,缺少 tr",
        3: "✓ 合法:table → tr → th,结构正确",
        4: "✗ 非法:文字不能直接放在 tr 里,必须放在 td/th 里",
        5: "✓ 合法:一行有两个 td(两列),结构正确",
        6: "✗ 非法:tr 必须在 table 里面,不能单独存在",
        7: "✓ 合法:一行中既有 th(表头)又有 td(数据),结构正确",
        8: "✗ 非法:td 必须在 table → tr 里面,不能单独存在",
    }
    for k, v in answers.items():
        print(f"  {k}. {v}")
