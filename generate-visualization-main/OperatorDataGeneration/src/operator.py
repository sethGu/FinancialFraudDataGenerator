# @Time    : 2023/5/17 20:45
# @Author  : SuperRich Liu
import random


class Operator:
    def __init__(self):
        self.original_ID = ''
        self.contactor = ''
        self.contactor_ID = ''
        self.mobile_phone_brand = ''
        self.mobile_operating_system = ''
        self.pv = ''
        self.terminal_type = ''
        self.video_website = ''
        self.shopping_website = ''
        self.overseas_taobao_shopping_channel = ''
        self.automotive_website = ''
        self.real_estate_website = ''
        self.travel_website = ''
        self.highest_calling = 0
        self.city_number = 0
        self.day_calling = 0
        self.night_calling = 0
        self.three_month_calling = 0

    def set_original_ID(self):
        original_ID = 'phone'
        for i in range(11):
            original_ID += str(random.randint(0, 9))
        self.original_ID = original_ID

    def set_contactor(self):
        contactor = random.choice(['IPTV', '手机', '宽带'])
        self.contactor = contactor

    def set_contactor_ID(self):
        contactor_ID = 'K_'
        for i in range(5):
            contactor_ID += str(random.randint(0, 9))
        self.contactor_ID = contactor_ID

    def set_mobile_phone_brand(self):
        brand_list = ['苹果', 'OPPO', '三星', '华为', '小米', '360', 'HTC', 'LG', '魅族', '中兴', '乐视', '索尼',
                      '联想', '金立,锤子', '海信', '康佳', '一加', '乐丰', '谷歌', '酷派', '天语', '摩托罗拉', '美图',
                      '至尊宝', '飞利浦', '华硕,小辣椒', '朵唯', '首云', '酷比', '广信', '语信', '海尔', '维图']
        mobile_phone_brand = random.choice(brand_list)
        self.mobile_phone_brand = mobile_phone_brand

    def set_mobile_operating_system(self):
        if self.mobile_phone_brand == '苹果':
            mobile_operating_system = 'iOS'
        else:
            mobile_operating_system = 'Android'
        self.mobile_operating_system = mobile_operating_system

    def set_pv(self):
        pv = random.choice(['高', '中', '低'])
        self.pv = pv

    def set_terminal_type(self):
        terminal_type = random.choice(['Mobile', 'Computer', 'Tablet'])
        self.terminal_type = terminal_type

    def set_video_website(self):
        website_list = ['搜狐', '爱奇艺', '腾讯视频', '优酷', '乐视', '土豆', '哔哩哔哩', 'AcFun']
        video_website = '视频网站-' + random.choice(website_list)
        self.video_website = video_website

    def set_shopping_website(self):
        website_list = ['淘宝', '京东', '唯品会', '天猫', '1号店', '苏宁易购', '贝贝', '返利网', '飞牛网', '国美在线',
                        '聚美优品', '拼多多', '转转', '美丽说', '蘑菇街', '一淘', '卷皮', '折800']
        shopping_website = '购物网站-' + random.choice(website_list)
        self.shopping_website = shopping_website

    def set_overseas_taobao_shopping_channel(self):
        website_list = ['小红书', '网易考拉', '洋码头', '亚马逊', '乐天', '宝贝格子', '达令']
        overseas_taobao_shopping_channel = '海淘电商-' + random.choice(website_list)
        self.overseas_taobao_shopping_channel = overseas_taobao_shopping_channel

    def set_automotive_website(self):
        website_list = ['太平洋汽车网', '汽车之家', '爱卡汽车', '新浪汽车', '搜狐汽车', '易车网']
        automotive_website = '汽车网站-' + random.choice(website_list)
        self.automotive_website = automotive_website

    def set_real_estate_website(self):
        website_list = ['房天下', '安居客', '链家', '中原房产', '我爱我家', '房多多', '居理新房']
        real_estate_website = '房产网站-' + random.choice(website_list)
        self.real_estate_website = real_estate_website

    def set_travel_website(self):
        website_list = ['携程', '同程旅游', '蚂蜂窝', '去哪儿', '穷游网', '驴妈妈', '途牛', '飞猪', '中青旅遨游旅行',
                        '众信旅游悠哉网', '猫途鹰', '游多多', '乐途旅游网', '国旅在线']
        travel_website = '旅游网站-' + random.choice(website_list)
        self.travel_website = travel_website

    def set_highest_calling(self):
        highest_calling = random.randint(0, 30)
        self.highest_calling = highest_calling

    def set_city_number(self):
        city_number = random.randint(0, 25)
        self.city_number = city_number

    def set_day_calling(self):
        day_calling = random.randint(0, self.highest_calling)
        self.day_calling = day_calling

    def set_night_calling(self):
        night_calling = random.randint(0, 50)
        self.night_calling = night_calling

    def set_three_month_calling(self):
        three_month_calling = random.randint(0, 30)
        self.three_month_calling = three_month_calling

    def get_all_items(self):
        all_items = {
            'original_ID': self.original_ID,
            'contactor': self.contactor,
            'contactor_ID': self.contactor_ID,
            'mobile_phone_brand': self.mobile_phone_brand,
            'mobile_operating_system': self.mobile_operating_system,
            'pv': self.pv,
            'terminal_type': self.terminal_type,
            'video_website': self.video_website,
            'shopping_website': self.shopping_website,
            'overseas_taobao_shopping_channel': self.overseas_taobao_shopping_channel,
            'automotive_website': self.automotive_website,
            'real_estate_website': self.real_estate_website,
            'travel_website': self.travel_website,
            'highest_calling': self.highest_calling,
            'city_number': self.city_number,
            'day_calling': self.day_calling,
            'night_calling': self.night_calling,
            'three_month_calling': self.three_month_calling,
        }
        return all_items


if __name__ == '__main__':
    print('*')
    # 自动生成get()和set()方法
    # Ope = Operator()
    # print(Ope.__dict__)
    # for k in Ope.__dict__:
    #     print("def set_" + k + "(self," + k + "):")
    #     print("\tself." + k, "=" + k)
    #     print("def get_" + k + "(self):")
    #     print("\treturn self." + k)
