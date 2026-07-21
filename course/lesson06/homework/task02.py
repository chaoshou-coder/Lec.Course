"""
[难度: ★★★]
[所属知识点: 多章节页面]
[预计完成时间: 20 分钟]
[类型: 选做]

题目:综合运用语义化标签,编写一个完整的"公司介绍"HTML 页面。

要求:
1. 完整文档骨架(DOCTYPE/html/head/body/title/meta charset)
2. title = "公司介绍"
3. 页面结构:
   - header: h1 主标题"ABC 公司" + p 副标题"让科技改变生活"
   - nav: 至少 4 个导航链接(首页/产品/关于我们/联系方式)
   - main 包含:
     - section"我们的使命":h2 + p
     - section"核心团队":h2 + 用 ul/li 列出 3 位成员
     - section"产品服务":h2 + 三个 article,每个 article 有
       h3 产品名 + p 产品描述
   - footer: 版权信息 + 联系地址(email 用 mailto: 链接)
4. 所有标签正确闭合,结构嵌套合理
"""

# ======================
# 学员代码区(独立编写完整页面)
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
    print('    <title>公司介绍</title>')
    print('</head>')
    print('<body>')
    print('    <header>')
    print('        <h1>ABC 公司</h1>')
    print('        <p>让科技改变生活</p>')
    print('    </header>')
    print('    <nav>')
    print('        <a href="index.html">首页</a>')
    print('        <a href="products.html">产品</a>')
    print('        <a href="about.html">关于我们</a>')
    print('        <a href="contact.html">联系方式</a>')
    print('    </nav>')
    print('    <main>')
    print('        <section>')
    print('            <h2>我们的使命</h2>')
    print('            <p>我们致力于用技术解决实际问题,'
    '为客户创造价值。</p>')
    print('        </section>')
    print('        <section>')
    print('            <h2>核心团队</h2>')
    print('            <ul>')
    print('                <li>张三 - CEO</li>')
    print('                <li>李四 - CTO</li>')
    print('                <li>王五 - 设计总监</li>')
    print('            </ul>')
    print('        </section>')
    print('        <section>')
    print('            <h2>产品服务</h2>')
    print('            <article>')
    print('                <h3>智能助手</h3>')
    print('                <p>基于 AI 的智能客服解决方案。</p>')
    print('            </article>')
    print('            <article>')
    print('                <h3>数据分析平台</h3>')
    print('                <p>帮助企业挖掘数据价值。</p>')
    print('            </article>')
    print('            <article>')
    print('                <h3>云存储服务</h3>')
    print('                <p>安全可靠的企业级云存储。</p>')
    print('            </article>')
    print('        </section>')
    print('    </main>')
    print('    <footer>')
    print('        <p>© 2026 ABC 公司</p>')
    print('        <p>联系: <a href="mailto:info@abc.com">'
    'info@abc.com</a></p>')
    print('    </footer>')
    print('</body>')
    print('</html>')
    print()
    print("验收要点:")
    print("  ✓ 文档骨架完整")
    print("  ✓ header/nav/main/footer 四个语义标签齐全")
    print("  ✓ main 里有 3 个 section,其中产品 section 有 3 个 article")
    print("  ✓ article 是独立内容,单独看也有意义")
    print("  ✓ footer 有 mailto: 邮箱链接")
