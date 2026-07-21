"""
[难度: ★★]
[所属知识点: break 与 continue]
[预计完成时间: 10 分钟]

题目描述:
  1. 在 "hello" 中找第一个 'l',打印并 break
  2. 用 continue 跳过 3,打印 1-10 中除 3 外的数

示例:
    输出:
      找到 l
      1 2 4 5 6 7 8 9 10
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 1. break 找第一个 'l'
    for ch in "hello":
        if ch == "l":
            print(f"找到 {ch}")
            break

    # 2. continue 跳过 3
    for i in range(1, 11):
        if i == 3:
            continue
        print(i, end=" ")
    print()
