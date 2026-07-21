"""
[难度: ★★★★][所属知识点: 综合应用][预计完成时间: 30 分钟][类型: 选做]

题目:输入一个身份证号(18 位),提取出生日期(第 7-14 位),
格式化为 "YYYY年MM月DD日" 输出。
如输入 "110101200001011234",输出 "2000年01月01日"。
"""

if __name__ == "__main__":
    print("参考答案:")
    print('id_card = input("请输入身份证号:")')
    print('year = id_card[6:10]')
    print('month = id_card[10:12]')
    print('day = id_card[12:14]')
    print('print(f"{year}年{month}月{day}日")')
