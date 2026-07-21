"""
[难度: ★★]
[所属知识点: input 类型辨析]
[预计完成时间: 10 分钟]

题目:下面的表单有 4 处错误,找出来并修正。

错误版本:
    <form action="/signup">
        <input type="text" placeholder="用户名" />
        <input type="password">请输入密码</input>
        <input type="radiobutton" name="gender" value="male" />
        <input type="check" name="agree" />
    </form>

要求:
1. form 缺少 method
2. input 类型名写错了
3. input 标签形态有误
4. 部分 input 缺少 name
"""

# ======================
# 学员代码区(写出修正后的完整表单)
# ======================
pass
# 在这里写出修正后的版本:

# ======================
# 测试区
# ======================
if __name__ == '__main__':
    print("参考答案:")
    print()
    print("4 处错误:")
    print('  1. <form action="/signup"> → '
          '<form action="/signup" method="POST">')
    print('     原因:提交注册信息应该用 POST')
    print()
    print('  2. <input type="text" placeholder="用户名" /> → '
          '<input type="text" name="username" placeholder="用户名" />')
    print('     原因:缺少 name 属性')
    print()
    print('  3. <input type="password">请输入密码</input> → '
          '<input type="password" name="password" />')
    print('     原因:input 是自闭合标签,不能写 </input>')
    print()
    print('  4. <input type="radiobutton" ...> → '
          '<input type="radio" ...>')
    print('     <input type="check" ...> → '
          '<input type="checkbox" ...>')
    print('     原因:类型名应该是 radio 和 checkbox')
    print()
    print("修正后完整版本:")
    print('<form action="/signup" method="POST">')
    print('    <input type="text" name="username" placeholder="用户名" />')
    print('    <input type="password" name="password" />')
    print('    <input type="radio" name="gender" value="male" />')
    print('    <input type="checkbox" name="agree" />')
    print('</form>')
