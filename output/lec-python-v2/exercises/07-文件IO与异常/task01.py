"""
[难度: ★★]
[所属知识点: json.dumps/loads]
[预计完成时间: 10 分钟]
[类型: 选做]

题目描述:
  有一个 JSON 字符串 [1, 2, 3, "four", 5],
  把它解析为 Python 列表,
  注意 four 是字符串,列表元素可以类型不同,
  然后把所有整数求和。

示例:
    输出:
      解析结果: [1, 2, 3, 'four', 5]
      整数和: 11
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    import json

    raw = '[1, 2, 3, "four", 5]'
    data = json.loads(raw)
    print('解析结果:', data)

    total = 0
    for item in data:
        if isinstance(item, int):
            total += item
    print('整数和:', total)
