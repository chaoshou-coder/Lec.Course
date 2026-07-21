"""
[难度: ★★][所属知识点: parametrize][预计完成时间: 8 分钟]

题目:用 parametrize 测试 add 函数的多组输入。
"""

if __name__ == "__main__":
    print("参考答案:")
    print("  @pytest.mark.parametrize('a,b,expected', [")
    print("      (2, 3, 5), (-1, 1, 0), (0, 0, 0)")
    print("  ])")
    print("  def test_add(a, b, expected):")
    print("      assert add(a, b) == expected")
