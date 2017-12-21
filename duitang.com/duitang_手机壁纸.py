import requests
import re
import time

url = "https://www.duitang.com/napi/blog/list/by_filter_id/?include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Csender%2Calbum&filter_id=%E6%97%B6%E5%B0%9A%E6%90%AD%E9%85%8D&start="
headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)'
}

def download(img_url):
    print(img_url)
    time.sleep(0.55)
    html = requests.get(img_url, headers=headers)
    file_name = img_url.split('/')[-1]
    if html.status_code == 200:
        with open('E:/image/%s' % file_name, 'wb') as file:
            file.write(html.content)
            #count += 1
            print('OK!!!', file_name)
    else:
        print("被抓！！！")

for url_x in range(1, 10000, 24):
    url_y = 1490589965129
    new_url = url + str(url_x) + '&_=' + str(url_y)
    print(new_url, url_y)
    url_y += 1
    html = requests.get(new_url, headers=headers).text
    reg = re.compile('https:\/\/a-ssl\.duitang\.com\/uploads\/item\/\d*\/\d*\/\w*\.jpeg')
    img_url = re.findall(reg, html)
    for img in img_url:
        download(img)