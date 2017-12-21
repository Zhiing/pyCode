import requests
import json
import re
import time

url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=3495093613&containerid=1076033495093613&page='
headers = {
        'Referer': 'http://m.weibo.cn/u/3495093613',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'
}

def download(img_url):
    try:
        img_html = requests.get(img_url, headers=headers)
        print(img_url)
    except:
        print("请求图片出错,等待60秒。。。。", img_html.status_code)
        time.sleep(61)
        return
    file_name = img_url.split('/')[-1]
    if img_html.status_code == 200:
        with open('D:/weibo_/%s' % file_name, 'wb') as file:
            file.write(img_html.content)
            print('OK!!!', file_name)
    else:
        print(img_html.status_code, " 等待60？？？")
        time.sleep(60)
        return

for i in range(1, 10000):
    new_url = url + str(i)
    print(new_url, "   ", i)
    res = requests.get(new_url, headers=headers)
    if res.status_code == 200:
        res_json = json.loads(res.text)
        print(res_json)
        reg = re.compile("'url': '(http://w[\w]+\.sinaimg\.cn/large/[\w]+\.[jpgif]{3})")
        img_urls = re.findall(reg, str(res_json))
        if img_urls != []:
            for img_url in img_urls:
                download(img_url)
        else:
            time.sleep(60)
            print("等待60。。。", res.status_code)
            i -= 1
            continue
    else:
        print("等待60！！！")
        time.sleep(60)
        continue