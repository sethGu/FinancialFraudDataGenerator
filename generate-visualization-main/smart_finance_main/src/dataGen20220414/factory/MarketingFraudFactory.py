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
        scene = "Scalper_marketing"
        self.transService = TransService(scene)
        self.userService = UserService(scene)
        self.cardService = CardService(scene)
        self.storeService = StoreService(scene)
        self.is_in_opening_time = is_in_opening_time

        #*********************************
        self.cloth_ratio = cloth_ratio
        self.life_service_ratio = life_service_ratio
        #*********************************

    def generate_data(self, fraud_user_quantity, store_quantity, start_year, start_month, start_day, duration):
        fraud_candidate_num = fraud_user_quantity * 3
        fraud_candidate, normal_user = self.get_fraud_candidate(fraud_candidate_num)

        for i in range(duration):
            fraud_user = self.get_fraud_user(fraud_candidate, fraud_user_quantity)
            store_list = self.get_stores(store_quantity)
            _, (y, m, d) = getday(start_year, start_month, start_day, i)
            self.generate_data_(fraud_user, normal_user, store_list, y, m, d)

    def generate_data_(self, fraud_user, normal_user, store_list, start_year, start_month, start_day):
        for f_user in fraud_user:
            self.userService.updateUserState(user_id=f_user.id, fraud_category='Scalper_marketing')

            normal_user_num = self.get_normal_user_num()

            cur_normal_user = [random.choice(normal_user) for _ in range(normal_user_num)]

            cur_store = random.choice(store_list)

            f_info = f_user.get_user_info()
            f_cards = f_info['cards']
            f_cards = json.loads(f_cards)
            f_card = random.choice(f_cards)

            self.cardService.updateCardState(f_card['C4'], 'Scalper_marketing')
            for user in cur_normal_user:

                n_info = user.get_user_info()

                n_cards = n_info['cards']

                n_cards = json.loads(n_cards)

                n_card = random.choice(n_cards)

                trans_day, _ = getday(start_year, start_month, start_day, 0)
                trans_time = self.get_trans_time(cur_store)

                amount = int(random.uniform(0.6, 0.9) * self.get_trans_amount(cur_store))
                S30s = json.loads(cur_store.getS30())
                S30 = "00000000"
                for key, value in S30s.items():
                    if value == "Normal":
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
                              abnormal_state={"Gambling_violation": 0, "Fake_registration": 0,"Credit_card_fraud":0, "Scalper_marketing":0, "Merchant_violation":0,"Abnormal_transfer":0}
                              )
                self.transService.insertTrans(trans)

                amount = int(random.uniform(0.6, 0.9) * amount)

                user_store_trans_time = trans_day + trans_time

                user_fraud_trans_time = get_before_time(user_store_trans_time)

                y_m_d=user_fraud_trans_time[:8]
                h_m_s=user_fraud_trans_time[8:14]

                trans = Trans(id=0, T2='03', T1=n_card['C4'],
                              T6='0', T14='4', T17=amount,
                              T19=h_m_s, T23=y_m_d,
                              T26=n_card['C5'],
                              T37=f_card['C4'],
                              T25='000000000000000',
                              T31='00000000',
                              abnormal=1,
                              abnormal_state={"Gambling_violation":0, "Fake_registration":0,"Credit_card_fraud":0, "Scalper_marketing":1, "Merchant_violation":0,"Abnormal_transfer":0}
                              )
                self.transService.insertTrans(trans)

    def get_trans_time(self, store):
        time_prob = [self.is_in_opening_time, 1 - self.is_in_opening_time]

        r = random.random()
        in_business = True if r <= time_prob[0] else False

        opening_time = store.getOpen_duration()

        min_minute = 0

        max_minute = 24 * 60

        patten = '(\d{1,2}:\d{1,2})'
        # ['9:00', '15:00']
        duration = re.findall(patten, opening_time)

        start_minute, end_minute = min_minute, max_minute

        for i in range(2):
            r = re.findall('(\d{1,2})', duration[i])

            if i == 0:
                start_minute = int(r[0]) * 60 + int(r[1])
            else:
                end_minute = int(r[0]) * 60 + int(r[1])

        trans_time = 0

        if start_minute == min_minute and end_minute == max_minute:
            in_business = True

        if in_business:
            trans_time = random.randint(start_minute, end_minute)
        else:
            if start_minute > min_minute and end_minute < max_minute:
                if random.random() < 0.5:
                    trans_time = random.randint(min_minute, start_minute)
                else:
                    trans_time = random.randint(end_minute, max_minute)
            elif start_minute == min_minute:
                trans_time = random.randint(end_minute, max_minute)
            else:
                trans_time = random.randint(min_minute, start_minute)

        trans_time = str("%02d" % (int(trans_time / 60) % 24)) + \
                     str("%02d" % int(trans_time % 60)) + \
                     str("%02d" % random.randint(0, 59))

        return trans_time

    def get_trans_amount(self, store):
        return get_amount(store)

    def get_fraud_candidate(self, fraud_candidate_num):
        users = self.userService.selectAllUser()
        random.shuffle(users)
        fraud_candidate = users[:fraud_candidate_num]
        normal_user = users[fraud_candidate_num:]
        return fraud_candidate, normal_user

    def get_fraud_user(self, fraud_candidate, quantity):
        random.shuffle(fraud_candidate)
        fraud_user = fraud_candidate[:quantity]
        return fraud_user

    def get_stores(self, quantity):
        stores = self.storeService.selectStores()
        random.shuffle(stores)

        store_type = [self.cloth_ratio, self.life_service_ratio, 1 - self.cloth_ratio - self.life_service_ratio]

        store_num = [0, 0, 0]

        store_list = []

        for i, v in enumerate(store_type):
            store_num[i] = math.ceil(v * quantity)

        for store in stores:
            if store_num[0] == 0 and store_num[1] == 0 and store_num[2] == 0:
                break
            if store.industry == 'Clothing_and_beauty' and store_num[0] > 0:
                store_list.append(store)
                store_num[0] -= 1
                continue
            if store.industry == 'Household_items_and_services' and store_num[1] > 0:
                store_list.append(store)
                store_num[1] -= 1
                continue
            if store.industry != 'Clothing_and_beauty' and store.industry != 'Household_items_and_services' and store_num[2] > 0:
                store_list.append(store)
                store_num[2] -= 1
                continue

        return store_list

    def get_normal_user_num(self):
        return int(gamma(4., 2., 1, 1))

    def get_minute_and_second(self):
        m = "%02d" % random.randint(0, 59)
        s = "%02d" % random.randint(0, 59)
        return str(m) + str(s)


if __name__ == '__main__':
    mff = MarketingFraudFactory()
    mff.generate_data(fraud_user_quantity=10, store_quantity=5, start_year=2022, start_month=9, start_day=1,
                      duration=10)
