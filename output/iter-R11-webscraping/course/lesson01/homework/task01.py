"""
[难度: ★★★]
[所属知识点: 修复爬虫错误]
[预计完成时间: 15 分钟]
[类型: 选做]

题目:下面的爬虫代码运行时报错,找出 2 处错误并修正。

    import requests
    response = requests.get("https://books.toscrape.com/")
    print(response.text)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find("h1").text
    print(title)
"""

if __name__ == "__main__":
    print("2 处错误:")
    print("  1. 缺少 from bs4 import BeautifulSoup")
    print("  2. 代码能运行,但 find('h1') 可能返回 None(如果页面结构变化)")
    print("     修正:title = soup.find('h1').text if soup.find('h1') else '未找到'")
