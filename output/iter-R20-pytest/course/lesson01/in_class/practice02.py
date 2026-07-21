"""
[难度: ★][所属知识点: fixture][预计完成时间: 5 分钟]

题目:用 fixture 提供测试数据 [1, 2, 3, 4, 5],测试 sum 和 len。
"""

if __name__ == "__main__":
    print("参考答案:")
    print("  @pytest.fixture")
    print("  def data(): return [1, 2, 3, 4, 5]")
    print("  def test_sum(data): assert sum(data) == 15")
    print("  def test_len(data): assert len(data) == 5")
