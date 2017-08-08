#set parameters
base_url = 'https://shopsearch.taobao.com/search?'
#base_url = 'https://shopsearch.taobao.com/search?app=shopsearch&q=' + keyword_1 '+' + keyword_2 + '&js=1&initiative_id=staobaoz_20170711&ie=utf8&loc=' + location + '&sort=sale-desc&s=' + page_numbers

user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]

SERVICE_ARGS = ['--load-images=false', '--disk-cache=true']

# set mongo database parameters
# MONGO_URL = 'mongodb://xxx:xxx@xxxx/'
# MONGO_URL = 'localhost'
# MONGO_DB = 'TAOBAO'
# MONGO_TABLE1 = 't3'
# MONGO_TABLE2 = 't2'

#地址
locations =['北京','上海','广州','深圳','杭州','长沙','长春','成都','重庆','大连','东莞','佛山','福州','贵阳','合肥','金华','济南','嘉兴','昆明','宁波','南昌','南京','青岛','泉州','沈阳','苏州','天津','温州','无锡','武汉','西安','厦门','郑州','中山','石家庄','哈尔滨','安徽','福建','甘肃','广东','广西','贵州','海南','河北','河南','湖北','湖南','江苏','江西','吉林','辽宁','宁夏','青海','山东','山西','陕西','云南','四川','西藏','新疆','浙江','澳门','香港','台湾','内蒙古','黑龙江']

#大类关键字
keywords_1 = ['女装','鞋靴','童装玩具','家电','美妆','珠宝','鲜花','家具','汽车','办公','百货','学习','男装','箱包','数码','洗护','动漫','生鲜','宠物','家饰','DIY','餐厨','卡券','内衣','服装配件','保健品','农资','建材','家纺','五金电子','家庭保健','本地服务','童鞋','童装','孕产用品','母婴用品','潮鞋','健身','户外','游泳','乐器','游戏','零食','甜点','主食','茶叶','中药材','白酒','运动']


