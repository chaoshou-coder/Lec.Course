"""
[难度: ★★★★]
[所属知识点: 部署上线实操]
[预计完成时间: 30 分钟]
[类型: 选做]

题目:把你前三天写的三个页面(index.html / projects.html / contact.html)
部署到 GitHub Pages,让它真正上线,成为一个可访问的网址。

要求:
1. 在 GitHub 创建一个新仓库,仓库名 = 你的用户名.github.io
   (例:用户名为 alice,仓库名 = alice.github.io)
2. 把三个 HTML 文件 push 到仓库的 main 分支
3. 进入仓库 Settings → Pages → Source 选择 "Deploy from a branch"
   → Branch 选 "main",文件夹选 "/ (root)" → Save
4. 等 1-2 分钟,访问 https://你的用户名.github.io
   应该能看到你的站点首页

验证清单:
  [ ] 仓库已创建,main 分支包含 index.html
  [ ] Pages 设置中 Source 已选择 main 分支
  [ ] 访问 https://用户名.github.io 能看到首页
  [ ] 首页导航能跳转到 projects.html 和 contact.html
  [ ] 所有图片正常加载(没有裂图)

进阶挑战(可选):
- 在仓库根目录增加一个 README.md,写上站点介绍 + 截图
- 试试在浏览器地址栏访问 https://用户名.github.io/projects.html
- 使用自定义域名(需要自己购买域名)
"""

# ======================
# 实操步骤(按顺序执行)
# ======================

步骤_创建仓库 = """
1. 打开 https://github.com/new
2. Repository name: 你的用户名.github.io
   (注意:必须是 用户名.github.io 格式,否则 Pages 不生效)
3. 选择 Public(公开,Pages 需要)
4. 勾选 Add a README file
5. 点击 Create repository
"""

步骤_推送文件 = """
# 在本地项目目录依次执行:

git init
git add index.html projects.html contact.html
git commit -m "feat: add three pages"
git branch -M main
git remote add origin https://github.com/用户名/用户名.github.io.git
git push -u origin main

# 如果使用 https 可能需要 Personal Access Token
# 建议使用:gh auth login  或 配置 SSH
"""

步骤_启用_pages = """
1. 打开仓库页面 → Settings
2. 左侧菜单找到 Pages
3. Source 选 "Deploy from a branch"
4. Branch 选 "main",文件夹选 "/ (root)"
5. Save
6. 等 1-2 分钟,页面上方会出现:
   ✅ Your site is live at https://用户名.github.io
"""

步骤_验证链接 = """
访问下面的链接,逐一验证:

首页:     https://用户名.github.io
作品集页: https://用户名.github.io/projects.html
联系页:   https://用户名.github.io/contact.html

预期:
  ✅ 三个页面都能正常渲染
  ✅ 导航跳转正常
  ✅ 图片正常加载
  ✅ 表单能正常填写(提交会 #,因为没有后端)
"""

if __name__ == '__main__':
    print("=" * 50)
    print("GitHub Pages 部署实操任务")
    print("=" * 50)
    print()
    print("请按照下面的顺序执行:")
    print()
    print("【第 1 步】创建仓库")
    print(步骤_创建仓库)
    print()
    print("【第 2 步】推送文件")
    print(步骤_推送文件)
    print()
    print("【第 3 步】启用 Pages")
    print(步骤_启用_pages)
    print()
    print("【第 4 步】验证链接")
    print(步骤_验证链接)
    print()
    print("=" * 50)
    print("部署完成后,把链接填在这里留作纪念:")
    print("我的第一个网站: https://____________.github.io")
    print("=" * 50)
