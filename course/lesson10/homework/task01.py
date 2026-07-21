"""
[难度: ★★★]
[所属知识点: 修复表单错误]
[预计完成时间: 15 分钟]
[类型: 选做]

题目:你收到一份"损坏"的联系表单,有 5 处错误。找出来并修正。

损坏版本:
    <section id="contact">
        <h2>联系我</h2>
        <form action="#">
            <p>
                <label="name">姓名</label>
                <input type="text" id="name" name="name" />
            </p>
            <p>
                <label for="email">邮箱</label>
                <input type="email" name="email" />
            </p>
            <p>
                <label for="phone">电话</label>
                <input type="tel" id="phone" name="phone"
                       placeholder="13800138000" value="13800138000" />
            </p>
            <p>
                <label for="msg">留言</label>
                <textarea id="msg" name="msg"></textarea>
            </p>
            <button type="button">提交</button>
        </form>
    </section>

要求:
1. 找出全部 5 处错误(提示:label 写法/id 缺失/placeholder 与 value/button type)
2. 写出修正后的完整 section
3. 每处错误标注原因
"""

# ======================
# 学员代码区(写出修正后 section)
# ======================
pass
# 在这里写出修正后的完整 section:


# ======================
# 测试区
# ======================
if __name__ == '__main__':
    print("5 处错误及修正:")
    print()
    print("  1. <label=\"name\"> → <label for=\"name\">")
    print("     原因:label 用 for 属性关联 input,不是 label=\"\"")
    print()
    print("  2. 邮箱 input 缺少 id=\"email\"")
    print("     原因:label for=\"email\" 需要对应 input id=\"email\"")
    print()
    print("  3. 电话 input 不应有 value=\"13800138000\"")
    print("     原因:value 是默认值,会提交到后台;placeholder 才是提示")
    print()
    print("  4. textarea 缺少 rows 和 cols")
    print("     原因:没有尺寸属性时 textarea 默认很小,体验差")
    print()
    print("  5. button type=\"button\" 应改为 type=\"submit\"")
    print("     原因:type=\"button\" 是普通按钮,不会触发表单提交")
    print()
    print("修正后完整 section:")
    print('<section id="contact">')
    print('    <h2>联系我</h2>')
    print('    <form action="#" method="post">')
    print('        <p>')
    print('            <label for="name">姓名</label>')
    print('            <input type="text" id="name" name="name" />')
    print('        </p>')
    print('        <p>')
    print('            <label for="email">邮箱</label>')
    print('            <input type="email" id="email" name="email" />')
    print('        </p>')
    print('        <p>')
    print('            <label for="phone">电话</label>')
    print('            <input type="tel" id="phone" name="phone"')
    print('                   placeholder="13800138000" />')
    print('        </p>')
    print('        <p>')
    print('            <label for="msg">留言</label>')
    print('            <textarea id="msg" name="msg"')
    print('                      rows="5" cols="30"></textarea>')
    print('        </p>')
    print('        <button type="submit">提交</button>')
    print('    </form>')
    print('</section>')
