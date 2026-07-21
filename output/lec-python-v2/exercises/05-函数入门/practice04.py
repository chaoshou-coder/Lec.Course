"""
[难度: ★★]
[所属知识点: return]
[预计完成时间: 10 分钟]

题目描述:
  定义函数 grade(score):
  - score < 60 返回 "不及格"
  - score < 80 返回 "良好"
  - 其他返回 "优秀"

示例:
    输出:
      不及格
      良好
      优秀
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    def grade(score):
        if score < 60:
            return "不及格"
        if score < 80:
            return "良好"
        return "优秀"

    print(grade(55))    # 不及格
    print(grade(75))    # 良好
    print(grade(95))    # 优秀
