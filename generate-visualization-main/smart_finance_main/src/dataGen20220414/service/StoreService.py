import json
import random
import datetime
import random
import time
from src.dataGen20220414.dao.StoreDao import StoreDao
from src.dataGen20220414.entity.Store import Store
from src.utils.functions import id_generator, read_json_file
from src.utils.config import BASE_DIR

store_name_dict = {
    "餐饮":{'低':"小厨","中":"餐厅","高":"酒店"},
    "衣着美容":{'低':"发廊","中":"美容","高":"衣柜"},
    "生活用品及服务":{'低':"便利店","中":"超市","高":"商场"},
    "交通通信":{'低':"公交","中":"出租公司","高":"航空"},
    "教育文化":{'低':"学校","中":"培训中心","高":"教育"},
    "医疗保健":{'低':"诊所","中":"医院","高":"医院"},
    "居住":{'低':"旅馆","中":"酒店","高":"大酒店"},
    "娱乐":{'低':"KTV","中":"酒吧","高":"会所"}
}

class StoreService():
    def __init__(self, scene):
        self.storeDao = StoreDao()

        self.table_names = {"黄牛营销欺诈": 'marketing_store', "信用卡违规套现": 'credit_store', "异常转账": 'abnormal_store',
                        "伪冒注册欺诈": 'register_store', "赌博违规交易": 'gambling_store',
                        "商户违规": 'store_store'}
        self.scene = self.table_names[scene]
    def createStoreTable(self):
        # for name in self.table_names.values():
        self.storeDao.createStoreTable(self.scene)

    def insertStores(self,storeList):
        self.storeDao.insertStores(storeList, self.scene)

    def selectStores(self):
        '''
        查询所有商户
        :return:
        '''
        select_res = self.storeDao.selectStores(self.scene)
        storeList = []
        for item in select_res:
            id, industry, name_, rank_, consumption_range, opening_hours, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S25, S26, S27, S28, S29, S30, abnormal, abnormal_state = item
            abnormal_state = json.loads(abnormal_state)
            consumption_range = eval(consumption_range)
            store = Store(id, industry, name_, rank_, consumption_range, opening_hours, S1, S2, S3, S4, S5, S6, S7, S8,
                          S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S25, S26, S27,
                          S28, S29, S30, abnormal, abnormal_state)

            storeList.append(store)
        return storeList


    def updateAcctOfStore(self,store_id, C4):
        self.storeDao.updateAcctOfStore(store_id, C4, self.scene)
    @staticmethod
    def createStore():
        store_name = ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba',3))
        store_id = StoreService.createStore_id()
        # 大类和子类
        industry, industry_ = StoreService.createIndustry()
        # 根据子类获取营业时间
        open_duration = StoreService.createOpen_duration(industry_)

        # 根据大类和子类获取商户等级
        result = StoreService.createSubClassLevel(industry, industry_)

        S30 = id_generator(size=8, chars='1234567890')
        S30s = {S30: "正常"}
        S30 =  json.dumps(S30s, ensure_ascii=False)
        #商户EXT创建时间
        MINTIME = datetime.datetime(2015, 2, 11, 0, 0, 0)  # 设置时间范围的开始时间
        MAXTIME = datetime.datetime(2022, 2, 12, 0, 0, 0)  # 设置时间范围的结束时间
        mintime_ts = int(time.mktime(MINTIME.timetuple()))
        maxtime_ts = int(time.mktime(MAXTIME.timetuple()))
        random_ts = random.randint(mintime_ts, maxtime_ts)
        RANDOMTIME = datetime.datetime.fromtimestamp(random_ts)
        year = str(RANDOMTIME.year)
        month = str(RANDOMTIME.month)
        if RANDOMTIME.month < 10:
            month = "0" + str(RANDOMTIME.month)
        day = str(RANDOMTIME.day)
        if RANDOMTIME.day < 10:
            day = "0" + str(RANDOMTIME.day)
        date = year + month + day
        ###################################

        S1 = id_generator(size=15, chars='1234567890')
        S2 = "0000000000"
        S3 = store_name
        S4 = store_name
        S5 = StoreService.createS5(industry_)
        S6 = "0000000000"
        S7 = date#随机时间吧，如果是异常商户，可以把它修改的与生成数据时间相近 ?????
        S8 = '001'
        S9 = '0'
        # T16
        S10 = '0'
        S11 = '0'
        list_ = ["0","1"]
        S12 =  random.choice(list_)

        ins = random.choice(["0001","0002","0003","0004","0005","0006"])
        place = random.choice(["0001","0002","0003"])
        S13 = "99"+ins+place
        S14 = random.choice(list_)
        S15 = '0001'
        S16 = '1'
        S17 = '07'
        S18 = random.randint(100000, 999999)
        S19 = ''.join(random.choice('0123456789') for _ in range(8))
        S20 = ''.join(random.choice('0123456789') for _ in range(18))
        S21 = ''.join(random.choice('0123456789') for _ in range(10))
        S22 = ''.join(random.choice('0123456789') for _ in range(15))
        S23 = ''.join(random.sample('ZXCVBNMASDFGHJKLQWERTYUIOP123456789ZXCVBNMASDFGHJKLQWERTYUIOP123456789ZXCVBNMASDFGHJKLQWERTYUIOP123456789',64))
        S24 = ''.join(random.choice('0123456789') for _ in range(10))
        S25 = ''.join(random.choice('0123456789') for _ in range(12))
        S26 = ''.join(random.choice('0123456789') for _ in range(10))
        S27 = ''.join(random.choice('0123456789') for _ in range(10))
        S28 = ''.join(random.choice('0123456789') for _ in range(8))
        S29 = '1'
        store_list = []
        for r in result:
            charge_duration = StoreService.createCharge_duration(r)
            store = Store(store_id, industry, store_name + r, r, charge_duration,open_duration,S1,
                 S2, S3, S4,S5, S6,S7,S8,S9,S10,S11,S12,S13, S14, S15, S16,S17,S18,S19,S20,S21,S22,S23,S24,S25,S26,S27,S28,S29,S30)
            store_list.append(store)

        return store_list

    @staticmethod
    def createStore_id():
        # 生成商户id暂时不考虑
        return 0

    @staticmethod
    def createIndustry():
        # industry_list = ["餐饮", "衣着美容", "生活用品及服务", "交通通信", "教育文化", "医疗保健", "居住", "娱乐"]
        # # 以下为各行业的比例，可以进行修改
        # industryProportion = [10, 3, 4, 2, 1, 1.5, 6, 2]
        # sum_ = sum(industryProportion)
        # pro_list = [0 for i in range(len(industryProportion))]
        # for i in range(len(industryProportion)):
        #     if i == 0:
        #         pro_list[i] = industryProportion[i] / sum_
        #     else:
        #         pro_list[i] = pro_list[i - 1] + industryProportion[i] / sum_
        # r = random.random()
        # for i in range(len(pro_list)):
        #     if r < pro_list[i]:
        #         return industry_list[i]
        industry_list = [
            "餐饮",
            "衣着美容",
            "生活用品及服务",
            "交通通信",
            # "教育文化",
            "医疗保健",
            "居住",
            "娱乐"
        ]
        industryProportion = [
            10,
            3,
            4,
            2,
            # 1,
            1.5,
            6,
            2]
        sum_ = sum(industryProportion)
        pro_list = [0 for i in range(len(industryProportion))]
        for i in range(len(industryProportion)):
            if i == 0:
                pro_list[i] = industryProportion[i] / sum_
            else:
                pro_list[i] = pro_list[i - 1] + industryProportion[i] / sum_
        r = random.random()
        # 行业大类
        industry = ''
        for i in range(len(pro_list)):
            if r < pro_list[i]:
                industry = industry_list[i]
                break
        jsonfile = BASE_DIR + '/src/json_file/store_generate_ratio.json'
        sub_industry_class = read_json_file(jsonfile)[industry]

        sub_class = []
        sub_class_value = []
        for key, value in sub_industry_class.items():
            sub_class.append(key)
            sub_class_value.append(value)
        sum_ = sum(sub_class_value)
        pro_list = [0 for i in range(len(sub_class_value))]
        for i in range(len(sub_class_value)):
            if i == 0:
                pro_list[i] = sub_class_value[i] / sum_
            else:
                pro_list[i] = pro_list[i - 1] + sub_class_value[i] / sum_
        r = random.random()
        # 行业小类
        industry_ = ''
        for i in range(len(pro_list)):
            if r < pro_list[i]:
                industry_ = sub_class[i]
                break
        return industry, industry_


    @staticmethod
    def createLevel(industry):
        # 以下为各行业的对应低中高档的比例，可以进行修改
        # 娱乐， 医疗保健，餐饮，居住又分为低中高三级， 其他不分类
        industry_level_info = {"餐饮":[8,1.5,0.5],"衣着美容":[8, 1.5, 0.5],"生活用品及服务":[8, 1.5, 0.5],"交通通信":[5, 1.5, 0.5],"教育文化":[3, 1.5, 0.5],"医疗保健":[8, 1.5, 0.5],"居住":[8, 1.5, 0.5],"娱乐":[8, 1.5, 0.5]}
        weight_list = industry_level_info[industry]
        level_list = ["低", "中", "高"]
        pro_list = [0 for i in range(len(weight_list))]
        sum_ = sum(weight_list)
        for i in range(len(weight_list)):
            if i == 0:
                pro_list[i] = weight_list[i] / sum_
            else:
                pro_list[i] = pro_list[i - 1] + weight_list[i] / sum_
        r = random.random()
        for i in range(len(pro_list)):
            if r < pro_list[i]:
                return level_list[i]

    @staticmethod
    def createSubClassLevel(industry, industry_):
        has_sub_class = ["餐饮", "医疗保健", "居住", "娱乐", "生活用品及服务"]
        result = []
        if industry not in has_sub_class:
            result.append(industry_)
            return result
        if industry == "居住" and industry_ == "青旅":
            result.append(industry_)
            return result
        if industry == "医疗保健":
            result.append(industry_ + "(低)")
            result.append(industry_ + "(中)")
        else:
            result.append(industry_ + "(低)")
            result.append(industry_ + "(中)")
            result.append(industry_ + "(高)")
        return result

    @staticmethod
    def createCharge_duration(industry):
        jsonfile = BASE_DIR + '/src/json_file/store_consume_section.json'
        jsonfile = read_json_file(jsonfile)
        industry_Charge_duration = jsonfile[industry]
        industry_Charge_duration = industry_Charge_duration.split('-')
        min = int(industry_Charge_duration[0])
        max = int(industry_Charge_duration[1])
        #生成商户最小消费值,范围为[min 到 2*min*max/(min+max)]
        min_ = random.randint(min, int((2 * min * max)/(min+max)))
        # 生成商户最大消费值,范围为[min+max/2 到 max]
        max_ = random.randint(int((min+max)/2), max)
        return [min_,max_]

    @staticmethod
    def createS5(industry):
        jsonfile = BASE_DIR + '/src/json_file/store_S5.json'
        jsonfile = read_json_file(jsonfile)
        list = jsonfile[industry]
        S5 = random.choice(list)
        return S5
    @staticmethod
    def createOpen_duration(industry):
        # r = random.random()
        # industry_Open_duration={
        #     "餐饮":{"低":["6:00-11:00","15:00-24:00","8:00-23:00"] ,"中":["9:00-22:00","10:00-22:00"],"高":[ "9:00-21:00","11:00-20:00" ]},
        #     "衣着美容":{"低": [ "15:00-24:00","8:00-23:00","9:00-22:00"  ],"中":["15:00-22:00","8:00-22:00","9:00-22:00"],"高":[ "14:00-24:00","10:00-23:00" ]},
        #     "生活用品及服务":{"低":["0:00-24:00","9:00-23:00","8:00-22:00"] ,"中":["8:00-22:00","9:00-22:00"],"高":[  "9:00-19:00", "10:00-22:00"  ]},
        #     "交通通信": {"低":["6:00-23:00","0:00-24:00,"], "中":["6:00-24:00"], "高":["6:00-24:00"]},
        #     "教育文化": {"低":[ "7:00-22:00" ], "中":[ "7:00-22:00"], "高":[ "7:00-22:00"]},
        #     "医疗保健": {"低":["8:00-24:00"], "中":["8:00-24:00"], "高":["8:00-24:00"]},
        #     "居住": {"低":["9:00-24:00"], "中":["9:00-24:00"], "高":["9:00-24:00"]},
        #     "娱乐": {"低":["0:00-24:00"], "中":["0:00-24:00"], "高":["0:00-24:00"]},
        # }
        # industry_Open_duration_list = industry_Open_duration[industry][level]
        # len_industry_Open_duration_list = len(industry_Open_duration_list)
        # pool = [i-1 for i in range(len_industry_Open_duration_list)]
        # index = random.choice(pool)
        # return industry_Open_duration_list[index]

        jsonfile = BASE_DIR + '/src/json_file/store_open_time.json'

        open_duration = read_json_file(jsonfile)
        return open_duration[industry]

    def updateStoreState(self, store_id, fraud_category):
        self.storeDao.updateStoreState(store_id, fraud_category, self.scene)

    def update_S30s(self, store_id, S30s):
        self.storeDao.update_S30s(store_id, S30s, self.scene)

    def selectStoreByS1(self, S1):
        res = self.storeDao.select_store_by_S1(S1, self.scene)

        id, industry, name_, rank_,consumption_range,opening_hours,S1, S2, S3, S4,S5, S6,S7,S8,S9,S10,S11,S12,S13, S14, S15, S16,S17,S18,S19,S20,S21,S22,S23,S24,S25,S26,S27,S28,S29,S30, abnormal, abnormal_state= res
        abnormal_state = json.loads(abnormal_state)
        consumption_range = eval(consumption_range)
        store = Store(id, industry, name_, rank_,consumption_range,opening_hours,S1, S2, S3, S4,S5, S6,S7,S8,S9,S10,S11,S12,S13, S14, S15, S16,S17,S18,S19,S20,S21,S22,S23,S24,S25,S26,S27,S28,S29,S30, abnormal, abnormal_state)
        return store