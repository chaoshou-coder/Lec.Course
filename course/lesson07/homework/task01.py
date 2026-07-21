"""
[难度: ★★★]
[所属知识点: 修复混乱代码]
[预计完成时间: 15 分钟]
[类型: 选做]

题目:你收到一份"混乱"的 HTML 文档,代码能跑但完全不可读。

混乱版本:
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<title>我的博客</title>
</head>
<body>
<header>
<h1>我的博客</h1>
<p>记录学习笔记</p>
</header>
<nav>
<a href="index.html">首页</a>
<a href="about.html">关于</a>
<a href="contact.html">联系</a>
</nav>
<main>
<article>
<h2>HTML 学习笔记</h2>
<p>今天学习了表单和语义化标签。</p>
<section>
<h3>什么是语义化</h3>
<p>语义化就是用有意义的标签名。</p>
</section>
<section>
<h3>语义化的好处</h3>
<p>搜索引擎更容易理解页面。</p>
</section>
</article>
</main>
<footer>
<p>© 2026 我的博客</p>
</footer>
</body>
</html>

要求:
1. 重新格式化代码,让缩进一致(每层 4 空格)
2. 在合适的位置加空行分隔逻辑块
3. 在关键位置加注释(至少 4 处)
4. 闭标签与开标签对齐
5. 保存为 blog.html,用浏览器打开验证
"""

# ======================
# 学员代码区
# ======================
pass
# 在这里写出格式化并加注释后的完整代码:

# ======================
# 测试区
# ======================
if __name__ == '__main__':
    print("参考答案(格式化 + 注释):")
    print()
    print('<!DOCTYPE html>')
    print('<html lang="zh-CN">')
    print('<head>')
    print('    <meta charset="utf-8">')
    print('    <title>我的博客</title>')
    print('</head>')
    print()
    print('<body>')
    print('    <!-- 页头:博客标题和副标题 -->')
    print('    <header>')
    print('        <h1>我的博客</h1>')
    print('        <p>记录学习笔记</p>')
    print('    </header>')
    print()
    print('    <!-- 导航栏:链接到首页/关于/联系 -->')
    print('    <nav>')
    print('        <a href="index.html">首页</a>')
    print('        <a href="about.html">关于</a>')
    print('        <a href="contact.html">联系</a>')
    print('    </nav>')
    print()
    print('    <!-- 主体内容:文章列表 -->')
    print('    <main>')
    print('        <article>')
    print('            <h2>HTML 学习笔记</h2>')
    print('            <p>今天学习了表单和语义化标签。</p>')
    print()
    print('            <!-- 章节 1:什么是语义化 -->')
    print('            <section>')
    print('                <h3>什么是语义化</h3>')
    print('                <p>语义化就是用有意义的标签名。</p>')
    print('            </section>')
    print()
    print('            <!-- 章节 2:语义化的好处 -->')
    print('            <section>')
    print('                <h3>语义化的好处</h3>')
    print('                <p>搜索引擎更容易理解页面。</p>')
    print('            </section>')
    print('        </article>')
    print('    </main>')
    print()
    print('    <!-- 页脚:版权信息 -->')
    print('    <footer>')
    print('        <p>© 2026 我的博客</p>')
    print('    </footer>')
    print('</body>')
    print('</html>')
    print()
    print("验收要点:")
    print("  ✓ 每层缩进 4 空格,闭标签对齐")
    print("  ✓ 空行分隔 header/nav/main/footer")
    print("  ✓ 至少 4 处注释,说明代码作用")
    print("  ✓ 浏览器渲染结果与原来一致")
