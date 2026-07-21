"""
[难度: ⭐⭐]
[所属知识点: checkout 多态函数]
[预计完成时间: 15 分钟]

题目描述:
基于 practice01 的 Alipay 和 WeChatPay,
新增一个 BankPay 类,同样实现 execute 方法。
验证 checkout 函数无需修改就能支持新类型。

示例:
    >>> checkout(200.0, BankPay())
    银行卡支付 200.0 元
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Alipay:
    def execute(self, amount):
        return f"支付宝支付 {amount} 元"

class WeChatPay:
    def execute(self, amount):
        return f"微信支付 {amount} 元"

class BankPay:
    pass  # 请实现 execute 方法

def checkout(total, payment):
    return payment.execute(total)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1:checkout(200.0, BankPay()) 正确
    # 测试 2:checkout 函数本身没有 if-elif
    # 测试 3:三种支付都能正常工作
    pass
