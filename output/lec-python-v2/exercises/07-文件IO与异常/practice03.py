"""
[难度: ★]
[所属知识点: with 上下文管理器]
[预计完成时间: 5 分钟]

题目描述:
  把 old_style.txt 里的内容复制一份到 new_style.txt,
  要求用 with 同时管理读文件和写文件。

示例:
    源文件内容:静夜思\n李白\n\n床前明月光\n
    new_style.txt 内容应该与源文件相同
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 准备源文件
    with open('old_style.txt', 'w', encoding='utf-8') as f:
        f.write('静夜思\n李白\n\n床前明月光\n')

    # 用 with 复制文件
    with open('old_style.txt', 'r', encoding='utf-8') as src:
        content = src.read()
    with open('new_style.txt', 'w', encoding='utf-8') as dst:
        dst.write(content)

    # 验证
    with open('new_style.txt', 'r', encoding='utf-8') as f:
        print(f.read())
