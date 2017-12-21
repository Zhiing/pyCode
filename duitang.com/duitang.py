import requests
import re

url = "https://www.duitang.com/napi/blog/list/by_search/?kw=taylor+swift&type=feed&include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Csender%2Calbum&_type=&start="
headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)'
}

def download(img_url):
    print(img_url)
    html = requests.get(img_url, headers=headers)
    file_name = img_url.split('/')[-1]
    if html.status_code == 200:
        with open('E:/imge/%s.jpeg' % file_name, 'wb') as file:
            file.write(html.content)
            print('OK!!!', file_name)
    else:
        print("被抓！！！")

for url_x in range(2616, 10000, 24):
    url_y = 1490507534726
    new_url = url + str(url_x) + '&_=' + str(url_y)
    print(new_url)
    html = requests.get(new_url, headers=headers).text
    reg = re.compile('https:\/\/a-ssl\.duitang\.com\/uploads\/item\/[\d]*\/[\d]*\/[\d]*_[\w]*\.jpeg')
    img_url = re.findall(reg, html)
    for img in img_url:
        download(img)
        url_y += 1