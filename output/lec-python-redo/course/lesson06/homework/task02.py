"""
[难度: ★★★][所属知识点: 字典统计][预计完成时间: 20 分钟][类型: 选做]

题目:输入一段文字,统计每个字出现的次数,存入字典并输出。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('text = input("请输入文字:")')
    print('count = {}')
    print('for ch in text:')
    print('    count[ch] = count.get(ch, 0) + 1')
    print('for ch, cnt in count.items():')
    print('    print(f"{ch}: {cnt}")')
