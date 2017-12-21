# coding:utf-8
#  https://static.pexels.com/photos/57768/pexels-photo-57768.jpeg
import time
import requests

headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)'
}
for i in range(51154, 100000):
    new_url = "https://static.pexels.com/photos/" + str(i) + "/pexels-photo-" + str(i) + ".jpeg"
    try:
        print(new_url, "正在下载。。。", i)
        html = requests.get(new_url, headers=headers)
        if html.status_code == 200:
            with open('E:/pexels/%s.jpeg' % i, 'wb') as file:
                file.write(html.content)
                print(i, "下载成功！")
        else:
            print("请求出错！")
    except:
        print("被抓！等待300s")
        time.sleep(300)
        continue