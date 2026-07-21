"""
[难度: ★★★]
[所属知识点: 综合]
[预计完成时间: 20 分钟]
[类型: 选做]

题目:提取 'Email: test@example.com, Phone: 13812345678' 中的邮箱和手机号。
"""

if __name__ == "__main__":
    print("参考答案:")
    print("  import re")
    print("  text = 'Email: test@example.com, Phone: 13812345678'")
    print("  emails = re.findall(r'[\\w.]+@[\\w.]+\\.\\w+', text)")
    print("  phones = re.findall(r'1[3-9]\\d{9}', text)")
