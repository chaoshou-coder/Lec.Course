"""
[难度: ★★★]
[所属知识点: 4 张卡片的完整列表]
[预计完成时间: 15 分钟]

题目:为一个"自由摄影师"编写包含 4 张作品卡片的完整列表。

每张卡片必须包含:
- img:src/alt/width(280)
- h3:作品名称(4 个字以内)
- p:简短描述(20 字以内)

4 个作品主题(任选或自拟):
  □ 人像写真  □ 风光摄影  □ 商业产品  □ 活动纪实

要求:
1. 用 <section> 包裹整个列表,h2 标题为 "作品展示"
2. 用 <ul> 包裹 4 个 <li>
3. 所有卡片结构一致(图 → 标题 → 描述)
4. alt 必须描述图片视觉内容,不是文件名
"""

# ======================
# 学员代码区(编写 4 张卡片的完整列表)
# ======================
pass
# 在这里写出完整 section:


# ======================
# 测试区
# ======================
if __name__ == '__main__':
    print("参考答案(示例):")
    print()
    print('<section>')
    print('    <h2>作品展示</h2>')
    print('    <ul>')
    print('        <li>')
    print('            <img src="portrait.jpg"')
    print('                 alt="室外自然光人像写真"')
    print('                 width="280" />')
    print('            <h3>人像写真</h3>')
    print('            <p>自然光与情绪捕捉。</p>')
    print('        </li>')
    print('        <li>')
    print('            <img src="landscape.jpg"')
    print('                 alt="日出时分的雪山风光"')
    print('                 width="280" />')
    print('            <h3>风光摄影</h3>')
    print('            <p>脚步丈量山河。</p>')
    print('        </li>')
    print('        <li>')
    print('            <img src="product.jpg"')
    print('                 alt="咖啡产品商业拍摄"')
    print('                 width="280" />')
    print('            <h3>商业产品</h3>')
    print('            <p>让产品自己说话。</p>')
    print('        </li>')
    print('        <li>')
    print('            <img src="event.jpg"')
    print('                 alt="音乐节现场纪实"')
    print('                 width="280" />')
    print('            <h3>活动纪实</h3>')
    print('            <p>记录高光瞬间。</p>')
    print('        </li>')
    print('    </ul>')
    print('</section>')
    print()
    print("验收要点:")
    print("  ✓ section 含 h2")
    print("  ✓ ul 包裹 4 个 li")
    print("  ✓ 每张卡片:img + h3 + p")
    print("  ✓ 所有 img 有 alt + width + 自闭合")
    print("  ✓ 卡片结构完全一致")
