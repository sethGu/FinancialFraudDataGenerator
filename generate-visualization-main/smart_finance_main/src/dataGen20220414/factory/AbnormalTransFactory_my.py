import datetime
import json
import random

from tqdm import tqdm

from src.dataGen20220414.service.TransService import TransService
from src.dataGen20220414.service.UserService import UserService
from src.utils.functions import getday
from src.dataGen20220414.entity.Trans import Trans
from src.dataGen20220414.factory.CardFactory import CardFactory
from src.dataGen20220414.factory.TransFactory import TransFactory
from src.dataGen20220414.factory.UserFactory import UserFactory
from src.utils.data_distribution_fuction import gamma
from src.dataGen20220414.service.CardService import CardService

'''
异常转账
'''


class AbnormalTransFactory:
    def __init__(self):
        scene = "异常转账"
        self.cardService = CardService(scene)
        self.transService = TransService(scene)
        self.userService = UserService(scene)

    def generate_data(self, gang_num=5, start_date='20220201', duration=30):
        # 诈骗最长周期定为10天
        fraud_cycle = 10
        if duration <= fraud_cycle:
            print("生成周期太短，至少在10天以上。")
            return
        # 将用户列表划分为团伙列表与受害人集合
        gangList, victims = self.getAbnormalGang(gang_num)

        # 对于每个团伙=》对每一个团伙生成交易
        for gang in gangList:
            # 每个团伙在生成时间段duration内有几个诈骗周期，也就是有几轮骗取汇款+取现/分赃的操作
            cycle_start_date = datetime.datetime.strptime(start_date, '%Y%m%d')
            # 每个团伙专门的人进行收款，同一受害者只向某张卡进行转账
            frauder = gang[0]
            f_info = frauder.get_user_info()
            f_cards = f_info['cards']
            # 这个罪犯可能有多个账户，记录每个账户的收款金额
            f_card_in_info = {}
            for card in f_cards:
                C4 = card["C4"]
                f_card_in_info[C4] = 0
            # 犯罪团伙每周分赃一次 workday为7时进行分赃
            cycle_day = 0
            cycle_amount = 0
            for day in range(duration - fraud_cycle):
                cycle_day += 1
                today = cycle_start_date + datetime.timedelta(days=day)
                # 被骗人受骗开始时间——接下来十天进行转账
                victimList = self.getVictims(victims)
                for victim in victimList:
                    # 选择诈骗者的银行卡
                    f_card = f_cards[random.randint(0, len(f_cards) - 1)]
                    self.cardService.updateCardState(f_card['C4'], '异常转账')
                    # 该受害者在该周期使用的一张银行卡
                    v_info = victim.get_user_info()
                    v_cards = v_info['cards']
                    v_card = v_cards[random.randint(0, len(v_cards) - 1)]
                    # 该受害者在该周期内向欺诈者汇款的次数
                    fraud_times = random.randint(1, 4)
                    # 汇款的最大间隔
                    gap = fraud_cycle / fraud_times
                    # 用户工资
                    wage = v_info['wage']
                    # 汇款时间列表
                    timeList = self.getTime(today, fraud_times, gap)
                    # 汇款时金额列表
                    amountList = self.getAmount(wage, fraud_times)

                    # print("被骗样例")
                    for i in range(fraud_times):
                        cycle_amount += amountList[i]
                        f_card_in_info[f_card['C4']] += amountList[i]


                        trans = Trans(id=0, T2='03', T1=f_card['C4'],
                                      T6='0', T14='4', T17=amountList[0],
                                      T19=timeList[i][8:14], T23=timeList[i][0:8],
                                      T26=f_card['C5'],

                                      T37=v_card['C4'],
                                      T25='000000000000000',
                                      T31='00000000',
                                      abnormal=1,
                                      abnormal_state={"赌博违规交易": 0, "伪冒注册欺诈": 0,"信用卡违规套现":0, "黄牛营销欺诈":0, "商户违规":0,"异常转账":1}
                                      )
                        # 插入交易
                        self.transService.insertTrans(trans)
                        # print(trans)
                # 2.其次是取现/分赃的阶段
                # 设定选择取现或分赃的概率
                if cycle_day == 7:
                    # 取现/分赃时间
                    t = today
                    hours = random.randint(0, 23)
                    # 偏向于非营业时间交易(22-6点)
                    p = random.random()
                    if p < 0.8:
                        hours = random.randint(-2, 6)
                        hours += 24
                    minutes = random.randint(0, 59)
                    t = t + datetime.timedelta(hours=hours, minutes=minutes)

                    # 相邻取现/分赃的最大时间间隔，比较短（10分钟内）
                    minute_gap = 10

                    # 取现,假设单笔取现限额是3万
                    p = random.random()
                    if p < 0.1:
                        # print('取现', cycle_amount)
                        # 收款者对名下的卡进行取现
                        for f_card in f_cards:
                            while f_card_in_info[f_card['C4']] > 0:
                                t = t + datetime.timedelta(minutes=random.randint(1, minute_gap))
                                str_t = t.strftime('%Y%m%d%H%M%S')
                                # print(str_t)

                                trans = Trans(id=0, T2='02', T1=f_card['C4'],
                                              T6='0', T14='4', T17=min(30000, f_card_in_info[f_card['C4']]),
                                              T19=str_t[8:14], T23=str_t[0:8],
                                              T26=f_card['C5'],
                                              T37='-',
                                              T25='000000000000000',
                                              T31='00000000',
                                              abnormal=1,
                                              abnormal_state={"赌博违规交易": 0, "伪冒注册欺诈": 0,"信用卡违规套现":0, "黄牛营销欺诈":0, "商户违规":0,"异常转账":1}
                                              )
                                f_card_in_info[f_card['C4']] -= min(30000, f_card_in_info[f_card['C4']])
                                # 插入交易
                                self.transService.insertTrans(trans)
                                # print("取现")
                                # print(trans)
                    # 分赃（平均分？）
                    else:
                        index = 0  # 先从第一张卡开始分，随之往后
                        # print('分赃', cycle_amount)
                        receivers = gang[1:]
                        amount = cycle_amount / (len(receivers) + 1)

                        # 团伙成员间互转
                        # 所有的卡
                        all_cards = []
                        for member in gang:
                            m_info = member.get_user_info()
                            m_cards = m_info['cards']
                            all_cards.extend(m_cards)

                        for _ in range(5):
                            for i, giver in enumerate(all_cards):
                                for j, receiver in enumerate(all_cards):
                                    if i == j:
                                        continue
                                    p_rec = random.random()
                                    if p_rec < 0.8:
                                        # 涉及字段中的新值
                                        self.cardService.updateCardState(giver['C4'], '异常转账')
                                        self.cardService.updateCardState(receiver['C4'], '异常转账')
                                        t = t + datetime.timedelta(minutes=random.randint(1, minute_gap))
                                        str_t = t.strftime('%Y%m%d%H%M%S')


                                        trans = Trans(id=0, T2='03', T1=giver['C4'],
                                              T6='0', T14='4', T17=random.randint(3000, 10000),
                                              T19=str_t[8:14], T23=str_t[0:8],
                                              T26=receiver['C5'],
                                              T37=receiver['C4'],
                                              T25='000000000000000',
                                              T31='00000000',
                                              abnormal=1,
                                              abnormal_state={"赌博违规交易": 0, "伪冒注册欺诈": 0,"信用卡违规套现":0, "黄牛营销欺诈":0, "商户违规":0,"异常转账":1}
                                              )
                                        # 插入交易
                                        self.transService.insertTrans(trans)
                                        # print(trans)

                        # 分赃（平均分）
                        for receiver in receivers:
                            # 还要对receiver转多少钱
                            amount_still = amount
                            Flag = False
                            r_info = receiver.get_user_info()
                            r_cards = r_info['cards']
                            r_card = r_cards[random.randint(0, len(r_cards) - 1)]

                            while Flag != True:  # 这个人还没有转完
                                f_card = f_cards[index]  # 转出卡
                                # 这张卡的剩余金额
                                remaining_amount = f_card_in_info[f_card['C4']]
                                if remaining_amount > amount_still:
                                    Flag = True
                                    f_card_in_info[f_card['C4']] -= amount_still
                                    amount_thistime = amount_still
                                else:
                                    amount_thistime = f_card_in_info[f_card['C4']]
                                    amount_still = amount_still - amount_thistime
                                    f_card_in_info[f_card['C4']] = 0

                                    index += 1
                                # 涉及字段中的新值
                                self.cardService.updateCardState(r_card['C4'], '异常转账')
                                t = t + datetime.timedelta(minutes=random.randint(1, minute_gap))
                                str_t = t.strftime('%Y%m%d%H%M%S')


                                trans = Trans(id=0, T2='03', T1=f_card['C4'],
                                              T6='0', T14='4', T17=amount_thistime,
                                              T19=str_t[8:14], T23=str_t[0:8],
                                              T26=r_card['C5'],
                                              T37=r_card['C4'],
                                              T25='000000000000000',
                                              T31='00000000',
                                              abnormal=1,
                                              abnormal_state={"赌博违规交易": 0, "伪冒注册欺诈": 0,"信用卡违规套现":0, "黄牛营销欺诈":0, "商户违规":0,"异常转账":1}
                                              )
                                # 插入交易
                                self.transService.insertTrans(trans)
                                # print(trans)
                    cycle_amount = 0  # cycle_amount重置为0

    # 将用户列表划分为团伙列表与受害人集合，年轻者容易受害
    def getAbnormalGang(self, gang_num):
        users = self.userService.selectUsers()
        random.shuffle(users)

        gangList = []
        victims = []
        victims_size = 10 * gang_num

        index = 0

        for i in range(gang_num):
            gang = []
            # 团伙大小
            gang_size = random.randint(7, 15)

            for j in range(gang_size):
                gang.append(users[index])
                index += 1
            gangList.append(gang)

        # <30岁被选为受害人的概率更高
        # for i in range(victims_size):
        i = 0
        while i < victims_size and i < len(users):
            u_age = users[index].get_user_info()['age']
            if u_age < 30 and random.uniform(0, 1) < 0.8:
                victims.append(users[index])
                i += 1
            elif u_age >= 30 and random.uniform(0, 1) < 0.6:
                victims.append(users[index])
                i += 1
            else:
                # 没选中，重选
                pass
            index += 1
        return gangList, victims

    # 从受害人集合中抽取一部分作为某个团伙某个周期的受害人，否则每次从整个正常用户中选开销太大
    def getVictims(self, victims):
        random.shuffle(victims)
        victim_size = random.randint(1, 4)
        return victims[0: victim_size]

    def getTime(self, start_date, fraud_times, gap_days):
        # start_date = datetime.datetime.strptime(start_date, '%Y%m%d')
        time_list = []
        for i in range(fraud_times):
            delt_day = random.randint(0, int(gap_days))

            # 发生交易具体几点
            hours = random.randint(0, 23)
            # 偏向于非营业时间交易(22-6点)
            p = random.random()
            if p < 0.8:
                hours = random.randint(-2, 6)
                hours += 24
            # 分钟纳入考虑，秒钟忽略
            minutes = random.randint(0, 59)
            seconds = random.randint(0, 59)
            # 发生交易测试的时间
            this_time = start_date + datetime.timedelta(days=delt_day, hours=hours, minutes=minutes, seconds=seconds)

            time_list.append(this_time)
        time_list = [str(t).replace('-','').replace(':','').replace(' ', '') for t in time_list]
        return time_list

    def getAmount(self, wage, fraud_times):
        amountList = []
        # 总共被骗金额gamma + 3000
        gamma_amount = gamma(shape=2., scale=0.3, size=1, multi=wage * 0.3)[0]
        total_amount = 3000 + gamma_amount
        # 暂定假设每次被骗金额一样
        for i in range(fraud_times):
            amountList.append(int(total_amount / fraud_times))
        return amountList


if __name__ == '__main__':
    AbnormalTrans = AbnormalTransFactory()
    # AbnormalTrans.generate_data(gang_num=5, start_date='20220201', duration=30)
    cycle_start_date = datetime.datetime.strptime('20220201', '%Y%m%d')
    today = cycle_start_date + datetime.timedelta(days=1)
    u = AbnormalTrans.getTime(today, 10, 10)
    print(u)

