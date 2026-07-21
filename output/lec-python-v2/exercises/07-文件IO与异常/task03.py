"""
[难度: ★★★★]
[所属知识点: 异常安全加载 JSON]
[预计完成时间: 20 分钟]
[类型: 选做]

题目描述:
  写一个函数 save_records(records, path):
  把记录列表保存到 JSON 文件,
  如果文件已存在则先备份再覆盖,
  任何异常都打印提示且不丢数据。

  提示:
  - 用 os.path.exists 判断文件是否存在
  - 备份文件名加 .bak 后缀
  - 用 try-except 捕获所有异常

示例:
    输出:
      保存成功
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
    import os
    import shutil

    def save_records(records, path):
        try:
            # 1. 已存在则备份
            if os.path.exists(path):
                backup = path + '.bak'
                shutil.copy(path, backup)
                print(f'已备份为 {backup}')
            # 2. 写入新文件
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(records, f, ensure_ascii=False, indent=2)
            print('保存成功')
        except Exception as e:
            print(f'保存失败: {e}')

    save_records([{'name': 'test'}], 'records.json')
