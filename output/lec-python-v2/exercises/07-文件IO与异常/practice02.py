"""
[难度: ★]
[所属知识点: 三种读法]
[预计完成时间: 5 分钟]

题目描述:
  给定的 data.txt 内容是若干行数字(可能有空行)。
  用 readlines 读取,打印出所有非空行的数量。

示例:
    文件内容:10\n\n20\n\n30\n
    输出:非空行数: 3
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 准备测试文件
    f = open('data.txt', 'w', encoding='utf-8')
    f.write('10\n\n20\n\n30\n')
    f.close()

    # 统计非空行数
    f = open('data.txt', 'r', encoding='utf-8')
    lines = f.readlines()
    f.close()

    count = 0
    for line in lines:
        if line.strip() != '':
            count += 1
    print('非空行数:', count)
