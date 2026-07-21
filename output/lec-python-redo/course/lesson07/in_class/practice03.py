"""
[难度: ★★][所属知识点: with 上下文管理][预计完成时间: 8 分钟]

题目:用 with 写一段代码,读取 data.txt 的内容并打印(自动关闭文件)。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('with open("data.txt", "r", encoding="utf-8") as f:')
    print('    content = f.read()')
    print('    print(content)')
    print('# 离开 with 块,f 自动关闭')
