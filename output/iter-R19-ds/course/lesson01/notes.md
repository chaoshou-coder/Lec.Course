### Day 01 · 数组与链表

> **痛点**:你用 Array/Object 但没理解底层。面试被要求写链表反转,你完全不会。今天你将用 Python 实现链表 —— 从零开始。
> **类比**:数组就像"连续书架" —— 每个位置有编号,直接访问。链表就像"散落的书+便签" —— 每本书有下一本书的地址。
> **解释**:**数据结构 = 组织和存储数据的方式**。今天学:数组 vs 链表的实现 + 时间复杂度。

---

#### 数组 —— 连续书架

```python
# 数组的基本操作
arr = [1, 2, 3, 4, 5]

# 访问:O(1)
print(arr[2])  # 3

# 末尾插入:O(1)
arr.append(6)  # [1, 2, 3, 4, 5, 6]

# 中间插入:O(n) —— 需要移动后续元素
arr.insert(2, 99)  # [1, 2, 99, 3, 4, 5, 6]

# 查找:O(n)
print(99 in arr)  # True
```

**逐行解剖**

- `arr[2]` = 直接访问索引 2,O(1)
- `arr.append(6)` = 末尾插入,O(1)
- `arr.insert(2, 99)` = 中间插入,需要移动后续元素,O(n)

---

#### 链表 —— 散落的书+便签

```python
# 链表节点定义
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 构建链表: 1 -> 2 -> 3
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

# 遍历链表:O(n)
current = head
while current:
    print(current.val)  # 1, 2, 3
    current = current.next

# 头部插入:O(1)
new_node = ListNode(0)
new_node.next = head
head = new_node  # 0 -> 1 -> 2 -> 3

# 中间插入:O(n) —— 需要先找到位置
```

**逐行解剖**

- `ListNode(val, next)` = 节点 = 值 + 指向下一个节点的指针
- `head` = 链表头节点
- 遍历 = 沿着 next 指针走,直到 None

> **ASCII 对比**
> ```
> 数组(连续):
> ┌───┬───┬───┬───┬───┐
> │ 1 │ 2 │ 3 │ 4 │ 5 │
> └───┴───┴───┴───┴───┘
>  ↑直接访问 arr[2] = O(1)
>
> 链表(散落):
> ┌───┐   ┌───┐   ┌───┐
> │ 1 │──▶│ 2 │──▶│ 3 │──▶ None
> └───┘   └───┘   └───┘
>  ↑必须从头遍历 = O(n)
> ```

**常见错误**

> 1. **错误现象**:遍历链表时死循环
>    **原因:**没有移动到下一个节点。修正:`current = current.next`
> 2. **错误现象**:插入节点时丢失后续节点
>    **原因:**先改了 next 指针。修正:先保存 next,再改指针

---

#### 执行过程跟踪

```python
# --- 执行过程 ---
# 构建链表 1 -> 2 -> 3:
#   ① head = ListNode(1)
#   ② head.next = ListNode(2)
#   ③ head.next.next = ListNode(3)
#
# 遍历:
#   ① current = head(值为 1)
#   ② 打印 1, current = current.next(值为 2)
#   ③ 打印 2, current = current.next(值为 3)
#   ④ 打印 3, current = current.next(None)
#   ⑤ 退出循环
```

---

#### 学员代码区

```python
# TODO: 定义 ListNode 类
# TODO: 构建链表 1 -> 2 -> 3 -> 4
# TODO: 遍历链表并打印每个值
# TODO: 在链表头部插入 0
# TODO: 反转链表(进阶)
```

---

#### 参考答案

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 构建
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

# 遍历
current = head
while current:
    print(current.val)
    current = current.next

# 头部插入
new_node = ListNode(0, head)
head = new_node
```

---

## 明日衔接

- 明天 Day 02 学什么:**栈与队列**
- 今天遗留的概念:今天学了数组/链表,但还没学基于它们的栈/队列
- NCDL 反模式预告:Day 2 展示"用数组模拟栈"的反模式
