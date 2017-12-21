import re
import json
import requests
from bs4 import BeautifulSoup


#下载图片
def download(imgurl):
    global count
    print(imgurl)
    img_html = requests.get(imgurl, headers=headers)
    if img_html.status_code == 200:
        with open('E:/各站图片_大包/bcy_net_JK_半次元/%s.jpg' % count, 'wb') as file:
            file.write(img_html.content)
            print('OK!!!', count)
            count += 1

#  获取主页 jk 图片辑的 id
def page_posr(res_json):
    reg = re.compile("'ud_id': ([\w]{6})")
    page_id = re.findall(reg, str(res_json))
    for id in page_id:
        img_urls = str('http://bcy.net/daily/detail/' + id)
        html = requests.get(img_urls, headers=headers).text
        obj = BeautifulSoup(html, 'lxml')
        soup = obj.find_all("img", {"class": "detail_std detail_clickable"})
        for imgurl in soup:
            imgurl = imgurl["src"]
            imgurl = imgurl.replace('/w650', '')
            #img_name = imgurl.split('/')[-1]
            download(imgurl)

#  获取主页 json
def page_url(url):
    for i in range(19500, 30000):
        data_str['since'] = str(i)+'.999'
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   ", i)
        resp = requests.post(url, data=data_str).text
        res_json = json.loads(resp)
        page_posr(res_json)

#  程序开始 传入url data信息
if __name__ == "__main__":
    count = 1
    url = 'http://bcy.net/tags/hot/load'
    data_str = {'tag_id': '492'}
    headers = {'X-Requested-With': 'XMLHttpRequest',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'}
    page_url(url)