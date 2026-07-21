"""
[难度: ★★]
[所属知识点: 图片卡片单体结构]
[预计完成时间: 10 分钟]

题目:补全下面一张项目卡片的 HTML,在 ??? 处填入正确内容。

    <li>
        <img src="???" alt="???" width="???" />
        <h3>宠物社交 App</h3>
        <p>???</p>
    </li>

要求:
1. src 设为 "pet-app.jpg"
2. alt 描述图片内容(不是文件名,不是"图片")
3. width 设为 280
4. p 写一句简短描述(10 字以内)

提示:alt 应该告诉读屏软件"这张图里有什么"。
"""

# ======================
# 学员代码区(补全卡片 HTML)
# ======================
pass
# 在这里写出完整 li:


# ======================
# 测试区
# ======================
if __name__ == '__main__':
    print("参考答案:")
    print()
    print('<li>')
    print('    <img src="pet-app.jpg"')
    print('         alt="宠物社交 App 的首页界面 mockup"')
    print('         width="280" />')
    print('    <h3>宠物社交 App</h3>')
    print('    <p>让爱宠人士相遇的社交平台。</p>')
    print('</li>')
    print()
    print("检查要点:")
    print("  1. src = \"pet-app.jpg\" ✓")
    print("  2. alt 描述了图片内容(不是文件名) ✓")
    print("  3. width = \"280\" ✓")
    print("  4. img 自闭合(有 />) ✓")
    print("  5. p 有简短描述 ✓")
