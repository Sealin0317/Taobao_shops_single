from urllib.parse import urlencode
import pymongo
import pymysql
from pyquery import PyQuery as pq
from config import *
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)
# wait = WebDriverWait(browser, 5)
# browser.set_window_size(1400, 900)


# mysql
# conn = pymysql.connect(host='106.14.196.40', unix_socket='/tmp/mysql.sock',
#                        user='root', passwd='mysqlroot', db='mysql', charset='utf8')
# cur = conn.cursor()
# cur.execute("USE taobao;")

# mongodb
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


# def save_to_mysql(k1,location,store_number):
#     print('begin to save to mysql~~~~~~~',k1)
#     cur.execute("INSERT INTO t1 (k1,location,store_number) VALUES (%s,%s,%s)",
#                 (k1,location,store_number))
#     cur.connection.commit()


def get_html_1(keyword1, location):
    print('begin to crawling html_1~~~~~~~~~', keyword1)
    data = {
        'app': 'shopsearch',
        'q': keyword1,
        'js': 1,
        'initiative_id': 'staobaoz_20170715',
        'ie': 'utf8',
        'loc': location,
        'sort': 'sale - desc',
        's': 0
     }
    queries = urlencode(data)
    url = base_url + queries
    browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)
    wait = WebDriverWait(browser, 5)
    try:
        browser.get(url)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#list-content')))
        html = browser.page_source
        if html:
            return html
        else:
            return None
    except TimeoutException:
        print('fail in getting response_1', url)
        browser.quit()
    finally:
        browser.quit()


# def get_html_2():
#     print('begin to crawling html_2~~~~~~~~~')
#     data ={
#         'app': 'shopsearch',
#         'q': keyword1 + keyword2,
#         'js': 1,
#         'initiative_id': 'staobaoz_20170711',
#         'ie': 'utf8',
#         'loc': '上海',
#         'sort': 'sale - desc',
#         's': 0
#     }
#     queries = urlencode(data)
#     url = base_url + queries
#     try:
#         browser.get(url)
#         wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#list-content')))
#         html = browser.page_source
#         if html:
#             return html
#         else:
#             return None
#     except TimeoutException:
#         print('fail in getting response_1', url)


def get_product_1(html):
    try:
        doc = pq(html)
        shopcount = doc('.shop-count b').text()
        if shopcount:
            return shopcount
        else:
            return None
    except TimeoutException:
        print('fail in getting product_1')


def save_to_mongodb(data):
    try:
        if db[MONGO_TABLE1].insert(data):
            print('successful saved~~~~~', data)
            return True
        return False
    except Exception:
        print('fail to save.')


def main():
    try:
        for key1 in keywords_1:
            keyword1 = key1
            for loc in locations:
                location = loc
                html_1 = get_html_1(keyword1, location)
                result = get_product_1(html_1)
                data = {
                    '大类：': keyword1,
                    '区域：': location,
                    '店铺总数：': result
                }
                save_to_mongodb(data)
                # print(type(result))
                print(keyword1, location, '店铺总数:', result)
                # save_to_mysql(keyword1, location, result)
    except Exception:
        print('Wrong in main processing~~~~')
        browser.quit()
    finally:
        browser.quit()
        # finally:
        # conn.close()
        # browser.close()
        # for i in range(0,100,20):
        # html = get_html_2(i)
        # product_2 = get_product_2(html)
        # print(product_1)


if __name__ == '__main__':
    main()
