[难度: ★★★★][所属知识点: 综合][预计完成时间: 30 分钟][类型: 选做]

题目:设计一个完整的图书管理 API,包含资源命名、HTTP 方法、状态码、错误处理。

参考答案:
GET /books(200) | POST /books(201)
GET /books/1(200/404) | PUT /books/1(200/404) | DELETE /books/1(200/404)
GET /books/1/reviews(200) | POST /books/1/reviews(201)
错误处理:{"error":{"code":404,"message":"Book not found"}}
