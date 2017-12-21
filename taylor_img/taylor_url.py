# coding:utf-8
import requests
from bs4 import BeautifulSoup

# http://taylorpictures.net/albums/photoshoots/
headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)',
        'Accept': 'text/plain, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Cookie': 'bdshare_firstime=1456041345958; Hm_lvt_a077b6b44aeefe3829d03416d9cb4ec3=1456041346; Hm_lpvt_a077b6b44aeefe3829d03416d9cb4ec3=1456048504',
    }

#  下载图片
def download_url(img_url):
    print(img_url)

#  判断图片
def url_if(new_url):
    thumb_ = "thumb_"
    if (new_url[-3:]) == "jpg":
        if thumb_ not in new_url:
            download_url(new_url)
    else:
        return new_url

#  寻找图片链接
def new_url():
    url = "http://taylorpictures.net/albums/photoshoots/"
    url_str = ""

    ts_url = requests.get(url + url_str, headers=headers)
    soup = BeautifulSoup(ts_url.text, "lxml")
    soup = soup.find_all("a")
    for ts_str in soup:
        new_url = url + ts_str.text.replace(' ', '')
        url_if(new_url)

new_url()
