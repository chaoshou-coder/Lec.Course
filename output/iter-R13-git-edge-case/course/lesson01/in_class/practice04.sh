/*
[难度: ★★]
[所属知识点: 多次 commit]
[预计完成时间: 10 分钟]

题目:创建 3 个文件(file1.txt/file2.txt/file3.txt),每个文件分别 commit 一次,然后 git log 查看历史。
*/

if [ -z "$1" ]; then
  echo "参考答案:"
  echo '  echo "file1" > file1.txt && git add file1.txt && git commit -m "Add file1"'
  echo '  echo "file2" > file2.txt && git add file2.txt && git commit -m "Add file2"'
  echo '  echo "file3" > file3.txt && git add file3.txt && git commit -m "Add file3"'
  echo '  git log --oneline'
fi
