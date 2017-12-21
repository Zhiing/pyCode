import re
import requests

# <a href="//wallpaperscraft.com/wallpaper/mountains_sky_clouds_mountain_range_stones_99500" title="" target="_blanck">
url_0 = 'https://wallpaperscraft.com/catalog/nature/3840x2160/page2'
def no0():
    k = 2
    while(k<49):
        url = url_0 + str(k)
        no1(url)
        k +=1

def no1(url):
    count = 1
    page = requests.get(url).text
    reg = re.compile('a href="(.*?)" title="" target="_blanck"')
    img_url = re.findall(reg, page)
    for i in img_url:
        newurl = 'https:' + i
        #print(newurl)
        with open('F:/img/%s.jpg' % count, 'wb') as file:
            img_data = requests.get(no2(newurl)).content
            file.write(img_data)
        count +=1

def no2(newurl):
    page_0 = requests.get(newurl).text
    reg_0 = re.compile('src="(//.*?\.jpg)"')
    img_url_0 = re.findall(reg_0, page_0)
    if len(img_url_0[0]) != 0:
        img_url_1 = 'https:' + str(img_url_0[0])
        print(img_url_1)
        return img_url_1
no0()