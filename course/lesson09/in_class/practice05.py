"""
[难度: ★★★]
[所属知识点: 完整项目展示页骨架]
[预计完成时间: 20 分钟]

题目:独立编写一个完整的设计师项目展示页 HTML。

要求:
1. 完整文档骨架(DOCTYPE/html/head/body/title/meta charset)
2. title = "作品集 - 设计师阿伟"
3. body 内包含:
   - <header>:h1(品牌名) + nav(首页/作品集/联系)
   - <main>:
     - <section id="projects">:
       - h2 "精选项目"
       - ul 包裹 3 个 li,每张卡片含:
         img(src/alt/width=280) + h3(含 a 链接) + p 描述
   - <footer>:版权小字
4. 三张卡片内容结构完全一致
5. 项目自己命名(参考:品牌/UI/插画/包装/海报)
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
    print("参考答案(示例):")
    print()
    print('<!DOCTYPE html>')
    print('<html lang="zh-CN">')
    print('<head>')
    print('    <meta charset="utf-8">')
    print('    <title>作品集 - 设计师阿伟</title>')
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
    print('        <section id="projects">')
    print('            <h2>精选项目</h2>')
    print('            <ul>')
    print('                <li>')
    print('                    <img src="brand.jpg"')
    print('                         alt="新锐茶饮品牌全案设计"')
    print('                         width="280" />')
    print('                    <h3><a href="#brand">茶饮品牌全案</a></h3>')
    print('                    <p>Logo 到包装的完整视觉。</p>')
    print('                </li>')
    print('                <li>')
    print('                    <img src="ui.jpg"')
    print('                         alt="记账 App 主界面"')
    print('                         width="280" />')
    print('                    <h3><a href="#ui">记账 App UI</a></h3>')
    print('                    <p>轻量化个人财务工具。</p>')
    print('                </li>')
    print('                <li>')
    print('                    <img src="poster.jpg"')
    print('                         alt="音乐节系列海报"')
    print('                         width="280" />')
    print('                    <h3><a href="#poster">音乐节海报</a></h3>')
    print('                    <p>系列化视觉延展设计。</p>')
    print('                </li>')
    print('            </ul>')
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
    print("  ✓ main 含 section(含 h2 + ul)")
    print("  ✓ 3 张卡片结构一致")
    print("  ✓ 每张卡片:img + h3(a) + p")
    print("  ✓ footer 含 small")
