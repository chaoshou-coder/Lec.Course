"""
[难度: ★★][所属知识点: JSON 读写][预计完成时间: 10 分钟]

题目:把字典 {"name": "张三", "age": 20} 写入 user.json,
再读取回来并打印 name。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('import json')
    print('data = {"name": "张三", "age": 20}')
    print('with open("user.json", "w", encoding="utf-8") as f:')
    print('    json.dump(data, f, ensure_ascii=False, indent=2)')
    print('with open("user.json", "r", encoding="utf-8") as f:')
    print('    loaded = json.load(f)')
    print('    print(loaded["name"])  # 张三')
