"""
[难度: ★★★]
[所属知识点: 完整联系表单]
[预计完成时间: 15 分钟]

题目:为一个"独立开发者"编写完整的联系表单 HTML。

要求:
1. section id="contact" 包裹,标题 h2 "联系我"
2. form action="#" method="post" 包裹
3. 三个字段:
   - 姓名:text + required
   - 邮箱:email + required
   - 留言:textarea(rows=5, cols=30) + required
4. 提交按钮:"发送留言"
5. 所有 label 与 input 通过 for/id 关联
"""

# ======================
# 学员代码区(编写完整联系表单)
# ======================
pass
# 在这里写出完整 contact section:


# ======================
# 测试区
# ======================
if __name__ == '__main__':
    print("参考答案:")
    print()
    print('<section id="contact">')
    print('    <h2>联系我</h2>')
    print('    <form action="#" method="post">')
    print('        <p>')
    print('            <label for="name">姓名</label>')
    print('            <input type="text" id="name" name="name"')
    print('                   required />')
    print('        </p>')
    print('        <p>')
    print('            <label for="email">邮箱</label>')
    print('            <input type="email" id="email" name="email"')
    print('                   required />')
    print('        </p>')
    print('        <p>')
    print('            <label for="message">留言</label>')
    print('            <textarea id="message" name="message"')
    print('                      rows="5" cols="30"')
    print('                      required></textarea>')
    print('        </p>')
    print('        <button type="submit">发送留言</button>')
    print('    </form>')
    print('</section>')
    print()
    print("验收要点:")
    print("  ✓ section 含 h2")
    print("  ✓ form 有 action + method")
    print("  ✓ 三个字段:text/email/textarea")
    print("  ✓ 所有 label 有 for,input 有 id")
    print("  ✓ 所有字段 required")
    print("  ✓ button type=\"submit\"")
