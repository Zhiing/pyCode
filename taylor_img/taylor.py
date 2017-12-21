#/usr/bin/python
# -*- coding: utf-8 -*-
import re
from io import BytesIO
from PIL import Image
import requests
from bs4 import BeautifulSoup

headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
def download_img(new_url):
    print(new_url)
    global str_count
    try:
        html = requests.get(new_url, headers=headers)
        img = Image.open(BytesIO(html.content))
        width, height = img.size
        if html.status_code == 200:
            if width and height >= 900:
                print(width, height, "图片合格！---------ok")
                with open('E:/img/%s.jpg' % str_count, 'wb') as file:
                    img_data = html.content
                    file.write(img_data)
                    print("成功下载！", str_count)
                    str_count += 1
        else:
            print("又怎么啦！001")
            return
    except:
        print('什么鬼？')
        return

def download_url(image_href):
    try:
        html = requests.get(image_href, headers=headers, allow_redirects=False)
        if html.status_code == 200:
            bsobj = BeautifulSoup(html.text, "lxml")
            for link in bsobj.findAll("img", {"class" "image"}):
                if "src" in link.attrs:
                    new_url = "http://taylorpictures.net/" + link.attrs["src"]
                    download_img(new_url.strip().replace('normal_', ''))
        else:
            print("无法获取图片地址")
    except:
        print("请求出错")
        return

def photo_url():
    for count in range(869, 3594):
        newurl = strurl + str(count)
        try:
            html = requests.get(newurl, headers=headers, allow_redirects=False)
            if html.status_code == 200:
                print(count, "===>>>  访问正常")
                bsobj = BeautifulSoup(html.text, "lxml")
                images = bsobj.findAll("a", {"href": re.compile("displayimage\.php\?album=[\w]*")})
                for image in images:
                    image_href = "http://taylorpictures.net/" + image["href"]
                    download_url(image_href)
            else:
                continue
        except:
            print("===>>>  访问错误")
            return
#count = 827
str_count = 5752 #命名
strurl = "http://taylorpictures.net/thumbnails.php?album="
photo_url()