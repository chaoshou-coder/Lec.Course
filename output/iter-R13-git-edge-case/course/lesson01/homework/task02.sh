/*
[难度: ★★★]
[所属知识点: 查看历史]
[预计完成时间: 20 分钟]
[类型: 选做]

题目:给定一个 Git 仓库,查看最近 5 次提交的 commit message 和作者。
*/

if [ -z "$1" ]; then
  echo "参考答案:"
  echo "  git log --oneline -5"
  echo "  git log --format='%h %an %s' -5"
fi
