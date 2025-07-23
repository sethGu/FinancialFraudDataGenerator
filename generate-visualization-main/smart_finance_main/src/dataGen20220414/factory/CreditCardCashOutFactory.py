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
        scene = "信用卡违规套现"
        self.transService = TransService(scene)
        self.userService = UserService(scene)
        self.cardService = CardService(scene)
        self.storeService = StoreService(scene)
        # 个人商户套现概率
        self.personal_cash_out_ratio = personal_cash_out_ratio
        # 个人商户占异常商户的比例
        self.personal_store_ratio = personal_store_ratio
        # 商户团伙大小的最小值
        self.store_group_size_min = store_group_size_min
        # 商户团伙大小的最大值
        self.store_group_size_max = store_group_size_max
        # 异常交易产生于商户营业时间内的概率
        self.is_in_opening_time = is_in_opening_time

    # 构建数据
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
        '''

        :param small_fraud_gap: 两次套现 短时间隔时长(h/小时)
        :param big_fraud_gap: 两次套现 长时间间隔时长(d/天)
        :param start_year: 开始年
        :param start_month: 开始月
        :param start_day: 开始日
        :param fraud_user: 欺诈用户列表
        :param fraud_store: 欺诈商户列表
        :return:
        '''

        # 个人商户列表  团伙商户列表
        personal_stores, store_groups = self.segment_stors_to_personal_or_group(fraud_store)

        # 遍历筛选出来的套现用户列表
        for f_user in fraud_user:

            # 当前用户的信用卡信息
            f_cards = fraud_cards[f_user.get_user_no()]
            f_deposit_cards = fraud_deposit_card[f_user.get_user_no()]

            # 选择一张信用卡作为套现卡
            card_index = random.randint(0, len(f_cards) - 1)

            # 将套现卡更新至数据库
            self.cardService.updateCardState(f_cards[card_index].getC4(), '信用卡违规套现')

            # 选择一张储蓄卡作为套现收款卡
            card_deposit_index = random.randint(0, len(f_deposit_cards) - 1)

            # 是否是个人商户套现
            # True: 个人  False：团伙
            is_personal_cash_out = self.is_personal_cash_out()

            # 个人商户套现
            if is_personal_cash_out:
                # 随机选择商户
                store_index = random.randint(0, len(personal_stores) - 1)

                # 商户相关信息
                # pos机
                store_m = personal_stores[store_index].getS1()
                # 商户绑定卡
                store_card = personal_stores[store_index].getCard_id()

                # 将欺诈商户更新至数据库
                # self.storeService.updateStoreState(fraud_store[store_index].getStore_id(), '信用卡违规套现')

                # 获取短时套现和长时间套现次数（不包含第一次套现）
                small_cash_out_times, big_cash_out_times = self.get_cash_out_times(user=f_user,
                                                                                   card=f_cards[card_index])

                # 首次套现年月日
                d, _ = getday(start_year, start_month, start_day, 0)

                # 首次套现时分秒
                d_ = self.get_trans_time(store=fraud_store[store_index])

                # 生成信用卡额度
                # quota = self.get_card_quota(f_cards[card_index])

                # 生成首次套现交易

                amount = self.get_trans_amount(user=f_user, card=f_cards[card_index])
                S30s = json.loads(personal_stores[store_index].getS30())
                S30 = "00000000"
                for key, value in S30s.items():
                    if value == "正常":
                        S30 = key
                        break
                trans = self.get_trans_info(f_cards[card_index].getC4(), amount, d_, d,
                                            f_cards[card_index].getC5(), store_m, store_card, S30)
                # print(trans)
                self.transService.insertTrans(trans)

                # 用于短时间隔的时间格式
                cur = d + d_[0:2]

                # 商家返钱金额
                amount_back = int(amount * 0.95)
                # 商家返钱时间 间隔一天吧
                trans_back_time = get_later_time(cur, duration=random.randint(0, 24))
                m_and_s = self.get_minute_and_second()
                trans_back = self.get_trans_back_info(store_card,
                                                      amount_back,
                                                      trans_back_time[8:10] + m_and_s, trans_back_time[0:8],
                                                      f_deposit_cards[card_deposit_index].getC4())
                # print(trans_back)
                self.transService.insertTrans(trans_back)

                # 生成短时间间隔套现交易
                for _ in range(small_cash_out_times):

                    # 生成短时时间间隔（h/小时）
                    gap = random.randint(0, small_fraud_gap)

                    # 短时间隔后时间
                    cur = get_later_time(cur, gap)

                    # 获取分秒
                    m_and_s = self.get_minute_and_second()

                    # 套现金额
                    amount = self.get_trans_amount(user=f_user,
                                                   card=f_cards[card_index])

                    # 生成交易
                    trans = self.get_trans_info(f_cards[card_index].getC4(), amount, cur[8:10] + m_and_s,
                                                cur[0:8],
                                                f_cards[card_index].getC5(), store_m,store_card, S30)
                    # print(trans)
                    self.transService.insertTrans(trans)
                    # 商家返钱金额
                    amount_back = int(amount * 0.95)
                    # 商家返钱时间 间隔一天吧
                    trans_back_time = get_later_time(cur, duration=random.randint(0, 24))
                    m_and_s = self.get_minute_and_second()
                    trans_back = self.get_trans_back_info(store_card,
                                                          amount_back,
                                                          trans_back_time[8:10] + m_and_s, trans_back_time[0:8],
                                                          f_deposit_cards[card_deposit_index].getC4())
                    # print(trans_back)
                    self.transService.insertTrans(trans_back)

                # 生成长时间间隔套现交易
                for _ in range(big_cash_out_times):

                    # 生成长时时间间隔（day/天）
                    gap = random.randint(20, big_fraud_gap)

                    # 长时间间隔后时间
                    d, _ = getday(int(d[0:4]), int(d[4:6]), int(d[6:8]), gap)

                    # 套现时分秒
                    d_ = self.get_trans_time(store=fraud_store[store_index])

                    # 套现金额
                    amount = self.get_trans_amount(user=f_user,
                                                   card=f_cards[card_index])

                    # 生成交易
                    trans = self.get_trans_info(f_cards[card_index].getC4(), amount, d_, d,
                                                f_cards[card_index].getC5(), store_m,store_card, S30)

                    # print(trans)
                    self.transService.insertTrans(trans)

                    # 商家返钱金额
                    amount_back = int(amount * 0.95)
                    # 商家返钱时间 间隔一天吧
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
                # 随机选择商户团伙
                group_index = random.randint(0, len(store_groups) - 1)

                # 商户团伙
                group = store_groups[group_index]

                # 从商户团伙中随机选择商户
                store_index = random.randint(0, len(group) - 1)

                # 获取短时套现和长时间套现次数（不包含第一次套现）
                small_cash_out_times, big_cash_out_times = self.get_cash_out_times(user=f_user,
                                                                                   card=f_cards[card_index])

                # 生成首次套现交易
                # 套现金额 gamma分布加上卡的等级信息
                amount = self.get_trans_amount(user=f_user, card=f_cards[card_index])

                # 首次套现年月日
                d, _ = getday(start_year, start_month, start_day, 0)

                # 首次套现时分秒
                d_ = self.get_trans_time(store=fraud_store[store_index])

                S30s = json.loads(group[store_index].getS30())
                S30 = "00000000"
                for key, value in S30s.items():
                    if value == "正常":
                        S30 = key
                        break

                trans = self.get_trans_info(f_cards[card_index].getC4(), amount, d_, d,
                                            f_cards[card_index].getC5(), group[store_index].getS1(), group[store_index].getCard_id(), S30)
                self.transService.insertTrans(trans)
                # print(trans)

                # 用于短时间隔的时间格式
                cur = d + d_[0:2]

                # 商家返钱金额
                amount_back = int(amount * 0.95)
                # 商家返钱时间 间隔一天吧
                trans_back_time = get_later_time(cur, duration=random.randint(0, 24))
                m_and_s = self.get_minute_and_second()
                trans_back = self.get_trans_back_info(group[store_index].getCard_id(),
                                                      amount_back,
                                                      trans_back_time[8:10] + m_and_s, trans_back_time[0:8],
                                                      f_deposit_cards[card_deposit_index].getC4())
                # print(trans_back)
                self.transService.insertTrans(trans_back)

                # 生成短时间间隔套现交易
                for _ in range(small_cash_out_times):
                    # 生成短时时间间隔（h/小时）
                    gap = random.randint(0, small_fraud_gap)

                    # 短时间隔后时间
                    cur = get_later_time(cur, gap)

                    # 获取分秒
                    m_and_s = self.get_minute_and_second()

                    # 套现金额
                    amount = self.get_trans_amount(user=f_user,
                                                   card=f_cards[card_index])

                    # 从商户团伙中随机选择商户
                    store_index = random.randint(0, len(group) - 1)

                    S30s = json.loads(group[store_index].getS30())
                    S30 = "00000000"
                    for key, value in S30s.items():
                        if value == "正常":
                            S30 = key
                            break

                    # 生成交易
                    trans = self.get_trans_info(f_cards[card_index].getC4(), amount, cur[8:10] + m_and_s,
                                                cur[0:8],
                                                f_cards[card_index].getC5(), group[store_index].getS1(), group[store_index].getCard_id(), S30)
                    self.transService.insertTrans(trans)
                    # print(trans)

                    # 商家返钱金额
                    amount_back = int(amount * 0.95)
                    # 商家返钱时间 间隔一天吧
                    trans_back_time = get_later_time(cur, duration=random.randint(0,24))
                    m_and_s = self.get_minute_and_second()
                    trans_back = self.get_trans_back_info(group[store_index].getCard_id(),
                                                          amount_back,
                                                          trans_back_time[8:10] + m_and_s, trans_back_time[0:8],
                                                          f_deposit_cards[card_deposit_index].getC4())
                    # print(trans_back)
                    self.transService.insertTrans(trans_back)

                # 生成长时间间隔套现交易
                for _ in range(big_cash_out_times):
                    # 生成长时时间间隔（day/天）
                    gap = random.randint(20, big_fraud_gap)

                    # 长时间间隔后时间
                    d, _ = getday(int(d[0:4]), int(d[4:6]), int(d[6:8]), gap)

                    # 套现时分秒
                    d_ = self.get_trans_time(store=fraud_store[store_index])

                    # 套现金额
                    amount = self.get_trans_amount(user=f_user,
                                                   card=f_cards[card_index])

                    # 从商户团伙中随机选择商户
                    store_index = random.randint(0, len(group) - 1)

                    S30s = json.loads(group[store_index].getS30())
                    S30 = "00000000"
                    for key, value in S30s.items():
                        if value == "正常":
                            S30 = key
                            break

                    # 生成交易
                    trans = self.get_trans_info(f_cards[card_index].getC4(), amount, d_, d,
                                                f_cards[card_index].getC5(), group[store_index].getS1(),group[store_index].getCard_id(), S30)


                    # print(trans)

                    self.transService.insertTrans(trans)

                    # 商家返钱金额
                    amount_back = int(amount * 0.95)
                    # 商家返钱时间 间隔一天吧
                    cur = d + d_[0:2]
                    trans_back_time = get_later_time(cur, duration=random.randint(0,24))
                    m_and_s = self.get_minute_and_second()
                    trans_back = self.get_trans_back_info(group[store_index].getCard_id(),
                                                          amount_back,
                                                          trans_back_time[8:10] + m_and_s, trans_back_time[0:8],
                                                          f_deposit_cards[card_deposit_index].getC4())
                    # print(trans_back)
                    self.transService.insertTrans(trans_back)


    # 是否是个人套现
    def is_personal_cash_out(self):
        # 个人商户套现概率
        ratio = 0.7

        if random.random() < self.personal_cash_out_ratio:
            return True
        else:
            return False

    # 交易信息
    def get_trans_info(self, T1, T17, T19, T23, C5, T25, T37, S30):
        trans = Trans(id=0, T2='01', T1=T1,
                      T6='0', T14='4', T17=T17,
                      T19=T19, T23=T23,
                      T26=C5,
                      T37=T37,
                      T25=T25,
                      T31=S30,
                      abnormal=1,
                      abnormal_state={"赌博违规交易": 0, "伪冒注册欺诈": 0, "信用卡违规套现": 1, "黄牛营销欺诈": 0, "商户违规": 0, "异常转账": 0}
                      )
        return trans

    # 商家返现交易
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
                      abnormal_state={"赌博违规交易": 0, "伪冒注册欺诈": 0, "信用卡违规套现": 0, "黄牛营销欺诈": 0, "商户违规": 0, "异常转账": 0}
                      )
        return trans

    # 获取套现用户列表并更新至数据库
    def get_fraud_user(self, quantity):
        fraud_user = []

        # 由于并不是欺诈用户的所有卡都是信用卡
        # 保存欺诈用户的信用卡
        # {user_no: [card1, card2]}  --- card1是信用卡实体
        fraud_cards = {}
        fraud_deposit_card = {}
        # 获取所有用户列表
        all_users = self.userService.selectAllUser()

        # 打乱用户列表， 防止每次筛选出的欺诈用户都是一样的
        random.shuffle(all_users)

        # 遍历用户列表，筛选套现用户
        for user in all_users:
            cards = user.getCard()
            cards = json.loads(cards)

            credit_cards = []
            deposit_cards = []
            # 查询当前用户的所有卡
            # 套现卡只能为信用卡,收款卡为储蓄卡
            for card in cards:

                # 查询卡具体信息
                c_info = self.cardService.getCardInfoByC4(card['C4'])


                C8 = c_info.getC8()

                C7 = c_info.getC7()

                C5 = c_info.getC5()

                if C8 != None and C8 != '--' and C7 != 'A卡':
                    credit_cards.append(c_info)
                if C5 == "01":
                    deposit_cards.append(c_info)
            # 若存在信用卡，那当前用户可作为欺诈用户
            if len(credit_cards) > 0:
                fraud_user.append(user)

                # 同时记录信用卡
                fraud_cards[user.get_user_no()] = credit_cards
                fraud_deposit_card[user.get_user_no()] = deposit_cards
            if len(fraud_user) == quantity:
                break
        # 将这些欺诈用户更新至数据库
        for u in fraud_user:
            self.userService.updateUserState(user_id=u.id, fraud_category='信用卡违规套现')

        return fraud_user, fraud_cards, fraud_deposit_card

    # 获取套现商户列表
    # 商户等级低中的概率较大
    def get_fraud_store(self, quantity):
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

        # 将欺诈商户更新至数据库
        for store in store_list:
            self.storeService.updateStoreState(store.getStore_id(), '信用卡违规套现')
        return store_list

    # 将欺诈商户分为个人商户和团伙商户
    def segment_stors_to_personal_or_group(self, stores):

        random.shuffle(stores)

        # 个人商户的比例
        personal_ratio = self.personal_store_ratio

        # 个人商户
        personal_stores = stores[0: int(len(stores) * personal_ratio)]

        # 剩下的作为商户团伙
        stores = stores[len(personal_stores):]

        # 剩下的商户数量
        lens = len(stores)

        # 团伙大小
        group_size = [int(self.store_group_size_min), int(self.store_group_size_max)]

        # 团伙
        stores_groups = []

        # 已选为商户团伙的商户数量
        choose_stores_num = 0

        # 分配商户团伙
        while True:

            # 本次团伙大小
            cur_size = random.randint(group_size[0], group_size[1])

            # 大小未超过剩下的商户数量
            if cur_size + choose_stores_num < lens:
                group = stores[choose_stores_num: choose_stores_num + cur_size]
                stores_groups.append(group)
            else:
                group = stores[choose_stores_num:]
                stores_groups.append(group)
                break
            choose_stores_num += cur_size

        return personal_stores, stores_groups

    # 获取交易时间
    # 根据商户营业时间 营业时间内概率小 营业时间外概率大
    def get_trans_time(self, store):

        # 营业时间内概率与营业时间外概率
        time_prob = [self.is_in_opening_time, 1 - self.is_in_opening_time]

        # 随机产生数来确定是否营业时间内
        r = random.random()
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
                    trans_time = random.randint(min_minute, start_minute)
                else:
                    trans_time = random.randint(end_minute, max_minute)
            elif start_minute == min_minute:
                trans_time = random.randint(end_minute, max_minute)
            else:
                trans_time = random.randint(min_minute, start_minute)

        # 转为按时间的字符串 并拼接秒
        trans_time = str("%02d" % (int(trans_time / 60) % 24)) + \
                     str("%02d" % int(trans_time % 60)) + \
                     str("%02d" % random.randint(0, 59))

        return trans_time

    # 生成交易金额
    # 根据用户工资和gamma分布
    # 二者加权和
    def get_trans_amount(self, user, card):

        # 用户年龄
        n_age = user.getAge()

        n_wage = user.getWage()
        fs = FraudSettings(n_wage)
        n_age_lvl = fs.get_age_lvl_from_age(n_age)
        # print(n_age_lvl)
        amount = fs.generate_basic_fraud_amount(fraud_scene_multi=1.5, age_lvl=n_age_lvl)

        # 依据卡等级调节金额
        card_amount = 0

        # 卡额度
        quota = self.get_card_quota(card)


        # 欺诈金额占比工资
        # rate = 0.05

        # 根据伽马生成欺诈金额
        gamma_amount = gamma(shape=2., scale=3., size=1, multi=800)[0]

        # 根据工资生成的欺诈金额占比
        wage_raito = 0.3

        # 根据伽马生成的欺诈金额占比
        gamma_raito = 0.7

        # 生成交易金额
        amount = amount * wage_raito + int(gamma_amount * gamma_raito)

        # 严格限制金额小于卡额度
        while amount > quota:
            amount *= 0.95

        # 套现金额往往接近整百整千
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

    # 生成长时间套现次数和短时间套现次数
    def get_cash_out_times(self, user, card):
        s = math.ceil(gamma(1.5, 2., 1, 1)[0])
        b = math.ceil(gamma(1.5, 2., 1, 1)[0])
        return s, b

    # 获取消费时间（分秒）
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
