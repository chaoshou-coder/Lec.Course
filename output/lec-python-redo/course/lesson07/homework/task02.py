"""
[难度: ★★★][所属知识点: JSON 数据处理][预计完成时间: 20 分钟][类型: 选做]

题目:创建一个书籍列表(每本书有 title/author/price),
写入 books.json,读取后打印所有书的标题。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('import json')
    print('books = [')
    print('    {"title": "Python入门", "author": "张三", "price": 59},')
    print('    {"title": "算法导论", "author": "李四", "price": 128}')
    print(']')
    print('with open("books.json", "w", encoding="utf-8") as f:')
    print('    json.dump(books, f, ensure_ascii=False, indent=2)')
    print('with open("books.json", "r", encoding="utf-8") as f:')
    print('    data = json.load(f)')
    print('    for book in data:')
    print('        print(book["title"])')
