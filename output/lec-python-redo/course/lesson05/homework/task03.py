"""
[难度: ★★★★][所属知识点: 综合应用][预计完成时间: 30 分钟][类型: 选做]

题目:用户登录系统。定义函数 register() 注册,
函数 login() 登录,函数 main() 主程序调用。
注册时输入用户名和密码,登录时验证,最多尝试 3 次。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('user = None')
    print('pwd = None')
    print()
    print('def register():')
    print('    global user, pwd')
    print('    user = input("设置用户名:")')
    print('    pwd = input("设置密码:")')
    print('    print("注册成功!")')
    print()
    print('def login():')
    print('    global user, pwd')
    print('    for i in range(3):')
    print('        u = input("用户名:")')
    print('        p = input("密码:")')
    print('        if u == user and p == pwd:')
    print('            print("登录成功!")')
    print('            return True')
    print('        print(f"失败,还剩 {2-i} 次")')
    print('    print("账户已锁定")')
    print('    return False')
    print()
    print('register()')
    print('login()')
