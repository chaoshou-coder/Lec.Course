"""
[难度: ★★★][所属知识点: 修复错误][预计完成时间: 15 分钟][类型: 选做]

题目:下面链表遍历有什么问题?如何修正?

def traverse(head):
    while head:
        print(head.val)
        # 忘记移动到下一个节点!
"""

if __name__ == "__main__":
    print("问题:没有 current = current.next,导致死循环")
    print("修正:在循环内加 current = current.next")
