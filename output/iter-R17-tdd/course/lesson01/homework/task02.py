"""
[难度: ★★★][所属知识点: 综合][预计完成时间: 20 分钟][类型: 选做]

题目:用 TDD 实现一个 Calculator 类(add/subtract/multiply/divide)。

参考答案:
def test_calculator():
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.subtract(5, 3) == 2
    assert calc.multiply(2, 3) == 6
    assert calc.divide(6, 2) == 3

class Calculator:
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b
    def divide(self, a, b): return a / b
"""
