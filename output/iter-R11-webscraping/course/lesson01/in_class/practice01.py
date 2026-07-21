"""
[难度: ★]
[所属知识点: requests 基础]
[预计完成时间: 5 分钟]

题目:补全下面的代码,获取 https://books.toscrape.com/ 的 HTML 源码。

要求:
1. 导入 requests 库
2. 发送 GET 请求
3. 打印状态码(应该是 200)
4. 打印 HTML 源码长度
"""

# 学员代码区
# 在这里写出你的代码:


# 测试区
if __name__ == "__main__":
    print("参考答案:")
    print("  import requests")
    print("  url = 'https://books.toscrape.com/'")
    print("  response = requests.get(url)")
    print("  print('状态码:', response.status_code)  # 200")
    print("  print('内容长度:', len(response.text))")
