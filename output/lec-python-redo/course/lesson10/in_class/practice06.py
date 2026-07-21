"""
[难度: ★★★★][所属知识点: 综合(完整购物车系统)][预计完成时间: 30 分钟]

题目:把 Day 10 所有函数组合成完整的购物车系统。
要求:
- 商品库至少 4 个商品
- 菜单循环(1.浏览 2.加购 3.查看 4.结算 0.退出)
- 所有 input 用 try-except 包裹
- 结算后清空购物车
"""

if __name__ == "__main__":
    print("参考答案:")
    print('import json, os')
    print('')
    print('DATA_FILE = "products.json"')
    print('products = [')
    print('    {"id": 1, "name": "Python 入门", "price": 39.9},')
    print('    {"id": 2, "name": "NumPy 实战",   "price": 49.9},')
    print('    {"id": 3, "name": "Pandas 精讲",  "price": 59.9},')
    print('    {"id": 4, "name": "爬虫基础",     "price": 29.9},')
    print(']')
    print('cart = []')
    print('')
    print('def load_products(): ...')
    print('def show_menu(): ...')
    print('def show_products(): ...')
    print('def add_to_cart(): ...')
    print('def view_cart(): ...')
    print('def checkout(): ...')
    print('def save_products(): ...')
    print('')
    print('def main():')
    print('    load_products()')
    print('    while True:')
    print('        choice = show_menu()')
    print('        if choice == "1": show_products()')
    print('        elif choice == "2": add_to_cart()')
    print('        elif choice == "3": view_cart()')
    print('        elif choice == "4": checkout()')
    print('        elif choice == "0":')
    print('            save_products()')
    print('            break')
    print('')
    print('if __name__ == "__main__":')
    print('    main()')
