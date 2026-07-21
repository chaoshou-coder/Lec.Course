"""
[难度: ★★★]
[所属知识点: 递归入门(阶乘)]
[预计完成时间: 15 分钟]
[类型: 选做]

题目描述:
  用递归实现阶乘函数 factorial(n):
  - factorial(0) = 1
  - factorial(n) = n * factorial(n-1)

  注意:递归需要有终止条件(基准情形)

示例:
    输入:5
    输出:120
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n - 1)

    print(factorial(5))    # 120
    print(factorial(0))    # 1
