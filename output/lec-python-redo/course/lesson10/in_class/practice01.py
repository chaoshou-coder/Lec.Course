"""
[难度: ★★][所属知识点: 数据结构(商品库设计)][预计完成时间: 10 分钟]

题目:设计商品库数据结构。
用列表嵌套字典,定义 4 个商品,字段为 id/name/price,
打印每个商品的名称和价格。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('products = [')
    print('    {"id": 1, "name": "Python 入门", "price": 39.9},')
    print('    {"id": 2, "name": "NumPy 实战",   "price": 49.9},')
    print('    {"id": 3, "name": "Pandas 精讲",  "price": 59.9},')
    print('    {"id": 4, "name": "爬虫基础",     "price": 29.9},')
    print(']')
    print('for p in products:')
    print('    print(f"{p[\'name\']} ¥{p[\'price\']}")')
