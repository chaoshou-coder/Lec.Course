"""
[难度: ★★]
[所属知识点: form 基础结构]
[预计完成时间: 10 分钟]

题目:补全下面 form 结构的 ??? 处。

    <form action="???" method="???">
        <p>
            <label for="??">用户名</label>
            <input type="text" id="???" name="???" />
        </p>
        <button type="???">提交</button>
    </form>

要求:
1. action="#"(提交到当前页)
2. method="post"
3. label for / input id / input name 都设为 "user"
4. button type="submit"

提示:label 的 for = input 的 id;input 的 name 是提交时的字段名。
"""

# ======================
# 学员代码区(补全 form)
# ======================
pass
# 在这里写出完整 form:


# ======================
# 测试区
# ======================
if __name__ == '__main__':
    print("参考答案:")
    print()
    print('<form action="#" method="post">')
    print('    <p>')
    print('        <label for="user">用户名</label>')
    print('        <input type="text" id="user" name="user" />')
    print('    </p>')
    print('    <button type="submit">提交</button>')
    print('</form>')
    print()
    print("检查要点:")
    print("  1. action=\"#\" ✓")
    print("  2. method=\"post\" ✓")
    print("  3. label for=\"user\" = input id=\"user\" ✓")
    print("  4. input name=\"user\"(字段名) ✓")
    print("  5. button type=\"submit\" ✓")
