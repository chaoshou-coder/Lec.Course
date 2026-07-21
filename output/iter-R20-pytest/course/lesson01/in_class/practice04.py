"""
[难度: ★★][所属知识点: mock][预计完成时间: 10 分钟]

题目:用 mock 替换外部 API 调用,测试一个依赖 API 的函数。
"""

if __name__ == "__main__":
    print("参考答案:")
    print("  from unittest.mock import patch")
    print("  @patch('module.requests.get')")
    print("  def test_fetch(mock_get):")
    print("      mock_get.return_value.json.return_value = {'key': 'value'}")
    print("      assert fetch_data() == {'key': 'value'}")
