"""
[难度: ★★★][所属知识点: 嵌套循环][预计完成时间: 20 分钟][类型: 选做]

题目:用嵌套循环打印九九乘法表(完整 9×9)。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('for i in range(1, 10):')
    print('    for j in range(1, i + 1):')
    print('        print(f"{j}×{i}={i*j}", end="\\t")')
    print('    print()')
