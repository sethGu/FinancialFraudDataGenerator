import json
import random
import numpy as np
from src.dataGen20220414.dao.CardDao import CardDao
from src.dataGen20220414.dao.StoreDao import StoreDao
from src.dataGen20220414.dao.UserDao import UserDao
from src.dataGen20220414.entity.Card import Card


class CardService():
    total_card_num = 1
    def __init__(self, scene):
        self.cardDao = CardDao()
        self.userDao = UserDao()
        self.storeDao = StoreDao()

        self.table_names = {"Scalper_marketing": 'marketing_card', "Credit_card_fraud": 'credit_card', "Abnormal_transfer": 'abnormal_card',
                            "Fake_registration": 'register_card', "Gambling_violation": 'gambling_card',
                            "Merchant_violation": 'store_card'}
        self.scene = self.table_names[scene]
    def createCardTable(self):

        # for name in self.table_names.values():
        self.cardDao.createCardTable(self.scene)

    def insertCard(self, card):
        self.cardDao.insertCard(card, self.scene)


    def insertCards(self,cardList, owner_id=None, index_by_id=True, user_no=None):
        for card in cardList:
            if owner_id!=None:
                card.setowner_id(owner_id)
            owner_id_ = card.getowner_id()
            owner_type = card.getowner_type()
            C4 = card.getC4()
            self.insertCard(card)
            if owner_type == "Regular_user":
                if index_by_id is True:
                    self.userDao.addUserCard(user_id=owner_id_, new_card=card, table_name=self.scene.replace("card", "user"))
                else:
                    self.userDao.addUserCard(owner_id_, card, user_no=user_no, table_name=self.scene.replace("card", "user"))
            elif owner_type == "Merchant":
                self.updateAcctOfStore(owner_id_, C4)
                self.updateS2OfStore(owner_id_, card.C11)

    def updateS2OfStore(self, owner_id_, C11):
        self.storeDao.updateS2OfStore(owner_id_, C11, self.scene.replace("card", "store"))


    def updateAcctOfStore(self, owner_id_, C4):
        self.storeDao.updateAcctOfStore(owner_id_, C4, self.scene.replace("card", "store"))

    def selectNormalCard(self):
        select_res = self.cardDao.selectNormalCard(self.scene)
        cardList = []
        for item in select_res:
            card_id, owner_type, owner_id, C4, C5, C6, C7, C8,C9,C10,C11, abnormal, abnormal_state = item

            if abnormal == 0:
                card = Card(card_id=card_id, owner_type=owner_type, owner_id=owner_id, C4=C4,
                            C5=C5, C6=C6, C7=C7, C8=C8,C9 = C9, C10 = C10,C11 = C11,
                            abnormal=abnormal, abnormal_state=abnormal_state)
                cardList.append(card)
        return cardList

    def selectFraudCard(self,fraud_category=None):
        select_res = self.cardDao.selectFraudCard(fraud_category, self.scene)
        cardList = []
        for item in select_res:
            card_id, owner_type, owner_id, C4, C5, C6, C7, C8, C9,C10,C11,abnormal, abnormal_state = item
            state = json.loads(abnormal_state)

            if fraud_category is None:
                if abnormal:
                    card = Card(card_id=card_id, owner_type=owner_type, owner_id=owner_id, C4=C4,
                                C5=C5, C6=C6, C7=C7, C8=C8,C9 = C9, C10 = C10, C11 = C11,
                                abnormal=abnormal, abnormal_state=abnormal_state)
                    cardList.append(card)
            else:
                if state[fraud_category] == 1:
                    card = Card(card_id=card_id, owner_type=owner_type, owner_id=owner_id, C4=C4,
                                C5=C5, C6=C6, C7=C7, C8=C8,C9 = C9, C10 = C10, C11 = C11,
                                abnormal=abnormal, abnormal_state=abnormal_state)
                    cardList.append(card)

        return cardList


    def createCardsFromHuman(self, human, contain_id=1):
        per_person_card_list = []
        card_num = CardService.from_human_to_card_num(human['wage'])
        credit_card_num = CardService.getCreditCardNum(card_num)

        for i in range(0, credit_card_num):
            card_id = CardService.total_card_num
            CardService.total_card_num += 1

            owner_type = "Regular_user"
            owner_id = human['id']

            C4 = ''.join(random.sample('zyxwvu0123456789tsrqponmlkjihgfedcba', 13))

            C5 = "02"
            C6 = CardService.getC6()
            C7 = CardService.getC7(human['job'])
            C8 = CardService.getC8(human['wage'])
            C9 = human['loc_id']
            C10 = CardService.getC10()
            C11 = C9+C10

            if contain_id:
                card = Card(card_id, owner_type, owner_id, C4, C5, C6, C7, C8,C9,C10,C11)
            else:
                card = Card(owner_type=owner_type, owner_id=owner_id, C4=C4, C5=C5,
                            C6=C6, C7=C7, C8=C8,C9 = C9, C10 = C10,C11 = C11)
            per_person_card_list.append(card)

        for i in range(credit_card_num, card_num):
            card_id = CardService.total_card_num
            CardService.total_card_num += 1

            owner_type = "Regular_user"
            owner_id = human['id']

            C4 = ''.join(random.sample('zyxwvu0123456789tsrqponmlkjihgfedcba', 13))

            C5 = "01"
            C6 = CardService.getC6()
            C7 = "--"
            C8 = "--"
            C9 = human['loc_id']
            # print(human)
            C10 = CardService.getC10()
            C11 = C9 + C10

            if contain_id:
                card = Card(card_id, owner_type, owner_id, C4, C5, C6, C7, C8,C9, C10,C11 )
            else:
                card = Card(owner_type=owner_type, owner_id=owner_id, C4=C4, C5=C5,
                            C6=C6, C7=C7, C8=C8, C9 = C9, C10 = C10, C11 = C11)
            per_person_card_list.append(card)

        return per_person_card_list

    def createCardsFromStore(self,store):
        per_store_card_list = []
        for i in range(0, 1):
            card_id = CardService.total_card_num
            CardService.total_card_num += 1

            owner_type = "Merchant"
            owner_id = store['id']

            C4 = ''.join(random.sample('zyxwvu0123456789tsrqponmlkjihgfedcba', 13))

            C5 = "01"
            C6 = CardService.getC6()
            C7 = "--"
            C8 = "--"
            C9 = CardService.getC9()
            C10 = CardService.getC10()
            C11 = C9 + C10

            card = Card(card_id, owner_type, owner_id, C4, C5, C6, C7, C8,C9,C10,C11)
            per_store_card_list.append(card)

        return per_store_card_list

    @staticmethod
    def from_human_to_card_num(wage):
        wage_card_num_dict = {"0-50000": [1, 2, 3, 4], "50000-100000": [3, 4, 5, 6, 7],
                              "100000-150000": [4, 5, 6, 7, 8], "150000-200000": [5, 6, 7, 8, 9],
                              "200000-250000": [6, 7, 8, 9, 10], "250000-300000": [7, 8, 9, 10, 11],
                              "300000-350000": [8, 9, 10, 11, 12], ">350000": [9, 10, 11, 12, 13, 14]}
        for key, value in wage_card_num_dict.items():
            if key != ">350000":
                st = int(key.strip("\"").split("-")[0])
                ed = int(key.strip("\"").split("-")[1])
                if wage >= st and wage <= ed:
                    return random.choice(value)
        return random.choice([9, 10, 11, 12, 13, 14])

    @staticmethod
    def getCreditCardNum(card_num):
        all_credict_nums = 5
        pro = 0
        card_credit_dict = {"0-2": 0, "2-5": 0.2, "5-8": 0.2, "8-11": 0.3, "11-14": 0.3, "14-15": 0.3}
        for key, value in card_credit_dict.items():
            st = int(key.strip("\"").split("-")[0])
            ed = int(key.strip("\"").split("-")[1])
            if card_num >= st and card_num < ed:
                pro = value
                break
        if card_num < 5:
            credit_card_nums = np.random.binomial(card_num, pro, 1)
        else:
            credit_card_nums = np.random.binomial(all_credict_nums, pro, 1)
        if card_num == credit_card_nums[0]:
            credit_card_nums -=1
        return credit_card_nums[0]

    @staticmethod
    def getC6():
        C6_list = ["00", "01", "02", "03", "04", "05", "06"]
        prob_distr = [0.02, 0.8, 0.04, 0.04, 0.04, 0.03, 0.03]
        pro_list = [0 for i in range(len(prob_distr))]
        for i in range(len(prob_distr)):
            if i == 0:
                pro_list[i] = prob_distr[i]
            else:
                pro_list[i] = pro_list[i - 1] + prob_distr[i]
        r = random.random()
        for i in range(len(pro_list)):
            if r < pro_list[i]:
                return C6_list[i]

    @staticmethod
    def getC7(job):
        C7 = ""
        pro = random.uniform(0, 1)
        if job == "Agriculture,Forestry,Animal_husbandry,Fishery":
            C7 = "Card_B"
        elif job in ["Mining_industry", "Manufacturing_industry", "Electricity,Heat,Gas,Water_production_and_supply_industry", "Construction_industry", "Wholesale_and_retail_industry", "Transportation,Warehousing,Postal_industry", "Accommodation_and_catering", "Information_transmission,Software,Information_technology_services_industry", "Financial_industry",
                     "Real_estate_industry", "Rental_and_business_services_industry", "Residential_services,Repair,Other_service_industries", "Culture,Sports,Entertainment_industry"]:
            if 0.3 < pro:
                C7 = "Card_C"
            elif 0.15 < pro:
                C7 = "Card_D"
            else:
                C7 = "Card_E"

        elif job in ["Education", "Public_administration,Social_security,Social_organizations", "Health_and_social_work", "Scientific_research_and_technical_services_industry", "Water_conservancy,Environment,Public_facilities_management_industry"]:
            if pro > 0.2:
                C7 = "Card_A"
            else:
                C7 = "Card_E"
        return C7

    @staticmethod
    def getC8(wage):
        wage_C8_dict = {"0-100000": {"01": "0-1"},
                          "100000-200000": {"01": "0-0.3", "02": "0.3-1"},
                          "200000-1000000": {"01": "0-0.2", "02": "0.2-0.5", "03": "0.5-1"},
                          "> 1000000": {"01": "0-0.1", "02": "0.1-0.3", "03": "0.3-0.5", "04": "0.5-1"}}
        pro = random.uniform(0, 1)
        for key, value in wage_C8_dict.items():
            if key != "> 1000000":
                wg_st = int(key.strip("\"").split("-")[0])
                wg_ed = int(key.strip("\"").split("-")[1])
                if wage >= wg_st and wage <= wg_ed:
                    for C8, prob in value.items():
                        st = float(prob.strip("\"").split("-")[0])
                        ed = float(prob.strip("\"").split("-")[1])
                        if pro >= st and pro < ed:
                            return C8.strip("\"")
            else:
                for C8, prob in value.items():
                    st = float(prob.strip("\"").split("-")[0])
                    ed = float(prob.strip("\"").split("-")[1])
                    # print("st,ed", st, ed)
                    if pro >= st and pro < ed:
                        return C8.strip("\"")


    @staticmethod
    def getC9():
        C9 = random.choice(["0001","0002","0003"])
        return C9

    @staticmethod
    def getC10():
        C10 = random.choice(["0000","0001","0002","0003"])
        return C10

    def getCardInfoByC4(self, C4):
        select_res = self.cardDao.selectCardInfoByC4(C4, self.scene)

        card_id, owner_type, owner_id, C4, C5, C6, C7, C8,C9,C10,C11, abnormal, abnormal_state = select_res

        card = Card(card_id, owner_type, owner_id, C4, C5, C6, C7, C8,C9,C10,C11, abnormal,
                    abnormal_state)
        return card


    def updateCardState(self, C4, abnormal_state):
        self.cardDao.updateCardState(C4, abnormal_state, self.scene)

    def getCardByOwnerId(self, ownerId):
        select_res =  self.cardDao.selectCardByOwnerId(ownerId, self.scene)
        cardList = []
        for item in select_res:
            card = Card(item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[8],item[9],item[10],item[11],item[12])
            cardList.append(card)
        return cardList

    def getTransferCardByOwnerId(self, ownerId):
        select_res = self.cardDao.selectTransferCardByOwnerId(ownerId, self.scene)
        cardList = []
        for item in select_res:
            card = Card(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9],
                        item[10], item[11], item[12])
            cardList.append(card)
        return cardList

