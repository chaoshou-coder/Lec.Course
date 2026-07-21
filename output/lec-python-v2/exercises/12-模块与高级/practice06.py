"""
[难度: ★★★][所属知识点: 上下文管理器 with][预计完成时间: 15 分钟]

题目:用 with 语句打开 "output.txt",
写入三行内容 "第1行\n第2行\n第3行",
然后再用 with 读取并打印全部内容。
(注意:不需要手动 close)

示例:
    第1行
    第2行
    第3行
"""

# TODO: 用 with + open 写入文件 "output.txt"
# TODO: 用 with + open 读取文件 "output.txt" 并打印
pass

if __name__ == '__main__':
    # 参考答案
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write("第1行\n第2行\n第3行")
    with open("output.txt", "r", encoding="utf-8") as f:
        print(f.read())
