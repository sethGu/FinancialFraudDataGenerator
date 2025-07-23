import copy
import random
import numpy as np
import sys
import json
# from src.utils.config import get_mysql_connection
from src.dataGen20220414.service.CardService import CardService
from src.dataGen20220414.service.StoreService import StoreService
from src.dataGen20220414.service.UserService import UserService
from src.utils.config import get_mysql_connection
from src.dataGen20220414.entity.Card import Card
from src.dataGen20220414.factory.StoreFactory import StoreFactory
from src.dataGen20220414.factory.UserFactory import UserFactory


class CardFactory:

    def __init__(self, scene):
        self.userService = UserService(scene)
        self.storeService = StoreService(scene)
        self.cardService = CardService(scene)

    def createCardTable(self):
        self.cardService.createCardTable()

    def createCards(self):
        cardList = []
        human_list = self.userService.selectUsers()
        for human in human_list:
            # print("human", human.get_user_info())
            cards_list_per_person = self.cardService.createCardsFromHuman(human.get_user_info())  # 生成一个人拥有的多张卡各自的值
            cardList.extend(cards_list_per_person)
        store_list = self.storeService.selectStores()
        pre_card_list_per_store = []
        pre_name = ''
        for store in store_list:
            name = store.getName().replace("(低)", "")
            name = name.replace("(中)", "")
            name = name.replace("(高)", "")
            if name == pre_name:
                self.cardService.updateAcctOfStore(store.getStore_id(), pre_card_list_per_store[0].getC4())
            else:
                card_list_per_store = self.cardService.createCardsFromStore(store.get_store_info())
                pre_card_list_per_store = copy.deepcopy(card_list_per_store)
                cardList.extend(card_list_per_store)
            pre_name = name

        # CardFactory.createCardTable()
        self.cardService.insertCards(cardList)


if __name__ == '__main__':
    #创建用户表
    userFactory = UserFactory()
    userFactory.createUserTable()
    # 创建用户
    userFactory.createUsers(30)

    # 创建商户表
    storeFactory = StoreFactory()
    storeFactory.createStoreTable()
    # 创建商户
    storeFactory.createStores(10)

    #创建银行卡表
    cardFactory = CardFactory()
    cardFactory.createCardTable()
    # 创建银行卡
    cardFactory.createCards()

