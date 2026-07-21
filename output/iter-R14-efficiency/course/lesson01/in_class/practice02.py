"""
[难度: ★]
[所属知识点: 量词]
[预计完成时间: 5 分钟]

题目:用量词提取 'aaa bb ccc' 中的所有连续相同字母。
"""

if __name__ == "__main__":
    print("参考答案:")
    print("  import re")
    print("  re.findall(r'a+|b+|c+', 'aaa bb ccc')  # ['aaa', 'bb', 'ccc']")
