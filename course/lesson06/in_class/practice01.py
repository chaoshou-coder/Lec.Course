"""
[难度: ★]
[所属知识点: button 类型认知]
[预计完成时间: 5 分钟]

题目:下面哪些描述是正确的?在正确的后面打 ✓,错误的后面打 ✗。

    1. <button>提交</button> 默认会提交表单          (  )
    2. <button type="button"> 点击后会提交表单      (  )
    3. <button type="reset"> 会清空表单所有输入     (  )
    4. <input type="submit" value="提交"> 比 <button> 更灵活(  )
    5. reset 按钮必须放在 form 里才能生效            (  )
    6. 一个 form 只能有一个 submit 按钮              (  )

提示:button 默认 type="submit",reset 需要关联表单才有效。
"""

# 学员不需要写代码,在纸上作答即可。
# 参考答案见下方测试区。

if __name__ == '__main__':
    # 参考答案
    answers = {
        1: "✓ 正确:button 默认 type=\"submit\",会提交",
        2: "✗ 错误:type=\"button\" 是普通按钮,不提交",
        3: "✓ 正确:reset 会恢复表单默认值",
        4: "✗ 错误:button 更灵活,里面可以放文字/图片等",
        5: "✓ 正确:reset 必须放在 form 里才能控制该表单",
        6: "✗ 错误:可以有多个,但通常只放一个",
    }
    for k, v in answers.items():
        print(f"  {k}. {v}")
