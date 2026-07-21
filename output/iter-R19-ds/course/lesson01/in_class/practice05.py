"""
[难度: ★★★][所属知识点: 综合][预计完成时间: 15 分钟]

题目:实现链表反转(迭代法)。
"""

if __name__ == "__main__":
    print("参考答案:")
    print("  prev = None")
    print("  current = head")
    print("  while current:")
    print("      next_temp = current.next")
    print("      current.next = prev")
    print("      prev = current")
    print("      current = next_temp")
    print("  head = prev")
