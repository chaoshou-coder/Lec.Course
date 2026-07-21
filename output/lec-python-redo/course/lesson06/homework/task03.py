"""
[难度: ★★★★][所属知识点: 综合应用][预计完成时间: 30 分钟][类型: 选做]

题目:实现一个简单的通讯录,支持 1.添加 2.查找 3.删除 4.显示全部 5.退出。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('phone = {}')
    print('while True:')
    print('    cmd = input("1.添加 2.查找 3.删除 4.显示 5.退出:")')
    print('    if cmd == "1":')
    print('        name = input("姓名:"); phone[name] = input("电话:")')
    print('    elif cmd == "2":')
    print('        name = input("姓名:"); print(phone.get(name, "未找到"))')
    print('    elif cmd == "3":')
    print('        name.pop(input("姓名:"), "不存在")')
    print('    elif cmd == "4":')
    print('        for k, v in phone.items(): print(f"{k}: {v}")')
    print('    elif cmd == "5": break')
