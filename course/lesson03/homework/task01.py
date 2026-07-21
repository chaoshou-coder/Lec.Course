"""
[难度: ★★★]
[所属知识点: 修复错误文档]
[预计完成时间: 15 分钟]
[类型: 选做]

题目:你收到一份"损坏"的 HTML 文档,文档本应显示一个"美食推荐"页面,但渲染出错。

损坏版本:
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <title>美食推荐</title>
    </head>
    <body>
        <h1>美食推荐</h1>
        <h2>川菜</h2>
        <img src="mapo.jpg">
        <p>麻婆豆腐是经典川菜。</p>
        <h2>粤菜</h2>
        <img src="dimsum.jpg" alt="点心" />
        <p>早茶点心种类丰富。</p>
        <h2>推荐餐厅</h2>
        <ul>
            <li><a href="https://restaurant1.com">餐厅一</a>
            <li><a "https://restaurant2.com">餐厅二</a></li>
            <p>餐厅三(暂无链接)</p>
        </ul>
    </body>
    </html>

要求:
1. 找出全部 6 处错误(提示:meta/img alt/a href/li 未闭合/ul 内放 p)
2. 写出修正后的完整文档
3. 保存为 food.html,用浏览器打开验证
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
    print("  1. 缺少 <meta charset=\"utf-8\"> (head 内)")
    print("  2. <img src=\"mapo.jpg\"> 缺少 alt 属性")
    print("  3. <li><a href=\"...\">餐厅一</a> 缺少闭标签 </li>")
    print("  4. <a \"https://restaurant2.com\"> 缺少 href 属性名")
    print("  5. <p>餐厅三...</p> 直接放在 ul 内(应为 li)")
    print("  6. 第 3 行 img 和第 6 行 img 的 alt 写法不一致")
    print()
    print("修正后完整文档(示例):")
    print('<!DOCTYPE html>')
    print('<html lang="zh-CN">')
    print('<head>')
    print('    <meta charset="utf-8">')
    print('    <title>美食推荐</title>')
    print('</head>')
    print('<body>')
    print('    <h1>美食推荐</h1>')
    print('    <h2>川菜</h2>')
    print('    <img src="mapo.jpg" alt="麻婆豆腐" />')
    print('    <p>麻婆豆腐是经典川菜。</p>')
    print('    <h2>粤菜</h2>')
    print('    <img src="dimsum.jpg" alt="点心" />')
    print('    <p>早茶点心种类丰富。</p>')
    print('    <h2>推荐餐厅</h2>')
    print('    <ul>')
    print('        <li><a href="https://restaurant1.com">餐厅一</a></li>')
    print('        <li><a href="https://restaurant2.com">餐厅二</a></li>')
    print('        <li>餐厅三(暂无链接)</li>')
    print('    </ul>')
    print('</body>')
    print('</html>')
