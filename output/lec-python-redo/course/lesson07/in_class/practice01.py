"""
[难度: ★][所属知识点: open 与文件模式][预计完成时间: 5 分钟]

题目:用写模式打开 test.txt,写入"Hello"和"World"(各一行),然后关闭。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('f = open("test.txt", "w", encoding="utf-8")')
    print('f.write("Hello\\n")')
    print('f.write("World")')
    print('f.close()')
