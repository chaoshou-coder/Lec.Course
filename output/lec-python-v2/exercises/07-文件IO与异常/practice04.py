"""
[难度: ★★]
[所属知识点: json.dump/load]
[预计完成时间: 10 分钟]

题目描述:
  把一个学生名单(列表套字典)写入 students.json,
  再用 json.load 读取,计算平均分。

  students = [
      {'name': '小明', 'score': 88},
      {'name': '小红', 'score': 95},
      {'name': '小刚', 'score': 72}
  ]

示例:
    输出:平均分: 85.0
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

    students = [
        {'name': '小明', 'score': 88},
        {'name': '小红', 'score': 95},
        {'name': '小刚', 'score': 72}
    ]

    # 写入 JSON 文件
    with open('students.json', 'w', encoding='utf-8') as f:
        json.dump(students, f, ensure_ascii=False, indent=2)

    # 读回并计算平均分
    with open('students.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    total = 0
    for s in data:
        total += s['score']
    print('平均分:', total / len(data))
