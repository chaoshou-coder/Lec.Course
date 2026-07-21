"""
[难度: ★★★]
[所属知识点: 表单无障碍(label)]
[预计完成时间: 15 分钟]

题目:下面是一个"缺少 label"的表单,请补全所有 label 并正确关联。

原版本(无 label):
    <form action="#" method="post">
        <p>
            <input type="text" id="fullname" name="fullname" />
        </p>
        <p>
            <input type="email" id="email" name="email" />
        </p>
        <p>
            <input type="tel" id="phone" name="phone" />
        </p>
        <p>
            <textarea id="msg" name="msg" rows="4"></textarea>
        </p>
        <button type="submit">提交</button>
    </form>

要求:
1. 为每个 input/textarea 添加 label
2. label 文本自拟(如"姓名""邮箱""电话""留言")
3. 通过 for/id 关联
4. label 放在 input 前面(视觉上标题在输入框上方或左侧)
"""

# ======================
# 学员代码区(添加 label)
# ======================
pass
# 在这里写出带 label 的完整 form:


# ======================
# 测试区
# ======================
if __name__ == '__main__':
    print("参考答案:")
    print()
    print('<form action="#" method="post">')
    print('    <p>')
    print('        <label for="fullname">姓名</label>')
    print('        <input type="text" id="fullname" name="fullname" />')
    print('    </p>')
    print('    <p>')
    print('        <label for="email">邮箱</label>')
    print('        <input type="email" id="email" name="email" />')
    print('    </p>')
    print('    <p>')
    print('        <label for="phone">电话</label>')
    print('        <input type="tel" id="phone" name="phone" />')
    print('    </p>')
    print('    <p>')
    print('        <label for="msg">留言</label>')
    print('        <textarea id="msg" name="msg" rows="4"></textarea>')
    print('    </p>')
    print('    <button type="submit">提交</button>')
    print('</form>')
    print()
    print("要点:")
    print("  ✓ label 的 for 必须等于 input 的 id")
    print("  ✓ label 提供了可点击的标题(提升体验)")
    print("  ✓ 读屏软件会朗读 label 文本")
