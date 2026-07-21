"""
[难度: ★★★]
[所属知识点: 综合(挑战题)]
[预计完成时间: 15 分钟]
[类型: 挑战题,不强制完成]

题目:下面代码有 3 处错误,找出来并修正。

    import requests
    from bs4 import BeautifulSoup

    url = "https://books.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html")

    title = soup.find("h1").text
    books = soup.find_all("h3")
    for book in books:
        print(book.find("a").text)  # 打印书名
        print(book.find("p").text)  # 打印价格

错误提示:解析器名称/提取方式/选择器
"""

if __name__ == "__main__":
    print("3 处错误:")
    print("  1. 'html' → 'html.parser'(解析器名称不对)")
    print("  2. book.find('a').text → book.find('a')['title'](text 是标签内文本,title 是属性)")
    print("  3. book.find('p') → 每本书没有 <p> 标签,价格在整个页面的其他位置")
