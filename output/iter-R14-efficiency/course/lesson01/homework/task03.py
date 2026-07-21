"""
[难度: ★★★★]
[所属知识点: 综合]
[预计完成时间: 30 分钟]
[类型: 选做]

题目:编写一个正则,验证密码强度(≥8 位,包含大小写字母和数字)。
"""

if __name__ == "__main__":
    print("参考答案:")
    print("  import re")
    print("  pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d).{8,}$'")
    print("  re.match(pattern, 'Abc12345')  # 匹配")
    print("  re.match(pattern, 'abc12345')  # 不匹配(无大写)")
