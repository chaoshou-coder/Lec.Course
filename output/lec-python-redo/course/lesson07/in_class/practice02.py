"""
[难度: ★][所属知识点: 三种读取方式][预计完成时间: 8 分钟]

题目:假设 file.txt 有 3 行内容,分别用 read()、readline()、readlines() 读取。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('# read() - 全部读取')
    print('f = open("file.txt", "r", encoding="utf-8")')
    print('content = f.read()')
    print('f.close()')
    print()
    print('# readlines() - 逐行读取成列表')
    print('f = open("file.txt", "r", encoding="utf-8")')
    print('lines = f.readlines()')
    print('for line in lines:')
    print('    print(line.strip())')
    print('f.close()')
