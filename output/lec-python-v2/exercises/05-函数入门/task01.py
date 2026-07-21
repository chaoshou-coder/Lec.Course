"""
[难度: ★★★]
[所属知识点: 工具函数(is_valid_phone)]
[预计完成时间: 15 分钟]
[类型: 选做]

题目描述:
  定义函数 is_valid_phone(phone),判断手机号是否合法:
  - 长度必须是 11 位
  - 必须全部是数字
  - 返回 True 或 False

示例:
    输入:13812345678
    输出:True
    输入:1381234567
    输出:False
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    def is_valid_phone(phone):
        return len(phone) == 11 and phone.isdigit()

    print(is_valid_phone("13812345678"))    # True
    print(is_valid_phone("1381234567"))     # False
    print(is_valid_phone("1381234567a"))    # False
