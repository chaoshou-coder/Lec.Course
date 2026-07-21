"""
[难度: ★★★★]
[所属知识点: 诗歌排版页面]
[预计完成时间: 30 分钟]
[类型: 选做]

题目:综合运用 Day 02 所有知识,编写一个"古诗词赏析"HTML 页面。

要求:
1. 完整文档骨架(DOCTYPE/html/head/body/title/meta charset)
2. 页面内容包含:
   - h1:古诗词赏析
   - h2 "静夜思":作者名(p 标签),诗的内容(每句用 br 换行)
   - h2 "春晓":作者名(p 标签),诗的内容(每句用 br 换行)
   - hr 分隔线
   - h2 "我的感悟":一段赏析文字(p 标签)
3. 标题层级正确(h1 → h2,不跳级)
4. 诗歌每句占一行(用 br 换行)
5. 保存为 poetry.html,用浏览器打开验证

进阶挑战(可选):
- 在页面底部加一行小字"© 2026 诗词赏析",用 <small> 标签
- 在两个 h2 诗歌之间加 hr 分隔线
"""

# ======================
# 学员代码区(独立编写完整页面)
# ======================
pass
# 在这里写出你的古诗词赏析页面:


# ======================
# 测试区
# ======================
if __name__ == '__main__':
    print("参考答案(示例结构):")
    print()
    print('<!DOCTYPE html>')
    print('<html lang="zh-CN">')
    print('<head>')
    print('    <meta charset="utf-8">')
    print('    <title>古诗词赏析</title>')
    print('</head>')
    print('<body>')
    print('    <h1>古诗词赏析</h1>')
    print('    <h2>静夜思</h2>')
    print('    <p>作者:李白</p>')
    print('    <p>床前明月光,<br>')
    print('    疑是地上霜。<br>')
    print('    举头望明月,<br>')
    print('    低头思故乡。</p>')
    print('    <hr>')
    print('    <h2>春晓</h2>')
    print('    <p>作者:孟浩然</p>')
    print('    <p>春眠不觉晓,<br>')
    print('    处处闻啼鸟。<br>')
    print('    夜来风雨声,<br>')
    print('    花落知多少。</p>')
    print('    <hr>')
    print('    <h2>我的感悟</h2>')
    print('    <p>这两首诗都描写了春天的夜晚,但表达的情感不同。')
    print('    李白写的是思乡之情,孟浩然写的是对春天的喜爱。</p>')
    print('    <small>© 2026 诗词赏析</small>')
    print('</body>')
    print('</html>')
    print()
    print("验收要点:")
    print("  ✓ 文档骨架完整")
    print("  ✓ h1 + 多个 h2 结构清晰")
    print("  ✓ 诗歌每句用 br 换行")
    print("  ✓ hr 用在主题分隔")
    print("  ✓ 标题层级正确(不跳级)")
