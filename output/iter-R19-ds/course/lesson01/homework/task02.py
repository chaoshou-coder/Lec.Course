"""
[难度: ★★★][所属知识点: 综合][预计完成时间: 20 分钟][类型: 选做]

题目:实现链表的反转(递归法)。
"""

if __name__ == "__main__":
    print("参考答案:")
    print("  def reverse(head):")
    print("      if not head or not head.next: return head")
    print("      new_head = reverse(head.next)")
    print("      head.next.next = head")
    print("      head.next = None")
    print("      return new_head")
