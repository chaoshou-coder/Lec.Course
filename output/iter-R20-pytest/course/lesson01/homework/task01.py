"""
[难度: ★★★][所属知识点: 修复测试][预计完成时间: 15 分钟][类型: 选做]

题目:下面的测试有什么问题?如何修正?

def test_add():
    result = add(2, 3)
    assert result == 5
    assert result.__class__ == int  # 测了实现细节!
"""

if __name__ == "__main__":
    print("问题:assert result.__class__ == int 测了实现细节")
    print("修正:只测行为(输入→输出),不测内部实现")
