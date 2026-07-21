"""
[难度: ★★★★]
[所属知识点: 综合调查问卷]
[预计完成时间: 30 分钟]
[类型: 选做]

题目:综合运用 Day 01~Day 05 所有知识,编写一个完整的"产品满意度调查问卷"HTML 页面。

要求:
1. 完整文档骨架(DOCTYPE/html/head/body/title/meta charset)
2. title = "产品满意度调查"
3. form action="/survey" method="POST"
4. 页面结构:
   - h1 主标题"产品满意度调查"
   - p 段落简要说明调查目的
   - hr 分隔线
5. 表单内容包含:
   - 姓名(text,name="name")
   - 邮箱(email,name="email")
   - 年龄段(radio,name="age_range",value 18以下/18-30/31-50/50以上)
   - 满意度(radio,name="satisfaction",value 非常满意/满意/一般/不满意)
   - 使用频率(radio,name="frequency",value 每天/每周/每月/几乎不用)
   - 喜欢的功能(checkbox,name="feature",至少 4 个选项)
   - 改进建议(textarea name="suggestion" rows=5 cols=40)
   - 是否愿意参加深度访谈(radio,name="interview",value 是/否)
   - 提交按钮(button type="submit")
6. 每个输入区域用 p 标签包裹,结构清晰

进阶挑战(可选):
- 在表单底部加一行小字"感谢您的参与!",用 <small> 标签
- 在满意度选项后加入表情符号(如 😊 😐 😞)
- 给必填项加上 *(星号)标记
"""

# ======================
# 学员代码区(独立编写完整问卷)
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
    print('    <title>产品满意度调查</title>')
    print('</head>')
    print('<body>')
    print('    <h1>产品满意度调查</h1>')
    print('    <p>感谢您花时间填写此问卷,您的反馈对我们非常重要。</p>')
    print('    <hr>')
    print('    <form action="/survey" method="POST">')
    print('        <p>姓名:')
    print('            <input type="text" name="name" />')
    print('        </p>')
    print('        <p>邮箱:')
    print('            <input type="email" name="email" />')
    print('        </p>')
    print('        <p>年龄段:')
    print('            <input type="radio" name="age_range" '
          'value="under18" /> 18以下')
    print('            <input type="radio" name="age_range" '
          'value="18-30" /> 18-30')
    print('            <input type="radio" name="age_range" '
          'value="31-50" /> 31-50')
    print('            <input type="radio" name="age_range" '
          'value="over50" /> 50以上')
    print('        </p>')
    print('        <p>满意度:')
    print('            <input type="radio" name="satisfaction" '
          'value="very_good" /> 非常满意')
    print('            <input type="radio" name="satisfaction" '
          'value="good" /> 满意')
    print('            <input type="radio" name="satisfaction" '
          'value="ok" /> 一般')
    print('            <input type="radio" name="satisfaction" '
          'value="bad" /> 不满意')
    print('        </p>')
    print('        <p>使用频率:')
    print('            <input type="radio" name="frequency" '
          'value="daily" /> 每天')
    print('            <input type="radio" name="frequency" '
          'value="weekly" /> 每周')
    print('            <input type="radio" name="frequency" '
          'value="monthly" /> 每月')
    print('            <input type="radio" name="frequency" '
          'value="rarely" /> 几乎不用')
    print('        </p>')
    print('        <p>喜欢的功能(可多选):')
    print('            <input type="checkbox" name="feature" '
          'value="ui" /> 界面美观')
    print('            <input type="checkbox" name="feature" '
          'value="speed" /> 速度快')
    print('            <input type="checkbox" name="feature" '
          'value="stable" /> 稳定性好')
    print('            <input type="checkbox" name="feature" '
          'value="support" /> 客服响应快')
    print('        </p>')
    print('        <p>改进建议:')
    print('            <textarea name="suggestion" rows="5" '
          'cols="40"></textarea>')
    print('        </p>')
    print('        <p>是否愿意参加深度访谈:')
    print('            <input type="radio" name="interview" '
          'value="yes" /> 是')
    print('            <input type="radio" name="interview" '
          'value="no" /> 否')
    print('        </p>')
    print('        <p>')
    print('            <button type="submit">提交问卷</button>')
    print('        </p>')
    print('    </form>')
    print('    <small>感谢您的参与!</small>')
    print('</body>')
    print('</html>')
    print()
    print("验收要点:")
    print("  ✓ 文档骨架完整,h1+p+hr+form 结构清晰")
    print("  ✓ text/email/radio/checkbox/textarea 类型正确")
    print("  ✓ 所有 radio 组 name 相同,option 有 value")
    print("  ✓ 所有 input/name/value 齐全")
    print("  ✓ textarea 有闭标签")
