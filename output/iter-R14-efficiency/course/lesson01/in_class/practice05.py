"""
[难度: ★★★]
[所属知识点: 综合]
[预计完成时间: 15 分钟]

题目:提取 'Price: $99.99' 中的所有数字(包括小数)。
"""

if __name__ == "__main__":
    print("参考答案:")
    print("  import re")
    print("  re.findall(r'\d+\.?\d*', 'Price: $99.99')  # ['99.99']")
