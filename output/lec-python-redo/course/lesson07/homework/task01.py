"""
[难度: ★★★][所属知识点: 文件读写综合][预计完成时间: 15 分钟][类型: 选做]

题目:输入多行文字,写入 notes.txt,直到输入"结束"停止,然后读取并打印。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('with open("notes.txt", "w", encoding="utf-8") as f:')
    print('    while True:')
    print('        line = input("输入(结束=退出):")')
    print('        if line == "结束": break')
    print('        f.write(line + "\\n")')
    print('with open("notes.txt", "r", encoding="utf-8") as f:')
    print('    print(f.read())')
