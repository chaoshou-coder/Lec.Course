"""
[难度: ★★]
[所属知识点: 重新赋值 let]
[预计完成时间: 10 分钟]

题目:下面的代码最后会输出什么?为什么?

    let count = 0;
    count = 5;
    count = count + 1;
    console.log(count);

边界:考虑 count 是否会出错(count 是空、未声明、重新声明等)
"""

# 学员作答
answer = """
(在这里写出你的预测和理由)
"""

# 测试区
if __name__ == '__main__':
    print("实际运行:")
    print('  let count = 0;')
    print('  count = 5;')
    print('  count = count + 1;')
    print('  console.log(count);')
    print()
    print("期望输出:6")
    print()
    print("解释:")
    print("  - 第 1 行:声明 count,值 0")
    print("  - 第 2 行:重新赋值 count,值 5(直接 = 表示修改)")
    print("  - 第 3 行:count + 1 = 5 + 1 = 6,赋值给 count")
    print("  - 第 4 行:打印 6")
    print()
    print("边界情况:")
    print("  - 如果第 1 行遗漏 'let':count 变成隐式全局变量(老 JS 行为,新规范报错)")
    print("  - 如果第 2 行加 'let':Uncaught SyntaxError(重复声明)")
    print("  - 如果 count 是 const:第 2-3 行会 TypeError(常量不能改)")
