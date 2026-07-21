"""
[难度: ★★★]
[所属知识点: 修复错误文档]
[预计完成时间: 15 分钟]
[类型: 选做]

题目:你收到一份"损坏"的 HTML 文档,文档本应显示一篇"菜谱",但渲染出错。

损坏版本:
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <title>番茄炒蛋</title>
    </head>
    <body>
        <h1>番茄炒蛋</h1>
        <h3>所需食材</h3>
        <p>鸡蛋 3 个
        <p>番茄 2 个</p>
        <h3>制作步骤</h3>
        <p>1. 打散鸡蛋<br></br>
        <p>2. 番茄切块</p>
        <p>3. 热锅下油<br>
        <hr></hr>
        <h6>小贴士</h6>
        <p>加点糖会更好吃。

要求:
1. 找出全部 7 处错误(提示:meta/head 闭合/标题跳级/p 未闭合/br/hr 误用)
2. 写出修正后的完整文档
3. 保存为 recipe.html,用浏览器打开验证
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
    print("7 处错误:")
    print("  1. 缺少 <meta charset=\"utf-8\"> (head 内)")
    print("  2. <h3>所需食材</h3> 前缺少 <h2>(标题从 h1 跳到 h3)")
    print("  3. <p>鸡蛋 3 个 没有闭标签 </p>")
    print("  4. <br></br> → <br> (br 是自闭合标签)")
    print("  5. <hr></hr> → <hr> (hr 是自闭合标签)")
    print("  6. <h6>小贴士</h6> 标题跳级(应改为 h2)")
    print("  7. <p>加点糖会更好吃。 没有闭标签 </p>")
    print()
    print("修正后完整文档(示例):")
    print('<!DOCTYPE html>')
    print('<html lang="zh-CN">')
    print('<head>')
    print('    <meta charset="utf-8">')
    print('    <title>番茄炒蛋</title>')
    print('</head>')
    print('<body>')
    print('    <h1>番茄炒蛋</h1>')
    print('    <h2>所需食材</h2>')
    print('    <p>鸡蛋 3 个</p>')
    print('    <p>番茄 2 个</p>')
    print('    <h2>制作步骤</h2>')
    print('    <p>1. 打散鸡蛋<br>')
    print('    2. 番茄切块</p>')
    print('    <p>3. 热锅下油</p>')
    print('    <hr>')
    print('    <h2>小贴士</h2>')
    print('    <p>加点糖会更好吃。</p>')
    print('</body>')
    print('</html>')
