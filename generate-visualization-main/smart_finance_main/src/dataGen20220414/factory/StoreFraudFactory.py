import datetime
import json
import random

from src.dataGen20220414.entity.Trans import Trans
from src.dataGen20220414.service.CardService import CardService
from src.dataGen20220414.service.TransService import TransService
from src.dataGen20220414.service.StoreService import StoreService
from src.utils.config import BASE_DIR
from src.utils.functions import read_json_file
from src.dataGen20220414.service.UserService import UserService
from src.utils.functions import id_generator

class StoreFraudFactory:
    def __init__(self):
        scene = "商户违规"
        self.storeService = StoreService(scene)
        self.userService = UserService(scene)
        self.cardService = CardService(scene)
        self.transService = TransService(scene)

    def create_abnormal_register_data(self, startDate, quantity):
        # 定义交易时间间隔
        timeInterval = 180
        # 选择商户欺诈的商户
        abnoramlStoreList = self.pick_abnormal_Store(quantity)
        for abnoramlStore in abnoramlStoreList:
            # 确定异常类型
            abnormalType = self.getAbnormalType()
            # 生成密集、夜间、非营业时间的交易时间
            timeList = self.getTimeList(startDate, 30, timeInterval, 5, abnormalType['abnormalTime'])

            if abnormalType['abnormalS30'] == True:
                self.generate_abnormal_F16(abnoramlStore)
            for time in timeList:
                try:
                    # 生成交易的用户，一方面，每个事件点都集体查询一次user，效率很差，另一方面，其他场景生成的异常用户，好像有的没有银行卡，不知道怎么回事，反正这里会报错
                    user = self.get_user()
                    # 选择交易卡
                    card = random.choice(user.getCard())
                except:
                    print("出错了 StoreFraudFactory create_abnormal_register_data")
                    continue

                T17 = self.getAmount(abnormalAmount=abnormalType['abnormalAmount'])

                F16 = self.get_F16(abnoramlStore, abnormalS30=abnormalType['abnormalS30'])

                self.transService.insertTrans(Trans(
                    id=0,
                    T2='01',
                    T1=card['C4'],
                    T6='0',
                    T14='4',
                    T17=T17,
                    T19=time[11:13] + time[14:16] + time[17:19],
                    T23=time[0:4] + time[5:7] + time[8:10],
                    T26=card['C5'],
                    T37=abnoramlStore.getS18(),
                    T25=abnoramlStore.getS1(),
                    abnormal=1,
                    abnormal_state={"赌博违规交易": 0, "伪冒注册欺诈": 0, "信用卡违规套现": 0, "黄牛营销欺诈": 0, "商户违规": 1, "异常转账": 0},
                    T31=F16
                ))
                # 更新操作者和其卡的abnormal_state
                self.userService.updateUserState(user.getId(), '商户违规')
                self.storeService.updateStoreState(abnoramlStore.getStore_id(), '商户违规')
                self.cardService.updateCardState(card['C4'], '商户违规')
                self.cardService.updateCardState(abnoramlStore.getCard_id(), '商户违规')

    def getAbnormalType(self):
        fraud_Amount = 0.8
        fraud_Time = 0.8
        fraud_TermId = 0.8
        abnormalType = {'abnormalAmount': True if random.random() < fraud_Amount else False,
                        'abnormalTime': True if random.random() < fraud_Time else False,
                        'abnormalS30': True if random.random() < fraud_TermId else False}
        return abnormalType

    def getTimeList(self, startDate='20220501', days=60, timeInterval=180, list_len=5, abnormalTime=False):
        '''
            startDate 到 startDate+days指的是时间列表起始时间的范围
            timeInterval指的是相邻交易的最大时间间隔，单位为分钟
            list_len:时间列表长度
            返回值：一个频繁时段内的时间列表
        '''
        # 发生测试交易的日期
        startDate = datetime.datetime.strptime(startDate, '%Y%m%d')
        days = random.randint(0, days)

        # 发生交易测试具体几点
        hours = random.randint(0, 23)
        # 偏向于非营业时间交易(22-6点)
        if abnormalTime==True:
            hours = random.randint(-2, 6)
            hours += 24
        # 分钟纳入考虑，秒钟忽略
        minutes = random.randint(0, 59)
        seconds = random.randint(0, 59)

        # 发生第一次交易的时间
        test_date = startDate + datetime.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)

        time_list = []
        time_list.append(test_date)
        for i in range(list_len-1):
            delt_min = random.randint(1, timeInterval)
            this_time = time_list[-1] + datetime.timedelta(minutes=delt_min)
            time_list.append(this_time)
        time_list = [str(t) for t in time_list]
        return time_list

    def getAmount(self, bottom=1000, top=10000, consumption_range=[33, 136], abnormalAmount=False):
        '''
        bottom: 金额下限
        top: 金额上限
        consumption_range: 店铺正常交易金额范围
        返回值: 实际交易金额
        '''
        if  abnormalAmount==True:
            # 随机决定异常小额或者异常大额
            p = random.random()
            if p < 0.5:
                amount = random.uniform(0.0002, 0.001) * bottom
            else:
                amount = random.uniform(3, 10) * top
            return int(amount)
        else:
            amount = random.randint(consumption_range[0], consumption_range[1])
            return amount

    # 随机商户，n就是quantity
    def pick_abnormal_Store(self, quantity):
        # 获取异常商户列表
        # 商户等级低中的概率较大
        '''

        :param quantity: 商户数量
        :return:
        '''
        store_list = []

        # 各类商户等级概率分布
        rank_prob = [0.4, 0.5, 0.1]

        # 各类等级商户数量:低、中、高
        low_rank_quantity = int(quantity * rank_prob[0])
        middle_rank_quantity = int(quantity * rank_prob[1])
        high_rank_quantity = int(quantity * rank_prob[2])

        jsonfile = BASE_DIR + '/src/json_file/store_rank_classes.json'
        store_rank_classes = read_json_file(jsonfile)
        low_sub_classes = []
        middle_sub_classes = []
        high_sub_classes = []

        for key, map in store_rank_classes.items():
            low_sub_classes.extend(map['低'])
            middle_sub_classes.extend(map['中'])
            high_sub_classes.extend(map['高'])

        # 获取所有商户列表
        stores = self.storeService.selectStores()
        random.shuffle(stores)

        # 遍历所有商户
        for store in stores:
            # 终止条件，使筛选的商户满足分布
            if low_rank_quantity == 0 and middle_rank_quantity == 0 and high_rank_quantity == 0:
                break

            # 获取商户类型
            rank = store.getLevel()

            # 筛选
            if rank in low_sub_classes and low_rank_quantity > 0:
                low_rank_quantity -= 1
                store_list.append(store)
            elif rank in middle_sub_classes and middle_rank_quantity > 0:
                middle_rank_quantity -= 1
                store_list.append(store)
            elif rank in high_sub_classes and high_rank_quantity > 0:
                high_rank_quantity -= 1
                store_list.append(store)

        return store_list

    # 随机用户
    def get_user(self):
        # 选出所有人
        user_list = self.userService.selectUsers()
        user = random.choice(user_list)
        return user

    def generate_abnormal_F16(self,store):
        store_id = store.getStore_id()

        F16s_str =  store.getS30()
        F16s = json.loads(F16s_str)

        # print("F16s_type", type(F16s) )

        #生成异常的
        ab_F16_num = random.choice([1,2,3,4,5,6])
        for num in range(ab_F16_num):
            F16 = id_generator(size=8, chars='1234567890')
            F16s[F16]="异常"
        # print("F16s",F16s)


        self.storeService.update_S30s(  store_id, F16s )
        store.setS30(json.dumps(F16s))


    def get_F16(self, store, abnormalS30=False):
        '''
        param:
        return:
        '''
        F16s_str = store.getS30()
        F16s = json.loads(F16s_str)

        candidate_F16 = []
        for key, value in F16s.items():
            if value == "异常" and abnormalS30 == True:
                candidate_F16.append(key)
            elif value == "正常" and abnormalS30==False:
                return key

        select_abnormal_term = random.choice(candidate_F16)
        return select_abnormal_term