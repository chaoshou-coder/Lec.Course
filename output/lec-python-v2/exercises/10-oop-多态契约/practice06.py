"""
[难度: ⭐⭐⭐⭐]
[所属知识点: Payment 支付系统综合]
[预计完成时间: 30 分钟]

题目描述:
综合本课全部知识点,实现 Payment 支付系统:
1. Payment(abc.ABC) 定义 execute 抽象方法
2. Alipay 和 WeChatPay 实现 execute
3. checkout(total, payment) 不判断类型
4. 漏写 execute 时实例化报错

示例:
    >>> checkout(99.0, Alipay())
    支付宝支付 99.00 元
    >>> checkout(50.0, WeChatPay())
    微信支付 50.00 元
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import abc

class Payment(abc.ABC):
    pass  # 请定义 execute 抽象方法

class Alipay(Payment):
    pass  # 请实现 execute

class WeChatPay(Payment):
    pass  # 请实现 execute

def checkout(total, payment):
    pass  # 请实现(不判断类型)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1:checkout(99.0, Alipay()) 正确
    # 测试 2:checkout(50.0, WeChatPay()) 正确
    # 测试 3:class BrokenPay(Payment): pass → BrokenPay() 报错
    # 测试 4:checkout 函数没有 if-elif
    pass
