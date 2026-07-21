"""
[难度: ★★★]
[所属知识点: 完整登录表单]
[预计完成时间: 15 分钟]

题目:独立编写一个完整的"用户登录"HTML 页面。

要求:
1. 完整文档骨架(DOCTYPE/html/head/body/title/meta)
2. title = "用户登录"
3. form 的 action="/login",method="POST"
4. 表单内容包含:
   - 用户名输入框(input type="text",name="username")
   - 密码输入框(input type="password",name="password")
   - 记住我复选框(checkbox,name="remember")
   - 登录按钮(button type="submit")
5. 每个输入前面有文字提示(用户名:/密码:/记住我)
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
    print("参考答案(示例):")
    print()
    print('<!DOCTYPE html>')
    print('<html lang="zh-CN">')
    print('<head>')
    print('    <meta charset="utf-8">')
    print('    <title>用户登录</title>')
    print('</head>')
    print('<body>')
    print('    <h1>用户登录</h1>')
    print('    <form action="/login" method="POST">')
    print('        <p>')
    print('            用户名:')
    print('            <input type="text" name="username" />')
    print('        </p>')
    print('        <p>')
    print('            密码:')
    print('            <input type="password" name="password" />')
    print('        </p>')
    print('        <p>')
    print('            <input type="checkbox" name="remember" /> 记住我')
    print('        </p>')
    print('        <p>')
    print('            <button type="submit">登录</button>')
    print('        </p>')
    print('    </form>')
    print('</body>')
    print('</html>')
    print()
    print("验收要点:")
    print("  ✓ 文档骨架完整")
    print("  ✓ form 有 action 和 method=\"POST\"")
    print("  ✓ 用户名 input type=\"text\" name=\"username\"")
    print("  ✓ 密码 input type=\"password\" name=\"password\"")
    print("  ✓ 记住我 checkbox name=\"remember\"")
    print("  ✓ 登录按钮 type=\"submit\"")
