"""
[难度: ⭐⭐]
[所属知识点: 鸭子类型基本用法]
[预计完成时间: 15 分钟]

题目描述:
定义两个类 Alipay 和 WeChatPay,
它们都有 execute(amount) 方法。
编写 checkout(total, payment) 函数,
不判断类型,直接调用 payment.execute(total)。

示例:
    >>> checkout(99.0, Alipay())
    支付宝支付 99.0 元
    >>> checkout(50.0, WeChatPay())
    微信支付 50.0 元
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Alipay:
    pass  # 请实现 execute 方法

class WeChatPay:
    pass  # 请实现 execute 方法

def checkout(total, payment):
    pass  # 请实现(不判断类型)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1:checkout(99.0, Alipay()) 返回正确字符串
    # 测试 2:checkout(50.0, WeChatPay()) 返回正确字符串
    # 测试 3:checkout(0, Alipay()) 边界情况
    pass
