import re
import requests

temp = 'http://caodan.org/'
count = 1
for i in range(1, 1519):
    url = temp + str(i) + '-photo.html'
    print(url)
    page = requests.get(url).text
    reg = re.compile('src="(http://.*?\.jpg)"')
    img_url = re.findall(reg, page)
    if img_url != []:
        with open('E:/img/%s.jpg' % count, 'wb') as file:
            img_data = requests.get(img_url[0]).content
            file.write(img_data)
            count += 1
    else:
        continue
print('完了没了')