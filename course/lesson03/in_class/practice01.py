"""
[难度: ★]
[所属知识点: 链接标签认知]
[预计完成时间: 5 分钟]

题目:下面哪些是合法的 HTML 链接/图片标签?在合法的后面打 ✓,非法的后面打 ✗。

    1. <a href="https://example.com">示例</a>        (  )
    2. <a "https://example.com">示例</a>             (  )
    3. <a href="https://example.com"></a>            (  )
    4. <img src="cat.jpg" alt="猫" />                (  )
    5. <img "cat.jpg" alt="猫">                       (  )
    6. <img src="cat.jpg"></img>                     (  )
    7. <img src="cat.jpg">                           (  )
    8. <a href="url" target="_blank">链接</a>       (  )

提示:a 标签需要 href + 链接文字;img 需要 src + alt,且是自闭合标签。
"""

# 学员不需要写代码,在纸上作答即可。
# 参考答案见下方测试区。

if __name__ == '__main__':
    # 参考答案
    answers = {
        1: "✓ 合法:有 href,有链接文字,正确闭合",
        2: "✗ 非法:缺少 href 属性名,只有属性值",
        3: "✗ 非法:没有链接文字,用户看不到也无法点击",
        4: "✓ 合法:有 src 有 alt,自闭合正确",
        5: "✗ 非法:src 写成纯文本,缺少属性名",
        6: "✗ 非法:img 是自闭合标签,不能写 </img>",
        7: "✗ 非法:缺少 alt 属性(必填)",
        8: "✓ 合法:href + target + 链接文字都正确",
    }
    for k, v in answers.items():
        print(f"  {k}. {v}")
