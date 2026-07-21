"""
[难度: ⭐⭐⭐]
[所属知识点: abc.ABC 抽象基类]
[预计完成时间: 20 分钟]

题目描述:
用 abc.ABC 定义 Payment 抽象基类,
包含 execute 抽象方法。
验证:直接实例化 Payment 会报 TypeError。

示例:
    >>> try:
    ...     p = Payment()
    ... except TypeError as e:
    ...     print(e)
    Can't instantiate abstract class Payment
    with abstract method execute
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import abc

class Payment(abc.ABC):
    pass  # 请定义 execute 抽象方法

# 测试:直接实例化应该报错
# try:
#     p = Payment()
# except TypeError as e:
#     print(f"报错: {e}")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1:Payment() 报 TypeError
    # 测试 2:错误信息包含 "execute"
    pass
