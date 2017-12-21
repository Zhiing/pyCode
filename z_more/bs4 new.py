from bs4 import BeautifulSoup
import requests

url = 'http://www.weddinginspirasi.com/category/western-wedding-dresses-dress-bridal-gowns/'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
print('获取所有的图片链接:')
links = soup.find_all('img')
for link in links:
    print(link.name, link['src'], link.get_text())