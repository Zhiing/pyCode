import re
import pymongo
import requests

from config import *
from requests.exceptions import ChunkedEncodingError
from urllib.parse import urlencode
from bs4 import BeautifulSoup
from multiprocessing import Pool

client = pymongo.MongoClient(MONGO_URL, connect=False)
db = client[MONGO_DB]

base_url = 'https://movie.douban.com/tag/%E7%88%B1%E6%83%85?'  # 标签为爱情
proxy_pool_url = 'http://127.0.0.1:5000/get'
proxy = None
headers = {
    'User-Agent': 'xxxxxxxxxxxxxxxxxxxxxxx'
}

#  获取代理 ip
def get_proxy():
    try:
        response = requests.get(proxy_pool_url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except ConnectionError:
        return None


#  请求 网页 源代码
def get_html(url):
    global proxy
    try:
        if proxy:
            proxies = {
                'http': 'http://' + proxy
            }
            response = requests.get(url, headers=headers, allow_redirects=False, proxies=proxies)
        else:
            response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            return response.text
        else:
            print('被抓住！！！', response.status_code, url)
            #  被抓住 状态码 自定
            if response.status_code != 200:
                # need proxy
                proxy = get_proxy()
                if proxy:
                    print('Using Proxy :', proxy)
                    return get_html(url)
                else:
                    print('Get Proxy Failed !!!')
                    return None
            else:
                print('未知错误，调试', response.status_code, url)
                return None

    except ChunkedEncodingError as e:
        print('请求出错', e.args)
        proxy = get_proxy()
        return get_html(url)

#  构造 检索页 地址
def get_index(start):
    data = {
        'start': start,
        'type': 'T',
    }
    queries = urlencode(data)
    url = base_url + queries
    html = get_html(url)
    return html

#  解析 检索 页 返回 子页 链接
def parse_index(html):
    pattern = re.compile('nbg"\shref="(.*?)"')
    items = re.findall(pattern, html)
    return items

#  解析子页
def parse_page_html(html, url):
    new_dict = {}
    movie_id = url.split("/")[4]
    soup = BeautifulSoup(html, 'lxml')
    content = soup.find('div', id='info')
    info = str(content.text)
    info = info.split('\n')
    for item in info:
        if len(item.split(':')) == 2:
            new_dict["_id"] = movie_id
            new_dict["豆瓣地址"] = url
            new_dict[item.split(':')[0]] = item.split(':')[1]
    return new_dict

# 储存数据库
def save_to_mongo(result):
    if db[MONGO_TABLE].insert(result):
        print('储存成功!!', result)
        return True
    else:
        print('储存失败！! !', result)
    return False

#  调度 主函数
def main(page):
    html = get_index(page)
    page_url = parse_index(html)
    for url in page_url:
        page_html = get_html(url)
        parse_page = parse_page_html(page_html, url)  # 把这个字典存库
        if parse_page:
            save_to_mongo(parse_page)
        else:
            print('没有数据！')

if __name__ == '__main__':
    groups = [x*20 for x in range(GROUP_START, GROUP_END + 1)]
    pool = Pool()
    pool.map(main, groups)