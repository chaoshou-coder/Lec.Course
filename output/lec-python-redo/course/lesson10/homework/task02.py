"""
[难度: ★★★★][所属知识点: 购物车 + 持久化][预计完成时间: 30 分钟][类型: 选做]

题目:在购物车系统基础上,增加购物车持久化功能。
要求:
- 启动时从 cart.json 加载购物车(如果文件存在)
- 退出时把购物车保存到 cart.json
- 使用 json.load / json.dump
- 用 try-except 处理文件不存在和 JSON 解析错误
"""

if __name__ == "__main__":
    print("参考答案:")
    print('import json, os')
    print('')
    print('CART_FILE = "cart.json"')
    print('')
    print('def load_cart():')
    print('    if os.path.exists(CART_FILE):')
    print('        try:')
    print('            with open(CART_FILE, "r", encoding="utf-8") as f:')
    print('                return json.load(f)')
    print('        except json.JSONDecodeError:')
    print('            print("购物车文件损坏,已重置")')
    print('    return []')
    print('')
    print('def save_cart(cart):')
    print('    with open(CART_FILE, "w", encoding="utf-8") as f:')
    print('        json.dump(cart, f, ensure_ascii=False, indent=2)')
    print('')
    print('def main():')
    print('    cart = load_cart()')
    print('    # ... 主循环 ...')
    print('    save_cart(cart)')
