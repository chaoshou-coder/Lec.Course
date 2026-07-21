"""
[难度: ★★★]
[所属知识点: 完整异常处理(try/except/else/finally)]
[预计完成时间: 15 分钟]
[类型: 选做]

题目描述:
  写一个函数 read_first_line(path),读取文件第一行。
  - 无论成功失败都打印 '读取结束'
  - 成功时返回内容
  - 失败时返回 None

示例:
    输出:
      第一行内容
      读取结束
      None
      读取结束
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
    with open('demo.txt', 'w', encoding='utf-8') as f:
        f.write('第一行\n第二行\n')

    def read_first_line(path):
        try:
            f = open(path, 'r', encoding='utf-8')
            line = f.readline()
        except FileNotFoundError:
            return None
        else:
            f.close()
            return line.strip()
        finally:
            print('读取结束')

    print(read_first_line('demo.txt'))
    print(read_first_line('不存在的文件.txt'))
