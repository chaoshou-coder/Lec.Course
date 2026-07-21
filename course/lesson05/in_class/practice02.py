"""
[难度: ★]
[所属知识点: 写出第一个表单]
[预计完成时间: 5 分钟]

题目:补全下面的表单,让它能接收用户名并提交到 /login,使用 POST 方式。

要求:
1. form 的 action="/login",method="POST"
2. 里面有一个 type="text" 的 input,name="username"
3. 有一个提交按钮
"""

# ======================
# 学员代码区(补全下面的表单)
# ======================
pass
# 在这里写出完整表单:

# ======================
# 测试区
# ======================
if __name__ == '__main__':
    # 参考答案
    print("参考答案:")
    print()
    print('<form action="/login" method="POST">')
    print('    <input type="text" name="username" />')
    print('    <button type="submit">登录</button>')
    print('</form>')
    print()
    print("检查要点:")
    print("  1. form 有 action 和 method ✓")
    print("  2. input 有 type=\"text\" 和 name=\"username\" ✓")
    print("  3. button 的 type=\"submit\" ✓")
    print("  4. input 是自闭合标签 ✓")
