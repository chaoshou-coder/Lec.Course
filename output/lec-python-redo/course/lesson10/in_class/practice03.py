"""
[难度: ★★][所属知识点: 加入购物车][预计完成时间: 12 分钟]

题目:实现 add_to_cart 函数。
输入商品编号,在商品库中查找,
找到后追加到 cart 列表(字典: name/price/qty),
找不到时提示"商品不存在"。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('def add_to_cart(products, cart):')
    print('    pid = int(input("输入商品编号:"))')
    print('    found = None')
    print('    for p in products:')
    print('        if p["id"] == pid:')
    print('            found = p')
    print('            break')
    print('    if found is None:')
    print('        print("商品不存在!")')
    print('        return')
    print('    qty = int(input("数量:"))')
    print('    cart.append({"name": found["name"],')
    print('                  "price": found["price"],')
    print('                  "qty": qty})')
