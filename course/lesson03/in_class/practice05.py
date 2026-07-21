"""
[难度: ★★★]
[所属知识点: 综合应用(链接+图片+列表)]
[预计完成时间: 15 分钟]

题目:独立编写一个完整的 HTML5 文档,主题是"我的旅行相册"。

要求:
1. 包含完整的文档骨架(DOCTYPE/html/head/body/title/meta)
2. title = "我的旅行相册"
3. body 内包含:
   - h1 标题:我的旅行相册
   - h2 "北京":一张图片(假设文件 beijing.jpg,alt 要有)+p 段落描述
   - h2 "上海":一张图片(假设文件 shanghai.jpg,alt 要有)+p 段落描述
   - hr 分隔线
   - h2 "更多目的地":ul/li 列出 3 个想去的地方
   - h2 "参考网站":a 标签链接到 https://www.example.com,target="_blank"
4. 所有标签正确闭合,img 有 alt
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
    print('    <title>我的旅行相册</title>')
    print('</head>')
    print('<body>')
    print('    <h1>我的旅行相册</h1>')
    print('    <h2>北京</h2>')
    print('    <img src="beijing.jpg" alt="北京天安门" width="300" />')
    print('    <p>北京是中国的首都,有故宫、长城等著名景点。</p>')
    print('    <h2>上海</h2>')
    print('    <img src="shanghai.jpg" alt="上海外滩" width="300" />')
    print('    <p>上海是中国最大的城市,外滩夜景非常美。</p>')
    print('    <hr>')
    print('    <h2>更多目的地</h2>')
    print('    <ul>')
    print('        <li>西安</li>')
    print('        <li>成都</li>')
    print('        <li>杭州</li>')
    print('    </ul>')
    print('    <h2>参考网站</h2>')
    print('    <p>')
    print('        <a href="https://www.example.com" target="_blank">')
    print('            访问旅行网站')
    print('        </a>')
    print('    </p>')
    print('</body>')
    print('</html>')
    print()
    print("验收要点:")
    print("  ✓ 文档骨架完整(DOCTYPE/html/head/body)")
    print("  ✓ meta charset 写了")
    print("  ✓ img 有 alt + 自闭合")
    print("  ✓ ul/li 列表正确嵌套")
    print("  ✓ a 标签有 href + target + 链接文字")
