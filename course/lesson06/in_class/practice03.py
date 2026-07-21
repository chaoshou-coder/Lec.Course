"""
[难度: ★★]
[所属知识点: fieldset 分组]
[预计完成时间: 10 分钟]

题目:下面这个表单有 3 处错误,找出来并修正。

错误版本:
    <form action="/register" method="POST">
        <fieldset>
            <p>姓名:<input type="text" name="name" /></p>
            <legend>基本信息</legend>
            <p>年龄:<input type="number" name="age" /></p>
        </fieldset>

        <fieldset>
            <legend>账号信息</legend>
            <p>用户名:<input type="text" name="user" /></p>
        </fieldset>

        <fieldset>
            <p>密码:<input type="password" name="pwd" /></p>
        </fieldset>
    </form>

要求:
1. legend 的位置不对
2. 有一个 fieldset 缺少 legend
3. 整体结构要合理
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
    print("3 处错误:")
    print()
    print("  1. 第一个 fieldset 中,legend 不是第一个子元素")
    print("     → legend 应该放在 <fieldset> 之后,p 之前")
    print()
    print("  2. 第三个 fieldset 缺少 legend")
    print("     → 添加 <legend>安全信息</legend>")
    print()
    print("修正后完整版本:")
    print()
    print('<form action="/register" method="POST">')
    print('    <fieldset>')
    print('        <legend>基本信息</legend>')
    print('        <p>姓名:<input type="text" name="name" /></p>')
    print('        <p>年龄:<input type="number" name="age" /></p>')
    print('    </fieldset>')
    print('    <fieldset>')
    print('        <legend>账号信息</legend>')
    print('        <p>用户名:<input type="text" name="user" /></p>')
    print('    </fieldset>')
    print('    <fieldset>')
    print('        <legend>安全信息</legend>')
    print('        <p>密码:<input type="password" name="pwd" /></p>')
    print('    </fieldset>')
    print('</form>')
