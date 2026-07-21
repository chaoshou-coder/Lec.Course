"""
[难度: ★★★][所属知识点: 综合(鸡兔同笼)][预计完成时间: 15 分钟]

题目:鸡兔同笼,头 35 个,脚 94 只,用循环求鸡和兔各多少只。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('for chicken in range(36):')
    print('    rabbit = 35 - chicken')
    print('    if chicken * 2 + rabbit * 4 == 94:')
    print('        print(f"鸡 {chicken} 只,兔 {rabbit} 只")')
    print('        break')
