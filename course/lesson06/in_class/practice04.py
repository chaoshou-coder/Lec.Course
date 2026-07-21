"""
[难度: ★★]
[所属知识点: 语义化标签辨析]
[预计完成时间: 10 分钟]

题目:把下面的 ??? 替换为正确的语义化标签名。

    <???>                               ← 页头(包含 h1 标题)
        <h1>我的网站</h1>
    </???>

    <???>                               ← 导航栏(包含 3 个链接)
        <a href="index.html">首页</a>
        <a href="about.html">关于</a>
        <a href="contact.html">联系</a>
    </???>

    <???>                               ← 主体内容(唯一)
        <???>                            ← 第一章节
            <h2>关于我们</h2>
            <p>我们是一个团队...</p>
        </???>
        <???>                            ← 第二章节
            <h2>我们的服务</h2>
            <p>我们提供...</p>
        </???>
    </???>

    <???>                               ← 页脚(版权信息)
        <p>© 2026 我的网站</p>
    </???>

要求:从以下标签中选择: header / nav / main / section / footer
"""

# ======================
# 学员代码区(写出完整结构)
# ======================
pass
# 在这里写出完整语义化结构:

# ======================
# 测试区
# ======================
if __name__ == '__main__':
    print("参考答案:")
    print()
    print('<header>')
    print('    <h1>我的网站</h1>')
    print('</header>')
    print('<nav>')
    print('    <a href="index.html">首页</a>')
    print('    <a href="about.html">关于</a>')
    print('    <a href="contact.html">联系</a>')
    print('</nav>')
    print('<main>')
    print('    <section>')
    print('        <h2>关于我们</h2>')
    print('        <p>我们是一个团队...</p>')
    print('    </section>')
    print('    <section>')
    print('        <h2>我们的服务</h2>')
    print('        <p>我们提供...</p>')
    print('    </section>')
    print('</main>')
    print('<footer>')
    print('    <p>© 2026 我的网站</p>')
    print('</footer>')
    print()
    print("要点:")
    print("  1. header = 页头 ✓")
    print("  2. nav = 导航 ✓")
    print("  3. main = 主体(唯一) ✓")
    print("  4. section = 章节 ✓")
    print("  5. footer = 页脚 ✓")
