import re
import requests

url = 'http://wufazhuce.com/one/'
# imgurl = 'http://image.wufazhuce.com/Fp7L1MIqpBJyGRjbvFulSmjnmPB8'
count = 506

def size(newurl):
    html = requests.get(newurl, headers=headers)
    html_codes =html.status_code
    print(newurl, ';', html_codes)
    return html_codes

def data(newurl):
    page = requests.get(newurl, headers=headers).text
    reg = re.compile('img src="(.*?)" alt=""')
    img_url = re.findall(reg, page)
    print(img_url, count)
    if img_url != []:
        with open('E:/imgs/%s.jpg' % count, 'wb') as file:
            img_data = requests.get(img_url[0]).content
            file.write(img_data)
    else:
        print("无法找到图片")

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
        'Accept': 'text/plain, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Cookie': 'bdshare_firstime=1456041345958; Hm_lvt_a077b6b44aeefe3829d03416d9cb4ec3=1456041346; Hm_lpvt_a077b6b44aeefe3829d03416d9cb4ec3=1456048504',
    }
    while(count<=1700):
        newurl = url + str(count)
        if(size(newurl)==200):
            data(newurl)
            count +=1
        else:
            count +=1
    print("完成！")