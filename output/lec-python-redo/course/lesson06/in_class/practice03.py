"""
[难度: ★★][所属知识点: 列表 CRUD][预计完成时间: 10 分钟]

题目:从空列表开始,末尾添加"a",开头添加"b",末尾添加"c",然后删除"a"。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('lst = []')
    print('lst.append("a")    # ["a"]')
    print('lst.insert(0, "b") # ["b", "a"]')
    print('lst.append("c")    # ["b", "a", "c"]')
    print('lst.remove("a")    # ["b", "c"]')
