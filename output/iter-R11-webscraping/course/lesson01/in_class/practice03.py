"""
[难度: ★★]
[所属知识点: 提取多个元素]
[预计完成时间: 10 分钟]

题目:提取 books.toscrape.com 页面中前 5 个书名。

提示:书名在 <h3> 标签内的 <a> 标签的 title 属性中。
"""

if __name__ == "__main__":
    print("参考答案:")
    print("  books = soup.find_all('h3')")
    print("  for book in books[:5]:")
    print("      book_title = book.find('a')['title']")
    print("      print('书名:', book_title)")
