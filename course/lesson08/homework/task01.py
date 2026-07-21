"""
[难度: ★★★]
[所属知识点: 修复语义化错误]
[预计完成时间: 15 分钟]
[类型: 选做]

题目:你收到一份"语义退化"的首页,本来应该用语义标签的地方全用了 div/span。
请把下面 5 处 div/span 替换为正确的语义标签。

原版本:
    <div class="page-top">
        <span class="brand">柠檬工作室</span>
        <div class="links">
            <a href="#home">首页</a>
            <a href="#work">作品</a>
            <a href="#contact">联系</a>
        </div>
    </div>

    <div class="page-body">
        <div class="welcome">
            <span class="big-title">我们做有温度的产品</span>
            <span class="sub-title">专注 UX 设计 · 10 年经验</span>
        </div>
    </div>

    <div class="page-bottom">
        <span class="copyright">© 2026 柠檬工作室</span>
    </div>

要求:
1. 找出全部 5 处应该改成语义标签的地方
2. 写出修正后的完整代码
3. 标注每处修改用了哪个语义标签
"""

# ======================
# 学员代码区(写出修正后代码)
# ======================
pass
# 在这里写出修正后的代码:


# ======================
# 测试区
# ======================
if __name__ == '__main__':
    print("5 处修改:")
    print()
    print("  1. <div class=\"page-top\"> → <header>")
    print("     原因:页面顶部是头部,应用 header")
    print()
    print("  2. <span class=\"brand\"> → <h1>")
    print("     原因:品牌名是最高级标题,应用 h1")
    print()
    print("  3. <div class=\"links\"> → <nav>")
    print("     原因:导航链接组应用 nav")
    print()
    print("  4. <div class=\"page-body\"> → <main>")
    print("     原因:主体内容应用 main")
    print()
    print("  5. <div class=\"page-bottom\"> → <footer>")
    print("     原因:底部版权区应用 footer")
    print()
    print("修正后代码:")
    print('<header>')
    print('    <h1>柠檬工作室</h1>')
    print('    <nav>')
    print('        <a href="#home">首页</a>')
    print('        <a href="#work">作品</a>')
    print('        <a href="#contact">联系</a>')
    print('    </nav>')
    print('</header>')
    print()
    print('<main>')
    print('    <section class="welcome">')
    print('        <h2>我们做有温度的产品</h2>')
    print('        <p>专注 UX 设计 · 10 年经验</p>')
    print('    </section>')
    print('</main>')
    print()
    print('<footer>')
    print('    <small>© 2026 柠檬工作室</small>')
    print('</footer>')
    print()
    print("要点:welcome 区域的 span.big-title → h2,span.sub-title → p")
