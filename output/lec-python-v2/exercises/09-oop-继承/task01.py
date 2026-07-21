"""
[难度: ⭐⭐⭐]
[所属知识点: 电商产品类型继承体系]
[类型: 选做]
[预计完成时间: 25 分钟]

题目描述:
为电商系统设计产品类型继承体系:
1. 基类 Product:sku、name、price、info()
2. 子类 Book:新增 author 属性,重写 info()
3. 子类 Food:新增 expire_date 属性,重写 info()
4. 子类 Clothing:新增 size 属性,重写 info()

示例:
    >>> b = Book("B001", "Python 入门", 59.8, "张三")
    >>> b.info()
    Book(sku=B001, name=Python 入门, price=59.8, author=张三)
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1:Book 的 info() 包含 author
    # 测试 2:Food 的 info() 包含 expire_date
    # 测试 3:Clothing 的 info() 包含 size
    # 测试 4:[p.info() for p in products] 全部正确
    pass
