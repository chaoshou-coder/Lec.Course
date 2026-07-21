"""
[难度: ★★★★][所属知识点: 综合][预计完成时间: 30 分钟][类型: 选做]

题目:实现一个栈(用链表),支持 push/pop/peek。
"""

if __name__ == "__main__":
    print("参考答案:")
    print("  class Stack:")
    print("      def __init__(self): self.head = None")
    print("      def push(self, val):")
    print("          self.head = ListNode(val, self.head)")
    print("      def pop(self):")
    print("          val = self.head.val")
    print("          self.head = self.head.next")
    print("          return val")
    print("      def peek(self): return self.head.val")
