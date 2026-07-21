# [难度: ★★★★][所属知识点: 综合][预计完成时间: 30 分钟][类型: 选做]
# 题目:运行一个 MySQL 容器,设置 root 密码,映射端口 3306
# 参考答案:docker run -d --name mysql -e MYSQL_ROOT_PASSWORD=secret -p 3306:3306 mysql:8
