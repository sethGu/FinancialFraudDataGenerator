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
    "Catering":{'Low':"Small_kitchen","Medium":"Restaurant","High":"Hotel"},
    "Clothing_and_beauty":{'Low':"Hair_salon","Medium":"Beauty_treatment","High":"Wardrobe"},
    "Household_items_and_services":{'Low':"Convenience_store","Medium":"Supermarket","High":"Shopping_mall"},
    "Transportation_and_communication":{'Low':"Bus","Medium":"Rental_company","High":"Aviation"},
    "Education_and_culture":{'Low':"School","Medium":"Training_center","High":"Education"},
    "Healthcare":{'Low':"Clinic","Medium":"Hospital","High":"Hospital"},
    "Residence":{'Low':"Inn","Medium":"Hotel","High":"Grand_hotel"},
    "Entertainment":{'Low':"KTV","Medium":"Bar","High":"Clubhouse"}
}

class StoreService():
    def __init__(self, scene):
        self.storeDao = StoreDao()

        self.table_names = {"Scalper_marketing": 'marketing_store', "Credit_card_fraud": 'credit_store', "Abnormal_transfer": 'abnormal_store',
                        "Fake_registration": 'register_store', "Gambling_violation": 'gambling_store',
                        "Merchant_violation": 'store_store'}
        self.scene = self.table_names[scene]
    def createStoreTable(self):
        # for name in self.table_names.values():
        self.storeDao.createStoreTable(self.scene)

    def insertStores(self,storeList):
        self.storeDao.insertStores(storeList, self.scene)

    def selectStores(self):
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
        industry, industry_ = StoreService.createIndustry()
        open_duration = StoreService.createOpen_duration(industry_)

        result = StoreService.createSubClassLevel(industry, industry_)

        S30 = id_generator(size=8, chars='1234567890')
        S30s = {S30: "Normal"}
        S30 =  json.dumps(S30s, ensure_ascii=False)
        MINTIME = datetime.datetime(2015, 2, 11, 0, 0, 0)
        MAXTIME = datetime.datetime(2022, 2, 12, 0, 0, 0)
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
        S7 = date
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
        return 0

    @staticmethod
    def createIndustry():
        # industry_list = ["Catering", "Clothing_and_beauty", "Household_items_and_services", "Transportation_and_communication", "Education_and_culture", "Healthcare", "Residence", "Entertainment"]
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
            "Catering",
            "Clothing_and_beauty",
            "Household_items_and_services",
            "Transportation_and_communication",
            # "教育文化",
            "Healthcare",
            "Residence",
            "Entertainment"
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
        industry_ = ''
        for i in range(len(pro_list)):
            if r < pro_list[i]:
                industry_ = sub_class[i]
                break
        return industry, industry_


    @staticmethod
    def createLevel(industry):
        industry_level_info = {"Catering":[8,1.5,0.5],"Clothing_and_beauty":[8, 1.5, 0.5],"Household_items_and_services":[8, 1.5, 0.5],"Transportation_and_communication":[5, 1.5, 0.5],"Education_and_culture":[3, 1.5, 0.5],"Healthcare":[8, 1.5, 0.5],"Residence":[8, 1.5, 0.5],"Entertainment":[8, 1.5, 0.5]}
        weight_list = industry_level_info[industry]
        level_list = ["Low", "Medium", "High"]
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
        has_sub_class = ["Catering", "Healthcare", "Residence", "Entertainment", "Household_items_and_services"]
        result = []
        if industry not in has_sub_class:
            result.append(industry_)
            return result
        if industry == "Residence" and industry_ == "Youth_hostel":
            result.append(industry_)
            return result
        if industry == "Healthcare":
            result.append(industry_ + "(Low)")
            result.append(industry_ + "(Medium)")
        else:
            result.append(industry_ + "(Low)")
            result.append(industry_ + "(Medium)")
            result.append(industry_ + "(High)")
        return result

    @staticmethod
    def createCharge_duration(industry):
        jsonfile = BASE_DIR + '/src/json_file/store_consume_section.json'
        jsonfile = read_json_file(jsonfile)
        industry_Charge_duration = jsonfile[industry]
        industry_Charge_duration = industry_Charge_duration.split('-')
        min = int(industry_Charge_duration[0])
        max = int(industry_Charge_duration[1])
        min_ = random.randint(min, int((2 * min * max)/(min+max)))
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