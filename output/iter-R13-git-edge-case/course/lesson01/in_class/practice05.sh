/*
[难度: ★★★]
[所属知识点: .gitignore]
[预计完成时间: 15 分钟]

题目:创建 .gitignore 文件,忽略 .DS_Store 和 node_modules/,然后验证 git status 不显示这些文件。
*/

if [ -z "$1" ]; then
  echo "参考答案:"
  echo '  echo ".DS_Store" > .gitignore'
  echo '  echo "node_modules/" >> .gitignore'
  echo '  mkdir -p node_modules && echo "test" > node_modules/test.txt'
  echo '  touch .DS_Store'
  echo '  git status(应该不显示 node_modules 和 .DS_Store)'
fi
