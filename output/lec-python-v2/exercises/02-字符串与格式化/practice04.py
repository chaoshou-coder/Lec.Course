"""
[难度: ★★]
[所属知识点: 字符串四件套]
[预计完成时间: 10 分钟]

题目描述:
  1. 给定 s = "  Python 编程  ",用 strip() 去头尾空白
  2. 给定 sentence = "我-喜欢-编程",
     用 split("-") 切分,再用 "." 重新 join
  3. 给定 line = "Hello Python",
     用 replace 把 "Python" 改成 "World"
  4. 给定 text = "xxx 是个好网站,xxx 很好用",
     用 replace 把 "xxx" 替换成 "***"

示例:
    输出:
      Python 编程
      我.喜欢.编程
      Hello World
      *** 是个好网站,*** 很好用
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    s = "  Python 编程  "
    print(s.strip())

    sentence = "我-喜欢-编程"
    parts = sentence.split("-")
    print(".".join(parts))

    line = "Hello Python"
    print(line.replace("Python", "World"))

    text = "xxx 是个好网站,xxx 很好用"
    print(text.replace("xxx", "***"))
