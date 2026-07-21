"""
[难度: ★★★★][所属知识点: 购物车 + 异常加固][预计完成时间: 30 分钟][类型: 选做]

题目:给购物车系统加三层异常加固。
要求:
- 输入商品编号时,非数字输入不崩溃(提示重试)
- 输入负数量时,拒绝并提示(数量必须 > 0)
- 文件写入时,捕获 IOError 并提示"保存失败"
- 封装一个 safe_input_int(prompt) 函数复用
"""

if __name__ == "__main__":
    print("参考答案:")
    print('def safe_input_int(prompt):')
    print('    while True:')
    print('        try:')
    print('            value = int(input(prompt))')
    print('            if value <= 0:')
    print('                print("请输入正整数!")')
    print('                continue')
    print('            return value')
    print('        except ValueError:')
    print('            print("请输入数字!")')
    print('')
    print('def save_products(products):')
    print('    try:')
    print('        with open("products.json", "w", encoding="utf-8") as f:')
    print('            json.dump(products, f, ensure_ascii=False)')
    print('    except IOError:')
    print('        print("保存失败!磁盘写入错误")')
    print('')
    print('def add_to_cart():')
    print('    pid = safe_input_int("商品编号:")')
    print('    qty = safe_input_int("数量:")')
    print('    # ... rest of logic ...')
