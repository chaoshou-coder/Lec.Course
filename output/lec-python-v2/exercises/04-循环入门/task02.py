"""
[难度: ★★★]
[所属知识点: while True + break(猜数字)]
[预计完成时间: 15 分钟]
[类型: 选做]

题目描述:
  编写一个猜数字游戏:
  - 预设答案 answer = 7
  - 用 while True 循环让用户反复猜
  - 猜对了打印 "恭喜,猜对了!" 并 break
  - 猜错了提示 "猜大了" 或 "猜小了"

  提示:用固定值模拟 input

示例:
    输入:5 → 提示"猜小了"
    输入:9 → 提示"猜大了"
    输入:7 → 提示"恭喜,猜对了!"
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    answer = 7
    # 模拟输入序列
    guesses = [5, 9, 7]
    idx = 0

    while True:
        guess = guesses[idx]
        idx += 1
        print(f"你猜:{guess}")
        if guess == answer:
            print("恭喜,猜对了!")
            break
        elif guess < answer:
            print("猜小了")
        else:
            print("猜大了")
