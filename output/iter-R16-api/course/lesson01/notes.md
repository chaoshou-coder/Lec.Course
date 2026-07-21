### Day 01 · REST 基础:资源 + HTTP 方法 + 状态码

> **痛点**:你用 fetch/axios 调用过 API,但从没设计过。REST 是"设计 API 的语法规则"。今天你将理解什么是 REST,并学会用 Postman 发请求。
> **类比**:REST 就像"餐厅点餐" —— 资源 = 菜品,HTTP 方法 = 操作类型(点单/修改/取消),状态码 = 服务员回应(做好了/没食材/订单找不到)。
> **解释**:**REST = 表征状态转移**,一种 API 设计风格。今天学:资源命名 + HTTP 方法 + 状态码。

---

#### 资源命名 —— API 的"地址"

> **痛点**:你不知道 API URL 应该怎么设计。是 `/getUser` 还是 `/users`?是 `/deleteUser` 还是 `/users/123`?
> **类比**:资源就像"文件名" —— 用名词(不是动词),用复数(不是单数),层级清晰。
> **解释**:**资源 = 系统中的实体**(用户/订单/商品)。URL 指向资源,不是操作。

```
# 好的 REST API 设计
GET    /users          # 获取所有用户
GET    /users/123      # 获取 ID 为 123 的用户
POST   /users          # 创建新用户
PUT    /users/123      # 更新用户(全量)
PATCH  /users/123      # 更新用户(部分)
DELETE /users/123      # 删除用户

# 差的设计(不推荐)
GET    /getUser?id=123    # 用了动词,不是资源
POST   /deleteUser        # POST 不应该用于删除
GET    /users/list        # list 是冗余的
```

**逐行解剖**

- `GET /users` = 获取用户列表(安全操作,不修改数据)
- `POST /users` = 创建用户(非幂等,多次调用创建多个)
- `PUT /users/123` = 更新用户(幂等,多次调用结果一样)
- `DELETE /users/123` = 删除用户

> **ASCII 请求流程**
> ```
> 客户端                    API 服务器
> │                          │
> │── GET /users/123 ───────▶│
> │                          │── 查询数据库
> │◀── 200 OK + JSON ────────│
> │                          │
> ```

---

#### HTTP 方法 —— API 的"操作类型"

| 方法 | 含义 | 幂等? | 示例 |
|------|------|-------|------|
| GET | 读取资源 | ✅ | 获取用户列表 |
| POST | 创建资源 | ❌ | 创建新用户 |
| PUT | 全量更新 | ✅ | 更新用户所有字段 |
| PATCH | 部分更新 | ✅ | 只更新邮箱 |
| DELETE | 删除资源 | ✅ | 删除用户 |

---

#### 状态码 —— API 的"回应"

| 状态码 | 含义 | 场景 |
|--------|------|------|
| 200 | OK | 请求成功 |
| 201 | Created | 创建成功 |
| 400 | Bad Request | 请求格式错误 |
| 404 | Not Found | 资源不存在 |
| 500 | Internal Server Error | 服务器内部错误 |

---

#### 执行过程跟踪

```
# --- 执行过程 ---
# 1. 客户端发送 GET /users/123
# 2. 服务器接收请求,解析 URL 和方法
# 3. 服务器查询数据库 WHERE id = 123
# 4. 找到用户 → 返回 200 + JSON
#   找不到   → 返回 404
```

---

#### 常见错误

> 1. **错误现象**:用 GET 删除资源
>    **原因:**GET 应该是安全的(不修改数据)。修正:用 DELETE
> 2. **错误现象**:所有响应都返回 200
>    **原因:**错误的状态码让调用方无法判断问题。修正:用正确的状态码

---

#### 学员代码区

用 Postman 或 curl 发一个 GET 请求:

```bash
# TODO:用 curl 请求 https://jsonplaceholder.typicode.com/users
# TODO:请求 https://jsonplaceholder.typicode.com/users/1
# TODO:观察返回的状态码和 JSON 结构
```

---

#### 参考答案

```bash
curl https://jsonplaceholder.typicode.com/users
curl https://jsonplaceholder.typicode.com/users/1
# 状态码:200,JSON 结构:[{"id":1,"name":"Leanne Graham",...}]
```

---

## 明日衔接

- 明天 Day 02 学什么:**API 设计**(资源命名 + 版本控制 + 错误处理)
- 今天遗留的概念:今天学了 REST 基础,但还没学如何设计一个完整的 API
- NCDL 反模式预告:Day 2 展示"用 GET 删除资源"的反模式
