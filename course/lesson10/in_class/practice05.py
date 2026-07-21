"""
[难度: ★★★]
[所属知识点: 站点文件结构整合]
[预计完成时间: 15 分钟]

题目:下面是一个三页官网的"目录结构",但文件组织有 5 处问题。
找出问题并写出修正后的正确结构。

当前结构(有问题):
    my-portfolio/
    ├── index.html
    ├── Homepage          ← 问题 1:不是 HTML 文件
    ├── contact.html
    ├── PROJECT1.JPG      ← 问题 2
    ├── project2.jpg
    ├── img/
    │   └── avatar.jpg
    └── img/              ← 问题 3:重复文件夹
        └── logo.png

要求:
1. 找出全部 5 处问题(文件命名/路径/重复)
2. 写出修正后的目录结构
3. 原因:文件名应全小写、图片统一放文件夹、不能有重复文件夹

提示:实际项目中,文件名全小写 + 全英文 + 短横线分隔是最佳实践。
"""

# 学员不需要写代码,在纸上作答即可。
# 参考答案见下方测试区。

if __name__ == '__main__':
    print("5 处问题:")
    print()
    print("  1. 'Homepage' 不是 HTML 文件 → 改为 projects.html")
    print("     原因:必须以 .html 结尾才能被浏览器识别")
    print()
    print("  2. 图片 PROJECT1.JPG 在根目录 → 移到 img/ 文件夹")
    print("     原因:图片应统一放一个文件夹,便于管理")
    print()
    print("  3. PROJECT1.JPG 大写字母 → 改为 project1.jpg")
    print("     原因:文件名全小写是最佳实践(服务器区分大小写)")
    print()
    print("  4. project2.jpg 在根目录 → 移到 img/ 文件夹")
    print("     原因:统一图片管理")
    print()
    print("  5. 有重复 img/ 文件夹 → 合并为一个")
    print("     原因:重复文件夹会导致路径混乱")
    print()
    print("修正后正确结构:")
    print("    my-portfolio/")
    print("    ├── index.html")
    print("    ├── projects.html")
    print("    ├── contact.html")
    print("    └── img/")
    print("        ├── avatar.jpg")
    print("        ├── logo.png")
    print("        ├── project1.jpg")
    print("        └── project2.jpg")
