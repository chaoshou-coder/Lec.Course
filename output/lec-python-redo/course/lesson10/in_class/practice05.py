"""
[难度: ★★★][所属知识点: 结算与小票打印][预计完成时间: 15 分钟]

题目:实现 checkout 函数。
遍历购物车,打印每项小计,对齐输出,
最后打印结算总价,然后清空购物车。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('def checkout(cart):')
    print('    if not cart:')
    print('        print("购物车为空")')
    print('        return')
    print('    print("=== 购物小票 ===")')
    print('    total = 0')
    print('    for item in cart:')
    print('        subtotal = item["price"] * item["qty"]')
    print('        total += subtotal')
    print('        print(f"  {item[\'name\']:8s} x{item[\'qty\']}  ¥{subtotal:.2f}")')
    print('    print(f"  总计: ¥{total:.2f}")')
    print('    cart.clear()')
    print('    print("结算成功!")')
