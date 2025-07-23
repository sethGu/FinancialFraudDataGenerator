# -*- coding:utf-8 -*-
# @Time     :2022/7/5 12:52
# @Author   :Guo Jiayu
import json
import math
import random
import re

from src.dataGen20220414.service.CardService import CardService
from src.dataGen20220414.service.StoreService import StoreService
from src.dataGen20220414.service.TransService import TransService
from src.dataGen20220414.service.UserService import UserService
from src.utils.comsumptionFunction import get_amount
from src.utils.functions import getday, get_later_time, get_before_time
from src.dataGen20220414.entity.Trans import Trans
from src.utils.data_distribution_fuction import gamma


class MarketingFraudFactory:
    def __init__(self, is_in_opening_time=1, cloth_ratio=0.45, life_service_ratio=0.45):
        scene = "黄牛营销欺诈"
        self.transService = TransService(scene)
        self.userService = UserService(scene)
        self.cardService = CardService(scene)
        self.storeService = StoreService(scene)
        # 异常交易产生于商户营业时间内的概率
        self.is_in_opening_time = is_in_opening_time

        #*********************************
        # 衣着美容行业的概率
        self.cloth_ratio = cloth_ratio
        # 生活用品及服务行业的概率
        self.life_service_ratio = life_service_ratio
        # 二者概率和不得超过 1
        #*********************************

    def generate_data(self, fraud_user_quantity, store_quantity, start_year, start_month, start_day, duration):
        # 确定欺诈用户候选列表的size (即欺诈用户集合的size)
        fraud_candidate_num = fraud_user_quantity * 3
        fraud_candidate, normal_user = self.get_fraud_candidate(fraud_candidate_num)

        for i in range(duration):
            fraud_user = self.get_fraud_user(fraud_candidate, fraud_user_quantity)  # 从欺诈候选中获取欺诈用户
            store_list = self.get_stores(store_quantity)  # 获取受欺诈商户列表
            _, (y, m, d) = getday(start_year, start_month, start_day, i)  # 生成duration中第i天的年月日
            self.generate_data_(fraud_user, normal_user, store_list, y, m, d)  # 传入的是新的(year,month,day)

    def generate_data_(self, fraud_user, normal_user, store_list, start_year, start_month, start_day):
        for f_user in fraud_user:
            self.userService.updateUserState(user_id=f_user.id, fraud_category='黄牛营销欺诈')

            # 获取一定数量的正常用户 （先得到数量，再随机选择）
            normal_user_num = self.get_normal_user_num()  # 得到数量

            cur_normal_user = [random.choice(normal_user) for _ in range(normal_user_num)]  # 随机选择一群

            cur_store = random.choice(store_list)  # 从受欺诈商户列表中随机选择一个商户

            # 20%的用户是正常消费 （normal_user_num中的20%）
            # for _ in range(int(normal_user_num * 0.2)):

            # 获取用户信息  （欺诈用户信息）
            f_info = f_user.get_user_info()
            f_cards = f_info['cards']
            f_cards = json.loads(f_cards)
            f_card = random.choice(f_cards)
            # 更新数据库
            self.cardService.updateCardState(f_card['C4'], '黄牛营销欺诈')
            # 80%的用户异常消费
            for user in cur_normal_user:

                n_info = user.get_user_info()
                # 提取银行卡数据
                n_cards = n_info['cards']

                n_cards = json.loads(n_cards)

                n_card = random.choice(n_cards)

                # 生成商户交易信息
                trans_day, _ = getday(start_year, start_month, start_day, 0)
                trans_time = self.get_trans_time(cur_store)  # 向商户交易的时分秒

                amount = int(random.uniform(0.6, 0.9) * self.get_trans_amount(cur_store))
                S30s = json.loads(cur_store.getS30())
                S30 = "00000000"
                for key, value in S30s.items():
                    if value == "正常":
                        S30 = key
                        break
                trans = Trans(id=0, T2='01', T1=n_card['C4'],
                              T6='0', T14='4', T17=amount,
                              T19=trans_time, T23=str(trans_day),
                              T26=n_card['C5'],
                              T37=cur_store.card_id,
                              T25=cur_store.S1,
                              T31=S30,
                              abnormal=0,
                              abnormal_state={"赌博违规交易": 0, "伪冒注册欺诈": 0, "信用卡违规套现": 0, "黄牛营销欺诈": 0,
                                              "商户违规": 0, "异常转账": 0}
                              )
                self.transService.insertTrans(trans)

                # 给黄牛用户的小额转账
                amount = int(random.uniform(0.6, 0.9) * amount)

                user_store_trans_time = trans_day + trans_time    #向商户消费的年月日时分秒

                # 获取消费者向黄牛转账的年月日时分秒，在向商户消费的基础上随机向前
                user_fraud_trans_time = get_before_time(user_store_trans_time)

                y_m_d=user_fraud_trans_time[:8]  #年月日
                h_m_s=user_fraud_trans_time[8:14]  #时分秒

                trans = Trans(id=0, T2='03', T1=n_card['C4'],
                              T6='0', T14='4', T17=amount,
                              T19=h_m_s, T23=y_m_d,
                              T26=n_card['C5'],
                              T37=f_card['C4'],
                              T25='000000000000000',
                              T31='00000000',
                              abnormal=1,
                              abnormal_state={"赌博违规交易": 0, "伪冒注册欺诈": 0, "信用卡违规套现": 0, "黄牛营销欺诈": 1,
                                              "商户违规": 0, "异常转账": 0}
                              )
                self.transService.insertTrans(trans)

    def get_trans_time(self, store):

        # 营业时间内概率与营业时间外概率
        time_prob = [self.is_in_opening_time, 1 - self.is_in_opening_time]

        # 随机产生数来确定是否营业时间内
        r = random.random()  # 取值范围[0,1)，全在营业时间内
        in_business = True if r <= time_prob[0] else False

        # 商户营业时间
        opening_time = store.getOpen_duration()

        ## 将营业时间转换为当天的分钟
        # 最小分钟数
        min_minute = 0

        # 最大分钟数
        max_minute = 24 * 60

        patten = '(\d{1,2}:\d{1,2})'
        # ['9:00', '15:00']
        duration = re.findall(patten, opening_time)

        # 开始、结束营业分钟数
        start_minute, end_minute = min_minute, max_minute

        # 计算开始、结束营业分钟数
        for i in range(2):
            r = re.findall('(\d{1,2})', duration[i])

            # 开始时间
            if i == 0:
                start_minute = int(r[0]) * 60 + int(r[1])
            # 结束时间
            else:
                end_minute = int(r[0]) * 60 + int(r[1])

        # 生成交易分钟
        trans_time = 0

        # 若全天营业则设in_business为True
        if start_minute == min_minute and end_minute == max_minute:
            in_business = True

        # 如果在营业时间内
        if in_business:
            trans_time = random.randint(start_minute, end_minute)
        # 如果不在营业时间内
        else:
            # 随机选择是营业前还是营业后
            # 营业前后均还有时间
            if start_minute > min_minute and end_minute < max_minute:
                if random.random() < 0.5:
                    trans_time = random.randint(min_minute, start_minute)  # 营业前
                else:
                    trans_time = random.randint(end_minute, max_minute)  # 营业后
            elif start_minute == min_minute:
                trans_time = random.randint(end_minute, max_minute)
            else:
                trans_time = random.randint(min_minute, start_minute)

        # 转为按时间的字符串 并拼接秒
        trans_time = str("%02d" % (int(trans_time / 60) % 24)) + \
                     str("%02d" % int(trans_time % 60)) + \
                     str("%02d" % random.randint(0, 59))

        return trans_time

    def get_trans_amount(self, store):
        return get_amount(store)

    # 打乱用户顺序，根据数量参数，将用户列表划分为欺诈用户候选列表和正常用户列表
    def get_fraud_candidate(self, fraud_candidate_num):
        users = self.userService.selectAllUser()
        random.shuffle(users)
        fraud_candidate = users[:fraud_candidate_num]
        normal_user = users[fraud_candidate_num:]
        return fraud_candidate, normal_user

    # 从欺诈用户候选列表中抽取一部分作为某天的欺诈用户，以避免每次从所有用户中随机选择，一个duration后几乎都是欺诈用户
    def get_fraud_user(self, fraud_candidate, quantity):
        random.shuffle(fraud_candidate)
        fraud_user = fraud_candidate[:quantity]
        return fraud_user

    def get_stores(self, quantity):
        stores = self.storeService.selectStores()
        random.shuffle(stores)

        # 各行业概率
        # 衣着美容、生活用品及服务、其他
        store_type = [self.cloth_ratio, self.life_service_ratio, 1 - self.cloth_ratio - self.life_service_ratio]

        store_num = [0, 0, 0]

        store_list = []

        for i, v in enumerate(store_type):
            store_num[i] = math.ceil(v * quantity)  # math.ceil()向上取整，获得各行业数量

        for store in stores:
            if store_num[0] == 0 and store_num[1] == 0 and store_num[2] == 0:
                break
            if store.industry == '衣着美容' and store_num[0] > 0:
                store_list.append(store)
                store_num[0] -= 1
                continue
            if store.industry == '生活用品及服务' and store_num[1] > 0:
                store_list.append(store)
                store_num[1] -= 1
                continue
            if store.industry != '衣着美容' and store.industry != '生活用品及服务' and store_num[2] > 0:
                store_list.append(store)
                store_num[2] -= 1
                continue

        return store_list

    # gamma分布，返回偏态随机数，函数在utils.data_distribution_fuction中
    def get_normal_user_num(self):
        return int(gamma(4., 2., 1, 1))

    # 获取消费时间（分秒）
    def get_minute_and_second(self):
        m = "%02d" % random.randint(0, 59)
        s = "%02d" % random.randint(0, 59)
        return str(m) + str(s)


if __name__ == '__main__':
    mff = MarketingFraudFactory()
    mff.generate_data(fraud_user_quantity=10, store_quantity=5, start_year=2022, start_month=9, start_day=1,
                      duration=10)
