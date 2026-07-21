"""
[难度: ★★★]
[所属知识点: 自定义变量类型]
[预计完成时间: 20 分钟]
[类型: 选做]

题目:JavaScript 是动态类型语言,一个变量可以先后装不同类型。
请编写一段代码,演示:
1. 一个变量先装数字,再装字符串,再装布尔
2. 用 console.log 在每种状态下打印变量值和它的类型(用 typeof)
3. 用 const 还是 let?为什么?
"""

# 学员作答
answer_code = """
(在这里写出你的代码)
"""

# 测试区
if __name__ == '__main__':
    print("参考答案:")
    print('  let mixed = 42;')           # 数字
    print('  console.log(mixed, typeof mixed);')
    print('  mixed = "hello";')         # 字符串
    print('  console.log(mixed, typeof mixed);')
    print('  mixed = true;')            # 布尔
    print('  console.log(mixed, typeof mixed);')
    print()
    print("期望输出:")
    print("  42 'number'")
    print("  hello string")
    print("  true boolean")
    print()
    print("用 let(不用 const): 因为后续要重新赋值")
