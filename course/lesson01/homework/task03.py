"""
[难度: ★★★★]
[所属知识点: 自我介绍页面]
[预计完成时间: 30 分钟]
[类型: 选做]

题目:综合运用 Day 01 所有知识,编写一个完整的"自我介绍"HTML 页面。

要求:
1. 完整文档骨架(DOCTYPE/html/head/body/title/meta charset)
2. 页面内容包含:
   - h1:你的名字
   - h2 "关于我":一段自我介绍(p 标签)
   - h2 "我的爱好":用无序列表 ul/li 列出 3 个爱好
   - h2 "我的照片":插入一张图片(img,必须有 alt)
   - h2 "联系我":包含你的邮箱链接(a href="mailto:...")
3. 所有标签正确闭合
4. 保存为 about-me.html,用浏览器打开验证

进阶挑战(可选):
- 在页面底部加一行小字"© 2026 我的名字",用 <small> 标签
- 给邮箱链接加上 target="_blank"
"""

# ======================
# 学员代码区(独立编写完整页面)
# ======================
pass
# 在这里写出你的自我介绍页面:

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
    print('    <p>我是一名正在学习 HTML 的初学者。</p>')
    print('    <h2>我的爱好</h2>')
    print('    <ul>')
    print('        <li>阅读</li>')
    print('        <li>编程</li>')
    print('        <li>摄影</li>')
    print('    </ul>')
    print('    <h2>我的照片</h2>')
    print('    <img src="me.jpg" alt="张三的照片" width="200" />')
    print('    <h2>联系我</h2>')
    print('    <p><a href="mailto:zhangsan@example.com">给我发邮件</a></p>')
    print('    <small>© 2026 张三</small>')
    print('</body>')
    print('</html>')
    print()
    print("验收要点:")
    print("  ✓ 文档骨架完整")
    print("  ✓ h1 + 多个 h2 结构清晰")
    print("  ✓ ul/li 列表正确嵌套")
    print("  ✓ img 有 alt + 自闭合")
    print("  ✓ a 标签 href 正确")
