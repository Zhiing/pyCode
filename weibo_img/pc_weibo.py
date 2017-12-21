import re
import json
import requests

# http://weibo.com/p/aj/album/loading?ajwvr=6&type=photo&owner_uid=2818688452&viewer_uid=&since_id=4083835759586537_4034496099635506_20170322_-1&page_id=1005052818688452&page=3&ajax_call=1&__rnd=1490714983769
url = 'http://weibo.com/p/aj/album/loading?ajwvr=6&type=photo&owner_uid=2818688452&viewer_uid=&since_id=4083835759586537_4034496099635506_20170322_-1&page_id=1005052818688452&page='
headers = {
        'Cookie':'_s_tentry=www.liaoxuefeng.com; Apache=9883927661317.031.1490258919014; SINAGLOBAL=9883927661317.031.1490258919014; ULV=1490258919423:1:1:1:9883927661317.031.1490258919014:; YF-Page-G0=074bd03ae4e08433ef66c71c2777fd84; YF-V5-G0=c6a30e994399473c262710a904cc33c5; login_sid_t=d9532d068307de384e9af6424056b118; YF-Ugrow-G0=ad06784f6deda07eea88e095402e4243; SSOLoginState=1490593394; un=18397827323; wvr=6; _T_WM=9e15fa7481455e7ac7e4e576d5a2ecbc; SCF=AqvzVdCt-lVwbmBCV1QpFw1VahzdpY7B74V6dicdjUNoVVNOQjZqPhvgwRRy4lpZ-tfpZ1aYAMCw3ejhrFgN59I.; SUB=_2A2513lEiDeRxGeNI6VcT9SrFyDuIHXVWqsXqrDV8PUJbmtANLUrekW8XF_ejtIHB-0OLEL3qTxEI1g1Lkw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWLWIWHDA6Z6bH5lN2-Ga005JpX5o2p5NHD95QfSozfeo-X1KeNWs4Dqc_zi--ciK.4i-iWi--fi-i8i-zNi--NiKy8iKLFi--ciK.Ni-27i--Ri-2fi-isi--Xi-iWiKLWi--ciKn0iKnfi--4iKLWiKLh; SUHB=0wn1kKJNs2TrB7; ALF=1522129394; UOR=www.liaoxuefeng.com,widget.weibo.com,www.liaoxuefeng.com; WBStorage=02e13baf68409715|undefined',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
}

for i in range(1, 1000):
    new_url = url +str(i) + '&ajax_call=1&__rnd=1490714983769'
    url_reqs = requests.get(new_url, headers=headers)
    url_json = json.loads(url_reqs.text)
    print(url_json)
    exit()