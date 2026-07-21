"""
[难度: ★★★]
[所属知识点: Hero 区骨架搭建]
[预计完成时间: 15 分钟]

题目:为一个"摄影师个人主页"编写 Hero 区的 HTML。

Hero 区必须包含三部分:
1. 主标题(h2):一句话说明身份
   —— 例如"用镜头记录美好瞬间"
2. 副标题(p):补充细节(经验/特色)
   —— 例如"独立摄影师 · 擅长人像与风景 · 8 年经验"
3. 行动按钮(a):引导访客下一步操作
   —— 例如"查看作品集",跳转到 #portfolio

要求:
1. 用 <section id="hero"> 包裹整个 Hero 区
2. h2、p、a 三个标签齐全
3. a 标签有 href 属性(跳转到 #portfolio)
4. 所有内容必须是中文
"""

# ======================
# 学员代码区(编写 Hero 区 HTML)
# ======================
pass
# 在这里写出 Hero 区的 HTML:


# ======================
# 测试区
# ======================
if __name__ == '__main__':
    print("参考答案(示例):")
    print()
    print('<section id="hero">')
    print("    <h2>用镜头记录美好瞬间</h2>")
    print("    <p>独立摄影师 · 擅长人像与风景 · 8 年经验</p>")
    print('    <a href="#portfolio">查看作品集 →</a>')
    print("</section>")
    print()
    print("验收要点:")
    print("  ✓ section 有 id=\"hero\"")
    print("  ✓ h2 是主标题")
    print("  ✓ p 是副标题(有具体细节)")
    print("  ✓ a 有 href 属性")
    print("  ✓ 三个标签都在 section 里面")
