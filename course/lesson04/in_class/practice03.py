"""
[难度: ★★]
[所属知识点: th 表头与 td 数据]
[预计完成时间: 10 分钟]

题目:下面的表格表头用的是 td 而不是 th,请修正,并加上表头行。

错误版本:
    <table>
        <tr>
            <td>商品A</td>
            <td>100 元</td>
        </tr>
        <tr>
            <td>商品B</td>
            <td>200 元</td>
        </tr>
    </table>

要求:
1. 添加表头行,用 th 标记两列:商品名称 / 价格
2. 数据行保持用 td
3. 理解 th 和 td 的区别
"""

# ======================
# 学员代码区(写出修正后的表格)
# ======================
pass
# 在这里写出修正后的表格:


# ======================
# 测试区
# ======================
if __name__ == '__main__':
    # 参考答案
    print("修正后:")
    print('  <table>')
    print('      <tr>')
    print('          <th>商品名称</th>')
    print('          <th>价格</th>')
    print('      </tr>')
    print('      <tr>')
    print('          <td>商品A</td>')
    print('          <td>100 元</td>')
    print('      </tr>')
    print('      <tr>')
    print('          <td>商品B</td>')
    print('          <td>200 元</td>')
    print('      </tr>')
    print('  </table>')
    print()
    print("修改要点:")
    print("  1. 添加了一行表头 <tr>")
    print("  2. 表头用 th 而不是 td")
    print("  3. th 默认加粗居中,td 默认普通文本")
