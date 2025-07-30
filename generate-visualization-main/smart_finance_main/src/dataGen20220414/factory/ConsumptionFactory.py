import json
from random import random, randint

from src.dataGen20220414.service.StoreService import StoreService
from src.dataGen20220414.service.TransService import TransService
from src.dataGen20220414.service.UserService import UserService
from src.utils.comsumptionFunction import get_consume_type, get_consume_rank, get_store_by_type_rank, get_user_card, \
    get_amount, get_consume_times
from src.utils.functions import getday
from src.utils.table_function import get_consume_time
from src.dataGen20220414.entity.Trans import Trans


class ConsumptionFactory:
    def __init__(self, scene):
        self.userService = UserService(scene)
        self.storeService = StoreService(scene)
        self.transService = TransService(scene)

    def generate_data(self,start_year,start_month,start_day,duration):
        # start_year = 2022
        # start_month = 2
        # start_day = 1
        # duration = 28
        end_day_str, (end_year, end_month, end_day) = getday(y=start_year, m=start_month, d=start_day, n=duration)
        # print(end_day_str, end_year, end_month, end_day)

        user_list =  self.userService.selectUsers()

        store_list = self.storeService.selectStores()
        # for store in store_list:
        #     print(store)

        for d in range(duration):
            today_day_str, (today_year, today_month, today_day) = getday(y=start_year, m=start_month, d=start_day, n=d)
            # print("d:",d)
            for user in user_list:
                consume_times = get_consume_times(user)
                consume_daily_type_times = dict()
                for c in range(consume_times):
                    try:
                        c_type = get_consume_type(user.get_user_info(), consume_daily_type_times)
                        consume_daily_type_times[c_type] = consume_daily_type_times.get(c_type,0) + 1

                        c_rank = get_consume_rank(user, c_type)

                        # print(user.getWage(), c_type, c_rank)
                        try:
                            store = get_store_by_type_rank(c_type, c_rank, store_list)
                        except Exception as e:
                            continue

                        amount = get_amount(store)
                        amount = amount + randint(0, 100) / 100

                        time = get_consume_time(c_rank)

                        user_card = get_user_card(user,store)
                        time2 = str(today_year)+str(today_month).zfill(2)+str(today_day).zfill(2)
                        abnormal = 0
                        abnormal_state= {"Gambling_violation": 0, "Fake_registration": 0,"Credit_card_fraud":0, "Scalper_marketing":0, "Merchant_violation":0,"Abnormal_transfer":0}


                        S30s = json.loads(store.getS30())
                        S30 = "00000000"
                        for key, value in S30s.items():
                            if value == "Normal":
                                S30 = key
                                break
                        trans = Trans(id=0,T2='01',T1=user_card['C4'],
                                      T6='0',T14='4',T17=amount,
                                      T19=time,T23=time2,
                                      T26=user_card['C5'],
                                      T37=store.card_id,T25=store.S1,
                                      T31=S30,
                                      abnormal = abnormal,
                                      abnormal_state=abnormal_state
                                      )
                        self.transService.insertTrans(trans)
                    except Exception as result:
                        continue


if __name__ == '__main__':
    cf = ConsumptionFactory()
    cf.generate_data(2022,2,1,1)
    # consume_daily_type_times = dict()
    # user = cf.userService.selectUsers()
    # for u in user:
    #     c_type = get_consume_type(u.get_user_info(), consume_daily_type_times)
    #     print(get_consume_rank(u, c_type))


