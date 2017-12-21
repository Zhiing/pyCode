# coding:utf-8
import threading
import requests

headers = {'X-Requested-With': 'XMLHttpRequest',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/56.0.2924.87 Safari/537.36'}

# 新线程执行的代码:
def loop():
    for i in range(1, 1000):
        html = requests.get("http://127.0.0.1:8000/blog/index/", threading.current_thread().name)
        print(html.status_code, i)
        #print(html.text)

print('thread %s is running...' % threading.current_thread().name)
t1 = threading.Thread(target=loop, name='LoopThread1')
t2 = threading.Thread(target=loop, name='LoopThread2')
t3 = threading.Thread(target=loop, name='LoopThread3')
t4 = threading.Thread(target=loop, name='LoopThread4')
t5 = threading.Thread(target=loop, name='LoopThread5')
t6 = threading.Thread(target=loop, name='LoopThread6')
t7 = threading.Thread(target=loop, name='LoopThread7')
t8 = threading.Thread(target=loop, name='LoopThread8')
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()