### Day 01 · SQL 基础查询

> **痛点**:你用 ORM 做 CRUD,但遇到复杂查询就傻眼。SQL 是"告诉数据库你要什么,而不是怎么做"。今天你将写出人生第一个 SQL 查询。
> **类比**:SQL 就像"Excel 筛选 + 透视表" —— SELECT = 选列,WHERE = 筛选行,ORDER BY = 排序。
> **解释**:**SQL = 结构化查询语言**,声明式语言。今天学:SELECT/WHERE/ORDER BY。

```sql
-- 你的第一个 SQL 查询(在 PostgreSQL 终端执行)

-- 1. 查看所有数据库
\l

-- 2. 连接数据库
\c your_database

-- 3. 查看所有表
\dt

-- 4. 查询所有列
SELECT * FROM users;

-- 5. 查询指定列
SELECT name, email FROM users;

-- 6. 带条件查询
SELECT name, email FROM users WHERE age > 25;

-- 7. 排序
SELECT name, age FROM users ORDER BY age DESC;

-- 8. 限制结果数
SELECT name, age FROM users ORDER BY age DESC LIMIT 10;
```

**逐行解剖**

- `SELECT * FROM users` = 查询 users 表的所有列
- `SELECT name, email` = 只查询 name 和 email 列
- `WHERE age > 25` = 筛选条件(只返回 age > 25 的行)
- `ORDER BY age DESC` = 按 age 降序排列
- `LIMIT 10` = 只返回前 10 行

> **ASCII 查询执行顺序**
> ```
> FROM users → WHERE age > 25 → SELECT name, email → ORDER BY age DESC → LIMIT 10
> ```

**常见错误**

> 1. **错误现象**:`ERROR: relation "users" does not exist`
>    **原因:**表名写错或没连接数据库。修正:\dt 查看表名
> 2. **错误现象**:SQL 语句末尾忘写分号
>    **原因:**SQL 用分号表示语句结束。修正:加 ;

---

#### 执行过程跟踪

```sql
-- --- 执行过程 ---
-- SELECT name, email FROM users WHERE age > 25 ORDER BY age DESC LIMIT 10:
--   ① FROM users:从 users 表读取数据
--   ② WHERE age > 25:过滤出 age > 25 的行
--   ③ SELECT name, email:只保留 name 和 email 列
--   ④ ORDER BY age DESC:按 age 降序排列
--   ⑤ LIMIT 10:只返回前 10 行
```

---

#### 学员代码区

```sql
-- TODO: 查询 products 表的所有列
-- TODO: 查询 name 和 price 列
-- TODO: 查询 price > 100 的产品
-- TODO: 按 price 降序排列,取前 5 个
```

---

#### 参考答案

```sql
SELECT * FROM products;
SELECT name, price FROM products;
SELECT name, price FROM products WHERE price > 100;
SELECT name, price FROM products ORDER BY price DESC LIMIT 5;
```

---

## 明日衔接

- 明天 Day 02 学什么:**多表 JOIN**(INNER/LEFT/RIGHT)
- 今天遗留的概念:今天只学了单表查询,还没学多表关联
- 脚手架递进预告:Day 2 在 Day 1 基础上关联多表
