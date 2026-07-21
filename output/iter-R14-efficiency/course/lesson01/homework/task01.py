"""
[难度: ★★★]
[所属知识点: 修复正则]
[预计完成时间: 15 分钟]
[类型: 选做]

题目:下面的正则有什么问题?如何修正?

    pattern = r'\d{11}'
    text = 'My phone is 13812345678 and 12345'
    re.findall(pattern, text)
"""

if __name__ == "__main__":
    print("问题:\d{11} 会匹配任意位置的 11 位数字")
    print("修正:pattern = r'\b\d{11}\b'(加单词边界)")
