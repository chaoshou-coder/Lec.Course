"""
[难度: ★★★]
[所属知识点: 修复错误表单]
[预计完成时间: 15 分钟]
[类型: 选做]

题目:你收到一份"损坏"的"用户注册"表单,本应能正确收集用户信息,但渲染和数据提交都有问题。

损坏版本:
    <html>
    <head><title>注册</title></head>
    <body>
        <form action="register.html">
            <p>用户名:<input type="text" /></p>
            <p>邮箱:<input type="email" name="email" /></p>
            <p>密码:<input type="password" name="pwd"></input></p>
            <p>性别:
                <input type="radio" name="gender" /> 男
                <input type="radio" name="gender" /> 女
            </p>
            <p>年龄段:
                <select name="age">
                    <option>18以下</option>
                    <option>18-30</option>
                </select>
            </p>
            <p>简介:<textarea name="intro" /></p>
        </form>
    </body>
    </html>

要求:
1. 找出全部 6 处错误(提示:涉及 DOCTYPE/meta/method/标签闭合/name/value)
2. 写出修正后的完整文档
3. 保存为 register.html,用浏览器打开验证
"""

# ======================
# 学员代码区
# ======================
pass
# 在这里写出修正后的完整文档:

# ======================
# 测试区
# ======================
if __name__ == '__main__':
    print("6 处错误:")
    print()
    print("  1. 缺少 <!DOCTYPE html> 和 <meta charset=\"utf-8\">")
    print('     原因:DOCTYPE 声明和编码声明不能少')
    print()
    print('  2. <form action="register.html"> 缺少 method')
    print('     原因:注册信息敏感,应该用 method="POST"')
    print()
    print('  3. <input type="text" /> 缺少 name')
    print('     原因:没有 name 提交时无法识别字段')
    print()
    print('  4. <input type="password" name="pwd"></input>')
    print('     原因:input 是自闭合标签,不能写 </input>')
    print()
    print('  5. radio 缺少 value 属性')
    print('     原因:没有 value 提交时不知道选了哪个')
    print()
    print('  6. option 缺少 value,textarea 自闭合写法错误')
    print('     原因:option 要用 value 存值,textarea 要写闭标签')
