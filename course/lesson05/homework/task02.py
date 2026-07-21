"""
[难度: ★★★]
[所属知识点: 注册表单]
[预计完成时间: 20 分钟]
[类型: 选做]

题目:综合运用 Day 05 知识,独立编写一个完整的"用户注册"HTML 页面。

要求:
1. 完整文档骨架(DOCTYPE/html/head/body/title/meta charset)
2. title = "用户注册"
3. form action="/register" method="POST"
4. 表单内容包含:
   - 用户名(text,name="username",placeholder 提示)
   - 密码(password,name="password")
   - 确认密码(password,name="confirm")
   - 邮箱(email,name="email")
   - 年龄(number,name="age",min="1" max="150")
   - 性别(radio,name="gender",value 男/女,默认选中男)
   - 爱好(checkbox,name="hobby",value 阅读/运动/音乐,至少 3 个)
   - 所在城市(select name="city",至少 4 个option,含"请选择"提示)
   - 自我介绍(textarea name="intro",rows=4 cols=30)
   - 同意条款(checkbox,name="agree")
   - 注册按钮(button type="submit")
5. 所有标签正确闭合,所有必要属性齐全
"""

# ======================
# 学员代码区(独立编写完整注册页面)
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
    print('    <title>用户注册</title>')
    print('</head>')
    print('<body>')
    print('    <h1>用户注册</h1>')
    print('    <form action="/register" method="POST">')
    print('        <p>用户名:')
    print('            <input type="text" name="username" '
          'placeholder="请输入用户名" />')
    print('        </p>')
    print('        <p>密码:')
    print('            <input type="password" name="password" />')
    print('        </p>')
    print('        <p>确认密码:')
    print('            <input type="password" name="confirm" />')
    print('        </p>')
    print('        <p>邮箱:')
    print('            <input type="email" name="email" />')
    print('        </p>')
    print('        <p>年龄:')
    print('            <input type="number" name="age" '
          'min="1" max="150" />')
    print('        </p>')
    print('        <p>性别:')
    print('            <input type="radio" name="gender" '
          'value="male" checked /> 男')
    print('            <input type="radio" name="gender" '
          'value="female" /> 女')
    print('        </p>')
    print('        <p>爱好:')
    print('            <input type="checkbox" name="hobby" '
          'value="reading" /> 阅读')
    print('            <input type="checkbox" name="hobby" '
          'value="sports" /> 运动')
    print('            <input type="checkbox" name="hobby" '
          'value="music" /> 音乐')
    print('        </p>')
    print('        <p>所在城市:')
    print('            <select name="city">')
    print('                <option value="">--请选择--</option>')
    print('                <option value="beijing">北京</option>')
    print('                <option value="shanghai">上海</option>')
    print('                <option value="guangzhou">广州</option>')
    print('                <option value="shenzhen">深圳</option>')
    print('            </select>')
    print('        </p>')
    print('        <p>自我介绍:')
    print('            <textarea name="intro" rows="4" cols="30">'
          '</textarea>')
    print('        </p>')
    print('        <p>')
    print('            <input type="checkbox" name="agree" /> '
          '我同意用户条款')
    print('        </p>')
    print('        <p>')
    print('            <button type="submit">注册</button>')
    print('        </p>')
    print('    </form>')
    print('</body>')
    print('</html>')
    print()
    print("验收要点:")
    print("  ✓ 文档骨架完整")
    print("  ✓ form action + method=\"POST\"")
    print("  ✓ 所有 input 都有 name")
    print("  ✓ radio 有 value 且 name 相同")
    print("  ✓ checkbox 有 value 且 name 相同")
    print("  ✓ select + option 结构正确,option 有 value")
    print("  ✓ textarea 有闭标签")
    print("  ✓ 提交按钮 type=\"submit\"")
