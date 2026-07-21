"""
[难度: ★★★]
[所属知识点: 综合项目(工具函数库)]
[预计完成时间: 20 分钟]
[类型: 选做]

题目描述:
  定义一组工具函数:
  1. mask_id(id_card):身份证脱敏,
     "110105199003071234" → "110105********1234"
  2. celsius_to_fahrenheit(c):摄氏转华氏
     公式: F = C × 9/5 + 32
  3. is_even(n):判断偶数,返回 bool

示例:
    输出:
      110105********1234
      98.6
      True
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    def mask_id(id_card):
        return id_card[:6] + "********" + id_card[-4:]

    def celsius_to_fahrenheit(c):
        return c * 9 / 5 + 32

    def is_even(n):
        return n % 2 == 0

    print(mask_id("110105199003071234"))
    print(celsius_to_fahrenheit(37))
    print(is_even(10))
