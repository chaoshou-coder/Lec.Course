"""
[难度: ★★]
[所属知识点: target 属性与路径]
[预计完成时间: 10 分钟]

题目:下面代码有 3 处错误(链接和图片的误用),找出来并修正。

错误版本:
    <a href="https://www.example.com" target="blank">新窗口打开</a>
    <img src="photo.jpg" alt="照片">
    <a href="https://www.example.com"></a>

要求:
1. target 属性的正确值写法
2. img 标签的自闭合规则
3. 链接必须有文字
"""

# ======================
# 学员代码区(写出修正后的代码)
# ======================
pass
# 在这里写出修正后的代码:


# ======================
# 测试区
# ======================
if __name__ == '__main__':
    # 参考答案
    print("修正后:")
    print('  <a href="https://www.example.com" target="_blank">新窗口打开</a>')
    print('  <img src="photo.jpg" alt="照片" />')
    print('  <a href="https://www.example.com">点击访问</a>')
    print()
    print("3 处错误:")
    print("  1. target=\"blank\" → target=\"_blank\"")
    print("     原因:target 的值必须带下划线前缀 _blank")
    print()
    print("  2. <img ...> → <img ... />")
    print("     原因:img 是自闭合标签,推荐加斜杠")
    print()
    print("  3. <a ...></a> 没有链接文字")
    print("     原因:没有文字用户看不到也无法点击链接")
    print()
    print("补充说明:")
    print("  target=\"_blank\"  = 在新标签页打开")
    print("  target=\"_self\"   = 在当前页打开(默认)")
