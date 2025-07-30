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
Abnormal_transfer
'''


class AbnormalTransFactory:
    def __init__(self):
        scene = "Abnormal_transfer"
        self.cardService = CardService(scene)
        self.transService = TransService(scene)
        self.userService = UserService(scene)

    def generate_data(self, gang_num=5, start_date='20220201', duration=30):
        fraud_cycle = 10
        if duration <= fraud_cycle:
            print("The generation cycle is too short; it should be at least 10 days or more.")
            return
        gangList, victims = self.getAbnormalGang(gang_num)

        for gang in gangList:
            cycle_start_date = datetime.datetime.strptime(start_date, '%Y%m%d')
            frauder = gang[0]
            f_info = frauder.get_user_info()
            f_cards = f_info['cards']
            f_card_in_info = {}
            for card in f_cards:
                C4 = card["C4"]
                f_card_in_info[C4] = 0
            cycle_day = 0
            cycle_amount = 0
            for day in range(duration - fraud_cycle):
                cycle_day += 1
                today = cycle_start_date + datetime.timedelta(days=day)
                victimList = self.getVictims(victims)
                for victim in victimList:
                    f_card = f_cards[random.randint(0, len(f_cards) - 1)]
                    self.cardService.updateCardState(f_card['C4'], 'Abnormal_transfer')
                    v_info = victim.get_user_info()
                    v_cards = v_info['cards']
                    v_card = v_cards[random.randint(0, len(v_cards) - 1)]
                    fraud_times = random.randint(1, 4)
                    gap = fraud_cycle / fraud_times
                    wage = v_info['wage']
                    timeList = self.getTime(today, fraud_times, gap)
                    amountList = self.getAmount(wage, fraud_times)
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
                                      abnormal_state={"Gambling_violation": 0, "Fake_registration": 0,"Credit_card_fraud":0, "Scalper_marketing":0, "Merchant_violation":0,"Abnormal_transfer":1}
                                      )
                        self.transService.insertTrans(trans)
                if cycle_day == 7:
                    t = today
                    hours = random.randint(0, 23)
                    p = random.random()
                    if p < 0.8:
                        hours = random.randint(-2, 6)
                        hours += 24
                    minutes = random.randint(0, 59)
                    t = t + datetime.timedelta(hours=hours, minutes=minutes)
                    minute_gap = 10
                    p = random.random()
                    if p < 0.1:
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
                                              abnormal_state={"Gambling_violation": 0, "Fake_registration": 0,"Credit_card_fraud":0, "Scalper_marketing":0, "Merchant_violation":0,"Abnormal_transfer":1}
                                              )
                                f_card_in_info[f_card['C4']] -= min(30000, f_card_in_info[f_card['C4']])
                                self.transService.insertTrans(trans)
                    else:
                        index = 0
                        receivers = gang[1:]
                        amount = cycle_amount / (len(receivers) + 1)

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
                                        self.cardService.updateCardState(giver['C4'], 'Abnormal_transfer')
                                        self.cardService.updateCardState(receiver['C4'], 'Abnormal_transfer')
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
                                              abnormal_state={"Gambling_violation": 0, "Fake_registration": 0,"Credit_card_fraud":0, "Scalper_marketing":0, "Merchant_violation":0,"Abnormal_transfer":1}
                                              )
                                        self.transService.insertTrans(trans)
                                        # print(trans)

                        for receiver in receivers:
                            amount_still = amount
                            Flag = False
                            r_info = receiver.get_user_info()
                            r_cards = r_info['cards']
                            r_card = r_cards[random.randint(0, len(r_cards) - 1)]

                            while Flag != True:
                                f_card = f_cards[index]
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
                                self.cardService.updateCardState(r_card['C4'], 'Abnormal_transfer')
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
                                              abnormal_state={"Gambling_violation": 0, "Fake_registration": 0,"Credit_card_fraud":0, "Scalper_marketing":0, "Merchant_violation":0,"Abnormal_transfer":1}
                                              )
                                self.transService.insertTrans(trans)
                                # print(trans)
                    cycle_amount = 0

    def getAbnormalGang(self, gang_num):
        users = self.userService.selectUsers()
        random.shuffle(users)

        gangList = []
        victims = []
        victims_size = 10 * gang_num

        index = 0

        for i in range(gang_num):
            gang = []
            gang_size = random.randint(7, 15)

            for j in range(gang_size):
                gang.append(users[index])
                index += 1
            gangList.append(gang)

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
                pass
            index += 1
        return gangList, victims

    def getVictims(self, victims):
        random.shuffle(victims)
        victim_size = random.randint(1, 4)
        return victims[0: victim_size]

    def getTime(self, start_date, fraud_times, gap_days):
        # start_date = datetime.datetime.strptime(start_date, '%Y%m%d')
        time_list = []
        for i in range(fraud_times):
            delt_day = random.randint(0, int(gap_days))

            hours = random.randint(0, 23)
            p = random.random()
            if p < 0.8:
                hours = random.randint(-2, 6)
                hours += 24
            minutes = random.randint(0, 59)
            seconds = random.randint(0, 59)
            this_time = start_date + datetime.timedelta(days=delt_day, hours=hours, minutes=minutes, seconds=seconds)

            time_list.append(this_time)
        time_list = [str(t).replace('-','').replace(':','').replace(' ', '') for t in time_list]
        return time_list

    def getAmount(self, wage, fraud_times):
        amountList = []
        gamma_amount = gamma(shape=2., scale=0.3, size=1, multi=wage * 0.3)[0]
        total_amount = 3000 + gamma_amount
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

