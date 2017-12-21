import requests
from bs4 import BeautifulSoup

headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)',
        'Accept': 'text/plain, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Cookie': 'bdshare_firstime=1456041345958; Hm_lvt_a077b6b44aeefe3829d03416d9cb4ec3=1456041346; Hm_lpvt_a077b6b44aeefe3829d03416d9cb4ec3=1456048504'
    }
# https://movie.douban.com/top250?start=0&filter=
str_url = "https://movie.douban.com/top250?start="
for count in range(0, 250, 25):
    url = str_url + str(count) + "&filter="
    movie_html = requests.get(url, headers=headers).text
    obj = BeautifulSoup(movie_html, 'lxml')
    soup = obj.find_all("div", {"class":"item"})
    for movie_div in soup:
        movie_title = movie_div.find("span", {"class":"title"}).text
        movie_num = movie_div.find("span", {"class":"rating_num"}).text
        movie_url = movie_div.find("a")
        print(movie_title, "评分：" + movie_num, "豆瓣地址：" + movie_url["href"])
print("结束！")

