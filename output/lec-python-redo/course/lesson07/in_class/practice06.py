"""
[难度: ★★★][所属知识点: 常见异常捕获][预计完成时间: 15 分钟]

题目:写一段代码,读取 JSON 文件,捕获 FileNotFoundError 和 JSONDecodeError。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('import json')
    print('try:')
    print('    with open("data.json", "r", encoding="utf-8") as f:')
    print('        data = json.load(f)')
    print('except FileNotFoundError:')
    print('    print("文件不存在")')
    print('except json.JSONDecodeError:')
    print('    print("JSON 格式错误")')
