import json
import random
import datetime

from src.dataGen20220414.dao.FraudTransDao import FraudTransDao
from src.dataGen20220414.dao.TransDao import TransDao
from src.dataGen20220414.entity.Trans import Trans
from src.dataGen20220414.service.CardService import CardService
from src.dataGen20220414.service.StoreService import StoreService
from src.dataGen20220414.entity.FraudTrans import FraduTrans



class TransService():
    def __init__(self, scene):
        self.transDao = TransDao()
        self.fraudTransDao = FraudTransDao()
        self.storeService = StoreService(scene)
        self.cardService = CardService(scene)

        self.table_names = {"Scalper_marketing": 'marketing_trans', "Credit_card_fraud": 'credit_trans', "Abnormal_transfer": 'abnormal_trans',
                        "Fake_registration": 'register_trans', "Gambling_violation": 'gambling_trans',
                        "Merchant_violation": 'store_trans'}
        self.scene = self.table_names[scene]
    def createTransTable(self):
        self.transDao.createTransTable(self.scene)

    def createFraudTransTable(self):
        self.fraudTransDao.createFraudTransTable(self.scene.replace('trans', 'f_t'))

    def selectAllTrans(self):
        select_res = self.transDao.selectTrans(self.scene)
        transList = []
        for item in select_res:
            id, T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,T18,T19,T20,T21,T22,T23,T24,T25,T26,T27,T28,T29,T30,T31,T32,T33,T34,T35,T36,T37,T38,T39, abnormal, abnormal_state = item
            abnormal_state = json.loads(abnormal_state)
            trans = Trans(id, T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,T18,T19,T20,T21,T22,T23,T24,T25,T26,T27,T28,T29,T30,T31,T32,T33,T34,T35,T36,T37,T38,T39, abnormal, abnormal_state)

            transList.append(trans)
        return transList

    def selectAllTransByTime(self):
        select_res = self.transDao.selectTransByTime(self.scene)
        transList = []
        for item in select_res:
            id, T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,T18,T19,T20,T21,T22,T23,T24,T25,T26,T27,T28,T29,T30,T31,T32,T33,T34,T35,T36,T37,T38,T39, abnormal, abnormal_state = item
            abnormal_state = json.loads(abnormal_state)
            trans = Trans(id, T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,T18,T19,T20,T21,T22,T23,T24,T25,T26,T27,T28,T29,T30,T31,T32,T33,T34,T35,T36,T37,T38,T39, abnormal, abnormal_state)

            transList.append(trans)
        return transList

    def selectAllFraudTrans(self):
        select_res = self.fraudTransDao.selectFraudTrans(self.scene.replace('trans', 'f_t'))
        transList = []
        for item in select_res:
            id,F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, F13, F14, F15, F16, F17, F18, F19, F20, F21, F22, F23, F24, F25, F26, F27, F28, F29, F30, F31, F32, F33, F34, F35, F36, F37, F38, F39, F40, F41, F42, F43, F44, F45 = item
            f_t = FraduTrans(id,F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, F13, F14, F15, F16, F17, F18, F19, F20, F21, F22, F23, F24, F25, F26, F27, F28, F29, F30, F31, F32, F33, F34, F35, F36, F37, F38, F39, F40, F41, F42, F43, F44, F45)

            transList.append(f_t)
        return transList

    def insertTrans(self,trans):

        trans.T9 = ''.join(random.choice('0123456789') for _ in range(6))



        trans.T4 = ''.join(random.choice('0123456789') for _ in range(12))

        trans.T12 = ''.join(random.choice('0123456789') for _ in range(8))
        trans.T34 = ''.join(random.choice('0123456789') for _ in range(4))
        trans.T10 = trans.T23[-4:] + trans.T19


        trans.T30 = '0000'
        if trans.T25 == '000000000000000':
            trans.T28 = random.choice(['01', '03', '07'])
            trans.T32 = 'XXXX_transfer'
        else:
            store = self.storeService.selectStoreByS1(trans.T25)
            trans.T28 = '01'
            trans.T32 = store.name
            trans.T30 = store.S5


        m = ['00', '01', '02', '03', '04', '05', '06', '07', '10', '11', '12', '13', '14', '15']
        trans.T33 = random.choice(m) + random.choice(['0', '1', '2'])
        trans.T29 = '00000000'

        card_info = self.cardService.getCardInfoByC4(trans.T1)
        ###########################
        trans.T20 = card_info.C11
        trans.T13 = card_info.C11
        trans.T3 = card_info.C11

        trans.T24 = card_info.C11
        trans.T36 = card_info.C6
        trans.T22 = trans.T20 + trans.T9 + trans.T10 + '0' + trans.T3
        self.transDao.insertTrans(trans, self.scene)

        if trans.abnormal == 1:
            rmb_to_usd = 6.6958
            F1 = '000' + ''.join(random.choice('0123456789') for _ in range(20))

            F3 = trans.T13
            F4 = trans.T24
            F5 = trans.T4
            F6 = trans.T9
            F7 = trans.T27
            F8 = trans.T2
            F9 = trans.T28
            F10 = trans.T17
            F11 = trans.T17
            F12 = trans.T23
            F13 = trans.T19
            F14 = trans.T23
            F15 = trans.T33
            F16 = trans.T31
            F17 = trans.T25
            if trans.T25 == '000000000000000':
                F18 = 'XXXX'
                F19 = '0000'
            else:
                F18 = store.name
                F19 = store.S5
            F20 = trans.T5
            F21 = F3[-4:]
            F22 = '000'
            type = {"Scalper_marketing": 81, "Credit_card_fraud": 82, "Abnormal_transfer": 83, "Fake_registration": 84, "Gambling_violation": 85, "Merchant_violation": 86, "Merchant_gang_fraud": 87}
            F23 = 0
            for k, v in trans.abnormal_state.items():
                if v == 1:
                    F23 = type[k]
                    break
            F2 = trans.T1
            if F23 == 81:
                F2 = trans.T37

            F24 = '06'
            F25 = trans.T23
            F26 = trans.T10
            F27 = trans.T26
            F28 = '0'
            # ?
            F29 = '00000000'
            F30 = ''.join(random.choice('0123456789') for _ in range(8))
            dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            F31 = dt
            F32 = dt
            F33 = '0'
            F34 = '001'
            F35 = trans.T17
            F36 = '001'
            F37 = trans.T17
            F38 = F37 / rmb_to_usd
            F39 = ''.join(random.choice('0123456789') for _ in range(8))
            F40 = ''.join(random.choice('0123456789') for _ in range(12))
            F41 = ''.join(random.choice('0123456789') for _ in range(10))
            F42 = ''.join(random.choice('0123456789') for _ in range(16))
            F43 = '0'
            if F23 == 81 and trans.T2 == '01':
                F44 = int(trans.T17 * random.uniform(0.5, 0.8))
            else:
                F44 = trans.T17
            F45 = '001'

            f_t = FraduTrans(0, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, F13,
                 F14, F15, F16, F17, F18, F19, F20, F21, F22, F23, F24, F25, F26, F27, F28, F29,
                 F30, F31, F32, F33, F34, F35, F36, F37,F38, F39, F40, F41, F42, F43, F44, F45)
            self.fraudTransDao.insertFraudTrans(f_t, self.scene.replace('trans', 'f_t'))
