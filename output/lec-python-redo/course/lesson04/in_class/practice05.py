"""
[难度: ★★★][所属知识点: 嵌套循环][预计完成时间: 12 分钟]

题目:用嵌套循环打印 5 行的直角三角形:
*
**
***
****
*****
"""

if __name__ == "__main__":
    print("参考答案:")
    print('for i in range(1, 6):')
    print('    for j in range(i):')
    print('        print("*", end="")')
    print('    print()')
    print()
    print("更简洁的写法:")
    print('for i in range(1, 6):')
    print('    print("*" * i)')
