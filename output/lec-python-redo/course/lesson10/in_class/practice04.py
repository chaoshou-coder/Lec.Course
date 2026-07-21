"""
[难度: ★★★][所属知识点: 查看购物车(累加求和)][预计完成时间: 12 分钟]

题目:实现 view_cart 函数。
遍历购物车列表,计算每条小计、累加总价,
打印购物清单。如果购物车为空,提示"购物车为空"。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('def view_cart(cart):')
    print('    if not cart:')
    print('        print("购物车为空")')
    print('        return')
    print('    total = 0')
    print('    for item in cart:')
    print('        subtotal = item["price"] * item["qty"]')
    print('        total += subtotal')
    print('        print(f"{item[\'name\']} x{item[\'qty\']} = ¥{subtotal:.2f}")')
    print('    print(f"合计: ¥{total:.2f}")')
