# https://movie.douban.com/top250
import requests
from bs4 import BeautifulSoup

url = "https://movie.douban.com/top250?start="
headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)',
        'Accept': 'text/plain, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Cookie': 'bdshare_firstime=1456041345958; Hm_lvt_a077b6b44aeefe3829d03416d9cb4ec3=1456041346; Hm_lpvt_a077b6b44aeefe3829d03416d9cb4ec3=1456048504',
    }

for count in range(0, 225, 25):
    new_url = url + str(count) + "&filter="
    #print(new_url)
    html = requests.get(new_url, headers=headers)
    soup = BeautifulSoup(html.text, 'lxml')
    movie_url = soup.find_all("div", {"class":"item"})
    for new_movieurl in movie_url:
        print(new_movieurl.a["href"])
    print("=====")
