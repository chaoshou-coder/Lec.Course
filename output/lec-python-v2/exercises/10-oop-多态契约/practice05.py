"""
[难度: ⭐⭐⭐]
[所属知识点: 接口:Notifier]
[预计完成时间: 25 分钟]

题目描述:
定义 Notifier 接口,包含 send(msg) 和 channel()
两个抽象方法。
实现 EmailNotifier 和 SMSNotifier 子类。
编写函数 notify_all(notifiers, msg),
让所有通知器发送消息。

示例:
    >>> notify_all([EmailNotifier(), SMSNotifier()], "订单已发货")
    [email] 邮件: 订单已发货
    [sms] 短信: 订单已发货
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import abc

class Notifier(abc.ABC):
    pass  # 请定义 send 和 channel 抽象方法

class EmailNotifier(Notifier):
    pass  # 请实现

class SMSNotifier(Notifier):
    pass  # 请实现

def notify_all(notifiers, msg):
    pass  # 请实现

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1:EmailNotifier().channel() == "email"
    # 测试 2:SMSNotifier().send("hi") 返回正确字符串
    # 测试 3:notify_all 输出所有通知
    pass
