"""
[难度: ★★★★]
[所属知识点: 带过滤标签的项目列表]
[预计完成时间: 30 分钟]
[类型: 选做]

题目:为一个"全栈开发者"做一个带分类标签的项目展示页。
同一份作品集,通过分类标签(All / Web / App / Design)过滤。

本题综合运用:
- Day 08:语义化标签(header/nav/main/section/footer)
- Day 09:ul/li + img 卡片列表
- 新增:用 a 做分类切换(锚点模拟),卡片按分类排列

要求:
1. complete document 骨架
2. header 里主导航 + 分类过滤导航(用 nav 包裹 4 个 a)
3. main 内按分类分 section(每个 section 一个 h2 + ul 卡片列表)
4. 至少 3 个分类,每个分类 2-3 张卡片
5. 每张卡片结构:img + h3(a) + p

题目:补全下面 projects.html 的分类导航和 Web 分类 section。

    <!-- 分类过滤导航(在 main 上面) -->
    <nav id="filter">
        <a href="#all">全部</a>
        <a href="#web">Web</a>
        <a href="#app">App</a>
        <a href="#design">设计</a>
    </nav>

    <!-- TODO: Web 分类 section,h2 "Web 项目" -->
    <!--      + ul 包裹 2 个 li,每张卡片含 img + h3(a) + p -->

要求:
1. 补全 Web section(2 张卡片)
2. App section(2 张卡片,自己写)
3. Design section(2 张卡片,自己写)
4. 每张卡片结构一致
"""

# ======================
# 学员代码区(补全分类 section)
# ======================
pass
# 在这里写出三个分类 section:


# ======================
# 测试区
# ======================
if __name__ == '__main__':
    print("参考答案(三个分类 section 示例):")
    print()
    print('<!-- Web 分类 -->')
    print('<section id="web">')
    print('    <h2>Web 项目</h2>')
    print('    <ul>')
    print('        <li>')
    print('            <img src="web1.jpg"')
    print('                 alt="电商后台管理系统界面"')
    print('                 width="280" />')
    print('            <h3><a href="#web1">电商后台</a></h3>')
    print('            <p>基于 React 的全栈商城方案。</p>')
    print('        </li>')
    print('        <li>')
    print('            <img src="web2.jpg"')
    print('                 alt="在线学习平台首页"')
    print('                 width="280" />')
    print('            <h3><a href="#web2">学习平台</a></h3>')
    print('            <p>支持直播与作业的教育 SaaS。</p>')
    print('        </li>')
    print('    </ul>')
    print('</section>')
    print()
    print('<!-- App 分类 -->')
    print('<section id="app">')
    print('    <h2>App 项目</h2>')
    print('    <ul>')
    print('        <li>')
    print('            <img src="app1.jpg"')
    print('                 alt="习惯追踪 App 主界面"')
    print('                 width="280" />')
    print('            <h3><a href="#app1">习惯追踪</a></h3>')
    print('            <p>每天一点点,养成好习惯。</p>')
    print('        </li>')
    print('        <li>')
    print('            <img src="app2.jpg"')
    print('                 alt="记账 App 报表页"')
    print('                 width="280" />')
    print('            <h3><a href="#app2">记账本</a></h3>')
    print('            <p>轻量个人财务助手。</p>')
    print('        </li>')
    print('    </ul>')
    print('</section>')
    print()
    print('<!-- Design 分类 -->')
    print('<section id="design">')
    print('    <h2>设计项目</h2>')
    print('    <ul>')
    print('        <li>')
    print('            <img src="design1.jpg"')
    print('                 alt="初创公司品牌 Logo"')
    print('                 width="280" />')
    print('            <h3><a href="#design1">品牌 Logo</a></h3>')
    print('            <p>初创公司视觉识别符号。</p>')
    print('        </li>')
    print('        <li>')
    print('            <img src="design2.jpg"')
    print('                 alt="活动主视觉海报"')
    print('                 width="280" />')
    print('            <h3><a href="#design2">活动海报</a></h3>')
    print('            <p>系列化视觉延展物料。</p>')
    print('        </li>')
    print('    </ul>')
    print('</section>')
    print()
    print("要点:")
    print("  ✓ 分类过滤 nav 的 href 指向各 section 的 id")
    print("  ✓ 每个分类一个 section,含 h2 + ul 卡片列表")
    print("  ✓ 每个 section 的 id 与过滤导航的锚点对应")
    print("  ✓ 更多分类 -> 加一个 section + 加一个 a 链接")
