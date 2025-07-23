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
        scene = '伪冒注册欺诈'
        self.userService = UserService(scene)
        self.cardService = CardService(scene)
        self.transService = TransService(scene)
        self.storeService = StoreService(scene)

    def create_abnormal_register_data(self, startDate, n):
        userLists = self.pick_victim(n)
        for userList in userLists:
            type = self.chooseType()
            # 返回商户id的list
            targetStoreList = self.getTargetStoreList()
            # 返回被转账对象id的list（和转账对象id的list互斥）
            targetUserList = self.getTargetUserList(self.userService.selectAllUser(), userList)
            for user in userList:
                if type == '套现':
                    # 根据userId和场景选择自己的对应卡
                    cardList = self.getCardList(type, user.getId())
                    if cardList != None:
                        for card in cardList:
                            # 根据开始时间，返回测试时间list和实施时间list
                            testTimeList, implementTimeList = self.getTimeList(startDate)
                            # 根据时间的类型以及对象卡id的list的长度，获得对应的金额
                            amountTestList = self.getAmountList("测试", card.getC8()[0:2], len(testTimeList))
                            amountImplementList = self.getAmountList("犯罪", card.getC8()[0:2], len(implementTimeList))
                            for index, time in enumerate(testTimeList):
                                targetObject = random.choice(targetStoreList['套现'])
                                # 根据目标对象，获取它对应的卡id
                                targetCardId = targetObject.getCard_id()
                                # 更新操作者和其卡的abnormal_state
                                self.userService.updateUserState(user.getId(), '伪冒注册欺诈')
                                self.cardService.updateCardState(card.getC4(), '伪冒注册欺诈')
                                F16s = json.loads(targetObject.getS30())
                                F16 = "00000000"
                                for key, value in F16s.items():
                                    if value == "正常":
                                        F16 = key
                                        break
                                # 插入数据
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
                                    abnormal_state= {"赌博违规交易": 0, "伪冒注册欺诈": 1,"信用卡违规套现":0, "黄牛营销欺诈":0, "商户违规":0,"异常转账":0}
                                    ))

                            for index, time in enumerate(implementTimeList):
                                targetObject = random.choice(targetStoreList['套现'])
                                # 根据目标对象，获取它对应的卡id
                                targetCardId = targetObject.getCard_id()
                                # 更新操作者和其卡的abnormal_state
                                self.userService.updateUserState(user.getId(), '伪冒注册欺诈')
                                self.cardService.updateCardState(card.getC4(), '伪冒注册欺诈')
                                F16s = json.loads(targetObject.getS30())
                                F16 = "00000000"
                                for key, value in F16s.items():
                                    if value == "正常":
                                        F16 = key
                                        break
                                # 插入数据
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
                                    abnormal_state={"赌博违规交易": 0, "伪冒注册欺诈": 1, "信用卡违规套现": 0, "黄牛营销欺诈": 0, "商户违规": 0,
                                                    "异常转账": 0}
                                ))
                elif type == '取现':
                    # 根据userId和场景选择自己的对应卡
                    cardList = self.getCardList(type, user.getId())
                    if cardList != None:
                        for card in cardList:
                            # 根据开始时间，返回测试时间list和实施时间list
                            testTimeList, implementTimeList = self.getTimeList(startDate)

                            amountTestList = self.getAmountList("测试", card.getC8()[0:2], len(testTimeList))
                            amountImplementList = self.getAmountList("犯罪", card.getC8()[0:2], len(implementTimeList))

                            for index, time in enumerate(testTimeList):
                                targetObject = card
                                # 根据目标对象，获取它对应的卡id
                                targetCardId = targetObject.getC4()
                                # 更新操作者和其卡的abnormal_state
                                self.userService.updateUserState(user.getId(), '伪冒注册欺诈')
                                self.cardService.updateCardState(card.getC4(), '伪冒注册欺诈')

                                # 插入数据
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
                                    abnormal_state={"赌博违规交易": 0, "伪冒注册欺诈": 1, "信用卡违规套现": 0, "黄牛营销欺诈": 0, "商户违规": 0,
                                                    "异常转账": 0}
                                ))

                            for index, time in enumerate(implementTimeList):
                                targetObject = card
                                # 根据目标对象，获取它对应的卡id
                                targetCardId = targetObject.getC4()
                                # 更新操作者和其卡的abnormal_state
                                self.userService.updateUserState(user.getId(), '伪冒注册欺诈')
                                self.cardService.updateCardState(card.getC4(), '伪冒注册欺诈')
                                # 插入数据
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
                                    abnormal_state={"赌博违规交易": 0, "伪冒注册欺诈": 1, "信用卡违规套现": 0, "黄牛营销欺诈": 0, "商户违规": 0,
                                                    "异常转账": 0}
                                ))
                elif type == '转账':
                    # 根据userId和场景选择自己的对应卡
                    cardList = self.getCardList(type, user.getId())
                    if cardList != None:
                        for card in cardList:
                            # 根据开始时间，返回测试时间list和实施时间list
                            testTimeList, implementTimeList = self.getTimeList(startDate)

                            amountTestList = self.getAmountList("测试", card.getC8()[0:2], len(testTimeList))
                            amountImplementList = self.getAmountList("犯罪",card.getC8()[0:2], len(implementTimeList))
                            for index, time in enumerate(testTimeList):
                                targetObject = random.choice(targetUserList)
                                # 根据目标对象，获取它对应的卡id
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
                                # 更新操作者和其卡的abnormal_state
                                self.userService.updateUserState(user.getId(), '伪冒注册欺诈')
                                self.cardService.updateCardState(card['C4'], '伪冒注册欺诈')
                                # 插入数据
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
                                    abnormal_state={"赌博违规交易": 0, "伪冒注册欺诈": 1, "信用卡违规套现": 0, "黄牛营销欺诈": 0, "商户违规": 0,
                                                    "异常转账": 0}
                                ))
                            for index, time in enumerate(implementTimeList):
                                targetObject = random.choice(targetUserList)
                                # 根据目标对象，获取它对应的卡id
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
                                # 更新操作者和其卡的abnormal_state
                                self.userService.updateUserState(user.getId(), '伪冒注册欺诈')
                                self.cardService.updateCardState(card['C4'], '伪冒注册欺诈')
                                # 插入数据
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
                                    abnormal_state={"赌博违规交易": 0, "伪冒注册欺诈": 1, "信用卡违规套现": 0, "黄牛营销欺诈": 0, "商户违规": 0,
                                                    "异常转账": 0}
                                ))
                elif type == '消费':
                    # 根据userId和场景选择自己的对应卡
                    cardList = self.getCardList(type, user.getId())
                    if cardList != None:
                        for card in cardList:
                            # 根据开始时间，返回测试时间list和实施时间list
                            testTimeList, implementTimeList = self.getTimeList(startDate)

                            amountTestList = self.getAmountList("测试", card.getC8()[0:2], len(testTimeList))
                            amountImplementList = self.getAmountList("犯罪", card.getC8()[0:2], len(implementTimeList))
                            for index, time in enumerate(testTimeList):
                                targetObject = random.choice(targetStoreList['消费'])
                                # 根据目标对象，获取它对应的卡id
                                targetCardId = targetObject.getCard_id()
                                # 更新操作者和其卡的abnormal_state
                                self.userService.updateUserState(user.getId(), '伪冒注册欺诈')
                                self.cardService.updateCardState(card.getC4(), '伪冒注册欺诈')
                                F16s = json.loads(targetObject.getS30())
                                F16 = "00000000"
                                for key, value in F16s.items():
                                    if value == "正常":
                                        F16 = key
                                        break
                                # 插入数据
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
                                    abnormal_state={"赌博违规交易": 0, "伪冒注册欺诈": 1, "信用卡违规套现": 0, "黄牛营销欺诈": 0, "商户违规": 0,
                                                    "异常转账": 0}
                                ))


                            for index, time in enumerate(implementTimeList):
                                targetObject = random.choice(targetStoreList['消费'])
                                # 根据目标对象，获取它对应的卡id
                                targetCardId = targetObject.getCard_id()
                                # 更新操作者和其卡的abnormal_state
                                self.userService.updateUserState(user.getId(), '伪冒注册欺诈')
                                self.cardService.updateCardState(card.getC4(), '伪冒注册欺诈')
                                F16s = json.loads(targetObject.getS30())
                                F16 = "00000000"
                                for key, value in F16s.items():
                                    if value == "正常":
                                        F16 = key
                                        break
                                # 插入数据
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
                                    abnormal_state={"赌博违规交易": 0, "伪冒注册欺诈": 1, "信用卡违规套现": 0, "黄牛营销欺诈": 0, "商户违规": 0,
                                                    "异常转账": 0}
                                ))

    # 需不需要考虑有一些人更容易被选中
    def pick_victim(self, N):  # N是犯罪分子的个数=受害者的组数
        N_victim_groups = []

        # 选出所有人
        user_list = self.userService.selectUsers()

        # 选出一些人更容易被选中成为受害者，比如年龄太小、太大的、工资太低的
        # 其实应该满足长尾分布，有些人的信息被盗就会经常被盗刷
        easy_victim = []
        uneasy_victim = []
        for user in user_list:
            if user.getAge() > 70 or (user.getAge() > 18 and user.getAge() < 22) or user.getWage() < 100000:
                easy_victim.append(user)
            else:
                uneasy_victim.append(user)

        for i in range(N):
            victim_list = []
            num = random.randint(1, 13)  # 一组受害者有1-130个人
            for j in range(num):
                user = None
                a = random.random()
                not_found = False
                if a <= 0.6:  # 有0.6的可能性从易成为受害者的人群中选中
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

    '''
    选择此次诈骗的类型
    '套现','取现','转账','消费'
    '''
    def chooseType(self):
        typeDic = {0:'套现', 1:'取现', 2:'转账', 3:'消费'}
        return typeDic[random.randint(0, 3)]

    # 如果是套现，一般来说，一个欺诈人会有一个固定的套现商户团伙，也可能是个人套现商户，且是中低端较多
    # 如果是消费，随机一个商户就行，中高端为主
    # 返回一个dict：{ '套现':[,,,...], '消费':[,,,...] }
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

            jsonfile = BASE_DIR + '/src/json_file/store_rank_classes.json'
            store_rank_classes = read_json_file(jsonfile)
            low_sub_classes = []
            middle_sub_classes = []
            high_sub_classes = []

            for key, map in store_rank_classes.items():
                low_sub_classes.extend(map['低'])
                middle_sub_classes.extend(map['中'])
                high_sub_classes.extend(map['高'])

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

        return store_list

    def segment_stors_to_personal_or_group(self, stores):

        random.shuffle(stores)

        # 个人商户的比例
        personal_ratio = 0.8

        # 个人商户
        personal_stores = stores[0: int(len(stores) * personal_ratio)]

        # 剩下的作为商户团伙
        stores = stores[len(personal_stores):]

        # 剩下的商户数量
        lens = len(stores)

        # 团伙大小
        group_size = [4, 10]

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

    def getTargetStoreList(self):
        targetStoreDict = {}
        # 先生成套现的商户列表
        fraud_store = self.get_fraud_store(150)
        personal_stores, store_groups = self.segment_stors_to_personal_or_group(fraud_store)
        # personal_stores.extend(store_groups)
        targetStoreDict['套现'] = personal_stores

        # 再生成消费的商户列表
        store_list = []
        # 各类商户等级概率分布，中高为主
        rank_prob = [0.4, 0.4, 0.2]
        # 各类等级商户数量:低、中、高
        low_rank_quantity = int(200 * rank_prob[0])
        middle_rank_quantity = int(200 * rank_prob[1])
        high_rank_quantity = int(200 * rank_prob[2])

        # 获取所有商户列表
        stores = self.storeService.selectStores()
        random.shuffle(stores)

        jsonfile = BASE_DIR + '/src/json_file/store_rank_classes.json'
        store_rank_classes = read_json_file(jsonfile)
        low_sub_classes = []
        middle_sub_classes = []
        high_sub_classes = []

        for key, map in store_rank_classes.items():
            low_sub_classes.extend(map['低'])
            middle_sub_classes.extend(map['中'])
            high_sub_classes.extend(map['高'])

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

        targetStoreDict['消费'] = store_list
        return targetStoreDict

    def getTargetUserList(self, allUsers, victimList, list_len=10):
        '''
        :param allUsers: 总的用户列表
        :param victimList:
        :return: 异常用户列表
        '''
        ab_list = []
        for i in range(list_len):
            t = random.randint(0, len(allUsers) - 1)
            while allUsers[t] in victimList:
                t = random.randint(0, len(allUsers) - 1)
            ab_list.append(allUsers[t])
        return ab_list

    # 根据场景类型，选择受害人userId的某张卡
    # 套现：只能是信用卡
    # 取现：只能是借记卡
    # 转账：信用卡和借记卡都可以转入转出，更可能是借记卡
    # 消费：信用卡和借记卡都可以，更可能是信用卡
    def getCardList(self, type, userId):
        # 取这个人的所有卡

        user_card = self.cardService.getCardByOwnerId(userId)

        # 将这个人的所有卡分为信用卡和借记卡
        credit_card = []
        debit_card = []
        for card in user_card:
            if card.getC5() == "01":
                debit_card.append(card)
            else:
                credit_card.append(card)

        # 这个人都没有卡，或者套现但是没信用卡，取现但是没借记卡，直接return none
        if (len(user_card) == 0) or (type == '套现' and len(credit_card) == 0) or (type == '取现' and len(debit_card) == 0):
            return None

        card_list = []
        # 在1-卡总数的范围内随机一个数
        if type == '套现':
            num = random.randint(1, len(credit_card))
            card_list = random.sample(credit_card, num)
        elif type == '取现':
            num = random.randint(1, len(debit_card))
            card_list = random.sample(debit_card, num)
        elif type == '转账':
            # 先选出debit_card的一部分，但可能没有debit_card，那就随便选两张信用卡
            if len(debit_card) == 0:
                credit_card_num = random.randint(1, len(credit_card))
                card_list = random.sample(credit_card, credit_card_num)
            else:
                num = random.randint(1, len(debit_card))
                card_list = random.sample(debit_card, num)
                debit_card_num = len(card_list)
                # 再选择一部分信用卡，借记卡的比例为 0.8-1
                a = random.uniform(0.8, 1)
                # 即：sum * a = debit_card_num
                sum = int(debit_card_num / a)
                credit_card_num = min((sum - debit_card_num), len(credit_card))
                card_list.extend(random.sample(credit_card, credit_card_num))
        else:  # 消费，优先信用卡
            # 先选出credit_card的一部分，但可能没有信用卡，那就随便选两张借记卡
            if len(credit_card) == 0:
                debit_card_num = random.randint(1, len(debit_card))
                card_list = random.sample(debit_card, debit_card_num)
            else:  # 有起码一张信用卡
                num = random.randint(1, len(credit_card))
                card_list = random.sample(credit_card, num)
                credit_card_num = len(card_list)
                # 再选择一部分debit_card，信用卡的比例为 0.8-1
                a = random.uniform(0.8, 1)
                sum = int(credit_card_num / a)
                debit_card_num = min((sum - credit_card_num), len(debit_card))
                card_list.extend(random.sample(debit_card, debit_card_num))
        return card_list

    def getTimeList(self, start_date='20220501', days=1, trans_list_len=5):
        '''
            start_date 到 start_date+days指的是第0次测试交易所在的时间范围
            trans_list_len:不包括测试交易
            返回值：时间列表，第0项是测试时间，剩下是犯罪时间
        '''
        # 两次交易的最大间隔时间，单位为分钟
        gap = 20

        # 发生测试交易的日期
        start_date = datetime.datetime.strptime(start_date, '%Y%m%d')
        days = random.randint(0, days)

        # 发生交易测试具体几点
        hours = random.randint(0, 23)
        # 偏向于非营业时间交易(22-6点)
        p = random.random()
        if p < 0.8:
            hours = random.randint(-2, 6)
            hours += 24
        # 分钟纳入考虑，秒钟忽略
        minutes = random.randint(0, 59)

        # 发生交易测试的时间
        test_date = start_date + datetime.timedelta(days=days, hours=hours, minutes=minutes)

        time_list = []
        time_list.append(test_date)
        for i in range(trans_list_len):
            delt_min = random.randint(1, gap)
            this_time = time_list[-1] + datetime.timedelta(minutes=delt_min)
            time_list.append(this_time)
        time_list = [str(t) for t in time_list]
        return time_list[0:1], time_list[1:]

    def getAmountList(self, type='犯罪', card_level='01', list_len=3):
        '''
        type: '测试' 或 '犯罪'
        salary: 该卡持有人（受害者）工资
        card_level: 这张卡的卡等级
        list_len: 金额列表长度
        返回值: 金额列表
        '''
        # 测试小金额范围
        mini_amount = [10, 100]
        # 卡等级对应的单笔限额
        constrain_amount_dict = {'01': 10000, '02': 30000, '03': 200000, '04': 500000}
        if type == '测试':
            amount_list = []
            for i in range(list_len):
                amount = random.randint(mini_amount[0], mini_amount[1])
                amount_list.append(amount)
            return amount_list

        else:
            # 普卡限额
            amount_limit = 1000

            if card_level in constrain_amount_dict.keys():
                    amount_limit = constrain_amount_dict[card_level]

            amount_list = []
            for i in range(list_len):
                amount = random.randint(amount_limit - 100, amount_limit)
                amount_list.append(amount)
            return amount_list
