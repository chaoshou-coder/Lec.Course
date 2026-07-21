"""
[难度: ★★]
[所属知识点: 贪婪/非贪婪]
[预计完成时间: 10 分钟]

题目:用贪婪和非贪婪匹配提取 '<div>Hello</div>' 中的标签内容。
"""

if __name__ == "__main__":
    print("参考答案:")
    print("  import re")
    print("  re.findall(r'<.*>', '<div>Hello</div>')   # ['<div>Hello</div>']")
    print("  re.findall(r'<.*?>', '<div>Hello</div>')  # ['<div>', '</div>']")
