# -*- coding:utf-8 -*-
# @Time     :2022/4/20 14:30
# @Author   :Guo Jiayu
import json
import random
import re
import math

from src.dataGen20220414.entity.Trans import Trans
from src.dataGen20220414.service.CardService import CardService
from src.dataGen20220414.service.TransService import TransService
from src.dataGen20220414.service.UserService import UserService
from src.dataGen20220414.service.StoreService import StoreService
from src.utils.config import BASE_DIR
from src.utils.data_distribution_fuction import gamma, normal
from src.utils.fraudSettings import FraudSettings
from src.utils.functions import getday, get_later_time, read_json_file


class CreditCardCashOutFactory:

    def __init__(self, personal_cash_out_ratio=0.7, personal_store_ratio=0.8, store_group_size_min = 4, store_group_size_max = 10, is_in_opening_time = 0.7):
        scene = "Credit_card_fraud"
        self.transService = TransService(scene)
        self.userService = UserService(scene)
        self.cardService = CardService(scene)
        self.storeService = StoreService(scene)
        self.personal_cash_out_ratio = personal_cash_out_ratio
        self.personal_store_ratio = personal_store_ratio
        self.store_group_size_min = store_group_size_min
        self.store_group_size_max = store_group_size_max
        self.is_in_opening_time = is_in_opening_time

    def generate_date(self, small_fraud_gap, big_fraud_gap, start_year, start_month, start_day, user_quantity=50,
                      store_quantity=50, duration=10):
        for i in range(duration):
            fraud_user, fraud_cards, fraud_deposit_card = self.get_fraud_user(quantity=user_quantity)
            fraud_store = self.get_fraud_store(quantity=store_quantity)
            _, (y, m, d) = getday(start_year, start_month, start_day, i)
            self.generate_date_(small_fraud_gap, big_fraud_gap, y, m, d, fraud_user, fraud_store,
                            fraud_cards, fraud_deposit_card)

    def generate_date_(self, small_fraud_gap, big_fraud_gap, start_year, start_month, start_day, fraud_user,
                       fraud_store, fraud_cards, fraud_deposit_card):
        personal_stores, store_groups = self.segment_stors_to_personal_or_group(fraud_store)

        for f_user in fraud_user:
            f_cards = fraud_cards[f_user.get_user_no()]
            f_deposit_cards = fraud_deposit_card[f_user.get_user_no()]

            card_index = random.randint(0, len(f_cards) - 1)

            self.cardService.updateCardState(f_cards[card_index].getC4(), 'Credit_card_fraud')

            card_deposit_index = random.randint(0, len(f_deposit_cards) - 1)

            is_personal_cash_out = self.is_personal_cash_out()

            if is_personal_cash_out:
                store_index = random.randint(0, len(personal_stores) - 1)

                store_m = personal_stores[store_index].getS1()
                store_card = personal_stores[store_index].getCard_id()

                # self.storeService.updateStoreState(fraud_store[store_index].getStore_id(), 'Credit_card_fraud')

                small_cash_out_times, big_cash_out_times = self.get_cash_out_times(user=f_user,
                                                                                   card=f_cards[card_index])

                d, _ = getday(start_year, start_month, start_day, 0)

                d_ = self.get_trans_time(store=fraud_store[store_index])

                # quota = self.get_card_quota(f_cards[card_index])

                amount = self.get_trans_amount(user=f_user, card=f_cards[card_index])
                S30s = json.loads(personal_stores[store_index].getS30())
                S30 = "00000000"
                for key, value in S30s.items():
                    if value == "Normal":
                        S30 = key
                        break
                trans = self.get_trans_info(f_cards[card_index].getC4(), amount, d_, d,
                                            f_cards[card_index].getC5(), store_m, store_card, S30)
                # print(trans)
                self.transService.insertTrans(trans)

                cur = d + d_[0:2]

                amount_back = int(amount * 0.95)
                trans_back_time = get_later_time(cur, duration=random.randint(0, 24))
                m_and_s = self.get_minute_and_second()
                trans_back = self.get_trans_back_info(store_card,
                                                      amount_back,
                                                      trans_back_time[8:10] + m_and_s, trans_back_time[0:8],
                                                      f_deposit_cards[card_deposit_index].getC4())
                # print(trans_back)
                self.transService.insertTrans(trans_back)

                for _ in range(small_cash_out_times):
                    gap = random.randint(0, small_fraud_gap)

                    cur = get_later_time(cur, gap)

                    m_and_s = self.get_minute_and_second()

                    amount = self.get_trans_amount(user=f_user,
                                                   card=f_cards[card_index])

                    trans = self.get_trans_info(f_cards[card_index].getC4(), amount, cur[8:10] + m_and_s,
                                                cur[0:8],
                                                f_cards[card_index].getC5(), store_m,store_card, S30)
                    # print(trans)
                    self.transService.insertTrans(trans)
                    amount_back = int(amount * 0.95)
                    trans_back_time = get_later_time(cur, duration=random.randint(0, 24))
                    m_and_s = self.get_minute_and_second()
                    trans_back = self.get_trans_back_info(store_card,
                                                          amount_back,
                                                          trans_back_time[8:10] + m_and_s, trans_back_time[0:8],
                                                          f_deposit_cards[card_deposit_index].getC4())
                    # print(trans_back)
                    self.transService.insertTrans(trans_back)

                for _ in range(big_cash_out_times):
                    gap = random.randint(20, big_fraud_gap)

                    d, _ = getday(int(d[0:4]), int(d[4:6]), int(d[6:8]), gap)

                    d_ = self.get_trans_time(store=fraud_store[store_index])

                    amount = self.get_trans_amount(user=f_user,
                                                   card=f_cards[card_index])

                    trans = self.get_trans_info(f_cards[card_index].getC4(), amount, d_, d,
                                                f_cards[card_index].getC5(), store_m,store_card, S30)

                    # print(trans)
                    self.transService.insertTrans(trans)

                    amount_back = int(amount * 0.95)
                    cur = d + d_[0:2]
                    trans_back_time = get_later_time(cur, duration=random.randint(0,24))
                    m_and_s = self.get_minute_and_second()
                    trans_back = self.get_trans_back_info(store_card,
                                                          amount_back,
                                                          trans_back_time[8:10] + m_and_s, trans_back_time[0:8],
                                                          f_deposit_cards[card_deposit_index].getC4())
                    # print(trans_back)
                    self.transService.insertTrans(trans_back)

            else:
                group_index = random.randint(0, len(store_groups) - 1)

                group = store_groups[group_index]

                store_index = random.randint(0, len(group) - 1)

                small_cash_out_times, big_cash_out_times = self.get_cash_out_times(user=f_user,
                                                                                   card=f_cards[card_index])

                amount = self.get_trans_amount(user=f_user, card=f_cards[card_index])

                d, _ = getday(start_year, start_month, start_day, 0)

                d_ = self.get_trans_time(store=fraud_store[store_index])

                S30s = json.loads(group[store_index].getS30())
                S30 = "00000000"
                for key, value in S30s.items():
                    if value == "Normal":
                        S30 = key
                        break

                trans = self.get_trans_info(f_cards[card_index].getC4(), amount, d_, d,
                                            f_cards[card_index].getC5(), group[store_index].getS1(), group[store_index].getCard_id(), S30)
                self.transService.insertTrans(trans)
                # print(trans)

                cur = d + d_[0:2]

                amount_back = int(amount * 0.95)
                trans_back_time = get_later_time(cur, duration=random.randint(0, 24))
                m_and_s = self.get_minute_and_second()
                trans_back = self.get_trans_back_info(group[store_index].getCard_id(),
                                                      amount_back,
                                                      trans_back_time[8:10] + m_and_s, trans_back_time[0:8],
                                                      f_deposit_cards[card_deposit_index].getC4())
                # print(trans_back)
                self.transService.insertTrans(trans_back)

                for _ in range(small_cash_out_times):
                    gap = random.randint(0, small_fraud_gap)

                    cur = get_later_time(cur, gap)

                    m_and_s = self.get_minute_and_second()

                    amount = self.get_trans_amount(user=f_user,
                                                   card=f_cards[card_index])

                    store_index = random.randint(0, len(group) - 1)

                    S30s = json.loads(group[store_index].getS30())
                    S30 = "00000000"
                    for key, value in S30s.items():
                        if value == "Normal":
                            S30 = key
                            break

                    trans = self.get_trans_info(f_cards[card_index].getC4(), amount, cur[8:10] + m_and_s,
                                                cur[0:8],
                                                f_cards[card_index].getC5(), group[store_index].getS1(), group[store_index].getCard_id(), S30)
                    self.transService.insertTrans(trans)
                    # print(trans)

                    amount_back = int(amount * 0.95)
                    trans_back_time = get_later_time(cur, duration=random.randint(0,24))
                    m_and_s = self.get_minute_and_second()
                    trans_back = self.get_trans_back_info(group[store_index].getCard_id(),
                                                          amount_back,
                                                          trans_back_time[8:10] + m_and_s, trans_back_time[0:8],
                                                          f_deposit_cards[card_deposit_index].getC4())
                    # print(trans_back)
                    self.transService.insertTrans(trans_back)

                for _ in range(big_cash_out_times):
                    gap = random.randint(20, big_fraud_gap)

                    d, _ = getday(int(d[0:4]), int(d[4:6]), int(d[6:8]), gap)

                    d_ = self.get_trans_time(store=fraud_store[store_index])

                    amount = self.get_trans_amount(user=f_user,
                                                   card=f_cards[card_index])

                    store_index = random.randint(0, len(group) - 1)

                    S30s = json.loads(group[store_index].getS30())
                    S30 = "00000000"
                    for key, value in S30s.items():
                        if value == "Normal":
                            S30 = key
                            break

                    trans = self.get_trans_info(f_cards[card_index].getC4(), amount, d_, d,
                                                f_cards[card_index].getC5(), group[store_index].getS1(),group[store_index].getCard_id(), S30)


                    # print(trans)

                    self.transService.insertTrans(trans)

                    amount_back = int(amount * 0.95)
                    cur = d + d_[0:2]
                    trans_back_time = get_later_time(cur, duration=random.randint(0,24))
                    m_and_s = self.get_minute_and_second()
                    trans_back = self.get_trans_back_info(group[store_index].getCard_id(),
                                                          amount_back,
                                                          trans_back_time[8:10] + m_and_s, trans_back_time[0:8],
                                                          f_deposit_cards[card_deposit_index].getC4())
                    # print(trans_back)
                    self.transService.insertTrans(trans_back)


    def is_personal_cash_out(self):
        ratio = 0.7

        if random.random() < self.personal_cash_out_ratio:
            return True
        else:
            return False

    def get_trans_info(self, T1, T17, T19, T23, C5, T25, T37, S30):
        trans = Trans(id=0, T2='01', T1=T1,
                      T6='0', T14='4', T17=T17,
                      T19=T19, T23=T23,
                      T26=C5,
                      T37=T37,
                      T25=T25,
                      T31=S30,
                      abnormal=1,
                      abnormal_state={"Gambling_violation": 0, "Fake_registration": 0,"Credit_card_fraud":1, "Scalper_marketing":0, "Merchant_violation":0,"Abnormal_transfer":0}
                      )
        return trans

    def get_trans_back_info(self, T1, T17, T19, T23,
                            T37):
        trans = Trans(id=0, T2='03', T1=T1,
                      T6='0', T14='4', T17=T17,
                      T19=T19, T23=T23,
                      T26='01',
                      T37=T37,
                      T25='000000000000000',
                      T31='00000000',
                      abnormal=0,
                      abnormal_state={"Gambling_violation": 0, "Fake_registration": 0,"Credit_card_fraud":0, "Scalper_marketing":0, "Merchant_violation":0,"Abnormal_transfer":0}
                      )
        return trans

    def get_fraud_user(self, quantity):
        fraud_user = []

        fraud_cards = {}
        fraud_deposit_card = {}

        all_users = self.userService.selectAllUser()

        random.shuffle(all_users)

        for user in all_users:
            cards = user.getCard()
            cards = json.loads(cards)

            credit_cards = []
            deposit_cards = []
            for card in cards:
                c_info = self.cardService.getCardInfoByC4(card['C4'])


                C8 = c_info.getC8()

                C7 = c_info.getC7()

                C5 = c_info.getC5()

                if C8 != None and C8 != '--' and C7 != 'Card_A':
                    credit_cards.append(c_info)
                if C5 == "01":
                    deposit_cards.append(c_info)
            if len(credit_cards) > 0:
                fraud_user.append(user)

                fraud_cards[user.get_user_no()] = credit_cards
                fraud_deposit_card[user.get_user_no()] = deposit_cards
            if len(fraud_user) == quantity:
                break
        for u in fraud_user:
            self.userService.updateUserState(user_id=u.id, fraud_category='Credit_card_fraud')

        return fraud_user, fraud_cards, fraud_deposit_card

    def get_fraud_store(self, quantity):
        store_list = []

        rank_prob = [0.4, 0.5, 0.1]

        low_rank_quantity = int(quantity * rank_prob[0])
        middle_rank_quantity = int(quantity * rank_prob[1])
        high_rank_quantity = int(quantity * rank_prob[2])

        jsonfile = BASE_DIR + '/src/json_file/store_rank_classes.json'
        store_rank_classes = read_json_file(jsonfile)
        low_sub_classes = []
        middle_sub_classes = []
        high_sub_classes = []

        for key, map in store_rank_classes.items():
            low_sub_classes.extend(map['Low'])
            middle_sub_classes.extend(map['Medium'])
            high_sub_classes.extend(map['High'])


        stores = self.storeService.selectStores()
        random.shuffle(stores)

        for store in stores:
            if low_rank_quantity == 0 and middle_rank_quantity == 0 and high_rank_quantity == 0:
                break


            rank = store.getLevel()

            if rank in low_sub_classes and low_rank_quantity > 0:
                low_rank_quantity -= 1
                store_list.append(store)
            elif rank in middle_sub_classes and middle_rank_quantity > 0:
                middle_rank_quantity -= 1
                store_list.append(store)
            elif rank in high_sub_classes and high_rank_quantity > 0:
                high_rank_quantity -= 1
                store_list.append(store)

        for store in store_list:
            self.storeService.updateStoreState(store.getStore_id(), 'Credit_card_fraud')
        return store_list

    def segment_stors_to_personal_or_group(self, stores):

        random.shuffle(stores)

        personal_ratio = self.personal_store_ratio

        personal_stores = stores[0: int(len(stores) * personal_ratio)]

        stores = stores[len(personal_stores):]

        lens = len(stores)

        group_size = [int(self.store_group_size_min), int(self.store_group_size_max)]

        stores_groups = []

        choose_stores_num = 0

        while True:
            cur_size = random.randint(group_size[0], group_size[1])

            if cur_size + choose_stores_num < lens:
                group = stores[choose_stores_num: choose_stores_num + cur_size]
                stores_groups.append(group)
            else:
                group = stores[choose_stores_num:]
                stores_groups.append(group)
                break
            choose_stores_num += cur_size

        return personal_stores, stores_groups

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

    def get_trans_amount(self, user, card):
        n_age = user.getAge()

        n_wage = user.getWage()
        fs = FraudSettings(n_wage)
        n_age_lvl = fs.get_age_lvl_from_age(n_age)
        # print(n_age_lvl)
        amount = fs.generate_basic_fraud_amount(fraud_scene_multi=1.5, age_lvl=n_age_lvl)

        card_amount = 0

        quota = self.get_card_quota(card)

        # rate = 0.05

        gamma_amount = gamma(shape=2., scale=3., size=1, multi=800)[0]

        wage_raito = 0.3

        gamma_raito = 0.7

        amount = amount * wage_raito + int(gamma_amount * gamma_raito)

        while amount > quota:
            amount *= 0.95

        amount = int(amount / 10) * 10

        if random.random() > 0.5:
            if amount < 100:
                return amount
            elif amount < 10000:
                amount = int(amount / 100) * 100
            else:
                amount = int(amount / 1000) * 1000
        else:
            amount -= random.randint(1, 5)

        return amount

    def get_cash_out_times(self, user, card):
        s = math.ceil(gamma(1.5, 2., 1, 1)[0])
        b = math.ceil(gamma(1.5, 2., 1, 1)[0])
        return s, b

    def get_minute_and_second(self):
        m = "%02d" % random.randint(0, 59)
        s = "%02d" % random.randint(0, 59)
        return str(m) + str(s)


    def get_card_quota(self, card):
        C8 = card.getC8()
        quota = 0
        if C8 == "01":
            while quota < 1000 or quota > 10000:
                quota = normal(5000, 2000)
        elif C8 == "02":
            while quota < 10000 or quota > 50000:
                quota = normal(30000, 8000)
        elif C8 == "02":
            while quota < 10000 or quota > 50000:
                quota = normal(30000, 6000)[0]
        elif C8 == "03":
            quota = gamma(shape=8., scale=9., size=1, multi=2000)[0]
        return quota


if __name__ == '__main__':
    cccof = CreditCardCashOutFactory()
    cccof.generate_date(small_fraud_gap=5, big_fraud_gap=50, start_year=2021, start_month=1, start_day=1,
                        user_quantity=20, store_quantity=10)
    # store_list = cccof.get_fraud_store(100)
    # p, g = cccof.segment_stors_to_personal_or_group(store_list)
    # for i in g:
    #     print(len(i))
    # print(g)
    # print(p)
    # print(len(p))
    # print(int('02'))
