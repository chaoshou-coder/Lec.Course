"""
[难度: ★★][所属知识点: 菜单循环][预计完成时间: 10 分钟]

题目:实现 while True 菜单循环。
显示 3 个选项并获取用户输入,
当用户输入 "0" 时退出循环,其他情况打印选择。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('while True:')
    print('    print("1. 浏览商品")')
    print('    print("2. 退出")')
    print('    print("0. 退出系统")')
    print('    choice = input("请选择:")')
    print('    if choice == "0":')
    print('        print("再见!")')
    print('        break')
    print('    else:')
    print('        print(f"你选择了 {choice}")')
