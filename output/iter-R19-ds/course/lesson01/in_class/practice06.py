"""
[难度: ★★★][所属知识点: 挑战题][预计完成时间: 15 分钟][类型: 挑战题]

题目:下面链表代码有什么问题?如何修正?

def traverse(head):
    while head.next:  # 问题:会漏掉最后一个节点
        print(head.val)
        head = head.next
"""

if __name__ == "__main__":
    print("问题:while head.next 会漏掉最后一个节点")
    print("修正:while head:")
