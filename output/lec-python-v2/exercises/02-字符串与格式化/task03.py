"""
[难度: ★★★]
[所属知识点: find + 切片(URL 解析)]
[预计完成时间: 15 分钟]
[类型: 选做]

题目描述:
  给定 URL: url = "https://www.example.com/search?q=python"
  提取并打印:
  1. 协议 (https)
  2. 域名 (www.example.com)
  3. 路径 (/search?q=python)

  提示:
  - 用 find("://") 找协议结束位置
  - 用 find("/") 找域名结束位置
  - 用切片提取各部分

示例:
    输出:
      协议: https
      域名: www.example.com
      路径: /search?q=python
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    url = "https://www.example.com/search?q=python"

    # 提取协议
    proto_end = url.find("://")
    protocol = url[:proto_end]

    # 提取域名
    rest = url[proto_end + 3:]        # www.example.com/search?q=python
    slash = rest.find("/")
    host = rest[:slash]
    path = rest[slash:]

    print("协议:", protocol)
    print("域名:", host)
    print("路径:", path)
