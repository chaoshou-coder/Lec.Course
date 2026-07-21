"""
[难度: ⭐⭐⭐⭐⭐]
[所属知识点: 综合项目:通知中心]
[预计完成时间: 45 分钟]

题目描述:
设计一个通知中心系统,综合本课全部知识:
1. Notifier(abc.ABC):send(msg) 和 channel() 抽象方法
2. 实现 EmailNotifier / SMSNotifier / WeChatNotifier
3. NotificationCenter:add_notifier + notify_all(msg)
4. 新增通知方式只需加一个类,原有代码零修改

示例:
    >>> center = NotificationCenter()
    >>> center.add_notifier(EmailNotifier())
    >>> center.add_notifier(SMSNotifier())
    >>> center.notify_all("订单已发货")
    [email] 邮件: 订单已发货
    [sms] 短信: 订单已发货
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import abc

class Notifier(abc.ABC):
    pass  # 请定义抽象方法

class EmailNotifier(Notifier):
    pass  # 请实现

class SMSNotifier(Notifier):
    pass  # 请实现

class WeChatNotifier(Notifier):
    pass  # 请实现

class NotificationCenter:
    pass  # 请实现

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1:三种 Notifier 都能正常实例化
    # 测试 2:notify_all 输出所有通知
    # 测试 3:新增 WeChatNotifier 无需修改 NotificationCenter
    # 测试 4:class BrokenNotifier(Notifier): pass → 实例化报错
    pass
