### Day 01 · Docker 基础与第一个容器

> **痛点**:你听说 Docker 是必备技能,但面对命令行就慌。网上教程一上来就讲架构原理,你只想知道"怎么开始用"。今天你将运行人生第一个容器 —— 从零开始,不废话。
> **类比**:Docker 就像"集装箱" —— 镜像 = 集装箱的设计图纸,容器 = 实际运行的集装箱,仓库 = 存放图纸的码头。
> **解释**:**Docker = 容器化平台**。今天学:装好 → 运行第一个容器 → 理解镜像/容器关系。

---

#### 运行你的第一个容器

```bash
# 在终端执行(Day 1 就跑通)

# 1. 检查 Docker 是否安装
docker --version

# 2. 运行 hello-world(验证安装)
docker run hello-world

# 3. 运行一个交互式 Ubuntu 容器
docker run -it ubuntu:22.04 bash

# 在容器内执行
cat /etc/os-release  # 查看系统版本
ls                   # 列出文件
exit                 # 退出容器

# 4. 查看正在运行的容器
docker ps
docker ps -a  # 包括已停止的

# 5. 查看本地镜像
docker images
```

**逐行解剖**

- `docker run hello-world` = 运行 hello-world 镜像,验证安装
- `docker run -it ubuntu:22.04 bash` = 运行 Ubuntu 容器并进入交互式 shell
- `docker ps` = 查看运行中的容器
- `docker images` = 查看本地镜像列表

> **ASCII 容器生命周期**
> ```
> 镜像(ubuntu:22.04) ──run──▶ 容器(运行中) ──stop──▶ 容器(已停止) ──rm──▶ 删除
> ```

**常见错误**

> 1. **错误现象**:`Cannot connect to the Docker daemon`
>    **原因:**Docker Desktop 没启动。修正:启动 Docker Desktop
> 2. **错误现象**:`docker: command not found`
>    **原因:**Docker 没安装。修正:安装 Docker Desktop

---

#### 执行过程跟踪

```bash
# --- 执行过程 ---
# $ docker run hello-world
#   ① 检查本地是否有 hello-world 镜像
#   ② 没有 → 从 Docker Hub 拉取
#   ③ 运行容器 → 打印 Hello from Docker!
#   ④ 容器自动停止
```

---

#### 学员代码区

```bash
# TODO: 运行 hello-world
# TODO: 运行 nginx 容器(docker run -d -p 8080:80 nginx)
# TODO: 访问 http://localhost:8080 查看 nginx 欢迎页
# TODO: 查看运行中的容器
# TODO: 停止并删除容器
```

---

#### 参考答案

```bash
docker run hello-world
docker run -d -p 8080:80 nginx
docker ps
docker stop <container_id>
docker rm <container_id>
```

---

## 明日衔接

- 明天 Day 02 学什么:**构建镜像与 Dockerfile**
- 今天遗留的概念:今天只学了运行别人的镜像,还没学如何构建自己的镜像
- NCDL 反模式预告:Day 2 展示"COPY 路径错误/依赖缺失"的反模式
