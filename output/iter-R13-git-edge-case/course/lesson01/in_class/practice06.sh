/*
[难度: ★★★]
[所属知识点: 综合(挑战题)]
[预计完成时间: 15 分钟]
[类型: 挑战题,不强制完成]

题目:下面代码有 3 处错误,找出来并修正。

    git init
    echo "Hello" > hello.txt
    git commit -m "Add hello"(错误 1)
    git add hello.txt(错误 2)
    git log(没有输出,为什么?错误 3)
*/

if [ -z "$1" ]; then
  echo "3 处错误:"
  echo "  1. git commit 前没有 git add(暂存区为空)"
  echo "  2. git add 应该在 commit 之前"
  echo "  3. commit 失败了,所以 log 没有输出"
fi
