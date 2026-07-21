"""
[难度: ★★★]
[所属知识点: 三页面网站]
[预计完成时间: 25 分钟]
[类型: 选做]

题目:独立搭建一个完整的"三页面"个人博客网站。

目录结构要求:
    my-blog/
    ├── index.html
    ├── about.html
    ├── contact.html
    └── images/
        └── logo.jpg

页面要求(三个页面共用部分一致):
- header: h1 "我的博客" + p "记录学习笔记"
- nav: 三个链接(首页/关于/联系),所有页面一致
- footer: p "© 2026 我的博客"

页面差异部分:
- index.html 的 main: 两篇 article,每篇 h2 + p
- about.html 的 main: h2 "关于我" + p 自我介绍 + ul/li 爱好列表
- contact.html 的 main: h2 "联系我" + form(姓名/邮箱/留言/提交)

代码要求:
1. 所有页面代码缩进一致(每层 4 空格)
2. 关键位置有注释(每个页面至少 3 处)
3. 表单使用 label 关联 input
4. 相对路径正确
"""

# ======================
# 学员代码区(独立编写三个页面)
# ======================

# index.html
pass
# 在这里写出 index.html:

# about.html
pass
# 在这里写出 about.html:

# contact.html
pass
# 在这里写出 contact.html:

# ======================
# 测试区
# ======================
if __name__ == '__main__':
    print("参考答案(三个页面的示例代码):")
    print()
    print("=" * 50)
    print("index.html:")
    print("=" * 50)
    print()
    print('<!DOCTYPE html>')
    print('<html lang="zh-CN">')
    print('<head>')
    print('    <meta charset="utf-8">')
    print('    <title>我的博客 - 首页</title>')
    print('</head>')
    print('<body>')
    print('    <!-- 页头 -->')
    print('    <header>')
    print('        <h1>我的博客</h1>')
    print('        <p>记录学习笔记</p>')
    print('    </header>')
    print('    <!-- 导航 -->')
    print('    <nav>')
    print('        <a href="index.html">首页</a>')
    print('        <a href="about.html">关于</a>')
    print('        <a href="contact.html">联系</a>')
    print('    </nav>')
    print('    <!-- 主体:文章列表 -->')
    print('    <main>')
    print('        <article>')
    print('            <h2>HTML 学习笔记</h2>')
    print('            <p>今天学习了表单和语义化标签...</p>')
    print('        </article>')
    print('        <article>')
    print('            <h2>CSS 入门</h2>')
    print('            <p>CSS 是层叠样式表...</p>')
    print('        </article>')
    print('    </main>')
    print('    <!-- 页脚 -->')
    print('    <footer>')
    print('        <p>© 2026 我的博客</p>')
    print('    </footer>')
    print('</body>')
    print('</html>')
    print()
    print("=" * 50)
    print("about.html:")
    print("=" * 50)
    print()
    print('<!DOCTYPE html>')
    print('<html lang="zh-CN">')
    print('<head>')
    print('    <meta charset="utf-8">')
    print('    <title>我的博客 - 关于</title>')
    print('</head>')
    print('<body>')
    print('    <header>')
    print('        <h1>我的博客</h1>')
    print('        <p>记录学习笔记</p>')
    print('    </header>')
    print('    <nav>')
    print('        <a href="index.html">首页</a>')
    print('        <a href="about.html">关于</a>')
    print('        <a href="contact.html">联系</a>')
    print('    </nav>')
    print('    <!-- 主体:关于我 -->')
    print('    <main>')
    print('        <h2>关于我</h2>')
    print('        <p>我是一名正在学习前端的初学者。</p>')
    print('        <h3>我的爱好</h3>')
    print('        <ul>')
    print('            <li>阅读</li>')
    print('            <li>编程</li>')
    print('            <li>摄影</li>')
    print('        </ul>')
    print('    </main>')
    print('    <footer>')
    print('        <p>© 2026 我的博客</p>')
    print('    </footer>')
    print('</body>')
    print('</html>')
    print()
    print("=" * 50)
    print("contact.html:")
    print("=" * 50)
    print()
    print('<!DOCTYPE html>')
    print('<html lang="zh-CN">')
    print('<head>')
    print('    <meta charset="utf-8">')
    print('    <title>我的博客 - 联系</title>')
    print('</head>')
    print('<body>')
    print('    <header>')
    print('        <h1>我的博客</h1>')
    print('        <p>记录学习笔记</p>')
    print('    </header>')
    print('    <nav>')
    print('        <a href="index.html">首页</a>')
    print('        <a href="about.html">关于</a>')
    print('        <a href="contact.html">联系</a>')
    print('    </nav>')
    print('    <!-- 主体:联系表单 -->')
    print('    <main>')
    print('        <h2>联系我</h2>')
    print('        <form action="/contact" method="POST">')
    print('            <p>')
    print('                <label for="name">姓名:</label>')
    print('                <input type="text" id="name" name="name" />')
    print('            </p>')
    print('            <p>')
    print('                <label for="email">邮箱:</label>')
    print('                <input type="email" id="email" name="email" />')
    print('            </p>')
    print('            <p>')
    print('                <label for="msg">留言:</label>')
    print('                <textarea id="msg" name="message" '
          'rows="4" cols="30"></textarea>')
    print('            </p>')
    print('            <p>')
    print('                <button type="submit">发送</button>')
    print('            </p>')
    print('        </form>')
    print('    </main>')
    print('    <footer>')
    print('        <p>© 2026 我的博客</p>')
    print('    </footer>')
    print('</body>')
    print('</html>')
    print()
    print("验收要点:")
    print("  ✓ 三个页面结构完整,nav 一致")
    print("  ✓ 代码缩进一致,有注释")
    print("  ✓ 表单 label 关联 input")
    print("  ✓ 相对路径正确")
