"""
[难度: ★★★]
[所属知识点: 综合应用(挑战题)]
[预计完成时间: 15 分钟]

题目:下面是一个"损坏"的表单,有 5 处错误,找出来并写出正确版本。

损坏版本:
    <!DOCTYPE html>
    <html>
    <head>
        <title>调查问卷</title>
    </head>
    <body>
        <form action="/survey">
            <p>姓名:<input type=text name=username></p>
            <p>性别:
                <input type="radio" value="male" /> 男
                <input type="radio" value="female" /> 女
            </p>
            <p>爱好:
                <input type="checkbox" name="hobby" /> 阅读
                <input type="checkbox" name="hobby" /> 音乐
            </p>
            <p>城市:
                <select>
                    <option beijing>北京</option>
                    <option shanghai>上海</option>
                </select>
            </p>
            <p>建议:<textarea name="advice" /></p>
        </form>
    </body>

要求:找出全部 5 处错误(提示:涉及 meta/属性引号/select/radio/textarea)
"""

# ======================
# 学员代码区(写出修正后的完整页面)
# ======================
pass
# 在这里写出修正后的完整 HTML 页面:

# ======================
# 测试区
# ======================
if __name__ == '__main__':
    print("5 处错误:")
    print()
    print("  1. 缺少 <meta charset=\"utf-8\">")
    print("     原因:没有 charset 中文可能乱码")
    print()
    print("  2. <input type=text name=username>")
    print("     → <input type=\"text\" name=\"username\" />")
    print("     原因:属性值必须加引号,且 input 是自闭合标签")
    print()
    print("  3. 两个 radio 都缺少 name 属性")
    print("     → <input type=\"radio\" name=\"gender\" value=\"male\" />")
    print("     原因:radio 必须 name 相同才能互斥")
    print()
    print("  4. <select> 缺少 name,<option> 的 value 写成了属性名")
    print("     → <select name=\"city\">")
    print("     →     <option value=\"beijing\">北京</option>")
    print("     原因:select 需要 name,option 的值应该写在 value 里")
    print()
    print('  5. <textarea name="advice" />')
    print('     → <textarea name="advice"></textarea>')
    print("     原因:textarea 不是自闭合标签")
    print()
    print("边界测试(考考自己):")
    print("  - form 没有写 method,默认是什么?")
    print("    答:GET,数据会暴露在 URL 里")
    print("  - 如果 radio 的 name 分别是 sex1 和 sex2,会怎样?")
    print("    答:两个都能选中,失去单选效果")
