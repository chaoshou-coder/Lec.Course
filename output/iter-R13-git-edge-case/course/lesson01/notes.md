### Day 01 · Git 基础概念与初始化

> **痛点**:你听说 Git 是必备技能,但打开终端面对命令行就慌。网上教程一上来就讲 object model / SHA-1,你只想知道"怎么开始用"。今天你将完成第一次 Git 提交 —— 从零开始,不废话。
> **类比**:Git 就像"时间线存档" —— 每次 commit 是一个存档点,你可以随时回到过去。分支是"平行时间线",你在一条线上工作不影响另一条。
> **解释**:**Git = 分布式版本控制系统**。今天学:装好 → 初始化 → 第一次 commit。

---

#### Git 是什么 —— 时间线存档

> **痛点**:你手动备份代码(project_v1.zip / project_v2_final.zip),结果不知道哪个版本改了什么。
> **类比**:Git 就像游戏存档 —— 每次 commit 是一个存档点,你可以随时读档。不像手动备份,Git 记录了每次改了什么。
> **解释**:Git 跟踪文件的每次变化,而不是保存完整副本。你可以查看历史、回退版本、在多个分支上并行工作。

```bash
# 你的第一次 Git 操作(在终端执行)

# 1. 检查 Git 是否安装
git --version

# 2. 配置用户名和邮箱(只需一次)
git config --global user.name "你的名字"
git config --global user.email "你的邮箱@example.com"

# 3. 创建项目目录并进入
mkdir my-first-repo && cd my-first-repo

# 4. 初始化 Git 仓库
git init

# 5. 创建第一个文件
echo "# My First Project" > README.md

# 6. 查看状态
git status

# 7. 添加到暂存区
git add README.md

# 8. 提交
git commit -m "Initial commit: add README"

# 9. 查看提交历史
git log --oneline
```

**逐行解剖**

- `git --version` = 检查 Git 是否安装(输出 git version 2.x.x)
- `git config --global` = 全局配置(只需做一次)
- `git init` = 初始化仓库,创建 `.git` 目录
- `git status` = 查看当前状态(哪些文件改了/哪些在暂存区)
- `git add` = 把文件添加到暂存区(准备提交)
- `git commit -m "message"` = 创建提交,message 描述改了什么
- `git log --oneline` = 查看提交历史(简洁模式)

> **ASCII 工作流程图**
> ```
> 工作区(编辑文件) ──add──▶ 暂存区(准备提交) ──commit──▶ 本地仓库(存档)
>      │                         │                         │
>      ▼                         ▼                         ▼
>   README.md             暂存区(index)             commit abc123
> ```

**常见错误**

> 1. **错误现象**:`fatal: not a git repository`
>    **原因:**还没 `git init`。修正:先执行 `git init`
> 2. **错误现象**:`please tell me who you are`(commit 时报错)
>    **原因:**没配置 user.name/user.email。修正:`git config --global ...`
> 3. **错误现象**:`nothing to commit, working tree clean`
>    **原因:**没有新文件或文件没改。修正:编辑文件后再 add/commit

---

#### 第一次提交后的世界

> **痛点**:你完成了第一次 commit,但不知道"提交后发生了什么"。
> **类比**:commit 就像"存档" —— Git 给每个 commit 一个唯一 ID(SHA-1 哈希),你可以随时回到这个存档点。
> **解释**:每次 commit 是一个快照,snapshot,记录了当前所有文件的状态。Git 通过链表组织这些快照。

```bash
# 继续你的 Git 之旅

# 10. 修改文件
echo "Some changes" >> README.md

# 11. 查看改了什么(在工作区但未 add)
git diff

# 12. 再次 add + commit
git add README.md
git commit -m "Update README with description"

# 13. 查看完整历史
git log --oneline --graph
```

**逐行解剖**

- `git diff` = 查看工作区和暂存区的差异(改了什么)
- `git log --graph` = 图形化显示历史(分支时更有用)

**常见错误**

> 1. **错误现象**:改了文件但 `git status` 显示红色
>    **原因:**还没 `git add`。修正:`git add .` 添加所有改动
> 2. **错误现象**:commit message 写得很随意("update"/"fix")
>    **原因:**不好的 commit message 会让后期难以回溯。修正:用"动词 + 描述"格式

---

#### 执行过程跟踪

```bash
# --- 执行过程 ---
# $ git init
#   ① 在当前目录创建 .git 目录
#   ② .git 存储所有版本信息
#
# $ git add README.md
#   ① 把 README.md 添加到暂存区(index)
#   ② git status 显示绿色(已暂存)
#
# $ git commit -m "Initial commit"
#   ① 创建 commit 对象
#   ② 生成 SHA-1 哈希(如 abc123def...)
#   ③ 记录作者/时间/message
#   ④ HEAD 指针指向这个 commit
```

---

#### 常见错误

> 1. **错误现象**:`git add .` 添加了不该提交的文件(如 .DS_Store / node_modules)
>    **原因:**没有 .gitignore。修正:创建 .gitignore 文件,列出要忽略的文件
> 2. **错误现象**:忘了 `git add` 就直接 commit
>    **原因:**commit 只提交暂存区的内容。修正:先 add 再 commit

---

#### 学员代码区

在终端执行下面的命令(Day 1 就跑通第一次 commit):

```bash
# TODO: 检查 Git 版本
# TODO: 配置 user.name 和 user.email
# TODO: 创建目录 my-first-repo 并进入
# TODO: git init
# TODO: 创建 README.md
# TODO: git add + git commit( message = "Initial commit" )
# TODO: git log 查看历史
```

---

#### 参考答案

```bash
git --version
git config --global user.name "张三"
git config --global user.email "zhangsan@example.com"
mkdir my-first-repo && cd my-first-repo
git init
echo "# My First Project" > README.md
git add README.md
git commit -m "Initial commit: add README"
git log --oneline
```

---

## 明日衔接

- 明天 Day 02 学什么:**日常工作循环**(add/commit/status/diff/log)
- 今天遗留的概念:今天只学了 init + 第一次 commit,还没学日常工作
- 脚手架递进预告:
  - Day 1:init + 第一次 commit
  - Day 2:日常工作(重复 add/commit 循环)
  - Day 3:分支管理(NCDL 节点)
  - Day 4:合并冲突(NCDL 节点)
  - Day 5:GitHub 协作
