"""
[难度: ⭐⭐⭐]
[所属知识点: 鸭子类型:序列化器]
[类型: 选做]
[预计完成时间: 25 分钟]

题目描述:
用鸭子类型实现序列化器:
1. JsonSerializer:serialize(obj) 返回 JSON 风格字符串
2. PlainSerializer:serialize(obj) 返回纯文本
3. 编写 save(data, serializer) 函数,不判断类型

示例:
    >>> save({"a": 1}, JsonSerializer())
    {"a": 1}
    >>> save({"a": 1}, PlainSerializer())
    a=1
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1:JsonSerializer 序列化 dict
    # 测试 2:PlainSerializer 序列化 dict
    # 测试 3:save 函数不判断类型
    pass
