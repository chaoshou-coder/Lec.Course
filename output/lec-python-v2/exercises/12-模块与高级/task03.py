"""
[难度: ★★★★][所属知识点: 综合项目-数据处理管道]
[预计完成时间: 25 分钟]

题目:综合运用生成器 + 装饰器 + 上下文管理器,
实现一个"数据处理管道":
1. 写一个 @log 装饰器,打印函数名和返回值
2. 写一个生成器 read_lines(path),逐行读取文件
3. 写一个生成器 filter_comments(lines),跳过空行
4. 用 with 打开 "data.txt",写入 3 行测试数据,
   再用管道读取并打印

示例:
    调用 read_lines,返回值=<generator>
    调用 filter_comments,返回值=<generator>
    第1行数据
    第2行数据
    第3行数据
"""

import functools

# TODO: 定义 log 装饰器
def log(fn):
    pass

# TODO: 定义 read_lines 生成器(逐行读取)
def read_lines(path):
    pass

# TODO: 定义 filter_comments 生成器(跳过空行)
def filter_comments(lines):
    pass

if __name__ == '__main__':
    # 参考答案
    # def log(fn):
    #     @functools.wraps(fn)
    #     def wrapper(*args, **kwargs):
    #         result = fn(*args, **kwargs)
    #         print(f"调用 {fn.__name__},返回值={result}")
    #         return result
    #     return wrapper
    #
    # @log
    # def read_lines(path):
    #     with open(path, "r", encoding="utf-8") as f:
    #         for line in f:
    #             yield line.strip()
    #
    # @log
    # def filter_comments(lines):
    #     for line in lines:
    #         if line:  # 跳过空行
    #             yield line
    #
    # 写入测试数据
    # with open("data.txt", "w", encoding="utf-8") as f:
    #     f.write("第1行数据\n第2行数据\n\n第3行数据\n")
    # 用管道读取
    # lines = read_lines("data.txt")
    # for line in filter_comments(lines):
    #     print(line)
    pass
