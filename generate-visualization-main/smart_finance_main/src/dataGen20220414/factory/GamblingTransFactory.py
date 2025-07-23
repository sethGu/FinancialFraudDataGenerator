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
        scene = "赌博违规交易"
        self.transService = TransService(scene)
        self.userService = UserService(scene)
        self.cardService = CardService(scene)
        self.storeService = StoreService(scene)
        # 商户异常交易产生于商户营业时间内的概率
        self.is_in_opening_time = is_in_opening_time
        # 赌徒在赌博时产生交易的时间在半夜的概率
        self.personal_trans_time_ratio = personal_trans_time_ratio
        # 赌博商户中各种等级的商户概率  相加为 1
        # 低
        self.low_rank_store_ratio = low_rank_store_ratio
        # 中
        self.middle_rank_store_ratio = middle_rank_store_ratio
        # 高
        self.high_rank_store_ratio = high_rank_store_ratio
        # 异常用户中赌博用户占的比例（其他用户是虚假用户或租赁用户）
        self.gambling_user_ratio = gambling_user_ratio
    # 创建数据
    def generate_date(self, year, month, day, duration, store_quantity, user_quantity):
        # 获取违规商户
        stores = self.get_gambling_stores(store_quantity)
        # print("stores:", len(stores))
        # 获取违规用户
        users, cards = self.get_gambling_users(user_quantity)
        users = list(users)
        # 三个场景分别使用不同的用户及商户
        # 场景1：商户平台和钱庄
        stores1 = stores[0: int(store_quantity * 0.6)]
        # 场景2： 钱庄
        stores2 = stores[int(store_quantity * 0.6): int(store_quantity * 0.8)]
        # print("stores2:",stores2)
        # 场景3： 钱庄
        stores3 = stores[int(store_quantity * 0.8):]

        user1 = users[0: int(user_quantity / 3)]
        user2 = users[int(user_quantity / 3): 2 * int(user_quantity / 3)]
        user3 = users[2 * int(user_quantity / 3):]

        # 场景1
        # 违规商户分类：平台和钱庄
        platform, bank = self.segment_stores_to_two_type(stores1)

        # 创建商户异常交易
        self.trans_list = []
        print('场景1 ')
        self.generate_store_abnormal_data(year, month, day, platform, bank, user1, cards, duration)#duration 生成交易天数
        print("场景一生成了" + str(len(self.trans_list)) + "条数据")
        num_1 = len(self.trans_list)
        # 场景2
        gambling_user, false_user = self.segment_user_to_two_type(user2)
        print('场景2 ')
        self.generate_false_user_data(year, month, day, gambling_user, false_user, cards, stores2, duration)
        print("场景二生成了" + str(len(self.trans_list)-num_1) + "条数据")
        num_2 = len(self.trans_list)
        # 场景3
        print('场景3 ')
        gambling_user, lease_user = self.segment_user_to_two_type(user3)
        self.generate_lease_user_data(year, month, day, gambling_user, lease_user, cards, stores3, duration)
        print("场景三生成了" + str(len(self.trans_list) - num_2) + "条数据")
    # 创建租赁用户异常交易
    def generate_lease_user_data(self, year, month, day, gambling_user, lease_user, card, bank, duration):
        # 将租赁用户分为收款用户和其他用户
        cash_in, other = lease_user[0: int(len(lease_user) * 0.5)], lease_user[int(len(lease_user) * 0.5):]

        # 交易日期
        for i in range(duration):
            # print(i)
            d, _ = getday(year, month, day, i)

            # 每个赌徒生成多笔赌博交易
            # lease_card_trans保存每张空头账户的收入总额和最晚时间
            lease_card_trans = self.generate_personal_trans(gambling_user, cash_in, card, d)

            # 其他用户的所有卡
            other_user_cards = []
            for user in other:
                other_user_cards.extend(card[user.get_user_no()])

            # 租赁卡收入金额多次进行转移
            for key in lease_card_trans:
                # 深拷贝、避免转移卡在同一次转移中多次使用
                cards = copy.deepcopy(other_user_cards)

                # 赃款转移次数
                transfer_times = self.get_transfer_times()

                # 卡最后交易时间
                last_time = lease_card_trans[key]['last_time']
                # 卡交易金额
                amount_sum = lease_card_trans[key]['amount_sum']

                # 最后收款的卡
                last_trans_card = None
                # 上一步收款卡卡号
                previous_trans_card = key

                other_user_cards_nums = len(other_user_cards)
                if other_user_cards_nums < transfer_times:
                    transfer_times = other_user_cards_nums
                for _ in range(transfer_times):
                    # 打乱后选择第一张卡作为当前转账卡
                    random.shuffle(cards)
                    last_trans_card = cards[0]
                    # 生成交易时间
                    last_time = get_later_time(d + last_time[0:2], random.randint(1, 24))

                    # 获取分秒
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
                    # print("转出卡:")
                    # print(last_trans_card.getC5())
                    # print("转入卡:")
                    self.trans_list.append(trans)
                    self.transService.insertTrans(trans)
                    del cards[0]

                # 最后收款卡将金额转入钱庄
                # 转出时间
                trans_time = get_later_time(last_time, random.randint(1, 24))
                # 分秒
                m_and_s = self.get_minute_and_second()
                # 随机选择钱庄
                bank_index = random.randint(0, len(bank) - 1)
                # 钱庄绑定卡信息
                c_info = self.cardService.getCardInfoByC4(bank[bank_index].getCard_id())
                trans = self.get_trans_info('03', c_info.getC4(), amount_sum, trans_time[8: 10] + m_and_s,
                                            trans_time[0: 8], c_info.getC5(),
                                            '000000000000000', last_trans_card.getC4(), S30='00000000')
                # print(trans)
                self.trans_list.append(trans)
                self.transService.insertTrans(trans)

    # 创建虚假用户异常交易
    def generate_false_user_data(self, year, month, day, gambling_user, false_user, card, bank, duration):
        # 交易日期
        for i in range(duration):
            d, _ = getday(year, month, day, i)
            # print(i)
            # 每个赌徒生成多笔赌博交易
            # false_card_trans保存每张空头账户的收入总额和最晚时间
            false_card_trans = self.generate_personal_trans(gambling_user, false_user, card, d)

            # 虚假账户给钱庄转账
            for key in false_card_trans.keys():
                info = false_card_trans[key]

                # 当前卡最后收款时间
                last_time = d + info['last_time'][0:2]

                # 转出时间
                trans_time = get_later_time(last_time, random.randint(1, 24))

                # 分秒
                m_and_s = self.get_minute_and_second()
                # 随机选择钱庄
                bank_index = random.randint(0, len(bank) - 1)

                # 钱庄绑定卡信息
                c_info = self.cardService.getCardInfoByC4(bank[bank_index].getCard_id())

                trans = self.get_trans_info('03', c_info.getC4(), info['amount_sum'], trans_time[8: 10] + m_and_s,
                                            trans_time[0: 8], c_info.getC5(),
                                            '000000000000000', key, S30='00000000')
                self.trans_list.append(trans)
                self.transService.insertTrans(trans)

    # 创建商户异常交易
    def generate_store_abnormal_data(self, year, month, day, gambling_platform, bank, gambling_users, user_card,duration):
        '''

        :param year:
        :param month:
        :param day:
        :param duration
        :param gambling_platform: 赌博平台商户
        :param bank: 钱庄商户
        :param user_card: 用户银行卡信息
        :return:
        '''
        # 绑定商户和赌徒的关系 一个赌徒只选择一到三个商户进行交易
        sgambling_platform2gambling_user = {}
        for platform in gambling_platform:
            sgambling_platform2gambling_user[platform] = []
        for user in gambling_users:
            #商户选择 每个用户会选择 1-3个平台进行赌博交易
            try:
                num = self.random_pick([1,2,3],[0.6,0.3,0.1])
            except  Exception as e:
                print(e)
            platforms= random.sample(gambling_platform, num)
            for platform in platforms:
                sgambling_platform2gambling_user[platform].append(user)

        # 交易日期
        for i in range(duration):
            # print(i)
            d, _ = getday(year, month, day, i)
            # 对每个赌博平台生成交易，每次参与的赌徒为选择该平台的一半人数
            for platform in gambling_platform:
                # print("platform:")
                # 当前平台的赌徒用户
                sgambling_platform_user_list = sgambling_platform2gambling_user[platform]
                # 当次商户赌博总金额
                amount_sum = 0.0
                t = random.randint(1, 1)
                # 生成一批或多批交易
                for _ in range(t):
                    # 从赌博用户中随机选取几个用户进行赌博（1-n）
                    num = self.store_gambling_user_nums(sgambling_platform_user_list)
                    # 打乱用户列表
                    random.shuffle(sgambling_platform_user_list)
                    cur_users = gambling_users[0: num]
                    # 遍历每个用户
                    for user in cur_users:
                        # 用户在当次赌博中的赌博次数
                        times = self.get_store_gambling_times()
                        # 用户银行卡
                        cards = user_card[user.get_user_no()]

                        # 循环生成多笔交易
                        for _ in range(times):
                            # 随机选一张卡交易
                            card_index = random.randint(0, len(cards) - 1)

                            # 本次交易金额
                            amount = self.get_store_amount(platform)

                            amount_sum += amount

                            # 生成交易时间
                            d_ = self.get_trans_time(platform)
                            S30s = json.loads(platform.getS30())
                            S30 = "00000000"
                            for key, value in S30s.items():
                                if value == "正常":
                                    S30 = key
                                    break
                            self.cardService.updateCardState(cards[card_index].getC4(),'赌博违规交易')
                            trans = self.get_trans_info('01', cards[card_index].getC4(), amount, d_, d,
                                                        cards[card_index].getC5(), platform.getS1(), platform.getCard_id(), S30=S30)
                            # print(trans)
                            self.trans_list.append(trans)
                            self.transService.insertTrans(trans)

                # 商户平台给钱庄汇款
                bank_index = random.randint(0, len(bank) - 1)
                # 交易日期， 在一定时间内，暂定三天内
                d_time, _ = getday(year, month, day, random.randint(1, 3))

                # 生成交易时间
                d_ = self.get_trans_time(bank[bank_index])

                # 钱庄绑定卡信息
                c_info = self.cardService.getCardInfoByC4(bank[bank_index].getCard_id())

                trans = self.get_trans_info('03', c_info.getC4(), amount_sum, d_, d_time, c_info.getC5(),
                                            '000000000000000', platform.getCard_id(), S30='00000000')

                # print(trans)
                self.trans_list.append(trans)
                self.transService.insertTrans(trans)


    # 赌徒在用户赌博中多次交易信息生成
    def generate_personal_trans(self, gambling_user, fraud_user, card, d):

        # 保存每张账户的收入总额和最晚时间
        card_trans = {}

        # 每个赌徒生成多笔赌博交易
        for user in gambling_user:

            # 随机选择一个虚假/租赁用户
            f_user = fraud_user[random.randint(0, len(fraud_user) - 1)]

            # 当前用户赌博次数
            trans_num = self.get_personal_gambling_times()

            for _ in range(trans_num):
                # 虚假用户的银行卡
                f_cards = card[f_user.get_user_no()]

                # 随机选择卡
                f_card_index = random.randint(0, len(f_cards) - 1)

                f_card = f_cards[f_card_index]

                # 赌博金额
                amount = self.get_personal_amount(user)

                # 交易时间
                trans_time = self.get_personal_trans_time()

                # 随机选课赌博用户的卡
                g_cards = card[user.get_user_no()]
                g_card_index = random.randint(0, len(g_cards) - 1)
                g_card = g_cards[g_card_index]
                self.cardService.updateCardState(f_card.getC4(), '赌博违规交易')
                trans = self.get_trans_info('03', f_card.getC4(), amount, trans_time, d,
                                            f_card.getC5(),
                                            '000000000000000', g_card.getC4(), S30='00000000')
                # print(trans)
                self.trans_list.append(trans)
                self.transService.insertTrans(trans)

                # 写入false_card_trans中
                # 卡有过交易信息
                if f_card.getC4() in card_trans.keys():
                    # 交易最晚时间及总额
                    info = card_trans[f_card.getC4()]
                    # 这张卡的收入总额
                    info['amount_sum'] = info['amount_sum'] + amount
                    # 这张卡的最晚交易时间
                    info['last_time'] = trans_time if trans_time > info['last_time'] else info['last_time']

                else:
                    info = {'amount_sum': amount, 'last_time': trans_time}
                    card_trans[f_card.getC4()] = info

        return card_trans

    # 交易信息
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
                      abnormal_state={"赌博违规交易": 1, "伪冒注册欺诈": 0, "信用卡违规套现": 0, "黄牛营销欺诈": 0, "商户违规": 0, "异常转账": 0}
                      )
        return trans

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

    # 获取交易时间
    # 以半夜为主
    def get_personal_trans_time(self):

        # 半夜和白天概率
        # 半夜 22：00 - 5：00
        ratio = [self.personal_trans_time_ratio, 1 - self.personal_trans_time_ratio]

        # 随机生成当前概率
        r = random.random()

        # 时间
        time = 0

        # 半夜
        if r < ratio[0]:

            if random.random() < 0.5:
                time = random.randint(22 * 60, 23 * 60 + 59)
            else:
                time = random.randint(0, 5 * 60)
        # 白天
        else:
            time = random.randint(5 * 60, 22 * 60)

        # 转为按时间的字符串 并拼接秒
        trans_time = str("%02d" % (int(time / 60) % 24)) + \
                     str("%02d" % int(time % 60)) + \
                     str("%02d" % random.randint(0, 59))

        return trans_time

    # 获取赌博商户列表
    # 商户等级低中的概率较大
    def get_gambling_stores(self, quantity):
        '''

                :param quantity: 商户数量
                :return:
                '''
        store_list = []

        # 各类商户等级概率分布
        rank_prob = [self.low_rank_store_ratio, self.middle_rank_store_ratio, self.high_rank_store_ratio]

        # 各类等级商户数量:低、中、高
        low_rank_quantity = int(quantity * rank_prob[0])
        middle_rank_quantity = int(quantity * rank_prob[1])
        high_rank_quantity = quantity - low_rank_quantity - middle_rank_quantity

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

            # 获取商户等级
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
            self.storeService.updateStoreState(store.getStore_id(), '赌博违规交易')
        return store_list

    # 将商户分为平台和钱庄
    def segment_stores_to_two_type(self, stores):
        # 平台和钱庄的比例
        type_prob = [0.9, 0.1]

        random.shuffle(stores)

        f_nums = int(len(stores) * type_prob[0])

        return stores[0:f_nums], stores[f_nums:]

    # 将用户分为两部分
    def segment_user_to_two_type(self, users):
        # 赌博用户和虚假用户或租赁用户比例
        ratio = [self.gambling_user_ratio, 1 - self.gambling_user_ratio]

        part1 = users[0: int(len(users) * ratio[0])]

        part2 = users[int(len(users) * ratio[0]):]

        return part1, part2

    # 获取赌博用户列表
    def get_gambling_users(self, quantity):
        fraud_user = set()

        # 由于并不是欺诈用户的所有卡都是信用卡
        # 保存欺诈用户的信用卡
        # {user_no: [card1, card2]}  --- card1是信用卡实体
        fraud_cards = {}
        # 获取所有用户列表
        all_users = self.userService.selectAllUser()

        # 打乱用户列表， 防止每次筛选出的欺诈用户都是一样的
        random.shuffle(all_users)

        # 用户多为大学生、务工务农人员，即工资较低
        max_wage = 75000

        # 初步筛选的用户
        users = []

        for user in all_users:
            if user.getWage() < max_wage:
                users.append(user)

        # 遍历用户列表，筛选套现用户
        for user in users:
            cards = user.getCard()
            cards = json.loads(cards)

            user_cards = []

            # 查询当前用户的所有卡
            for card in cards:
                # 查询卡具体信息
                c_info = self.cardService.getCardInfoByC4(card['C4'])

                user_cards.append(c_info)
                # 若存在信用卡，那当前用户可作为欺诈用户

                fraud_user.add(user)

                # 同时记录信用卡
                fraud_cards[user.get_user_no()] = user_cards

            if len(fraud_user) == quantity:
                break
        # 将这些欺诈用户更新至数据库
        for u in fraud_user:
            self.userService.updateUserState(user_id=u.id, fraud_category='赌博违规交易')

        return fraud_user, fraud_cards

    # 获取少量正常用户
    # 可作为幕后BOSS
    def get_normal_users(self, quantity):
        users = self.userService.selectNormalUser()
        random.shuffle(users)
        return users[0: quantity]

    # 小额测试金额
    def get_small_amount(self):
        # 使用gamma分布产生小额测试金额
        amount = gamma(2., 2., 1, 2)[0]

        # 保留两位小数
        amount = round(amount, 2)

        return amount

    # 个人赌博交易次数（较少）
    def get_personal_gambling_times(self):

        times = 0

        # 使用gamma分布生成交易次数
        # 保证至少有一次交易
        while times == 0:
            times = int(gamma(2.5, 1., 1, 1)[0])

        return times

    # 商户赌博次数（较多）
    def get_store_gambling_times(self):

        times = 0
        # 使用gamma分布生成交易次数
        # 保证至少有一次交易
        while times == 0:
            times = int(gamma(3.5, 2., 1, 1)[0])

        return times

    # 商户赌博交易金额
    # 金额较小，与商户消费水平挂钩
    def get_store_amount(self, store):

        # 商户消费范围
        consumption_range = store.getCharge_duration()

        # 金额小于商户最低消费金额且为整数
        # 金额占消费金额的比率
        ratio = [0.8, 5]

        r = random.uniform(ratio[0], ratio[1])

        amount = 0
        # 生成金额
        while amount == 0:
            amount = int(consumption_range[0] * r)

        return amount

    # 个人赌博交易金额
    # 与用户工资挂钩与gamma分布挂钩
    def get_personal_amount(self, user):

        # 工资对应的欺诈金额比例
        # wage_ = 0.01

        # 根据工资生成的欺诈金额占比
        wage_ratio = 0.4

        # 根据伽马生成的欺诈金额占比
        gamma_raito = 0.6

        # 根据伽马生成欺诈金额
        gamma_amount = gamma(shape=2., scale=3., size=1, multi=50)[0]

        # 用户年龄
        n_age = user.getAge()

        n_wage = user.getWage()
        fs = FraudSettings(n_wage)
        n_age_lvl = fs.get_age_lvl_from_age(n_age)
        # print(n_age_lvl)
        amount = fs.generate_basic_fraud_amount(fraud_scene_multi=1.5, age_lvl=n_age_lvl)

        amount = int(amount * wage_ratio + gamma_amount * gamma_raito)

        return amount

    # 商户赌博 赌博人数
    def store_gambling_user_nums(self,store_gambling_user_list):
        return random.randint(int(0.2 * len(store_gambling_user_list)), int(0.8 * len(store_gambling_user_list)))

    # 获取消费时间（分秒）
    def get_minute_and_second(self):
        m = "%02d" % random.randint(0, 59)
        s = "%02d" % random.randint(0, 59)
        return str(m) + str(s)

    # 获取使用租赁用户转移赌博款次数
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

