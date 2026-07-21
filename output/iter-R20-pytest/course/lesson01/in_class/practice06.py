"""
[难度: ★★★][所属知识点: 挑战题][预计完成时间: 15 分钟][类型: 挑战题]

题目:用 pytest 测试一个会抛出异常的函数。
"""

if __name__ == "__main__":
    print("参考答案:")
    print("  def test_divide_by_zero():")
    print("      with pytest.raises(ValueError):")
    print("          divide(5, 0)")
