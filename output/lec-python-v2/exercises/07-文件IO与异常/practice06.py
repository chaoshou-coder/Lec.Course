"""
[难度: ★★]
[所属知识点: 异常类型速查]
[预计完成时间: 10 分钟]

题目描述:
  分析以下代码会抛出哪种异常,并在 except 中捕获:
  data = [{'name': 'a'}]; print(data[1]['name'])

  提示:错误发生在 data[1] 还是 ['name']?

示例:
    输出:捕获到 IndexError: list index out of range
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    data = [{'name': 'a'}]
    try:
        print(data[1]['name'])
    except IndexError as e:
        print('捕获到 IndexError:', e)
    except KeyError as e:
        print('捕获到 KeyError:', e)
