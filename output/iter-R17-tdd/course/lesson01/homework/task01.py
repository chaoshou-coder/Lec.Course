"""
[难度: ★★★][所属知识点: 修复 TDD 错误][预计完成时间: 15 分钟][类型: 选做]

题目:下面的 TDD 实践有什么问题?如何修正?

# 一次性写完所有功能
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b

# 然后补测试
def test_all():
    assert add(2, 3) == 5
    assert subtract(5, 3) == 2
    assert multiply(2, 3) == 6

问题:先写代码再补测试,违反了 TDD 原则。
修正:一次只写一个测试 → 写最少代码通过 → 重构 → 下一个测试
"""
