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
    xflx_je_dict = {"Small": "2-600", "Medium": "60-500", "Large": "50-5000"}
    jefw = xflx_je_dict[xflx]
    je_st = int(jefw.strip("\"").split("-")[0])
    je_ed = int(jefw.strip("\"").split("-")[1])
    if xflx == 'Medium':
        return random.randint(je_st, je_ed) * 10
    elif xflx == 'Large':
        return random.randint(je_st, je_ed) * 100
    return random.randint(je_st, je_ed)


def get_trans_time_duration(xflx):
    xflx_je_dict = {"Small":"1-30", "Medium":"10-20", "Large":"20-30" }
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
        # duration = 365
        end_day_str, (end_year, end_month, end_day) = getday(y=start_year, m=start_month, d=start_day, n=duration)
        # print(end_day_str, end_year, end_month, end_day)

        user_list =  self.userService.selectUsers()

        for d in range(duration):
            for user in user_list:
                transferService = TransferService()
                total_trans_num = transferService.from_wage_to_total_trans_num(user.wage)
                per_ji_transfer_time = transferService.per_ji_tras_time( total_trans_num  )

                neighboursDic = self.relativeService.getNearestNeighborsOfN( user.id, 3 )
                for js in range(1,4):
                    if not neighboursDic.__contains__(js):
                        continue
                    benjie_qqlb = neighboursDic[js]
                    for c in range( per_ji_transfer_time[js] ):
                        dx = random.choice(benjie_qqlb)
                        dx_card_list = self.cardService.getTransferCardByOwnerId(dx)
                        dx_card = random.choice( dx_card_list )

                        xflx = transferService.from_wage_to_xflx(user.wage)
                        je = from_xflx_to_je( xflx )
                        user_card = random.choice( user.getCard() )

                        trans_time_duration = get_trans_time_duration( xflx )
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
                                          abnormal_state= {"Gambling_violation":0, "Fake_registration":0,"Credit_card_fraud":0, "Scalper_marketing":0, "Merchant_violation":0,"Abnormal_transfer":0}
                                          )

                            self.transService.insertTrans(trans)


if __name__ == '__main__':
    tf = TransferFactory()
    tf.generate_relative_transfer_data(2022,2,1,365)
