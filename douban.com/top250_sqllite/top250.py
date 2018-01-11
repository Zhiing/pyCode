import sqlite3
import requests
import json
import time


# 创建数据库 表格
def create_table():
    pass
    # ----------------------------------------------
    # movie_id          电影ID
    # title             电影名称
    # original_title    原名
    # alt               豆瓣地址
    # rating            评分
    # year              上映年份
    # collect_count     评价人数
    # genres            类型
    # images            电影封面

    # directors 导演
    # casts     演员
    # ----------------------------------------------
    # conn = sqlite3.connect('top.db')
    # c = conn.cursor()
    # print('DATABASE OPEN OK')
    # c.execute('''CREATE TABLE Top250Movie(
    #             movie_id INT PRIMARY KEY NOT NULL ,
    #             title VARCHAR,
    #             original_title VARCHAR,
    #             alt VARCHAR,
    #             rating FLOAT,
    #             year INT,
    #             collect_count INT,
    #             genres VARCHAR,
    #             images VARCHAR,
    #             directors VARCHAR,
    #             casts VARCHAR
    #           )''')
    # c.execute('''CREATE TABLE Top250People(
    #             pp_id INT PRIMARY KEY NOT NULL ,
    #             pp_name VARCHAR,
    #             pp_alt VARCHAR,
    #             pp_avatars VARCHAR
    #           )''')
    # print('OK')
    # conn.commit()
    # conn.close()


# 储存数据库
def insert_db(insert_str):
    # print(insert_str)
    conn = sqlite3.connect('top.db')
    c = conn.cursor()
    # print('DATABASE OPEN OK')
    try:
        c.execute(insert_str)

        print('INSERT OK', insert_str)
        conn.commit()
        conn.close()
    except:
    	# 出错基本上都是 一个演员演了多部电影
    	# 演员ID 为 主键 
    	# 所以就直接跳过 抬走 下一位
        conn.close()
        print('---------------------------------------INSERT Error')
        return


# 拼接字符串 演员表
def read_people(people_list):
    return_str = ''
    for people_item in people_list:
        pp_id = people_item['id']
        pp_name = people_item['name']
        pp_alt = people_item['alt']
        try:
            pp_avatars = people_item['avatars']['small']
        except:
            pp_avatars = None
        return_str = return_str + str(pp_id) + '/'
        # 拼接字符串 储存数据库
        insert_str = 'INSERT INTO Top250People (pp_id,pp_name,pp_alt,pp_avatars) VALUES ({0},"{1}","{2}","{3}")'\
            .format(pp_id, pp_name, pp_alt, pp_avatars)
        insert_db(insert_str)
    return return_str


# 将数组 转换为 字符串
def read_genres(genres_list):
    return_str = ''
    for str_item in genres_list:
        return_str = return_str + str_item + '/'
    return return_str


# 拼接url 请求数据 解析数据 拼接字符串 电影表
for i in range(1, 14):
    start = (i-1)*20
    url_str = 'https://api.douban.com/v2/movie/top250?count=20&start={}'.format(start)
    print('\n', url_str)
    html = requests.get(url_str)
    print(i * 20, 'request ok ------------------->', html.status_code, '\n')
    json_str = json.loads(html.text)
    # print(json_str)
    json_body = json_str['subjects']
    for movie_item in json_body:
        movie_id = int(movie_item['id'])  # 0 int
        title = movie_item['title']  # 1
        original_title = movie_item['original_title']  # 2
        alt = movie_item['alt']  # 3
        rating = movie_item['rating']['average']  # 4 float
        year = movie_item['year']  # 5 int
        collect_count = movie_item['collect_count']  # 6 int
        genres = read_genres(movie_item['genres'])  # 7
        images = movie_item['images']['small']  # 8
        directors = read_people(movie_item['directors'])  # 9
        casts = read_people(movie_item['casts'])  # 10

        # 拼接字符串 储存数据库
        insert_str = 'INSERT INTO Top250Movie VALUES ({0},"{1}","{2}","{3}",{4},{5},{6},"{7}","{8}","{9}","{10}")'\
            .format(movie_id, title, original_title, alt, rating, year, collect_count, genres, images, directors, casts)
        insert_db(insert_str)

    # 稳健加个 时间等待
    time.sleep(5)
