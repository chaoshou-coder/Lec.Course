"""
[难度: ★★★][所属知识点: 综合][预计完成时间: 15 分钟]

题目:下面测试有什么问题?如何修正?

def test_user():
    user = User(name="Alice", age=25)  # 真实数据库操作!
    assert user.name == "Alice"
"""

if __name__ == "__main__":
    print("问题:测试依赖真实数据库,慢且不隔离")
    print("修正:用 mock 或 fixture 隔离数据库")
