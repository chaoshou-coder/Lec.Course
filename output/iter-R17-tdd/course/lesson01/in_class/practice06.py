"""
[难度: ★★★][所属知识点: 挑战题][预计完成时间: 15 分钟][类型: 挑战题]

题目:用 TDD 实现一个 Stack(栈)的 push/pop/peek 操作。

参考答案:
def test_stack():
    s = Stack()
    s.push(1)
    s.push(2)
    assert s.peek() == 2
    assert s.pop() == 2
    assert s.pop() == 1

class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
"""
