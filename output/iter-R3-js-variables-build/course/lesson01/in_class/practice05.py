"""
[难度: ★★★]
[所属知识点: const 的限制]
[预计完成时间: 15 分钟]

题目:下面 4 段代码,哪段能运行?哪段报错?为什么?

代码段 A:
    const x = 5;
    x = 10;
    console.log(x);

代码段 B:
    const y = 5;
    console.log(y);

代码段 C:
    const z = 5;
    const z = 10;
    console.log(z);

代码段 D:
    const w = 5;
    console.log(w);
    w = 10;
"""

# 学员作答:写出每段代码的结果和理由

# 测试区
if __name__ == '__main__':
    print("A: ❌ TypeError(常量不能重新赋值)")
    print("B: ✅ 输出 5")
    print("C: ❌ SyntaxError(重复声明 z)")
    print("D: ❌ 输出 5 后 TypeError('w' is constant 时赋值,后面的代码不执行)")
    print()
    print("启示:")
    print("  - const 声明后立即打印可以(没尝试重新赋值)")
    print("  - 但任何尝试修改 const 的语句都会报错")
    print("  - const 适合'装永远不变的东西'(如配置项、圆周率)")
