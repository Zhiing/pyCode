import time
import requests
from bs4 import BeautifulSoup

# http://www.meizitu.com/a/5519.html
count = 6987
headers = {
        #'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        #'Accept-Encoding':'gzip, deflate, sdch',
        #'Accept-Language':'zh-CN,zh;q=0.8',
        #'Cache-Control':'max-age=0',
        #'Host': 'mm.howkuai.com',
        #'If-Modified-Since': 'Mon, 10 Apr 2017 23:56:22 GMT',
        #'Proxy-Connection': 'keep-alive',
        'Referer': 'http://www.meizitu.com/a/',
        #'Upgrade-Insecure-Requests': 1,
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
}

def download(img_url):
    global count
    print(img_url)
    try:
        img_html = requests.get(img_url, headers=headers)
        if img_html.status_code == 200:
            with open('E:/mzitu/%s.jpg' % count, 'wb') as file:
                file.write(img_html.content)
                print('OK!!!', count)
                count += 1
        else:
            print("被抓！！！", img_html.status_code)
            time.sleep(10)
            return
    except:
        print("等待")
        time.sleep(61)
        return

for i in range(4581, 6000):
    url = "http://www.meizitu.com/a/" + str(i) + ".html"
    print(url, "  正在请求 =》 ", i)
    try:
        html = requests.get(url, headers=headers)
        if html.status_code == 200:
            obj = BeautifulSoup(html.text, 'lxml')
            for p_url in obj.find_all("div", {"id": "picture"}):
                for img_url in p_url.find_all("img"):
                    img = img_url["src"]
                    download(img)
        else:
            print("空的出错====等待》", html.status_code)
            time.sleep(3)
            continue
    except:
        print("等待!被抓！")
        time.sleep(120)
        continue