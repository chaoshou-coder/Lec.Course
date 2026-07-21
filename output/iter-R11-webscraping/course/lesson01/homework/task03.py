"""
[难度: ★★★★]
[所属知识点: 综合爬虫]
[预计完成时间: 30 分钟]
[类型: 选做]

题目:编写一个完整的爬虫,抓取 books.toscrape.com 首页的所有书名和价格,打印出来。

要求:
1. 用 requests 获取网页
2. 用 BeautifulSoup 解析
3. 提取书名(<h3><a title="...">) 和价格(<p class="price_color">)
4. 打印格式:书名 | 价格
"""

if __name__ == "__main__":
    print("参考答案:")
    print("  import requests")
    print("  from bs4 import BeautifulSoup")
    print("  url = 'https://books.toscrape.com/'")
    print("  response = requests.get(url)")
    print("  soup = BeautifulSoup(response.text, 'html.parser')")
    print("  books = soup.find_all('article', class_='product_pod')")
    print("  for book in books:")
    print("      title = book.h3.a['title']")
    print("      price = book.find('p', class_='price_color').text")
    print("      print(f'{title} | {price}')")
