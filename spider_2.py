from ky import *
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

# washing keywords2
shoe = shoe.split('\t')
toy = toy.split('\t')
appliance = appliance.split('\t')
makeup = makeup.split('\t')
jewelry = jewelry.split('\t')
flower = flower.split('\t')
furniture = furniture.split('\t')
car = car.split('\t')
supplies = supplies.split('\t')
stuff = stuff
study = study.split('\t')
men = men.split('\t')
bag = bag.split('\t')
digital = digital.split('\t')
washing = washing.split('\t')
comic = comic.split('\t')
fresh = fresh.split('\t')
pet = pet.split('\t')
homeware = homeware
DIY = DIY.split('\t')
kitchen = kitchen.split('\t')
bonouce = bonouce.split('\t')
underware = underware.split('\t')
accessory = accessory.split('\t')
health_product = health_product.split('\t')
agricultural = agricultural.split('\t')
building_materials = building_materials.split('\t')
textiles = textiles.split('\t')
hardware = hardware.split('\t')
home_care = home_care.split('\t')
service = service.split('\t')
chr_shoe = chr_shoe.split('\t')
chr_clothes = chr_clothes.split('\t')
pregnant = pregnant.split('\t')
infant = infant.split('\t')
special_shoe = special_shoe.split('\t')
fitness = fitness.split('\t')
outdorrs = outdorrs.split('\t')
swimming = swimming.split('\t')
instrument = instrument.split('\t')
game = game.split('\t')
snacks = snacks.split('\t')
dessert = dessert.split('\t')
staple = staple.split('\t')
tea = tea.split('\t')
medic = medic.split('\t')
wine = wine.split('\t')
sports = sports.split('\t')

keywords_2 = [dress, shoe, toy, appliance, makeup, jewelry, flower, furniture, car, supplies, stuff, study,
              men, bag, digital, washing, comic, fresh, pet, homeware, DIY, kitchen, bonouce, underware, accessory,
              health_product, agricultural, building_materials, textiles, hardware, home_care, service,
              chr_shoe, chr_clothes, pregnant, infant, special_shoe, fitness, outdorrs, swimming, instrument,
              game, snacks, dessert, staple, tea, medic, wine, sports]
keywords_1 = ['女装', '鞋靴', '童装玩具', '家电', '美妆', '珠宝', '鲜花', '家具', '汽车', '办公', '百货', '学习', '男装', '箱包',
              '数码', '洗护', '动漫', '生鲜', '宠物', '家饰', 'DIY', '餐厨', '卡券', '内衣', '服装配件', '保健品', '农资',
              '建材', '家纺', '五金电子', '家庭保健', '本地服务', '童鞋', '童装', '孕产用品', '母婴用品', '潮鞋', '健身',
              '户外', '游泳', '乐器', '游戏', '零食', '甜点', '主食', '茶叶', '中药材', '白酒', '运动']

# print(len(keywords_1),len(keywords_2))
# k1 = ['女装','鞋靴']
# k2 = [dress,shoe]

# merging keywords
dic = dict(zip(keywords_1, keywords_2))
count = 0

# set mysql
conn = pymysql.connect(host='47.93.32.130', unix_socket='/tmp/mysql.sock',
                       user='ant', passwd='Qljl1rh!', db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute("USE taobao;")


# save to mysql
def save_to_mysql(k1, k2, title, location, rank, rate, sales, amount):
    print('begin to save to mysql~~~~~~~', k1, k2, title, location, rank, rate, sales, amount)
    cur.execute("INSERT INTO t2 (k1,k2,title,location,rank,rate,sales,amount) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                (k1, k2, title, location, rank, rate, sales, amount))
    cur.connection.commit()


# get index
def get_index(k1, k2, location):
    print('begin to crawling index--------------------------------', k1, k2, location)
    data = {
        'app': 'shopsearch',
        'q': k1 + k2,
        'js': 1,
        'initiative_id': 'staobaoz_20170724',
        'ie': 'utf8',
        'loc': location,
        'sort': 'sale-desc',
        's': 0
    }
    queries = urlencode(data)
    url = base_url + queries
    browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)
    wait = WebDriverWait(browser, 5)
    try:
        browser.get(url)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_Filter > div > span > b')))
        html = browser.page_source
        html = html.replace('&lt;', '<').replace('&gt;', '>')
        doc = pq(html)
        store_number = int(doc('#J_Filter > div > span > b').text())
        print(store_number,type(store_number))
        if store_number <= 20 and store_number != 0:
            page_numbers = 1
        elif store_number == 0:
            page_numbers = 0
        else:
            page_numbers = int(doc('#shopsearch-pager > div > div > div > div.total').text()[2:-3])
        return [store_number, page_numbers]
    except TimeoutException:
        print('fail in getting response', k1, k2, location)
        browser.quit()
        return None
    finally:
        browser.quit()


# get html
def get_html(k1, k2, location, page_numbers, store_number):
    print('begin to crawling html~~~~~~~~~', k1, k2, count)
    data = {
        'app': 'shopsearch',
        'q': k1 + k2,
        'js': 1,
        'initiative_id': 'staobaoz_20170724',
        'ie': 'utf8',
        'loc': location,
        'sort': 'sale-desc',
        's': 0
    }
    queries = urlencode(data)
    url = base_url + queries
    browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)
    wait = WebDriverWait(browser, 5)
    try:
        browser.get(url)
        if page_numbers == 1:
            print('begin to crawl page', page_numbers, k1, k2, location)
            html = browser.page_source
            html = html.replace('&lt;', '<').replace('&gt;', '>')
            if html:
                get_info(k1, k2, location, html, store_number)
                return True
            else:
                return None
        else:
            print('begin to crawl page', page_numbers, k1, k2, location)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_Filter > div > span > b')))
            input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#shopsearch-pager > div > div > div > div.form > input')))
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#shopsearch-pager > div > div > div > div.form > span.btn.J_Submit')))
            input.clear()
            input.send_keys(page_numbers)
            submit.click()
            wait.until(EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, '#shopsearch-pager > div > div > div > ul > li.item.active > span'),
                str(page_numbers))
                               )
            html = browser.page_source
            html = html.replace('&lt;', '<').replace('&gt;', '>')
            if html:
                get_info(k1, k2, location, html, store_number)
                return True
            else:
                return None
    except TimeoutException:
        print('fail in getting response', k1, k2, location)
        browser.quit()
    finally:
        browser.quit()


def get_info(k1, k2, location, html, store_number):
    try:
        doc = pq(html)
        if store_number <= 20:
            for i in range(0, store_number):
                print('count~~~~~~~~~~~store_number:', i)
                title = doc('#list-container .list-item .list-info h4 .shop-name').eq(i).text()
                if doc('#list-container li h4 .rank').eq(i):
                    rank = doc('#list-container li h4 .rank').eq(i).attr['class'][17:]
                    rate = doc('#list-container li .good-comt').eq(i).text()[5:]
                else:
                    rank = '100'
                    rate = '100'
                sales = doc('#list-container li .info-sale em').eq(i).text()
                amount = doc('#list-container li .info-sum em').eq(i).text()
                save_to_mysql(k1, k2, title, location, rank, rate, sales, amount)
                # print(k1, k2, title, location, rank, rate, sales, amount)
        else:
            for i in range(0, 20):
                print('count~~~~~~~~~~~store_number:', i)
                title = doc('#list-container .list-item .list-info h4 .shop-name').eq(i).text()
                if doc('#list-container li h4 .rank').eq(i):
                    rank = doc('#list-container li h4 .rank').eq(i).attr['class'][17:]
                    rate = doc('#list-container li .good-comt').eq(i).text()[5:]
                else:
                    rank = '100'
                    rate = '100'
                sales = doc('#list-container li .info-sale em').eq(i).text()
                amount = doc('#list-container li .info-sum em').eq(i).text()
                if title:
                    # save_to_mysql(k1, k2, title, location, rank, rate, sales, amount)
                    print(k1, k2, title, location, rank, rate, sales, amount)
                else:
                    pass
            # print(k1, k2, title, location, rank, rate, sales, amount)
            # yield {
            #     'title': title,
            #     'rank': rank,
            #     'rate': rate,
            #     'sales': sales,
            #     'amount': amount
            # }
    except TimeoutException:
        print('fail in getting info')


def main():
    try:
        global count
        for k in dic.keys():
            k1 = k
            for v in dic.get(k1):
                k2 = v
                count += 1
                for loc in locations:
                    location = loc
                    result = get_index(k1, k2, location)
                    store_number = result[0]
                    page_numbers = result[1]
                    print(store_number, page_numbers)
                    if page_numbers == 0:
                        pass
                    #     continue
                    # elif page_numbers == 1:
                    #     get_html(k1, k2, location, page_numbers, store_number)
                    else:
                        for page_numbers in range(1, int(page_numbers + 1)):
                            get_html(k1, k2, location, page_numbers, store_number)
                    # get_html(k1, k2, location)
                    # get_info(k1,k2,location,html)
                    # for item in results.items():
                    #     save_to_mysql(k1,k2,item[0],location,item[1],item[2],item[3],item[4])
    except Exception as e:
        print('Wrong in main processing~~~~', e.args)
    finally:
        conn.close()


if __name__ == '__main__':
    main()
