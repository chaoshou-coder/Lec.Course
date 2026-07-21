"""
[难度: ★]
[所属知识点: 表单结构认知]
[预计完成时间: 5 分钟]

题目:下面哪些是合法的表单相关标签/属性?在合法的后面打 ✓,非法的后面打 ✗。

    1. <form action="/login" method="POST">   (  )
    2. <input type="text"></input>             (  )
    3. <select><option>苹果</option></select> (  )
    4. <textarea />                            (  )
    5. <input type="radio" name="a" />         (  )
    6. <form action="/login" />                (  )
    7. <option value="a">苹果</option>         (  )
    8. <input type="password">                 (  )

提示:input 是自闭合标签,textarea 不是自闭合标签,
     option 必须放在 select 里才有意义。
"""

# 学员不需要写代码,在纸上作答即可。
# 参考答案见下方测试区。

if __name__ == '__main__':
    # 参考答案
    answers = {
        1: "✓ 合法:form 的 action 和 method 都正确",
        2: "✗ 非法:input 是自闭合标签,不能写 </input>",
        3: "✓ 合法:select 包裹 option 是正确的",
        4: "✗ 非法:textarea 不是自闭合标签,应写为 <textarea></textarea>",
        5: "✓ 合法:radio 是合法的 input 类型",
        6: "✗ 非法:提交敏感数据应该用 method,默认 GET 不安全",
        7: "✓ 合法:option 语法正确(虽然通常放在 select 里)",
        8: "✓ 合法:password 是合法的 input 类型",
    }
    for k, v in answers.items():
        print(f"  {k}. {v}")
