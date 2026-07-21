"""
[难度: ★★★][所属知识点: 综合(挑战题)][预计完成时间: 15 分钟]

题目:输入一个邮箱字符串,提取用户名(@ 前面的部分)和域名(@ 后面的部分),
用 f-string 输出"用户名:XX, 域名:XX"。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('email = input("请输入邮箱:")')
    print('pos = email.find("@")')
    print('user = email[:pos]')
    print('domain = email[pos+1:]')
    print('print(f"用户名:{user}, 域名:{domain}")')
