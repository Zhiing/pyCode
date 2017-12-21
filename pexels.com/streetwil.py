import requests
from bs4 import BeautifulSoup

#  "http://streetwill.co/posts?_=1490438645306&page=1&type=recent"
#url = "http://streetwill.co/posts?_=1490438645306&page=1&type=recent"
headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)'
}
for count in range(1, 15):
    new_url = 'http://streetwill.co/posts?_=1490438645306&page=' + str(count) + '&type=recent'
    img_html = requests.get(new_url, headers=headers)
    #print(img_html)
    soup = BeautifulSoup(img_html.text, 'lxml')
    img_soup = soup.find_all("a", {"class":"download-button svg"})
    for Dld in img_soup:
        img_url ='http://streetwill.co' + Dld['href']
        print(img_url)
        headers['Referer'] = img_url[:-9]
        img = requests.get(img_url, headers=headers)
        file_name = img_url.split('/')[-2]
        with open('E:/img/%s.jpg' % file_name, 'wb') as file:
            file.write(img.content)
            print('OK!!!', file_name)