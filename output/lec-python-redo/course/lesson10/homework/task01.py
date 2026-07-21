"""
[难度: ★★★][所属知识点: 函数拆分重构][预计完成时间: 20 分钟][类型: 选做]

题目:下面是一个"万能函数",把加载、显示、加法全写在一起。
请按"每函数只做一件事"原则,拆成 4 个独立函数。

    def everything():
        # 加载商品
        products = [...]
        # 显示菜单
        while True:
            print("1.浏览 2.退出")
            c = input()
            if c == "0":
                break
            # 浏览商品
            for p in products:
                print(p)
"""

if __name__ == "__main__":
    print("参考答案:")
    print('def load_products():')
    print('    return [{"id": 1, "name": "Python 入门", "price": 39.9}, ...]')
    print('')
    print('def show_menu():')
    print('    print("1.浏览商品 2.退出")')
    print('    return input("请选择:")')
    print('')
    print('def show_products(products):')
    print('    for p in products:')
    print('        print(f"{p[\'name\']} ¥{p[\'price\']}")')
    print('')
    print('def main():')
    print('    products = load_products()')
    print('    while True:')
    print('        choice = show_menu()')
    print('        if choice == "0": break')
    print('        show_products(products)')
