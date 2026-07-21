"""
[难度: ⭐⭐⭐]
[所属知识点: @abstractmethod 强制契约]
[预计完成时间: 20 分钟]

题目描述:
基于 practice03 的 Payment 抽象基类,
定义 Alipay 和 WeChatPay 子类,实现 execute。
验证:子类能正常实例化,漏写 execute 则报错。

示例:
    >>> alipay = Alipay()
    >>> alipay.execute(99.0)
    支付宝支付 99.0 元
    >>> class BrokenPay(Payment): pass
    >>> BrokenPay()  # 报 TypeError
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import abc

class Payment(abc.ABC):
    @abc.abstractmethod
    def execute(self, amount):
        ...

class Alipay(Payment):
    pass  # 请实现 execute

class WeChatPay(Payment):
    pass  # 请实现 execute

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1:Alipay().execute(99.0) 正确
    # 测试 2:WeChatPay().execute(50.0) 正确
    # 测试 3:class BrokenPay(Payment): pass → BrokenPay() 报错
    pass
