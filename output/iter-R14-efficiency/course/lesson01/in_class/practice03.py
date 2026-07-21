"""
[难度: ★★]
[所属知识点: 锚点]
[预计完成时间: 8 分钟]

题目:用锚点匹配以 'Hello' 开头的行。
"""

if __name__ == "__main__":
    print("参考答案:")
    print("  import re")
    print("  re.findall(r'^Hello', 'Hello world')  # ['Hello']")
    print("  re.findall(r'^Hello', 'world Hello')  # []")
