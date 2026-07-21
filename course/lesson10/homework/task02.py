"""
[难度: ★★★★]
[所属知识点: 完整联系页面实现]
[预计完成时间: 25 分钟]
[类型: 选做]

题目:为一个"独立设计师"编写完整的联系页面 HTML。

要求:
1. 完整文档骨架(DOCTYPE/html/head/body/title/meta charset)
2. title = "联系我 - 设计师阿伟"
3. body 内包含:
   - <header>:h1(品牌名) + nav(首页/作品集/联系)
   - <main>:
     - <section id="info"> 联系信息区:
       h2 "联系方式" + ul 列出 3 项(邮箱/电话/地址)
       邮箱用 mailto 链接
     - <section id="form"> 表单区:
       h2 "给我留言" + form(action="#", method="post")
       字段:姓名(text,required) + 邮箱(email,required) +
            电话(tel) + 留言(textarea rows=5,required) +
            提交按钮
       所有 label 与 input 通过 for/id 关联
   - <footer>:版权小字
4. 所有标签正确闭合,嵌套关系正确
"""

# ======================
# 学员代码区(独立编写完整联系页面)
# ======================
pass
# 在这里写出完整 HTML 文档:


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
    print('    <title>联系我 - 设计师阿伟</title>')
    print('</head>')
    print('<body>')
    print('    <header>')
    print('        <h1>阿伟 Design</h1>')
    print('        <nav>')
    print('            <a href="index.html">首页</a>')
    print('            <a href="projects.html">作品集</a>')
    print('            <a href="contact.html">联系</a>')
    print('        </nav>')
    print('    </header>')
    print()
    print('    <main>')
    print('        <section id="info">')
    print('            <h2>联系方式</h2>')
    print('            <ul>')
    print('                <li>')
    print('                    邮箱:')
    print('                    <a href="mailto:wei@example.com">')
    print('                        wei@example.com</a>')
    print('                </li>')
    print('                <li>电话:13800138000</li>')
    print('                <li>地址:上海市徐汇区</li>')
    print('            </ul>')
    print('        </section>')
    print()
    print('        <section id="form">')
    print('            <h2>给我留言</h2>')
    print('            <form action="#" method="post">')
    print('                <p>')
    print('                    <label for="name">姓名</label>')
    print('                    <input type="text" id="name"')
    print('                           name="name" required />')
    print('                </p>')
    print('                <p>')
    print('                    <label for="email">邮箱</label>')
    print('                    <input type="email" id="email"')
    print('                           name="email" required />')
    print('                </p>')
    print('                <p>')
    print('                    <label for="phone">电话</label>')
    print('                    <input type="tel" id="phone"')
    print('                           name="phone" />')
    print('                </p>')
    print('                <p>')
    print('                    <label for="msg">留言</label>')
    print('                    <textarea id="msg" name="msg"')
    print('                              rows="5" cols="30"')
    print('                              required></textarea>')
    print('                </p>')
    print('                <button type="submit">发送留言</button>')
    print('            </form>')
    print('        </section>')
    print('    </main>')
    print()
    print('    <footer>')
    print('        <p><small>© 2026 阿伟 Design. 保留所有权利。</small></p>')
    print('    </footer>')
    print('</body>')
    print('</html>')
    print()
    print("验收要点:")
    print("  ✓ 文档骨架完整")
    print("  ✓ header 含 h1 + nav")
    print("  ✓ 联系信息区 ul/li + mailto")
    print("  ✓ 表单区 4 个字段(姓名/邮箱/电话/留言)")
    print("  ✓ 所有 label 有 for,input 有 id")
    print("  ✓ 必填字段有 required")
    print("  ✓ footer 含 small")
