"""
[难度: ★★★★]
[所属知识点: 完整企业官网首页]
[预计完成时间: 30 分钟]
[类型: 选做]

题目:综合运用 Day 01~Day 06 所有知识,编写一个完整的"企业官网首页"HTML 页面。

要求:
1. 完整文档骨架(DOCTYPE/html/head/body/title/meta charset)
2. title = "TechCorp 官网"
3. 页面结构(语义化):
   - header: h1 公司名 + p 标语
   - nav: 至少 5 个导航链接
   - main 包含:
     - section"英雄区":h2 大标题 + p 描述 + a 链接(了解更多)
     - section"服务介绍":h2 + 三个 article,每个 article 有
       h3 + p + img(有 alt)
     - section"数据展示":h2 + table 展示 3 项核心数据(带 th)
     - section"联系我们":h2 + form
       - fieldset"您的信息":legend + label + input(text/email)
       - fieldset"留言内容":legend + label + textarea
       - button type="submit" 提交
   - footer: 版权 + 导航链接组 + 邮箱 mailto: 链接
4. 表单使用 label 关联 input,fieldset 分组,legend 为第一个子元素
5. 所有标签正确闭合,结构嵌套合理

进阶挑战(可选):
- 在 header 里加一个 img 作为公司 logo
- 在数据表格里用 th 做表头
- 给外部链接加 target="_blank"
- 在 footer 里加 small 标签声明版权
"""

# ======================
# 学员代码区(独立编写完整官网首页)
# ======================
pass
# 在这里写出你的完整 HTML 页面:


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
    print('    <title>TechCorp 官网</title>')
    print('</head>')
    print('<body>')
    print('    <header>')
    print('        <h1>TechCorp</h1>')
    print('        <p>创新驱动未来</p>')
    print('    </header>')
    print('    <nav>')
    print('        <a href="index.html">首页</a>')
    print('        <a href="services.html">服务</a>')
    print('        <a href="about.html">关于我们</a>')
    print('        <a href="cases.html">案例</a>')
    print('        <a href="contact.html">联系我们</a>')
    print('    </nav>')
    print('    <main>')
    print('        <section>')
    print('            <h2>引领数字化转型</h2>')
    print('            <p>我们为企业提供一站式技术解决方案。</p>')
    print('            <a href="services.html">了解更多</a>')
    print('        </section>')
    print('        <section>')
    print('            <h2>我们的服务</h2>')
    print('            <article>')
    print('                <h3>Web 开发</h3>')
    print('                <img src="web.jpg" alt="Web 开发" width="200" />')
    print('                <p>专业的网站和 Web 应用开发服务。</p>')
    print('            </article>')
    print('            <article>')
    print('                <h3>移动应用</h3>')
    print('                <img src="mobile.jpg" alt="移动应用" width="200" />')
    print('                <p>iOS 和 Android 原生应用开发。</p>')
    print('            </article>')
    print('            <article>')
    print('                <h3>云服务</h3>')
    print('                <img src="cloud.jpg" alt="云服务" width="200" />')
    print('                <p>安全可靠的云计算基础设施。</p>')
    print('            </article>')
    print('        </section>')
    print('        <section>')
    print('            <h2>核心数据</h2>')
    print('            <table>')
    print('                <tr><th>指标</th><th>数据</th></tr>')
    print('                <tr><td>服务客户</td><td>500+</td></tr>')
    print('                <tr><td>完成项目</td><td>1200+</td></tr>')
    print('                <tr><td>团队规模</td><td>150+</td></tr>')
    print('            </table>')
    print('        </section>')
    print('        <section>')
    print('            <h2>联系我们</h2>')
    print('            <form action="/contact" method="POST">')
    print('                <fieldset>')
    print('                    <legend>您的信息</legend>')
    print('                    <p>')
    print('                        <label for="cname">姓名:</label>')
    print('                        <input type="text" id="cname" name="name" />')
    print('                    </p>')
    print('                    <p>')
    print('                        <label for="cemail">邮箱:</label>')
    print('                        <input type="email" id="cemail" name="email" />')
    print('                    </p>')
    print('                </fieldset>')
    print('                <fieldset>')
    print('                    <legend>留言内容</legend>')
    print('                    <p>')
    print('                        <label for="msg">留言:</label>')
    print('                        <textarea id="msg" name="message" '
          'rows="5" cols="40"></textarea>')
    print('                    </p>')
    print('                </fieldset>')
    print('                <p>')
    print('                    <button type="submit">提交</button>')
    print('                </p>')
    print('            </form>')
    print('        </section>')
    print('    </main>')
    print('    <footer>')
    print('        <p><small>© 2026 TechCorp. 保留所有权利。</small></p>')
    print('        <a href="mailto:info@techcorp.com">info@techcorp.com</a>')
    print('    </footer>')
    print('</body>')
    print('</html>')
    print()
    print("验收要点:")
    print("  ✓ 文档骨架完整,语义化标签齐全")
    print("  ✓ header/nav/main/footer 结构清晰")
    print("  ✓ main 里有 4 个 section,服务 section 有 3 个 article")
    print("  ✓ table 有 th 表头")
    print("  ✓ form 有 fieldset 分组,label 关联 input")
    print("  ✓ legend 是 fieldset 的第一个子元素")
    print("  ✓ img 有 alt,textarea 有闭标签")
