"""
[难度: ★★★]
[所属知识点: 修复错误表单]
[预计完成时间: 15 分钟]
[类型: 选做]

题目:你收到一份"损坏"的"用户调查"表单,本应分组收集用户信息,但结构混乱。

损坏版本:
    <html>
    <head><title>用户调查</title></head>
    <body>
        <form action="/survey">
            <fieldset>
                <p>姓名:<input type="text" name="name" /></p>
                <legend>基本信息</legend>
                <p>性别:
                    <input type="radio" value="male" /> 男
                    <input type="radio" value="female" /> 女
                </p>
            </fieldset>
            <fieldset>
                <legend>偏好设置</legend>
                <p>爱好:
                    <input type="checkbox" value="reading" /> 阅读
                    <input type="checkbox" value="music" /> 音乐
                </p>
            </fieldset>
            <button>提交</button>
        </form>
    </body>
    </html>

要求:
1. 找出全部 7 处错误(提示:涉及 DOCTYPE/meta/method/legend/name/button/label)
2. 写出修正后的完整文档
3. 保存为 survey.html,用浏览器打开验证
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
    print("7 处错误:")
    print()
    print("  1. 缺少 <!DOCTYPE html>")
    print("     原因:DOCTYPE 声明不能少")
    print()
    print("  2. 缺少 <meta charset=\"utf-8\">")
    print("     原因:没有 charset 中文可能乱码")
    print()
    print("  3. form 缺少 method")
    print("     原因:应该用 method=\"POST\"")
    print()
    print("  4. 第一个 fieldset 里 legend 不是第一个子元素")
    print("     原因:legend 必须在 fieldset 的最前面")
    print()
    print("  5. radio 缺少 name 属性")
    print("     原因:radio 必须 name 相同才能互斥")
    print()
    print("  6. checkbox 缺少 name 属性")
    print("     原因:没有 name 无法识别提交的数据")
    print()
    print("  7. <button> 没有 type")
    print("     原因:默认 submit,但显式写明更规范")
    print()
    print("额外优化(非错误):建议给 input 加 label 关联")
