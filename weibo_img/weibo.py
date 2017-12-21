import requests
import json
import re
import time

# url = 'http://m.weibo.cn/container/getIndex?type=uid&value=2818688452&containerid=1076032818688452&page='
url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=5118612601&containerid=1076035118612601&page='
headers = {
        'Referer': 'http://m.weibo.cn/u/5118612601',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'
}

# http://m.weibo.cn/container/getIndex?type=uid&value={userid}&containerid=107603{userid}&page={page}
# http://m.weibo.cn/container/getIndex?type=uid&value=3941136922&containerid=1076033941136922&page=

def download(img_url):
    #time.sleep(0.5)
    try:
        print(img_url)
        img_html = requests.get(img_url, headers=headers)
    except:
        print("请求图片出错", img_html.status_code)
        return
    file_name = img_url.split('/')[-1]
    if img_html.status_code == 200:
        with open('E:/weibo_5118612601/%s' % file_name, 'wb') as file:
            file.write(img_html.content)
            print('OK!!!', file_name)
    else:
        print([img_html.url], "被抓！！！等待60秒")
        time.sleep(60)
        return

for i in range(1, 1000):
    new_url = url + str(i)
    print(new_url, "   ", i)
    #time.sleep(1.1)
    res = requests.get(new_url, headers=headers)
    if res.status_code == 200:
        res_json = json.loads(res.text)
        #rint(res_json)
        reg = re.compile("'url': '(https://w\w+.sinaimg.cn/large/\w+.[jpgif]{3})")
        img_urls = re.findall(reg, str(res_json))
        if img_urls != []:
            for img_url in img_urls:
                #print(img_url)
                download(img_url)
        else:
            time.sleep(60)
            print("被抓！等待60秒。。。。。。。。。。")
            i -= 1
            continue
    else:
        print("结束！")
        break