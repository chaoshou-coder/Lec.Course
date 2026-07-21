"""
[难度: ★★★★]
[所属知识点: 完整多页面站点]
[预计完成时间: 40 分钟]
[类型: 选做]

题目:综合运用 Day 01~Day 07 所有知识,独立搭建一个完整的"企业官网"多页面站点。

目录结构要求:
    company-site/
    ├── index.html              ← 首页
    ├── about.html              ← 关于我们
    ├── products.html           ← 产品页
    ├── contact.html            ← 联系页
    ├── css/
    │   └── style.css           ← 样式文件(只需创建空文件)
    ├── js/
    │   └── main.js             ← 脚本文件(只需创建空文件)
    └── images/
        ├── logo.jpg            ← Logo(可用占位图片)
        └── banner.jpg          ← 横幅(可用占位图片)

页面要求(所有页面共用):
- header: img logo + h1 公司名 + p 标语
- nav: 4 个链接(首页/关于/产品/联系),所有页面一致
- footer: 版权信息 + 邮箱 mailto: 链接 + 导航链接组

页面差异部分:
- index.html: 英雄区(h2 + p + a) + 服务介绍(3 个 article,含 img)
- about.html: 公司简介(h2 + p) + 核心数据(table 带 th,3 行)
- products.html: 产品列表(3 个 article,每个含 h3 + img + p + 价格)
- contact.html: 联系信息(h2 + ul/li) + 联系表单
  - form 用 fieldset 分组(您的信息 + 留言内容)
  - 您的信息:姓名(text) + 邮箱(email) + 电话(tel)
  - 留言内容:主题(select) + 留言(textarea)
  - 提交按钮

代码要求:
1. 所有页面代码缩进一致(每层 4 空格)
2. 关键位置有注释(每个页面至少 4 处)
3. 表单使用 label 关联 input,fieldset 分组
4. 所有相对路径正确
5. 语义化标签齐全(header/nav/main/section/article/footer)
6. 代码可读性强,空行分隔逻辑块

进阶挑战(可选):
- 在 about.html 的表格里用 th 做表头
- 在 products.html 里给产品加"购买"链接(a 标签)
- 在 contact.html 的电话 input 使用 type="tel"
- 在 footer 里加 small 标签声明版权
"""

# ======================
# 学员代码区(独立编写完整站点)
# ======================

# index.html
pass
# 在这里写出 index.html:

# about.html
pass
# 在这里写出 about.html:

# products.html
pass
# 在这里写出 products.html:

# contact.html
pass
# 在这里写出 contact.html:

# ======================
# 测试区
# ======================
if __name__ == '__main__':
    print("参考答案(四个页面的示例结构):")
    print()
    print("=" * 50)
    print("index.html (首页):")
    print("=" * 50)
    print()
    print('<!DOCTYPE html>')
    print('<html lang="zh-CN">')
    print('<head>')
    print('    <meta charset="utf-8">')
    print('    <title>TechCorp - 首页</title>')
    print('    <link rel="stylesheet" href="css/style.css" />')
    print('</head>')
    print('<body>')
    print('    <!-- 页头:Logo + 公司名 + 标语 -->')
    print('    <header>')
    print('        <img src="images/logo.jpg" alt="TechCorp Logo" />')
    print('        <h1>TechCorp</h1>')
    print('        <p>创新驱动未来</p>')
    print('    </header>')
    print()
    print('    <!-- 导航栏:链接到所有页面 -->')
    print('    <nav>')
    print('        <a href="index.html">首页</a>')
    print('        <a href="about.html">关于</a>')
    print('        <a href="products.html">产品</a>')
    print('        <a href="contact.html">联系</a>')
    print('    </nav>')
    print()
    print('    <!-- 主体内容 -->')
    print('    <main>')
    print('        <!-- 英雄区 -->')
    print('        <section>')
    print('            <h2>引领数字化转型</h2>')
    print('            <p>我们为企业提供一站式技术解决方案。</p>')
    print('            <a href="about.html">了解更多</a>')
    print('        </section>')
    print()
    print('        <!-- 服务介绍 -->')
    print('        <section>')
    print('            <h2>我们的服务</h2>')
    print('            <article>')
    print('                <h3>Web 开发</h3>')
    print('                <img src="images/web.jpg" alt="Web 开发" />')
    print('                <p>专业的网站和 Web 应用开发。</p>')
    print('            </article>')
    print('            <article>')
    print('                <h3>移动应用</h3>')
    print('                <img src="images/mobile.jpg" alt="移动应用" />')
    print('                <p>iOS 和 Android 原生应用开发。</p>')
    print('            </article>')
    print('            <article>')
    print('                <h3>云服务</h3>')
    print('                <img src="images/cloud.jpg" alt="云服务" />')
    print('                <p>安全可靠的云计算基础设施。</p>')
    print('            </article>')
    print('        </section>')
    print('    </main>')
    print()
    print('    <!-- 页脚 -->')
    print('    <footer>')
    print('        <p><small>© 2026 TechCorp. 保留所有权利。</small></p>')
    print('        <a href="mailto:info@techcorp.com">info@techcorp.com</a>')
    print('    </footer>')
    print('    <script src="js/main.js"></script>')
    print('</body>')
    print('</html>')
    print()
    print("=" * 50)
    print("about.html (关于我们):")
    print("=" * 50)
    print()
    print('(header/nav/footer 与 index.html 相同,省略)')
    print()
    print('    <!-- 主体内容 -->')
    print('    <main>')
    print('        <!-- 公司简介 -->')
    print('        <section>')
    print('            <h2>公司简介</h2>')
    print('            <p>TechCorp 成立于 2020 年,'
    '专注于企业数字化转型。</p>')
    print('        </section>')
    print()
    print('        <!-- 核心数据 -->')
    print('        <section>')
    print('            <h2>核心数据</h2>')
    print('            <table>')
    print('                <tr><th>指标</th><th>数据</th></tr>')
    print('                <tr><td>服务客户</td><td>500+</td></tr>')
    print('                <tr><td>完成项目</td><td>1200+</td></tr>')
    print('                <tr><td>团队规模</td><td>150+</td></tr>')
    print('            </table>')
    print('        </section>')
    print('    </main>')
    print()
    print("=" * 50)
    print("products.html (产品页):")
    print("=" * 50)
    print()
    print('(header/nav/footer 与 index.html 相同,省略)')
    print()
    print('    <!-- 主体内容 -->')
    print('    <main>')
    print('        <section>')
    print('            <h2>我们的产品</h2>')
    print('            <article>')
    print('                <h3>智能助手</h3>')
    print('                <img src="images/product1.jpg" alt="智能助手" />')
    print('                <p>基于 AI 的智能客服解决方案。</p>')
    print('                <p>价格:¥9999</p>')
    print('                <a href="contact.html">立即购买</a>')
    print('            </article>')
    print('            <article>')
    print('                <h3>数据分析平台</h3>')
    print('                <img src="images/product2.jpg" alt="数据分析" />')
    print('                <p>帮助企业挖掘数据价值。</p>')
    print('                <p>价格:¥14999</p>')
    print('                <a href="contact.html">立即购买</a>')
    print('            </article>')
    print('            <article>')
    print('                <h3>云存储服务</h3>')
    print('                <img src="images/product3.jpg" alt="云存储" />')
    print('                <p>安全可靠的企业级云存储。</p>')
    print('                <p>价格:¥4999</p>')
    print('                <a href="contact.html">立即购买</a>')
    print('            </article>')
    print('        </section>')
    print('    </main>')
    print()
    print("=" * 50)
    print("contact.html (联系页):")
    print("=" * 50)
    print()
    print('(header/nav/footer 与 index.html 相同,省略)')
    print()
    print('    <!-- 主体内容 -->')
    print('    <main>')
    print('        <!-- 联系信息 -->')
    print('        <section>')
    print('            <h2>联系信息</h2>')
    print('            <ul>')
    print('                <li>地址:北京市海淀区科技路 1 号</li>')
    print('                <li>电话:400-123-4567</li>')
    print('                <li>邮箱:info@techcorp.com</li>')
    print('            </ul>')
    print('        </section>')
    print()
    print('        <!-- 联系表单 -->')
    print('        <section>')
    print('            <h2>给我们留言</h2>')
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
    print('                    <p>')
    print('                        <label for="cphone">电话:</label>')
    print('                        <input type="tel" id="cphone" name="phone" />')
    print('                    </p>')
    print('                </fieldset>')
    print('                <fieldset>')
    print('                    <legend>留言内容</legend>')
    print('                    <p>')
    print('                        <label for="csubject">主题:</label>')
    print('                        <select id="csubject" name="subject">')
    print('                            <option value="">--请选择--</option>')
    print('                            <option value="consult">咨询</option>')
    print('                            <option value="cooperate">合作</option>')
    print('                            <option value="other">其他</option>')
    print('                        </select>')
    print('                    </p>')
    print('                    <p>')
    print('                        <label for="cmsg">留言:</label>')
    print('                        <textarea id="cmsg" name="message" '
          'rows="5" cols="40"></textarea>')
    print('                    </p>')
    print('                </fieldset>')
    print('                <p>')
    print('                    <button type="submit">提交</button>')
    print('                </p>')
    print('            </form>')
    print('        </section>')
    print('    </main>')
    print()
    print("验收要点:")
    print("  ✓ 目录结构清晰,css/js/images 分目录")
    print("  ✓ 四个页面 nav 一致,header/footer 相同")
    print("  ✓ 语义化标签齐全")
    print("  ✓ 代码缩进一致,有注释")
    print("  ✓ 表单 fieldset 分组,label 关联 input")
    print("  ✓ table 有 th 表头")
    print("  ✓ 所有相对路径正确")
    print("  ✓ img 有 alt,textarea 有闭标签")
