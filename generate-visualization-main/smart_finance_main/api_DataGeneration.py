# @Time    : 2022/10/16 11:15
# @Author  : SuperRich Liu

import datetime
import random
import time
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from src.dataGen20220414.dao.UserDao import UserDao
from src.dataGen20220414.factory.AbnormalTransFactory_my import AbnormalTransFactory
from src.dataGen20220414.factory.CardFactory import CardFactory
from src.dataGen20220414.factory.ConsumptionFactory import ConsumptionFactory
from src.dataGen20220414.factory.CreditCardCashOutFactory import CreditCardCashOutFactory
from src.dataGen20220414.factory.GamblingTransFactory import GamblingTransFactory
from src.dataGen20220414.factory.MarketingFraudFactory import MarketingFraudFactory
from src.dataGen20220414.factory.RegisterFraudFactory import RegisterFraudFactory
from src.dataGen20220414.factory.StoreFactory import StoreFactory
from src.dataGen20220414.factory.StoreFraudFactory import StoreFraudFactory
from src.dataGen20220414.factory.TransFactory import TransFactory
from src.dataGen20220414.factory.TransferFactory import TransferFactory
from src.dataGen20220414.factory.UserFactory import UserFactory
from src.dataGen20220414.factory.RelativeFactory import RelativeFactory
from src.dataGen20220414.service.CardService import CardService
from src.dataGen20220414.service.RelativeService import RelativeService
from src.dataGen20220414.service.StoreService import StoreService
from src.utils import export_to_csv


def api_user_table(scene):
    userFactory = UserFactory(scene)
    userFactory.createUserTable()


def api_user(scene, number_of_users=200):
    userFactory = UserFactory(scene)
    userFactory.createUsers(number_of_users)


def api_store_table(scene):
    storeFactory = StoreFactory(scene)
    storeFactory.createStoreTable()


def api_store(scene, number_of_stores=50):
    storeFactory = StoreFactory(scene)
    storeFactory.createStores(number_of_stores)


def api_card_table(scene):
    cardFactory = CardFactory(scene)
    cardFactory.createCardTable()


def api_card(scene):
    cardFactory = CardFactory(scene)
    cardFactory.createCards()


def api_trans_table(scene):
    transFactory = TransFactory(scene)
    transFactory.createTransTable()
    transFactory.createFraudTransTable()
    relativeFactory = RelativeFactory(scene)
    relativeFactory.createRelativeTable()


def api_consumption(scene, year=2022, month=2, day=1, duration=30):
    cf = ConsumptionFactory(scene)
    cf.generate_data(year, month, day, duration)


def api_relative(scene, year=2022, month=2, day=1, duration=30):
    relativeFactory = RelativeFactory(scene)
    # print("start create relation")
    relativeFactory.createRelative()
    # print("start write into db")
    relativeFactory.insertRelative()
    # print("insert relative end")
    tranferFactory = TransferFactory(scene)
    tranferFactory.generate_relative_transfer_data(year, month, day, duration)


def api_MarketingFraud(is_in_opening_time=1, cloth_ratio=0.45, life_service_ratio=0.45, fraud_user_quantity=2,
                       store_quantity=1, start_year=2022, start_month=2, start_day=1,
                       duration=20):
    mff = MarketingFraudFactory(is_in_opening_time, cloth_ratio, life_service_ratio)
    mff.generate_data(fraud_user_quantity, store_quantity, start_year, start_month, start_day, duration)


def api_registerFraud(ymd='20220201', number_of_victims=3):
    registerFraudFactory = RegisterFraudFactory()
    registerFraudFactory.create_abnormal_register_data(ymd, number_of_victims)


def api_CreditCardCashOut(personal_cash_out_ratio=0.7, personal_store_ratio=0.8, store_group_size_min=4,
                          store_group_size_max=10, is_in_opening_time=0.7, small_fraud_gap=5, big_fraud_gap=20,
                          start_year=2022, start_month=2, start_day=1,
                          user_quantity=30, store_quantity=10, duration=30):
    cccof = CreditCardCashOutFactory(personal_cash_out_ratio, personal_store_ratio, store_group_size_min,
                                     store_group_size_max, is_in_opening_time)
    cccof.generate_date(small_fraud_gap, big_fraud_gap, start_year, start_month, start_day,
                        user_quantity, store_quantity, duration)


def api_GamblingTrans(is_in_opening_time=0.8, personal_trans_time_ratio=0.7, low_rank_store_ratio=0.3,
                      middle_rank_store_ratio=0.6, high_rank_store_ratio=0.1,
                      gambling_user_ratio=0.7, year=2022, month=2, day=11, duration=10, store_quantity=5 * 3,
                      user_quantity=10 * 3):
    gtf = GamblingTransFactory(is_in_opening_time, personal_trans_time_ratio, low_rank_store_ratio,
                               middle_rank_store_ratio, high_rank_store_ratio,
                               gambling_user_ratio)
    gtf.generate_date(year, month, day, duration, store_quantity, user_quantity)


def api_storeFraud(ymd='20220201', number_of_stores=25):
    storeFraudFactory = StoreFraudFactory()
    storeFraudFactory.create_abnormal_register_data(ymd, number_of_stores)


def api_AbnormalTrans(gang_num=2, start_date='20220201', duration=30):
    AbnormalTrans = AbnormalTransFactory()
    AbnormalTrans.generate_data(gang_num, start_date, duration)

def api_export_to_csv(scene, path='/datas/'):
    export_to_csv.out_put(scene, path)




if __name__ == '__main__':
    print("start")
    scene = 'Credit_card_fraud'
    api_user(scene,10)
    api_store(scene,10)
    api_card(scene)
    api_consumption(scene)
    api_relative(scene)
    api_CreditCardCashOut()

    print("end")
