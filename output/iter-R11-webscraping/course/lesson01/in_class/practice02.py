"""
[难度: ★]
[所属知识点: BeautifulSoup 解析]
[预计完成时间: 5 分钟]

题目:补全下面的代码,用 BeautifulSoup 解析 HTML 并提取 <h1> 标签的文本。
"""

if __name__ == "__main__":
    print("参考答案:")
    print("  from bs4 import BeautifulSoup")
    print("  soup = BeautifulSoup(response.text, 'html.parser')")
    print("  title = soup.find('h1').text")
    print("  print('页面标题:', title)")
