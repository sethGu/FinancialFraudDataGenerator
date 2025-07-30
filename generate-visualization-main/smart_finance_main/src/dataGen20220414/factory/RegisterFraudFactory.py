import datetime
import json

from src.dataGen20220414.entity.Trans import Trans
from src.dataGen20220414.service.CardService import CardService
from src.dataGen20220414.service.StoreService import StoreService
from src.dataGen20220414.service.TransService import TransService
from src.dataGen20220414.service.UserService import UserService
from src.utils.config import BASE_DIR
from src.utils.functions import read_json_file
import random

class RegisterFraudFactory:
    def __init__(self):
        scene = 'Fake_registration'
        self.userService = UserService(scene)
        self.cardService = CardService(scene)
        self.transService = TransService(scene)
        self.storeService = StoreService(scene)

    def create_abnormal_register_data(self, startDate, n):
        userLists = self.pick_victim(n)
        for userList in userLists:
            type = self.chooseType()
            targetStoreList = self.getTargetStoreList()
            targetUserList = self.getTargetUserList(self.userService.selectAllUser(), userList)
            for user in userList:
                if type == 'Cash_out':
                    cardList = self.getCardList(type, user.getId())
                    if cardList != None:
                        for card in cardList:
                            testTimeList, implementTimeList = self.getTimeList(startDate)
                            amountTestList = self.getAmountList("Test", card.getC8()[0:2], len(testTimeList))
                            amountImplementList = self.getAmountList("Crime", card.getC8()[0:2], len(implementTimeList))
                            for index, time in enumerate(testTimeList):
                                targetObject = random.choice(targetStoreList['Cash_out'])
                                targetCardId = targetObject.getCard_id()
                                self.userService.updateUserState(user.getId(), 'Fake_registration')
                                self.cardService.updateCardState(card.getC4(), 'Fake_registration')
                                F16s = json.loads(targetObject.getS30())
                                F16 = "00000000"
                                for key, value in F16s.items():
                                    if value == "Normal":
                                        F16 = key
                                        break
                                self.transService.insertTrans(Trans(
                                    id=0,
                                    T2='01',
                                    T1=card.getC4(),
                                    T6='0',
                                    T14='4',
                                    T17=amountTestList[index],
                                    T19=time[11:13]+time[14:16]+time[17:19],
                                    T23=time[0:4]+time[5:7]+time[8:10],
                                    T26=card.getC5(),
                                    T37=targetCardId,
                                    T25=targetObject.getS1(),
                                    T31=F16,
                                    abnormal=1,
                                    abnormal_state= {"Gambling_violation":0, "Fake_registration":1,"Credit_card_fraud":0, "Scalper_marketing":0, "Merchant_violation":0,"Abnormal_transfer":0}
                                    ))

                            for index, time in enumerate(implementTimeList):
                                targetObject = random.choice(targetStoreList['Cash_out'])
                                targetCardId = targetObject.getCard_id()
                                self.userService.updateUserState(user.getId(), 'Fake_registration')
                                self.cardService.updateCardState(card.getC4(), 'Fake_registration')
                                F16s = json.loads(targetObject.getS30())
                                F16 = "00000000"
                                for key, value in F16s.items():
                                    if value == "Normal":
                                        F16 = key
                                        break
                                self.transService.insertTrans(Trans(
                                    id=0,
                                    T2='01',
                                    T1=card.getC4(),
                                    T6='0',
                                    T14='4',
                                    T17=amountImplementList[index],
                                    T19=time[11:13] + time[14:16] + time[17:19],
                                    T23=time[0:4] + time[5:7] + time[8:10],
                                    T26=card.getC5(),
                                    T37=targetCardId,
                                    T25=targetObject.getS1(),
                                    T31=F16,
                                    abnormal=1,
                                    abnormal_state={"Gambling_violation":0, "Fake_registration":1,"Credit_card_fraud":0, "Scalper_marketing":0, "Merchant_violation":0,"Abnormal_transfer":0}
                                ))
                elif type == 'Withdraw_cash':
                    cardList = self.getCardList(type, user.getId())
                    if cardList != None:
                        for card in cardList:
                            testTimeList, implementTimeList = self.getTimeList(startDate)

                            amountTestList = self.getAmountList("Test", card.getC8()[0:2], len(testTimeList))
                            amountImplementList = self.getAmountList("Crime", card.getC8()[0:2], len(implementTimeList))

                            for index, time in enumerate(testTimeList):
                                targetObject = card
                                targetCardId = targetObject.getC4()
                                self.userService.updateUserState(user.getId(), 'Fake_registration')
                                self.cardService.updateCardState(card.getC4(), 'Fake_registration')

                                self.transService.insertTrans(Trans(
                                    id=0,
                                    T2='02',
                                    T1=card.getC4(),
                                    T6='0',
                                    T14='4',
                                    T17=amountTestList[index],
                                    T19=time[11:13] + time[14:16] + time[17:19],
                                    T23=time[0:4] + time[5:7] + time[8:10],
                                    T26=card.getC5(),
                                    T37=targetCardId,
                                    T25='000000000000000',
                                    T31='00000000',
                                    abnormal=1,
                                    abnormal_state={"Gambling_violation":0, "Fake_registration":1,"Credit_card_fraud":0, "Scalper_marketing":0, "Merchant_violation":0,"Abnormal_transfer":0}
                                ))

                            for index, time in enumerate(implementTimeList):
                                targetObject = card
                                targetCardId = targetObject.getC4()
                                self.userService.updateUserState(user.getId(), 'Fake_registration')
                                self.cardService.updateCardState(card.getC4(), 'Fake_registration')
                                self.transService.insertTrans(Trans(
                                    id=0,
                                    T2='02',
                                    T1=card.getC4(),
                                    T6='0',
                                    T14='4',
                                    T17=amountImplementList[index],
                                    T19=time[11:13] + time[14:16] + time[17:19],
                                    T23=time[0:4] + time[5:7] + time[8:10],
                                    T26=card.getC5(),
                                    T37=targetCardId,
                                    T25='000000000000000',
                                    T31='00000000',
                                    abnormal=1,
                                    abnormal_state={"Gambling_violation":0, "Fake_registration":1,"Credit_card_fraud":0, "Scalper_marketing":0, "Merchant_violation":0,"Abnormal_transfer":0}
                                ))
                elif type == 'Transfer':
                    cardList = self.getCardList(type, user.getId())
                    if cardList != None:
                        for card in cardList:
                            testTimeList, implementTimeList = self.getTimeList(startDate)

                            amountTestList = self.getAmountList("Test", card.getC8()[0:2], len(testTimeList))
                            amountImplementList = self.getAmountList("Crime",card.getC8()[0:2], len(implementTimeList))
                            for index, time in enumerate(testTimeList):
                                targetObject = random.choice(targetUserList)
                                targetCardList = json.loads(targetObject.getCard())
                                random.shuffle(targetCardList)
                                targetCard = None
                                for card in targetCardList:
                                    if card['C5'] == '01':
                                        targetCard = card
                                        break
                                if targetCard == None:
                                    continue
                                targetCardId = targetCard['C4']
                                self.userService.updateUserState(user.getId(), 'Fake_registration')
                                self.cardService.updateCardState(card['C4'], 'Fake_registration')
                                self.transService.insertTrans(Trans(
                                    id=0,
                                    T2='03',
                                    T1=card['C4'],
                                    T6='0',
                                    T14='4',
                                    T17=amountTestList[index],
                                    T19=time[11:13] + time[14:16] + time[17:19],
                                    T23=time[0:4] + time[5:7] + time[8:10],
                                    T26=card['C5'],
                                    T37=targetCardId,
                                    T25='000000000000000',
                                    T31='00000000',
                                    abnormal=1,
                                    abnormal_state={"Gambling_violation":0, "Fake_registration":1,"Credit_card_fraud":0, "Scalper_marketing":0, "Merchant_violation":0,"Abnormal_transfer":0}
                                ))
                            for index, time in enumerate(implementTimeList):
                                targetObject = random.choice(targetUserList)
                                targetCardList = json.loads(targetObject.getCard())
                                random.shuffle(targetCardList)
                                targetCard = None
                                for card in targetCardList:
                                    if card['C5'] == '01':
                                        targetCard = card
                                        break
                                if targetCard == None:
                                    continue
                                targetCardId = targetCard['C4']
                                self.userService.updateUserState(user.getId(), 'Fake_registration')
                                self.cardService.updateCardState(card['C4'], 'Fake_registration')
                                self.transService.insertTrans(Trans(
                                    id=0,
                                    T2='03',
                                    T1=card['C4'],
                                    T6='0',
                                    T14='4',
                                    T17=amountImplementList[index],
                                    T19=time[11:13] + time[14:16] + time[17:19],
                                    T23=time[0:4] + time[5:7] + time[8:10],
                                    T26=card['C5'],
                                    T37=targetCardId,
                                    T25='000000000000000',
                                    T31='00000000',
                                    abnormal=1,
                                    abnormal_state={"Gambling_violation":0, "Fake_registration":1,"Credit_card_fraud":0, "Scalper_marketing":0, "Merchant_violation":0,"Abnormal_transfer":0}
                                ))
                elif type == 'Consumption':
                    cardList = self.getCardList(type, user.getId())
                    if cardList != None:
                        for card in cardList:
                            testTimeList, implementTimeList = self.getTimeList(startDate)

                            amountTestList = self.getAmountList("Test", card.getC8()[0:2], len(testTimeList))
                            amountImplementList = self.getAmountList("Crime", card.getC8()[0:2], len(implementTimeList))
                            for index, time in enumerate(testTimeList):
                                targetObject = random.choice(targetStoreList['Consumption'])
                                targetCardId = targetObject.getCard_id()
                                self.userService.updateUserState(user.getId(), 'Fake_registration')
                                self.cardService.updateCardState(card.getC4(), 'Fake_registration')
                                F16s = json.loads(targetObject.getS30())
                                F16 = "00000000"
                                for key, value in F16s.items():
                                    if value == "Normal":
                                        F16 = key
                                        break
                                self.transService.insertTrans(Trans(
                                    id=0,
                                    T2='01',
                                    T1=card.getC4(),
                                    T6='0',
                                    T14='4',
                                    T17=amountTestList[index],
                                    T19=time[11:13] + time[14:16] + time[17:19],
                                    T23=time[0:4] + time[5:7] + time[8:10],
                                    T26=card.getC5(),
                                    T37=targetCardId,
                                    T25=targetObject.getS1(),
                                    T31=F16,
                                    abnormal=1,
                                    abnormal_state={"Gambling_violation":0, "Fake_registration":1,"Credit_card_fraud":0, "Scalper_marketing":0, "Merchant_violation":0,"Abnormal_transfer":0}
                                ))


                            for index, time in enumerate(implementTimeList):
                                targetObject = random.choice(targetStoreList['Consumption'])
                                targetCardId = targetObject.getCard_id()
                                self.userService.updateUserState(user.getId(), 'Fake_registration')
                                self.cardService.updateCardState(card.getC4(), 'Fake_registration')
                                F16s = json.loads(targetObject.getS30())
                                F16 = "00000000"
                                for key, value in F16s.items():
                                    if value == "Normal":
                                        F16 = key
                                        break
                                self.transService.insertTrans(Trans(
                                    id=0,
                                    T2='01',
                                    T1=card.getC4(),
                                    T6='0',
                                    T14='4',
                                    T17=amountImplementList[index],
                                    T19=time[11:13] + time[14:16] + time[17:19],
                                    T23=time[0:4] + time[5:7] + time[8:10],
                                    T26=card.getC5(),
                                    T37=targetCardId,
                                    T25=targetObject.getS1(),
                                    T31=F16,
                                    abnormal=1,
                                    abnormal_state={"Gambling_violation":0, "Fake_registration":1,"Credit_card_fraud":0, "Scalper_marketing":0, "Merchant_violation":0,"Abnormal_transfer":0}
                                ))

    def pick_victim(self, N):
        N_victim_groups = []

        user_list = self.userService.selectUsers()

        easy_victim = []
        uneasy_victim = []
        for user in user_list:
            if user.getAge() > 70 or (user.getAge() > 18 and user.getAge() < 22) or user.getWage() < 100000:
                easy_victim.append(user)
            else:
                uneasy_victim.append(user)

        for i in range(N):
            victim_list = []
            num = random.randint(1, 13)
            for j in range(num):
                user = None
                a = random.random()
                not_found = False
                if a <= 0.6:
                    if len(easy_victim) == 0:
                        not_found = True
                    else:
                        user = random.choice(easy_victim)
                        cnt = 0
                        while (user in victim_list):
                            cnt += 1
                            if cnt == 10:
                                not_found = True
                                break
                            user = random.choice(easy_victim)
                if a > 0.6 or not_found == True:
                    user = random.choice(uneasy_victim)
                    while (user in victim_list):
                        user = random.choice(uneasy_victim)
                if user != None:
                    victim_list.append(user)
            N_victim_groups.append(victim_list)
        return N_victim_groups

    def chooseType(self):
        typeDic = {0:'Cash_out', 1:'Withdraw_cash', 2:'Transfer', 3:'Consumption'}
        return typeDic[random.randint(0, 3)]

    def get_fraud_store(self, quantity):
        store_list = []

        rank_prob = [0.4, 0.5, 0.1]

        low_rank_quantity = int(quantity * rank_prob[0])
        middle_rank_quantity = int(quantity * rank_prob[1])
        high_rank_quantity = int(quantity * rank_prob[2])

        stores = self.storeService.selectStores()
        random.shuffle(stores)

        for store in stores:
            if low_rank_quantity == 0 and middle_rank_quantity == 0 and high_rank_quantity == 0:
                break

            rank = store.getLevel()

            jsonfile = BASE_DIR + '/src/json_file/store_rank_classes.json'
            store_rank_classes = read_json_file(jsonfile)
            low_sub_classes = []
            middle_sub_classes = []
            high_sub_classes = []

            for key, map in store_rank_classes.items():
                low_sub_classes.extend(map['Low'])
                middle_sub_classes.extend(map['Medium'])
                high_sub_classes.extend(map['High'])

            if rank in low_sub_classes and low_rank_quantity > 0:
                low_rank_quantity -= 1
                store_list.append(store)
            elif rank in middle_sub_classes and middle_rank_quantity > 0:
                middle_rank_quantity -= 1
                store_list.append(store)
            elif rank in high_sub_classes and high_rank_quantity > 0:
                high_rank_quantity -= 1
                store_list.append(store)

        return store_list

    def segment_stors_to_personal_or_group(self, stores):

        random.shuffle(stores)

        personal_ratio = 0.8

        personal_stores = stores[0: int(len(stores) * personal_ratio)]

        stores = stores[len(personal_stores):]

        lens = len(stores)

        group_size = [4, 10]

        stores_groups = []

        choose_stores_num = 0

        while True:
            cur_size = random.randint(group_size[0], group_size[1])

            if cur_size + choose_stores_num < lens:
                group = stores[choose_stores_num: choose_stores_num + cur_size]
                stores_groups.append(group)
            else:
                group = stores[choose_stores_num:]
                stores_groups.append(group)
                break
            choose_stores_num += cur_size

        return personal_stores, stores_groups

    def getTargetStoreList(self):
        targetStoreDict = {}
        fraud_store = self.get_fraud_store(150)
        personal_stores, store_groups = self.segment_stors_to_personal_or_group(fraud_store)
        # personal_stores.extend(store_groups)
        targetStoreDict['Cash_out'] = personal_stores

        store_list = []
        rank_prob = [0.4, 0.4, 0.2]
        low_rank_quantity = int(200 * rank_prob[0])
        middle_rank_quantity = int(200 * rank_prob[1])
        high_rank_quantity = int(200 * rank_prob[2])

        stores = self.storeService.selectStores()
        random.shuffle(stores)

        jsonfile = BASE_DIR + '/src/json_file/store_rank_classes.json'
        store_rank_classes = read_json_file(jsonfile)
        low_sub_classes = []
        middle_sub_classes = []
        high_sub_classes = []

        for key, map in store_rank_classes.items():
            low_sub_classes.extend(map['Low'])
            middle_sub_classes.extend(map['Medium'])
            high_sub_classes.extend(map['High'])

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

        targetStoreDict['Consumption'] = store_list
        return targetStoreDict

    def getTargetUserList(self, allUsers, victimList, list_len=10):
        ab_list = []
        for i in range(list_len):
            t = random.randint(0, len(allUsers) - 1)
            while allUsers[t] in victimList:
                t = random.randint(0, len(allUsers) - 1)
            ab_list.append(allUsers[t])
        return ab_list

    def getCardList(self, type, userId):
        user_card = self.cardService.getCardByOwnerId(userId)

        credit_card = []
        debit_card = []
        for card in user_card:
            if card.getC5() == "01":
                debit_card.append(card)
            else:
                credit_card.append(card)

        if (len(user_card) == 0) or (type == 'Cash_out' and len(credit_card) == 0) or (type == 'Withdraw_cash' and len(debit_card) == 0):
            return None

        card_list = []
        if type == 'Cash_out':
            num = random.randint(1, len(credit_card))
            card_list = random.sample(credit_card, num)
        elif type == 'Withdraw_cash':
            num = random.randint(1, len(debit_card))
            card_list = random.sample(debit_card, num)
        elif type == 'Transfer':
            if len(debit_card) == 0:
                credit_card_num = random.randint(1, len(credit_card))
                card_list = random.sample(credit_card, credit_card_num)
            else:
                num = random.randint(1, len(debit_card))
                card_list = random.sample(debit_card, num)
                debit_card_num = len(card_list)
                a = random.uniform(0.8, 1)
                sum = int(debit_card_num / a)
                credit_card_num = min((sum - debit_card_num), len(credit_card))
                card_list.extend(random.sample(credit_card, credit_card_num))
        else:
            if len(credit_card) == 0:
                debit_card_num = random.randint(1, len(debit_card))
                card_list = random.sample(debit_card, debit_card_num)
            else:
                num = random.randint(1, len(credit_card))
                card_list = random.sample(credit_card, num)
                credit_card_num = len(card_list)
                a = random.uniform(0.8, 1)
                sum = int(credit_card_num / a)
                debit_card_num = min((sum - credit_card_num), len(debit_card))
                card_list.extend(random.sample(debit_card, debit_card_num))
        return card_list

    def getTimeList(self, start_date='20220501', days=1, trans_list_len=5):
        gap = 20

        start_date = datetime.datetime.strptime(start_date, '%Y%m%d')
        days = random.randint(0, days)

        hours = random.randint(0, 23)
        p = random.random()
        if p < 0.8:
            hours = random.randint(-2, 6)
            hours += 24
        minutes = random.randint(0, 59)

        test_date = start_date + datetime.timedelta(days=days, hours=hours, minutes=minutes)

        time_list = []
        time_list.append(test_date)
        for i in range(trans_list_len):
            delt_min = random.randint(1, gap)
            this_time = time_list[-1] + datetime.timedelta(minutes=delt_min)
            time_list.append(this_time)
        time_list = [str(t) for t in time_list]
        return time_list[0:1], time_list[1:]

    def getAmountList(self, type='Crime', card_level='01', list_len=3):
        mini_amount = [10, 100]
        constrain_amount_dict = {'01': 10000, '02': 30000, '03': 200000, '04': 500000}
        if type == 'Test':
            amount_list = []
            for i in range(list_len):
                amount = random.randint(mini_amount[0], mini_amount[1])
                amount_list.append(amount)
            return amount_list

        else:
            amount_limit = 1000

            if card_level in constrain_amount_dict.keys():
                    amount_limit = constrain_amount_dict[card_level]

            amount_list = []
            for i in range(list_len):
                amount = random.randint(amount_limit - 100, amount_limit)
                amount_list.append(amount)
            return amount_list
