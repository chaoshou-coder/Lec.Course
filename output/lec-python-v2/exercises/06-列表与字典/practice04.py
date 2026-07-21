"""
[难度: ★]
[所属知识点: 字典创建与取值]
[预计完成时间: 5 分钟]

题目描述:
  创建一个字典 product,包含:
  "title": "Python 入门", "price": 59.8
  1. 用 [] 取值打印 title
  2. 用 get 取值打印 price
  3. 用 get 取值打印 "stock",默认值 0

示例:
    输出:
      Python 入门
      59.8
      0
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    product = {"title": "Python 入门", "price": 59.8}
    print(product["title"])          # Python 入门
    print(product.get("price"))      # 59.8
    print(product.get("stock", 0))   # 0
