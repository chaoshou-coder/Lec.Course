"""
[难度: ★★★]
[所属知识点: 完整文档]
[预计完成时间: 15 分钟]

题目:独立编写一个完整的 HTML5 文档,主题是"我的宠物"。

要求:
1. 包含完整的文档骨架(DOCTYPE/html/head/body/title/meta)
2. title = "我的宠物"
3. body 内包含:
   - h1 标题:宠物的名字
   - p 段落:一句话描述宠物
   - img 标签:插入一张宠物图片(假设图片文件名为 pet.jpg,在同一目录)
4. img 标签必须包含 alt 属性(替代文本)
"""

# ======================
# 学员代码区(独立编写完整文档)
# ======================
pass
# 在这里写出你的完整 HTML 文档:

# ======================
# 测试区
# ======================
if __name__ == '__main__':
    print("参考答案(示例):")
    print()
    print('<!DOCTYPE html>')
    print('<html lang="zh-CN">')
    print('<head>')
    print('    <meta charset="utf-8">')
    print('    <title>我的宠物</title>')
    print('</head>')
    print('<body>')
    print('    <h1>小白</h1>')
    print('    <p>小白是一只三岁的金毛犬,最喜欢追蝴蝶。</p>')
    print('    <img src="pet.jpg" alt="小白在草地上奔跑" width="300" />')
    print('</body>')
    print('</html>')
    print()
    print("验收要点:")
    print("  ✓ 文档骨架完整(DOCTYPE/html/head/body)")
    print("  ✓ meta charset 写了")
    print("  ✓ title 正确")
    print("  ✓ h1 + p + img 都有")
    print("  ✓ img 有 alt 属性")
