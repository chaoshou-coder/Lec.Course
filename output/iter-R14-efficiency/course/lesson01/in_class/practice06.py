"""
[难度: ★★★]
[所属知识点: 挑战题]
[预计完成时间: 15 分钟]
[类型: 挑战题,不强制完成]

题目:下面正则有什么问题?如何修正?

    pattern = r'<div>.*</div>'
    text = '<div>Hello</div><div>World</div>'
    re.findall(pattern, text)
    # 返回 ['<div>Hello</div><div>World</div>'] 而不是两个独立标签
"""

if __name__ == "__main__":
    print("问题:贪婪匹配 .* 匹配了太多内容")
    print("修正:")
    print("  pattern = r'<div>.*?</div>'(非贪婪)")
    print("  re.findall(pattern, text)  # ['<div>Hello</div>', '<div>World</div>']")
