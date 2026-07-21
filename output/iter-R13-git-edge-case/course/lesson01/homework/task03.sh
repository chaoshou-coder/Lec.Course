/*
[难度: ★★★★]
[所属知识点: 综合实战]
[预计完成时间: 30 分钟]
[类型: 选做]

题目:从零开始,创建一个 Git 仓库,添加 3 个文件,每个文件分别 commit,然后查看历史。
*/

if [ -z "$1" ]; then
  echo "参考答案:"
  echo "  mkdir project && cd project"
  echo "  git init"
  echo "  echo '# Title' > README.md && git add . && git commit -m 'Initial'"
  echo "  echo 'print()' > main.py && git add . && git commit -m 'Add main'"
  echo "  echo 'test' > test.py && git add . && git commit -m 'Add test'"
  echo "  git log --oneline"
fi
