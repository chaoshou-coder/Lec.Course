"""
[难度: ★★★][所属知识点: 综合][预计完成时间: 20 分钟][类型: 选做]

题目:用 pytest 测试一个 Calculator 类(add/subtract/multiply/divide)。
"""

if __name__ == "__main__":
    print("参考答案:")
    print("  class TestCalculator:")
    print("      def test_add(self): assert calc.add(2, 3) == 5")
    print("      def test_subtract(self): assert calc.subtract(5, 3) == 2")
    print("      def test_multiply(self): assert calc.multiply(2, 3) == 6")
    print("      def test_divide(self): assert calc.divide(6, 2) == 3")
    print("      def test_divide_by_zero(self):")
    print("          with pytest.raises(ValueError): calc.divide(5, 0)")
