# -*- coding:utf-8 -*-
# @Time     :2022/4/28 17:54
# @Author   :Guo Jiayu
import copy
import json
import random
import re

from src.dataGen20220414.entity.Trans import Trans
from src.dataGen20220414.service.CardService import CardService
from src.dataGen20220414.service.TransService import TransService
from src.dataGen20220414.service.UserService import UserService
from src.dataGen20220414.service.StoreService import StoreService
from src.utils.config import BASE_DIR
from src.utils.data_distribution_fuction import gamma, normal
from src.utils.fraudSettings import FraudSettings
from src.utils.functions import getday, get_later_time, read_json_file


class GamblingTransFactory():

    def __init__(self, is_in_opening_time=0.8, personal_trans_time_ratio=0.7, low_rank_store_ratio=0.3, middle_rank_store_ratio=0.6, high_rank_store_ratio=0.1,
                 gambling_user_ratio = 0.7):
        scene = "Gambling_violation"
        self.transService = TransService(scene)
        self.userService = UserService(scene)
        self.cardService = CardService(scene)
        self.storeService = StoreService(scene)
        self.is_in_opening_time = is_in_opening_time
        self.personal_trans_time_ratio = personal_trans_time_ratio

        self.low_rank_store_ratio = low_rank_store_ratio

        self.middle_rank_store_ratio = middle_rank_store_ratio

        self.high_rank_store_ratio = high_rank_store_ratio

        self.gambling_user_ratio = gambling_user_ratio

    def generate_date(self, year, month, day, duration, store_quantity, user_quantity):
        stores = self.get_gambling_stores(store_quantity)
        # print("stores:", len(stores))
        users, cards = self.get_gambling_users(user_quantity)
        users = list(users)
        stores1 = stores[0: int(store_quantity * 0.6)]
        stores2 = stores[int(store_quantity * 0.6): int(store_quantity * 0.8)]
        stores3 = stores[int(store_quantity * 0.8):]

        user1 = users[0: int(user_quantity / 3)]
        user2 = users[int(user_quantity / 3): 2 * int(user_quantity / 3)]
        user3 = users[2 * int(user_quantity / 3):]

        platform, bank = self.segment_stores_to_two_type(stores1)

        self.trans_list = []
        print('Scenario 1 ')
        self.generate_store_abnormal_data(year, month, day, platform, bank, user1, cards, duration)
        print("Scenario 1 has been generated" + str(len(self.trans_list)) + "data entries")
        num_1 = len(self.trans_list)
        gambling_user, false_user = self.segment_user_to_two_type(user2)
        print('Scenario 2 ')
        self.generate_false_user_data(year, month, day, gambling_user, false_user, cards, stores2, duration)
        print("Scenario 2 has been generated" + str(len(self.trans_list)-num_1) + "data entries")
        num_2 = len(self.trans_list)
        print('Scenario 3 ')
        gambling_user, lease_user = self.segment_user_to_two_type(user3)
        self.generate_lease_user_data(year, month, day, gambling_user, lease_user, cards, stores3, duration)
        print("Scenario 3 has been generated" + str(len(self.trans_list) - num_2) + "data entries")

    def generate_lease_user_data(self, year, month, day, gambling_user, lease_user, card, bank, duration):
        cash_in, other = lease_user[0: int(len(lease_user) * 0.5)], lease_user[int(len(lease_user) * 0.5):]

        for i in range(duration):
            # print(i)
            d, _ = getday(year, month, day, i)

            lease_card_trans = self.generate_personal_trans(gambling_user, cash_in, card, d)

            other_user_cards = []
            for user in other:
                other_user_cards.extend(card[user.get_user_no()])

            for key in lease_card_trans:
                cards = copy.deepcopy(other_user_cards)

                transfer_times = self.get_transfer_times()

                last_time = lease_card_trans[key]['last_time']
                amount_sum = lease_card_trans[key]['amount_sum']

                last_trans_card = None
                previous_trans_card = key

                other_user_cards_nums = len(other_user_cards)
                if other_user_cards_nums < transfer_times:
                    transfer_times = other_user_cards_nums
                for _ in range(transfer_times):
                    random.shuffle(cards)
                    last_trans_card = cards[0]
                    last_time = get_later_time(d + last_time[0:2], random.randint(1, 24))

                    m_and_s = self.get_minute_and_second()
                    if _ == 0:
                        trans = self.get_trans_info('03',last_trans_card.getC4(), amount_sum,
                                                    last_time[8:10] + m_and_s, last_time[0: 8],
                                                    last_trans_card.getC5(), '000000000000000', previous_trans_card, S30='00000000')
                        previous_trans_card  =  last_trans_card.getC4()
                    else:
                        trans = self.get_trans_info('03', last_trans_card.getC4(), amount_sum,
                                                    last_time[8:10] + m_and_s, last_time[0: 8],
                                                    last_trans_card.getC5(), '000000000000000', previous_trans_card, S30='00000000')
                        previous_trans_card  =  last_trans_card.getC4()
                    self.trans_list.append(trans)
                    self.transService.insertTrans(trans)
                    del cards[0]

                trans_time = get_later_time(last_time, random.randint(1, 24))
                m_and_s = self.get_minute_and_second()
                bank_index = random.randint(0, len(bank) - 1)
                c_info = self.cardService.getCardInfoByC4(bank[bank_index].getCard_id())
                trans = self.get_trans_info('03', c_info.getC4(), amount_sum, trans_time[8: 10] + m_and_s,
                                            trans_time[0: 8], c_info.getC5(),
                                            '000000000000000', last_trans_card.getC4(), S30='00000000')
                # print(trans)
                self.trans_list.append(trans)
                self.transService.insertTrans(trans)

    def generate_false_user_data(self, year, month, day, gambling_user, false_user, card, bank, duration):
        for i in range(duration):
            d, _ = getday(year, month, day, i)
            false_card_trans = self.generate_personal_trans(gambling_user, false_user, card, d)

            for key in false_card_trans.keys():
                info = false_card_trans[key]

                last_time = d + info['last_time'][0:2]

                trans_time = get_later_time(last_time, random.randint(1, 24))

                m_and_s = self.get_minute_and_second()
                bank_index = random.randint(0, len(bank) - 1)

                c_info = self.cardService.getCardInfoByC4(bank[bank_index].getCard_id())

                trans = self.get_trans_info('03', c_info.getC4(), info['amount_sum'], trans_time[8: 10] + m_and_s,
                                            trans_time[0: 8], c_info.getC5(),
                                            '000000000000000', key, S30='00000000')
                self.trans_list.append(trans)
                self.transService.insertTrans(trans)

    def generate_store_abnormal_data(self, year, month, day, gambling_platform, bank, gambling_users, user_card,duration):
        sgambling_platform2gambling_user = {}
        for platform in gambling_platform:
            sgambling_platform2gambling_user[platform] = []
        for user in gambling_users:
            try:
                num = self.random_pick([1,2,3],[0.6,0.3,0.1])
            except  Exception as e:
                print(e)
            platforms= random.sample(gambling_platform, num)
            for platform in platforms:
                sgambling_platform2gambling_user[platform].append(user)

        for i in range(duration):
            # print(i)
            d, _ = getday(year, month, day, i)
            for platform in gambling_platform:
                # print("platform:")
                sgambling_platform_user_list = sgambling_platform2gambling_user[platform]
                amount_sum = 0.0
                t = random.randint(1, 1)
                for _ in range(t):
                    num = self.store_gambling_user_nums(sgambling_platform_user_list)
                    random.shuffle(sgambling_platform_user_list)
                    cur_users = gambling_users[0: num]
                    for user in cur_users:
                        times = self.get_store_gambling_times()
                        cards = user_card[user.get_user_no()]

                        for _ in range(times):
                            card_index = random.randint(0, len(cards) - 1)

                            amount = self.get_store_amount(platform)

                            amount_sum += amount

                            d_ = self.get_trans_time(platform)
                            S30s = json.loads(platform.getS30())
                            S30 = "00000000"
                            for key, value in S30s.items():
                                if value == "Normal":
                                    S30 = key
                                    break
                            self.cardService.updateCardState(cards[card_index].getC4(),'Gambling_violation')
                            trans = self.get_trans_info('01', cards[card_index].getC4(), amount, d_, d,
                                                        cards[card_index].getC5(), platform.getS1(), platform.getCard_id(), S30=S30)
                            # print(trans)
                            self.trans_list.append(trans)
                            self.transService.insertTrans(trans)

                bank_index = random.randint(0, len(bank) - 1)
                d_time, _ = getday(year, month, day, random.randint(1, 3))

                d_ = self.get_trans_time(bank[bank_index])

                c_info = self.cardService.getCardInfoByC4(bank[bank_index].getCard_id())

                trans = self.get_trans_info('03', c_info.getC4(), amount_sum, d_, d_time, c_info.getC5(),
                                            '000000000000000', platform.getCard_id(), S30='00000000')

                # print(trans)
                self.trans_list.append(trans)
                self.transService.insertTrans(trans)


    def generate_personal_trans(self, gambling_user, fraud_user, card, d):
        card_trans = {}

        for user in gambling_user:
            f_user = fraud_user[random.randint(0, len(fraud_user) - 1)]

            trans_num = self.get_personal_gambling_times()

            for _ in range(trans_num):
                f_cards = card[f_user.get_user_no()]

                f_card_index = random.randint(0, len(f_cards) - 1)

                f_card = f_cards[f_card_index]

                amount = self.get_personal_amount(user)

                trans_time = self.get_personal_trans_time()

                g_cards = card[user.get_user_no()]
                g_card_index = random.randint(0, len(g_cards) - 1)
                g_card = g_cards[g_card_index]
                self.cardService.updateCardState(f_card.getC4(), 'Gambling_violation')
                trans = self.get_trans_info('03', f_card.getC4(), amount, trans_time, d,
                                            f_card.getC5(),
                                            '000000000000000', g_card.getC4(), S30='00000000')
                # print(trans)
                self.trans_list.append(trans)
                self.transService.insertTrans(trans)

                if f_card.getC4() in card_trans.keys():
                    info = card_trans[f_card.getC4()]
                    info['amount_sum'] = info['amount_sum'] + amount
                    info['last_time'] = trans_time if trans_time > info['last_time'] else info['last_time']

                else:
                    info = {'amount_sum': amount, 'last_time': trans_time}
                    card_trans[f_card.getC4()] = info

        return card_trans

    def get_trans_info(self, T2, T1, T17, T19, T23, T26, T25,
                       T37, S30):
        trans = Trans(id=0, T2=T2, T1=T1,
                      T6='0', T14='4', T17=T17,
                      T19=T19, T23=T23,
                      T26=T26,
                      T37=T37,
                      T25=T25,
                      T31=S30,
                      abnormal=1,
                      abnormal_state={"Gambling_violation": 1, "Fake_registration": 0,"Credit_card_fraud":0, "Scalper_marketing":0, "Merchant_violation":0,"Abnormal_transfer":0}
                      )
        return trans

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

    def get_personal_trans_time(self):
        ratio = [self.personal_trans_time_ratio, 1 - self.personal_trans_time_ratio]

        r = random.random()

        time = 0

        if r < ratio[0]:

            if random.random() < 0.5:
                time = random.randint(22 * 60, 23 * 60 + 59)
            else:
                time = random.randint(0, 5 * 60)
        else:
            time = random.randint(5 * 60, 22 * 60)

        trans_time = str("%02d" % (int(time / 60) % 24)) + \
                     str("%02d" % int(time % 60)) + \
                     str("%02d" % random.randint(0, 59))

        return trans_time

    def get_gambling_stores(self, quantity):
        store_list = []

        rank_prob = [self.low_rank_store_ratio, self.middle_rank_store_ratio, self.high_rank_store_ratio]

        low_rank_quantity = int(quantity * rank_prob[0])
        middle_rank_quantity = int(quantity * rank_prob[1])
        high_rank_quantity = quantity - low_rank_quantity - middle_rank_quantity

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
            self.storeService.updateStoreState(store.getStore_id(), 'Gambling_violation')
        return store_list

    def segment_stores_to_two_type(self, stores):
        type_prob = [0.9, 0.1]

        random.shuffle(stores)

        f_nums = int(len(stores) * type_prob[0])

        return stores[0:f_nums], stores[f_nums:]

    def segment_user_to_two_type(self, users):
        ratio = [self.gambling_user_ratio, 1 - self.gambling_user_ratio]

        part1 = users[0: int(len(users) * ratio[0])]

        part2 = users[int(len(users) * ratio[0]):]

        return part1, part2

    def get_gambling_users(self, quantity):
        fraud_user = set()

        fraud_cards = {}
        all_users = self.userService.selectAllUser()

        random.shuffle(all_users)

        max_wage = 75000

        users = []

        for user in all_users:
            if user.getWage() < max_wage:
                users.append(user)

        for user in users:
            cards = user.getCard()
            cards = json.loads(cards)

            user_cards = []

            for card in cards:
                c_info = self.cardService.getCardInfoByC4(card['C4'])

                user_cards.append(c_info)

                fraud_user.add(user)

                fraud_cards[user.get_user_no()] = user_cards

            if len(fraud_user) == quantity:
                break

        for u in fraud_user:
            self.userService.updateUserState(user_id=u.id, fraud_category='Gambling_violation')

        return fraud_user, fraud_cards

    def get_normal_users(self, quantity):
        users = self.userService.selectNormalUser()
        random.shuffle(users)
        return users[0: quantity]

    def get_small_amount(self):
        amount = gamma(2., 2., 1, 2)[0]

        amount = round(amount, 2)

        return amount

    def get_personal_gambling_times(self):

        times = 0

        while times == 0:
            times = int(gamma(2.5, 1., 1, 1)[0])

        return times

    def get_store_gambling_times(self):

        times = 0

        while times == 0:
            times = int(gamma(3.5, 2., 1, 1)[0])

        return times

    def get_store_amount(self, store):
        consumption_range = store.getCharge_duration()

        ratio = [0.8, 5]

        r = random.uniform(ratio[0], ratio[1])

        amount = 0
        while amount == 0:
            amount = int(consumption_range[0] * r)

        return amount

    def get_personal_amount(self, user):
        # wage_ = 0.01
        wage_ratio = 0.4

        gamma_raito = 0.6

        gamma_amount = gamma(shape=2., scale=3., size=1, multi=50)[0]

        n_age = user.getAge()

        n_wage = user.getWage()
        fs = FraudSettings(n_wage)
        n_age_lvl = fs.get_age_lvl_from_age(n_age)
        # print(n_age_lvl)
        amount = fs.generate_basic_fraud_amount(fraud_scene_multi=1.5, age_lvl=n_age_lvl)

        amount = int(amount * wage_ratio + gamma_amount * gamma_raito)

        return amount

    def store_gambling_user_nums(self,store_gambling_user_list):
        return random.randint(int(0.2 * len(store_gambling_user_list)), int(0.8 * len(store_gambling_user_list)))

    def get_minute_and_second(self):
        m = "%02d" % random.randint(0, 59)
        s = "%02d" % random.randint(0, 59)
        return str(m) + str(s)

    def get_transfer_times(self):
        return random.randint(1, 5)

    def random_pick(self, some_list, probabilitie_list):
        x = random.uniform(0, 1)
        cumulative_probability = 0.0
        item = 0
        for item, item_probability in zip(some_list, probabilitie_list):
            cumulative_probability = cumulative_probability + item_probability
            if x < cumulative_probability:
                break
        return item

if __name__ == '__main__':
    gtf = GamblingTransFactory()
    # l = gtf.get_gambling_stores(10)
    # for i in l:
    #     print(type(gtf.get_store_amount(i)))
    # print(random.uniform(0.5, 0.6))

    gtf.generate_date(year=2022, month=2, day=1, duration=30, store_quantity=5 * 3, user_quantity=15 * 3)

