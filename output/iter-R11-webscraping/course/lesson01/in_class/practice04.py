"""
[难度: ★★]
[所属知识点: CSS 选择器入门]
[预计完成时间: 10 分钟]

题目:用 CSS 选择器提取所有价格( class="price_color" 的 <p> 标签)。

提示:用 soup.select("p.price_color") 或 soup.find_all("p", class_="price_color")
"""

if __name__ == "__main__":
    print("参考答案:")
    print("  prices = soup.find_all('p', class_='price_color')")
    print("  for price in prices[:5]:")
    print("      print('价格:', price.text)")
