[难度: ★★★][所属知识点: 挑战题][预计完成时间: 15 分钟][类型: 挑战题]

题目:下面 API 设计有 3 个问题,找出来。

GET /users/list(用了动词 list)
POST /deleteUser(用 POST 删除)
GET /users?id=123(查询单个用户应该用路径参数)

参考答案:1. /users/list → /users 2. /deleteUser → DELETE /users/123 3. /users?id=123 → GET /users/123
