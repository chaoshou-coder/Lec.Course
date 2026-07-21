"""
[难度: ★★★][所属知识点: 字符串方法综合][预计完成时间: 20 分钟][类型: 选做]

题目:输入一个句子(如 "I love Python"),把句子中每个单词首字母
变成大写,其他小写,输出结果。提示:用 split()、upper()、lower()、join()。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('s = input("请输入句子:")')
    print('words = s.split()')
    print('result = []')
    print('for w in words:')
    print('    result.append(w[0].upper() + w[1:].lower())')
    print('print(" ".join(result))')
