/*
[难度: ★★★]
[所属知识点: 修复 Git 错误]
[预计完成时间: 15 分钟]
[类型: 选做]

题目:你在终端执行 git commit 时报错:
    fatal: unable to auto-detect email address
解释原因并修复。
*/

if [ -z "$1" ]; then
  echo "原因:没有配置 user.email"
  echo "修复:"
  echo "  git config --global user.email 'your@email.com'"
  echo "  git config --global user.name 'Your Name'"
fi
