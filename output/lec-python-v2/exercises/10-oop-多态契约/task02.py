"""
[难度: ⭐⭐⭐⭐]
[所属知识点: abc.ABC:日志系统]
[预计完成时间: 30 分钟]

题目描述:
用 abc.ABC 实现日志系统:
1. Logger(abc.ABC):抽象方法 log(level, msg)
2. ConsoleLogger:输出到控制台
3. FileLogger:模拟写入文件(存入列表)
4. 漏写 log 时实例化报错

示例:
    >>> console = ConsoleLogger()
    >>> console.log("INFO", "启动成功")
    [INFO] 启动成功
    >>> file_logger = FileLogger()
    >>> file_logger.log("ERROR", "异常")
    >>> file_logger.logs
    [('ERROR', '异常')]
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import abc

class Logger(abc.ABC):
    pass  # 请定义 log 抽象方法

class ConsoleLogger(Logger):
    pass  # 请实现

class FileLogger(Logger):
    pass  # 请实现

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1:ConsoleLogger().log("INFO", "msg") 输出正确
    # 测试 2:FileLogger 的 logs 列表记录日志
    # 测试 3:class BrokenLogger(Logger): pass → 实例化报错
    pass
