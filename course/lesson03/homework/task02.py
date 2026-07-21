"""
[难度: ★★★]
[所属知识点: 导航栏与图片展示页]
[预计完成时间: 20 分钟]
[类型: 选做]

题目:用 HTML 制作一个"电影推荐"页面,包含导航、图片展示和列表。

下面是一篇关于电影的资料,请用合适的 HTML 标签重新组织:

    电影推荐
    正在上映
    流浪地球 3:一部科幻史诗,讲述了人类寻找新家园的故事。
    封神第二部:中国古代神话故事,视觉效果震撼。
    经典回顾
    1. 肖申克的救赎 - 关于希望的故事
    2. 阿甘正传 - 一个简单男人的不平凡人生
    3. 泰坦尼克号 - 经典的爱情悲剧
    更多电影资讯请访问示例电影网站。

要求:
1. 用 h1 做主标题
2. 用 h2 做每个板块的标题
3. 正在上映的每部电影用 h3 + 图片(img,假设文件名为电影名.jpg)+ p 描述
4. 经典回顾用 ol/li 有序列表
5. "更多电影资讯"用 a 标签链接到 https://www.movie.com,target="_blank"
6. 完整文档骨架
"""

# ======================
# 学员代码区
# ======================
pass
# 在这里写出结构化后的 HTML 文档:


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
    print('    <title>电影推荐</title>')
    print('</head>')
    print('<body>')
    print('    <h1>电影推荐</h1>')
    print('    <h2>正在上映</h2>')
    print('    <h3>流浪地球 3</h3>')
    print('    <img src="the-wandering-earth.jpg" alt="流浪地球 3 海报" width="200" />')
    print('    <p>一部科幻史诗,讲述了人类寻找新家园的故事。</p>')
    print('    <h3>封神第二部</h3>')
    print('    <img src="fengshen.jpg" alt="封神第二部 海报" width="200" />')
    print('    <p>中国古代神话故事,视觉效果震撼。</p>')
    print('    <h2>经典回顾</h2>')
    print('    <ol>')
    print('        <li>肖申克的救赎 - 关于希望的故事</li>')
    print('        <li>阿甘正传 - 一个简单男人的不平凡人生</li>')
    print('        <li>泰坦尼克号 - 经典的爱情悲剧</li>')
    print('    </ol>')
    print('    <p>')
    print('        <a href="https://www.movie.com" target="_blank">')
    print('            更多电影资讯请访问示例电影网站')
    print('        </a>')
    print('    </p>')
    print('</body>')
    print('</html>')
    print()
    print("要点:")
    print("  ✓ h1 → h2 → h3 层级清晰")
    print("  ✓ img 有 alt + 自闭合")
    print("  ✓ ol/li 列表正确")
    print("  ✓ a 标签有 href + target + 链接文字")
