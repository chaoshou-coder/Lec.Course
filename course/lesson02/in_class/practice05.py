"""
[难度: ★★★]
[所属知识点: 完整文章页面]
[预计完成时间: 15 分钟]

题目:独立编写一个完整的 HTML5 文档,主题是"我的一天"。

要求:
1. 包含完整的文档骨架(DOCTYPE/html/head/body/title/meta)
2. title = "我的一天"
3. body 内包含:
   - h1 标题:我的一天
   - h2 "早晨":一段描述(p 标签)
   - h2 "中午":一段描述(p 标签)
   - h2 "晚上":一段描述,包含换行(br)列出 3 件事
   - hr 分隔线
   - h2 "总结":一段话(p 标签)
4. 标题层级正确(h1 → h2,不跳级)
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
    print('    <title>我的一天</title>')
    print('</head>')
    print('<body>')
    print('    <h1>我的一天</h1>')
    print('    <h2>早晨</h2>')
    print('    <p>早上 7 点起床,吃完早餐后去上班。</p>')
    print('    <h2>中午</h2>')
    print('    <p>中午和同事一起吃饭,聊了会天。</p>')
    print('    <h2>晚上</h2>')
    print('    <p>晚上做了三件事:<br>')
    print('    跑步 5 公里<br>')
    print('    看了一章书<br>')
    print('    给家人打了电话</p>')
    print('    <hr>')
    print('    <h2>总结</h2>')
    print('    <p>今天过得很充实,明天继续努力!</p>')
    print('</body>')
    print('</html>')
    print()
    print("验收要点:")
    print("  ✓ 文档骨架完整(DOCTYPE/html/head/body)")
    print("  ✓ meta charset 写了")
    print("  ✓ h1 只有一个,h2 有多个")
    print("  ✓ 标题层级正确(h1 → h2,不跳级)")
    print("  ✓ br 用在段落内换行")
    print("  ✓ hr 用在主题分隔")
