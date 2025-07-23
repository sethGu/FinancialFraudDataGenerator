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
        # duration = 28  # 生成的持续时间
        end_day_str, (end_year, end_month, end_day) = getday(y=start_year, m=start_month, d=start_day, n=duration)
        # print(end_day_str, end_year, end_month, end_day)


        # 读取user
        user_list =  self.userService.selectUsers()

        store_list = self.storeService.selectStores()
        # for store in store_list:
        #     print(store)

        for d in range(duration):
            today_day_str, (today_year, today_month, today_day) = getday(y=start_year, m=start_month, d=start_day, n=d)
            # print("d:",d)
            for user in user_list: # 针对每一个用户
                # 第一步：确定要生成的消费数量
                # 每个用户 累加:每天每种类型消费次数最大值*对应消费类型概率，在一定范围内随机浮动。表1和表3
                # 赵征明生成
                consume_times = get_consume_times(user)
                consume_daily_type_times = dict()
                # 针对该用户的每一笔交易 consume c
                for c in range(consume_times):
                    try:
                        # 第二步：通过用户数据，通过加权随机获取消费商户类型（大类）
                        c_type = get_consume_type(user.get_user_info(), consume_daily_type_times)
                        consume_daily_type_times[c_type] = consume_daily_type_times.get(c_type,0) + 1

                        # 第三步：通过用户数据，获取消费层次
                        c_rank = get_consume_rank(user, c_type)

                        # print(user.getWage(), c_type, c_rank)
                        try:
                            # 第四步：选择消费对象商户与银行卡
                            store = get_store_by_type_rank(c_type, c_rank, store_list)
                        except Exception as e:
                            # print("报错，可能没有生成出对应类型商户",e)
                            continue

                        # 第五步：选择消费金额
                        amount = get_amount(store)
                        amount = amount + randint(0, 100) / 100

                        # 第六步：选择消费时间
                        time = get_consume_time(c_rank)

                        # 第七步：选择用户银行卡
                        user_card = get_user_card(user,store)
                        time2 = str(today_year)+str(today_month).zfill(2)+str(today_day).zfill(2)
                        abnormal = 0
                        abnormal_state= {"赌博违规交易": 0, "伪冒注册欺诈": 0,"信用卡违规套现":0, "黄牛营销欺诈":0, "商户违规":0,"异常转账":0}


                        S30s = json.loads(store.getS30())
                        S30 = "00000000"
                        for key, value in S30s.items():
                            if value == "正常":
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
                        # print('生成失败，跳过本次生成',result)
                        continue


if __name__ == '__main__':
    cf = ConsumptionFactory()
    cf.generate_data(2022,2,1,1)
    # consume_daily_type_times = dict()
    # user = cf.userService.selectUsers()
    # for u in user:
    #     c_type = get_consume_type(u.get_user_info(), consume_daily_type_times)
    #     print(get_consume_rank(u, c_type))


