"""
[难度: ★★★][所属知识点: 作用域][预计完成时间: 12 分钟]

题目:下面代码输出什么?为什么?
x = 10
def modify():
    x = 20
    print("函数内:", x)
modify()
print("函数外:", x)
"""

if __name__ == "__main__":
    print("参考答案:")
    print('输出:')
    print('  函数内: 20')
    print('  函数外: 10')
    print('原因:函数内 x = 20 是新建局部变量,不影响全局变量')
    print('如果要修改全局变量,需要加 global x')
