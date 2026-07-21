"""
[难度: ★★★★]
[所属知识点: 个人主页(综合)]
[预计完成时间: 30 分钟]
[类型: 选做]

题目:综合运用 Day 01~Day 03 所有知识,编写一个完整的"个人主页"HTML 页面。

要求:
1. 完整文档骨架(DOCTYPE/html/head/body/title/meta charset)
2. 页面内容包含:
   - h1:你的名字
   - h2 "关于我":一段自我介绍(p 标签)
   - h2 "我的照片":插入一张图片(img,必须有 alt)
   - h2 "我的爱好":用无序列表 ul/li 列出 3 个爱好
   - h2 "学习目标":用有序列表 ol/li 列出 3 个目标
   - hr 分隔线
   - h2 "我的城市":h3 城市名 + img 图片 + p 描述
   - h2 "与我联系":包含邮箱链接(a href="mailto:you@example.com")
3. 所有标签正确闭合
4. 保存为 my-page.html,用浏览器打开验证

进阶挑战(可选):
- 在页面底部加一行小字"© 2026 我的名字",用 <small> 标签
- 给外部链接加上 target="_blank"
- 在爱好列表中,每个爱好文字做成链接(a href),点击跳转到相关介绍页
"""

# ======================
# 学员代码区(独立编写完整页面)
# ======================
pass
# 在这里写出你的个人主页:


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
    print('    <title>张三的个人主页</title>')
    print('</head>')
    print('<body>')
    print('    <h1>张三</h1>')
    print('    <h2>关于我</h2>')
    print('    <p>我是一名正在学习 HTML 的初学者,热爱编程和设计。</p>')
    print('    <h2>我的照片</h2>')
    print('    <img src="me.jpg" alt="张三的照片" width="200" />')
    print('    <h2>我的爱好</h2>')
    print('    <ul>')
    print('        <li>阅读</li>')
    print('        <li>编程</li>')
    print('        <li>摄影</li>')
    print('    </ul>')
    print('    <h2>学习目标</h2>')
    print('    <ol>')
    print('        <li>掌握 HTML 基础</li>')
    print('        <li>学会 CSS 样式</li>')
    print('        <li>制作个人作品集</li>')
    print('    </ol>')
    print('    <hr>')
    print('    <h2>我的城市</h2>')
    print('    <h3>北京</h3>')
    print('    <img src="beijing.jpg" alt="北京天安门" width="300" />')
    print('    <p>北京是中国的首都,历史悠久,文化底蕴深厚。</p>')
    print('    <h2>与我联系</h2>')
    print('    <p><a href="mailto:zhangsan@example.com">给我发邮件</a></p>')
    print('    <small>© 2026 张三</small>')
    print('</body>')
    print('</html>')
    print()
    print("验收要点:")
    print("  ✓ 文档骨架完整")
    print("  ✓ h1 + 多个 h2 + h3 结构清晰")
    print("  ✓ ul/li 和 ol/li 列表正确")
    print("  ✓ img 有 alt + 自闭合")
    print("  ✓ a 标签 href 正确(mailto: 邮箱链接)")
