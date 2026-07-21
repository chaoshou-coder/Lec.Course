"""
[难度: ★★][所属知识点: 综合][预计完成时间: 8 分钟]

题目:用 TDD 实现 is_even 函数(先写测试,再写代码)

参考答案:
def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False

def is_even(n):
    return n % 2 == 0
"""
