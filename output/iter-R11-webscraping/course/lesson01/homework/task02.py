"""
[难度: ★★★]
[所属知识点: 提取复杂结构]
[预计完成时间: 20 分钟]
[类型: 选做]

题目:提取 books.toscrape.com 中所有书的"库存状态"(In stock / Out of stock)。

提示:库存状态在 <p class="instock availability"> 中。
"""

if __name__ == "__main__":
    print("参考答案:")
    print("  stocks = soup.find_all('p', class_='instock')")
    print("  for stock in stocks[:5]:")
    print("      print('库存:', stock.text.strip())")
