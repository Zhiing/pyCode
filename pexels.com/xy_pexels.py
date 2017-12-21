import re
import requests
import time

#  https://www.pexels.com/search/clouds/?page=5&seed=2017-04-14+15%3A07%3A19++0000&format=js&seed=2017-04-14%2015:07:19%20+0000
#  海 https://www.pexels.com/search/sea/  夕阳  https://www.pexels.com/search/sunset/  绿色  https://www.pexels.com/search/nature%20wallpaper/
#  https://images.pexels.com/photos/\d+/.+[jpeg].+
headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)'
}
url_01 = "https://www.pexels.com/search/clouds/?page="
url_02 = "&seed=2017-04-14+15%3A07%3A19++0000&format=js&seed=2017-04-14%2015:07:19%20+0000"
# src=\"https://images.pexels.com/photos/36717/amazing-animal-beautiful-beautifull.jpg?h=350&amp;auto=compress&amp;cs=tinysrgb\"
count = 1

def download(img_url):
    global count
    print(img_url)
    try:
        img_html = requests.get(img_url, headers=headers)
        if img_html.status_code == 200:
            with open('E:/clouds/%s.jpeg' % count, 'wb') as file:
                file.write(img_html.content)
                print('OK!!!', count)
                count += 1
        else:
            print("被抓！！！")
    except:
        print("等待")
        time.sleep(300)
        return

for i in range(1, 1000):
    new_url = url_01 + str(i) + url_02
    print("正在请求：  ", new_url)
    try:
        html = requests.get(new_url, headers=headers).text
        imgs = re.findall('src=.{2}(https:\/\/images\.pexels\.com\/photos\/\d+\/[\w\-]+\.[jpeg]{3,4})', html)
        if imgs != []:
            for img in imgs:
                download(img)
    except:
        print("等待")
        time.sleep(300)
        continue