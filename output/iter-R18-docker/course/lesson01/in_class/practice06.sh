# [难度: ★★★][所属知识点: 挑战题][预计完成时间: 15 分钟]
# 题目:下面命令有什么问题?如何修正?
# docker run -it ubuntu:22.04
# docker run -it ubuntu:22.04(再次运行,容器名冲突)
# 问题:没有 --rm 参数,停止后容器还在;没有 --name,自动命名可能冲突
# 修正:docker run -it --rm ubuntu:22.04
