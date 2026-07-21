"""
[难度: ★★★★][所属知识点: 综合应用][预计完成时间: 30 分钟][类型: 选做]

题目:猜数字程序:程序随机生成 1 到 100 的整数,用户反复猜,
程序提示"大了"或"小了",直到猜中,输出猜了多少次。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('import random')
    print('target = random.randint(1, 100)')
    print('count = 0')
    print('while True:')
    print('    guess = int(input("猜一个 1-100 的数:")')
    print('    count += 1')
    print('    if guess > target:')
    print('        print("大了")')
    print('    elif guess < target:')
    print('        print("小了")')
    print('    else:')
    print('        print(f"猜中了!共猜了 {count} 次")')
    print('        break')
