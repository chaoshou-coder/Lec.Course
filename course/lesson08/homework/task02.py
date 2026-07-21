"""
[难度: ★★★★]
[所属知识点: 完整 Hero 区实现]
[预计完成时间: 25 分钟]
[类型: 选做]

题目:综合运用 Day 01-Day 08 所有知识,为一个"旅行博主"编写完整的首页。

要求:
1. 完整文档骨架(DOCTYPE/html/head/body/title/meta charset)
2. body 内包含:
   - <header>:h1(博主名) + nav(首页/#travel/#about/#contact)
   - <main>:
     - <section id="hero"> Hero 区:
       h2 主标题(一句旅行口号)
       p 副标题(旅行风格/去过多少国家等)
       a 行动按钮(查看游记)
     - <section id="travel"> 游记区:
       h2 "精选游记" + ul 列出 3 篇旅行笔记(每篇 a 链接)
     - <section id="about"> 关于区:
       h2 "关于我" + p 一段自我介绍
       img 一张头像(必须有 alt,假设文件名为 avatar.jpg)
     - <section id="contact"> 联系区:
       h2 "联系我" + p 包含邮箱链接(a href="mailto:...")
   - <footer>:版权小字
3. 所有标签正确闭合,嵌套关系正确
"""

# ======================
# 学员代码区(独立编写完整首页)
# ======================
pass
# 在这里写出你的完整首页 HTML:


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
    print('    <title>旅行博主小林的个人主页</title>')
    print('</head>')
    print('<body>')
    print('    <header>')
    print('        <h1>小林 Wanderlust</h1>')
    print('        <nav>')
    print('            <a href="#hero">首页</a>')
    print('            <a href="#travel">游记</a>')
    print('            <a href="#about">关于</a>')
    print('            <a href="#contact">联系</a>')
    print('        </nav>')
    print('    </header>')
    print()
    print('    <main>')
    print('        <section id="hero">')
    print('            <h2>在路上,找到更好的自己</h2>')
    print('            <p>独立旅行博主 · 走过 30 国 · 5 年持续更新</p>')
    print('            <a href="#travel">查看我的游记 →</a>')
    print('        </section>')
    print()
    print('        <section id="travel">')
    print('            <h2>精选游记</h2>')
    print('            <ul>')
    print('                <li><a href="#japan">日本樱花季 15 天全攻略</a></li>')
    print('                <li><a href="#iceland">冰岛环岛自驾 10 日记</a></li>')
    print('                <li><a href="#peru">秘鲁马丘比丘徒步手记</a></li>')
    print('            </ul>')
    print('        </section>')
    print()
    print('        <section id="about">')
    print('            <h2>关于我</h2>')
    print('            <p>我是小林,一名辞职旅行的自由职业者。')
    print('            相信走过的路不会骗人。</p>')
    print('            <img src="avatar.jpg" alt="小林在冰岛的背影" />')
    print('        </section>')
    print()
    print('        <section id="contact">')
    print('            <h2>联系我</h2>')
    print('            <p><a href="mailto:xiaolin@example.com">给我发邮件</a></p>')
    print('        </section>')
    print('    </main>')
    print()
    print('    <footer>')
    print('        <p><small>© 2026 小林 Wanderlust. 保留所有权利。</small></p>')
    print('    </footer>')
    print('</body>')
    print('</html>')
    print()
    print("验收要点:")
    print("  ✓ 文档骨架完整")
    print("  ✓ header 含 h1 + nav(4 个链接)")
    print("  ✓ Hero 区 h2 + p + a 齐全")
    print("  ✓ 游记区 ul/li/a 正确嵌套")
    print("  ✓ 关于区含 img(有 alt)")
    print("  ✓ 联系区含 mailto 链接")
    print("  ✓ footer 含 small")
