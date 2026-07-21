"""
[难度: ★★]
[所属知识点: select 和 textarea]
[预计完成时间: 10 分钟]

题目:补全下面的表单片段,把 ??? 替换为正确内容。

    <form action="/feedback" method="POST">
        <!-- 下拉框:选择满意度 -->
        <select ???="satisfaction">
            <???>非常满意</???>
            <???>满意</???>
            <???>不满意</???>
        </select>

        <!-- 多行文本:填写建议 -->
        <??? name="suggestion" rows="5"></???>
    </form>

要求:
1. select 需要 name 属性,option 需要 value 属性
2. textarea 需要正确的标签名和闭标签
"""

# ======================
# 学员代码区(写出完整表单片段)
# ======================
pass
# 在这里写出完整表单片段:

# ======================
# 测试区
# ======================
if __name__ == '__main__':
    print("参考答案:")
    print()
    print('<form action="/feedback" method="POST">')
    print('    <select name="satisfaction">')
    print('        <option value="good">非常满意</option>')
    print('        <option value="ok">满意</option>')
    print('        <option value="bad">不满意</option>')
    print('    </select>')
    print('    <textarea name="suggestion" rows="5"></textarea>')
    print('</form>')
    print()
    print("要点:")
    print("  1. select 的 name 写在 select 标签上 ✓")
    print("  2. option 用 value 存储提交值 ✓")
    print("  3. textarea 有开标签和闭标签 ✓")
    print("  4. textarea 的 name 写在标签上,内容写在标签之间 ✓")
