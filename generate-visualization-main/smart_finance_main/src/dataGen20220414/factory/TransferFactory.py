import json
import random

from src.dataGen20220414.service.CardService import CardService
from src.dataGen20220414.service.UserService import UserService
from src.dataGen20220414.service.RelativeService import RelativeService
from src.dataGen20220414.service.TransService import TransService
from src.dataGen20220414.service.TransferService import TransferService
from src.dataGen20220414.entity.Trans import Trans
from src.utils.functions import getday


def from_xflx_to_je(xflx):
    xflx_je_dict = {"小": "2-600", "中": "60-500", "大": "50-5000"}
    jefw = xflx_je_dict[xflx]
    je_st = int(jefw.strip("\"").split("-")[0])
    je_ed = int(jefw.strip("\"").split("-")[1])
    if xflx == '中':
        return random.randint(je_st, je_ed) * 10
    elif xflx == '大':
        return random.randint(je_st, je_ed) * 100
    return random.randint(je_st, je_ed)


def get_trans_time_duration(xflx):
    xflx_je_dict = {"小":"1-30", "中":"10-20", "大":"20-30" }
    jefw = xflx_je_dict[xflx]
    je_st = int(jefw.strip("\"").split("-")[0])
    je_ed = int(jefw.strip("\"").split("-")[1])
    return random.randint( je_st,je_ed )


class TransferFactory:
    def __init__(self, scene):
        self.userService = UserService(scene)
        self.relativeService = RelativeService(scene)
        self.transService = TransService(scene)
        self.cardService = CardService(scene)

    def generate_relative_transfer_data(self,start_year,start_month,start_day,duration):
        # start_year = 2022
        # start_month = 2
        # start_day = 1
        # duration = 365  # 生成的持续时间
        end_day_str, (end_year, end_month, end_day) = getday(y=start_year, m=start_month, d=start_day, n=duration)
        # print(end_day_str, end_year, end_month, end_day)

        # 读取user
        user_list =  self.userService.selectUsers()

        for d in range(duration):
            for user in user_list: # 针对每一个用户
                #第一步：根据工资生成总转账次数
                transferService = TransferService()
                total_trans_num = transferService.from_wage_to_total_trans_num(user.wage)
                # 第二步：根据总转账次数，得到user分别给1、2、3阶中亲戚的总转账记录条数
                per_ji_transfer_time = transferService.per_ji_tras_time( total_trans_num  )

                #针对1、2、3每一阶
                neighboursDic = self.relativeService.getNearestNeighborsOfN( user.id, 3 )
                for js in range(1,4):
                    if not neighboursDic.__contains__(js):
                        continue
                    benjie_qqlb = neighboursDic[js]
                    # 针对该用户每一阶的每一笔转账
                    for c in range( per_ji_transfer_time[js] ):
                        # 第三步：选择转账对象与他的银行卡
                        dx = random.choice(benjie_qqlb)
                        dx_card_list = self.cardService.getTransferCardByOwnerId(dx)     #查接受对象的银行卡列表
                        dx_card = random.choice( dx_card_list )

                        # 第四步：确定消费类型：学费、月度零花钱、日常小额转账【这里对应是确定大中小类型】
                        xflx = transferService.from_wage_to_xflx(user.wage)
                        # print("消费类型 ", xflx)
                        # 第四步：确定转账金额
                        je = from_xflx_to_je( xflx )
                        # print("金额",je)
                        #第五步：确定自己转出的信用卡。（这里要考虑转账金额要小于信用卡额度吗）
                        user_card = random.choice( user.getCard() )

                        # 第六步：根据消费类型，选择消费时间。消费类型越大，时间间隔越大
                        trans_time_duration = get_trans_time_duration( xflx )
                        # 到了转账的日子了：
                        if d % trans_time_duration == 0:
                            trans_time_duration = random.randint(
                                (trans_time_duration - 3) if trans_time_duration - 3 >= 0 else 0,
                                (trans_time_duration + 3) if trans_time_duration + 3 <= duration else duration)
                            today_day_str, (today_year, today_month, today_day) = getday(y=start_year, m=start_month,
                                                                                         d=start_day, n=trans_time_duration)
                            trans_time = today_day_str

                            hour = "%02d" % random.randint(0,23)

                            minute = "%02d" % random.randint(0, 59)

                            seconds = "%02d" % random.randint(0, 59)

                            time =  str(hour) + str(minute) + str(seconds)

                            trans = Trans(id=0, T1=dx_card.C4, T2='03',T3='00000000', T4='000000000000', T5='0000',
                                          T6='0',T7='01', T8='1', T9='000000',T10='', T11='0', T12='0000000000',T13='',
                                          T14='4',T15='',T16='0', T17=je, T18='01',
                                          T19=time, T20='00000000',T21='0',T22='',
                                          T23=today_day_str,T24='00000000', T25='000000000000000',
                                          T26=dx_card.C5, T27='00', T28='',
                                          T29='00000000', T30='', T31='00000000',T32='', T33='', T34='', T35='01', T36='', T37=user_card['C4'], T38='1',
                                          T39='1',
                                          abnormal=0,
                                          abnormal_state= {"赌博违规交易": 0, "伪冒注册欺诈": 0,"信用卡违规套现":0, "黄牛营销欺诈":0, "商户违规":0,"异常转账":0}
                                          )

                            self.transService.insertTrans(trans)


if __name__ == '__main__':
    tf = TransferFactory()
    tf.generate_relative_transfer_data(2022,2,1,365)
