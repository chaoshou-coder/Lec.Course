"""
[难度: ★★★]
[所属知识点: 完整分组表单]
[预计完成时间: 15 分钟]

题目:独立编写一个完整的"用户注册"HTML 页面,要求使用 label + fieldset + button。

要求:
1. 完整文档骨架(DOCTYPE/html/head/body/title/meta)
2. title = "用户注册"
3. form action="/register" method="POST"
4. 表单内容包含两个 fieldset:
   - 字段组 1 "基本信息":姓名(text) + 年龄(number) + 性别(radio)
   - 字段组 2 "账号信息":用户名(text) + 密码(password)
5. 所有 input 用 label 关联(for/id)
6. 底部有 submit 按钮和 reset 按钮
7. legend 必须是每个 fieldset 的第一个子元素
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
    print('    <title>用户注册</title>')
    print('</head>')
    print('<body>')
    print('    <h1>用户注册</h1>')
    print('    <form action="/register" method="POST">')
    print('        <fieldset>')
    print('            <legend>基本信息</legend>')
    print('            <p>')
    print('                <label for="name">姓名:</label>')
    print('                <input type="text" id="name" name="name" />')
    print('            </p>')
    print('            <p>')
    print('                <label for="age">年龄:</label>')
    print('                <input type="number" id="age" name="age" />')
    print('            </p>')
    print('            <p>')
    print('                <label>性别:</label>')
    print('                <input type="radio" name="gender" '
          'value="male" /> 男')
    print('                <input type="radio" name="gender" '
          'value="female" /> 女')
    print('            </p>')
    print('        </fieldset>')
    print('        <fieldset>')
    print('            <legend>账号信息</legend>')
    print('            <p>')
    print('                <label for="user">用户名:</label>')
    print('                <input type="text" id="user" name="username" />')
    print('            </p>')
    print('            <p>')
    print('                <label for="pwd">密码:</label>')
    print('                <input type="password" id="pwd" name="password" />')
    print('            </p>')
    print('        </fieldset>')
    print('        <p>')
    print('            <button type="submit">注册</button>')
    print('            <button type="reset">重置</button>')
    print('        </p>')
    print('    </form>')
    print('</body>')
    print('</html>')
    print()
    print("验收要点:")
    print("  ✓ 文档骨架完整")
    print("  ✓ 两个 fieldset,legend 都是第一个子元素")
    print("  ✓ label 通过 for 关联 input 的 id")
    print("  ✓ radio 的 name 相同")
    print("  ✓ submit + reset 按钮齐全")
