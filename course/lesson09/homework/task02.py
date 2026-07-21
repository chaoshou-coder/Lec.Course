"""
[难度: ★★★★]
[所属知识点: 完整项目展示页实现]
[预计完成时间: 25 分钟]
[类型: 选做]

题目:为一个"插画师个人官网"编写完整的项目展示页。

要求:
1. 完整文档骨架(DOCTYPE/html/head/body/title/meta charset)
2. title = "作品集 - 插画师小鹿"
3. body 内包含:
   - <header>:h1(品牌名) + nav(首页/#about/作品集/联系)
   - <main>:
     - <section id="intro"> 简介区:
       h2 "关于我的画" + p 一段风格介绍
     - <section id="projects"> 作品区:
       h2 "精选插画" + ul 包裹 4 个 li
       每张卡片:img(src/alt/width=280) + h3(含 a) + p
       (4 个主题:儿插/头像/海报/文创,或其他)
     - <section id="contact"> 联系区:
       h2 "合作联系" + p 含 mailto 链接
   - <footer>:版权小字
4. 所有标签正确闭合,嵌套关系正确
5. 卡片结构完全一致
"""

# ======================
# 学员代码区(独立编写完整项目展示页)
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
    print('    <title>作品集 - 插画师小鹿</title>')
    print('</head>')
    print('<body>')
    print('    <header>')
    print('        <h1>小鹿 Illustrates</h1>')
    print('        <nav>')
    print('            <a href="index.html">首页</a>')
    print('            <a href="#about">关于</a>')
    print('            <a href="#projects">作品集</a>')
    print('            <a href="#contact">联系</a>')
    print('        </nav>')
    print('    </header>')
    print()
    print('    <main>')
    print('        <section id="intro">')
    print('            <h2>关于我的画</h2>')
    print('            <p>用水彩与数码结合,画温暖的故事。</p>')
    print('        </section>')
    print()
    print('        <section id="projects">')
    print('            <h2>精选插画</h2>')
    print('            <ul>')
    print('                <li>')
    print('                    <img src="child.jpg"')
    print('                         alt="儿童绘本内页插画"')
    print('                         width="280" />')
    print('                    <h3><a href="#child">儿童绘本</a></h3>')
    print('                    <p>给孩子的温暖故事。</p>')
    print('                </li>')
    print('                <li>')
    print('                    <img src="avatar.jpg"')
    print('                         alt="定制头像插画示例"')
    print('                         width="280" />')
    print('                    <h3><a href="#avatar">头像定制</a></h3>')
    print('                    <p>独一无二的你。</p>')
    print('                </li>')
    print('                <li>')
    print('                    <img src="poster.jpg"')
    print('                         alt="展览主视觉海报"')
    print('                         width="280" />')
    print('                    <h3><a href="#poster">展览海报</a></h3>')
    print('                    <p>为品牌活动量身定制。</p>')
    print('                </li>')
    print('                <li>')
    print('                    <img src="product.jpg"')
    print('                         alt="文创产品包装插画"')
    print('                         width="280" />')
    print('                    <h3><a href="#product">文创产品</a></h3>')
    print('                    <p>从贺卡到贴纸的周边延展。</p>')
    print('                </li>')
    print('            </ul>')
    print('        </section>')
    print()
    print('        <section id="contact">')
    print('            <h2>合作联系</h2>')
    print('            <p><a href="mailto:xiaolu@example.com">')
    print('               给我发邮件</a></p>')
    print('        </section>')
    print('    </main>')
    print()
    print('    <footer>')
    print('        <p><small>© 2026 小鹿 Illustrates. 保留所有权利。</small></p>')
    print('    </footer>')
    print('</body>')
    print('</html>')
    print()
    print("验收要点:")
    print("  ✓ 文档骨架完整")
    print("  ✓ header 含 h1 + nav(4 个链接)")
    print("  ✓ 简介区 h2 + p")
    print("  ✓ 作品区 4 张卡片结构一致")
    print("  ✓ 每张卡片:img + h3(a) + p")
    print("  ✓ 联系区含 mailto")
    print("  ✓ footer 含 small")
