"""
[难度: ★★★]
[所属知识点: 完整首页骨架]
[预计完成时间: 20 分钟]

题目:独立编写一个完整的"咖啡师个人主页"首页骨架 HTML。

要求:
1. 完整文档骨架(DOCTYPE/html/head/body/title/meta charset)
2. title = "咖啡师阿杰的个人主页"
3. body 内包含:
   - <header>:h1(品牌名) + nav(3 个锚点链接:#home/#menu/#contact)
   - <main>:
     - <section id="home"> Hero 区:h2 主标题 + p 副标题 + a 行动按钮
     - <section id="menu"> 菜单区:h2 "招牌饮品" + ul 列出 3 款饮品
   - <footer>:版权小字(用 small 标签)
4. 所有标签正确闭合,嵌套关系正确
"""

# ======================
# 学员代码区(独立编写完整首页骨架)
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
    print('    <title>咖啡师阿杰的个人主页</title>')
    print('</head>')
    print('<body>')
    print('    <header>')
    print('        <h1>阿杰咖啡</h1>')
    print('        <nav>')
    print('            <a href="#home">首页</a>')
    print('            <a href="#menu">菜单</a>')
    print('            <a href="#contact">联系我</a>')
    print('        </nav>')
    print('    </header>')
    print()
    print('    <main>')
    print('        <section id="home">')
    print('            <h2>一杯好咖啡,一段慢时光</h2>')
    print('            <p>SCA 认证咖啡师 · 单品手冲 · 自家烘焙</p>')
    print('            <a href="#menu">查看菜单 →</a>')
    print('        </section>')
    print()
    print('        <section id="menu">')
    print('            <h2>招牌饮品</h2>')
    print('            <ul>')
    print('                <li>耶加雪菲手冲</li>')
    print('                <li>冰滴咖啡</li>')
    print('                <li>脏脏拿铁</li>')
    print('            </ul>')
    print('        </section>')
    print('    </main>')
    print()
    print('    <footer>')
    print('        <p><small>© 2026 阿杰咖啡. 保留所有权利。</small></p>')
    print('    </footer>')
    print('</body>')
    print('</html>')
    print()
    print("验收要点:")
    print("  ✓ 文档骨架完整")
    print("  ✓ header 含 h1 + nav")
    print("  ✓ main 含两个 section")
    print("  ✓ Hero 区 h2 + p + a 齐全")
    print("  ✓ 菜单区 ul/li 正确")
    print("  ✓ footer 含 small")
