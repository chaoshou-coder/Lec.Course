"""
[难度: ★★★]
[所属知识点: 综合提取]
[预计完成时间: 15 分钟]

题目:提取 books.toscrape.com 中前 3 本书的完整信息(书名 + 价格 + 评分)。

提示:
- 每本书在 <article class="product_pod"> 中
- 书名在 <h3><a title="..."> 中
- 价格在 <p class="price_color"> 中
- 评分在 <p class="star-rating Three"> 中(Three 是星级)
"""

if __name__ == "__main__":
    print("参考答案:")
    print("  books = soup.find_all('article', class_='product_pod')")
    print("  for book in books[:3]:")
    print("      title = book.h3.a['title']")
    print("      price = book.find('p', class_='price_color').text")
    print("      rating = book.p['class'][1]  # ['star-rating', 'Three']")
    print("      print(f'{title} | {price} | {rating}')")
