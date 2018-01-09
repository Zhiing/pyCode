import requests
import sqlite3

from bs4 import BeautifulSoup
from requests.exceptions import ChunkedEncodingError


def insert_data(data, count):
    conn = sqlite3.connect('wufazhuce_com.db')
    c = conn.cursor()
    print('DATABASE OPEN OK')

    # CREATE TABLE
    # c.execute('''CREATE TABLE OneArticulo(
    #             ID INT PRIMARY KEY NOT NULL,
    #             TITLE VARCHAR(255) NULL,
    #             AUTOR VARCHAR(20) NULL,
    #             COMILLA VARCHAR(255) NULL,
    #             ARTICULO TEXT NULL
    #           )''')

    # INSERT DATA
    # str(count)
    # data.title
    # data.autor
    # data.comilla
    # data.articulo

    sql_str = "INSERT INTO OneArticulo(ID, TITLE, AUTOR, COMILLA, ARTICULO) " \
              "VALUES ({0}, '{1}', '{2}', '{3}', '{4}')".format(count, data['title'], data['autor'], data['comilla'], data['articulo'])
    # print(sql_str)
    c.execute(sql_str)

    conn.commit()
    print('INSERT OK ---------------------------------------------------------------------->>', count)
    conn.close()


def get_articulo(html):
    soup = BeautifulSoup(html, 'lxml')
    articulo_soup = soup.find('div', class_='one-articulo')

    soup_comilla = articulo_soup.find('div', class_='comilla-cerrar')
    soup_title = articulo_soup.find('h2', class_='articulo-titulo')
    soup_autor = articulo_soup.find('p', class_='articulo-autor')
    soup_articulo = articulo_soup.find('div', class_='articulo-contenido')

    comilla = soup_comilla.text
    title = soup_title.text
    autor = soup_autor.text
    articulo = soup_articulo.text

    articulo_data = {
        'title': title.replace('\t', '').replace('"', '”').replace("'", "‘").strip(),
        'autor': autor.replace('\t', '').replace('"', '”').replace("'", "‘").replace("作者/", "").strip(),
        'comilla': comilla.replace('\t', '').replace('"', '”').replace("'", "‘").strip(),
        'articulo': articulo.replace('"', '”').replace("'", "‘").strip()
    }
    return articulo_data


def get_url(count):
    url = url_str + str(count)
    print(url)
    try:
        reqs = requests.get(url)
        if reqs.status_code == 200:
            html = reqs.text
            return html
        else:
            return None
    except ChunkedEncodingError as e:
        print('请求出错', e.args)
        return None


def main():
    for count in range(3021, 3022):
        html = get_url(count)
        if html != None:
            articulo_data = get_articulo(html)
            msg = insert_data(articulo_data, count)
        else:
            continue


if __name__ == '__main__':
    url_str = 'http://wufazhuce.com/article/'
    main()

