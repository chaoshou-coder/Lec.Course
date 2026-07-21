"""
[难度: ★★]
[所属知识点: header 与 nav 结构]
[预计完成时间: 10 分钟]

题目:补全下面的 header 结构,在 ??? 处填入正确的标签。

    <header>
        <???>小花的甜品屋</???>
        <???>
            <a href="#home">首页</a>
            <a href="#menu">菜单</a>
            <a href="#about">关于我们</a>
        <???>
    </header>

要求:
1. 品牌名用 h1(最重要的一行)
2. 导航链接组用 nav 包裹
3. 所有标签正确闭合

提示:header 里通常包含品牌(h1) + 导航(nav)。
"""

# ======================
# 学员代码区(填入正确标签名)
# ======================
pass
# 在这里写出完整 header:


# ======================
# 测试区
# ======================
if __name__ == '__main__':
    print("参考答案:")
    print()
    print("<header>")
    print("    <h1>小花的甜品屋</h1>")
    print("    <nav>")
    print('        <a href="#home">首页</a>')
    print('        <a href="#menu">菜单</a>')
    print('        <a href="#about">关于我们</a>')
    print("    </nav>")
    print("</header>")
    print()
    print("检查要点:")
    print("  1. h1 用了开标签和闭标签 ✓")
    print("  2. nav 包裹了三个 a ✓")
    print("  3. header 正确闭合 ✓")
