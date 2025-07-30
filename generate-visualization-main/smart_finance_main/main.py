import datetime
import random
import time


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



def run():
    sences = ["Scalper_marketing", "Credit_card_fraud", "Abnormal_transfer", "Fake_registration", "Gambling_violation",
                        "Merchant_violation"]
    # for s in sences:
    #     userFactory = UserFactory(s)
    #     userFactory.createUserTable()
        # userFactory.createUsers(20)

    # for s in sences:
    #     storeFactory = StoreFactory(s)
    #     storeFactory.createStoreTable()
        # storeFactory.createStores(10)

    # cardFactory = CardFactory("Credit_card_fraud")
    # cardFactory.createCardTable()
    # cardFactory.createCards()

    # for s in sences:
    #     transFactory = TransFactory(s)
    #     transFactory.createTransTable()
    #     transFactory.createFraudTransTable()
    #
    # cf = ConsumptionFactory()
    # cf.generate_data(2022, 2, 1, 30)

    # print("start create relation table")
    # for s in sences:
    #     relativeFactory = RelativeFactory(s)
    #     relativeFactory.createRelativeTable()
    # print("start create relation")
    #     relativeFactory.createRelative()
    # print("start write into db")
    # relativeFactory.insertRelative()
    # print("insert relative end")
    # tranferFactory = TransferFactory()
    # tranferFactory.generate_relative_transfer_data(2022, 2, 1, 30)



    # mff = MarketingFraudFactory()
    # mff.generate_data(fraud_user_quantity=2, store_quantity=1, start_year=2022, start_month=2, start_day=1, duration=20)
    #
    # registerFraudFactory = RegisterFraudFactory()
    # registerFraudFactory.create_abnormal_register_data('20220201', 30)

    # cccof = CreditCardCashOutFactory()
    # cccof.generate_date(small_fraud_gap=5, big_fraud_gap=50, start_year=2022, start_month=2, start_day=1,
    #                     user_quantity=6, store_quantity=10, duration=5)

    # gtf = GamblingTransFactory()
    # gtf.generate_date(year=2022, month=2, day=1, duration=30, store_quantity=5 * 3, user_quantity=10 * 3)
    # gtf.generate_date(year=2022, month=2, day=1, store_quantity=5 * 3, user_quantity=10 * 3) #store_quantity需要大于一定值，否则会报错,第二个场景产生数据过少？
    #
    # storeFraudFactory = StoreFraudFactory()
    # storeFraudFactory.create_abnormal_register_data('20220201', 25)
    # AbnormalTrans = AbnormalTransFactory()
    # AbnormalTrans.generate_data(gang_num=2, start_date='20220201', duration=30)

def xx():
    # sences = ["Scalper_marketing", "Credit_card_fraud", "Abnormal_transfer", "Fake_registration", "Gambling_violation",
    #                     "Merchant_violation"]
    # sences = [
    #           "Merchant_violation"]
    # for s in sences:
    #     userFactory = UserFactory(s)
    #     userFactory.createUserTable()
    #     userFactory.createUsers(20)
    #     storeFactory = StoreFactory(s)
    #     storeFactory.createStoreTable()
    #     storeFactory.createStores(10)
    #     cardFactory = CardFactory(s)
    #     cardFactory.createCardTable()
    #     cardFactory.createCards()
    #     transFactory = TransFactory(s)
    #     transFactory.createTransTable()
    #     transFactory.createFraudTransTable()
    #     cf = ConsumptionFactory(s)
    #     cf.generate_data(2022, 2, 1, 30)
    #     relativeFactory = RelativeFactory(s)
    #     relativeFactory.createRelativeTable()
    #     relativeFactory.createRelative()
    #     relativeFactory.insertRelative()
    #     tranferFactory = TransferFactory(s)
    #     tranferFactory.generate_relative_transfer_data(2022, 2, 1, 30)


    # mff = MarketingFraudFactory()
    # mff.generate_data(fraud_user_quantity=2, store_quantity=1, start_year=2022, start_month=2, start_day=1, duration=20)
    # registerFraudFactory = RegisterFraudFactory()
    # registerFraudFactory.create_abnormal_register_data('20220201', 30)
    # cccof = CreditCardCashOutFactory()
    # cccof.generate_date(small_fraud_gap=5, big_fraud_gap=50, start_year=2022, start_month=2, start_day=1,
    #                     user_quantity=6, store_quantity=10, duration=5)
    # gtf = GamblingTransFactory()
    # gtf.generate_date(year=2022, month=2, day=1, duration=30, store_quantity=5 * 3, user_quantity=5 * 3)

    # storeFraudFactory = StoreFraudFactory()
    # storeFraudFactory.create_abnormal_register_data('20220201', 25)
    s = "Abnormal_transfer"
    # userFactory = UserFactory(s)
    # userFactory.createUserTable()
    # userFactory.createUsers(200)
    # storeFactory = StoreFactory(s)
    # storeFactory.createStoreTable()
    # storeFactory.createStores(50)
    # cardFactory = CardFactory(s)
    # cardFactory.createCardTable()
    # cardFactory.createCards()
    # transFactory = TransFactory(s)
    # transFactory.createTransTable()
    # transFactory.createFraudTransTable()

    AbnormalTrans = AbnormalTransFactory()
    AbnormalTrans.generate_data(gang_num=2, start_date='20220201', duration=30)
if __name__ == '__main__':
    xx()

    # cccof = CreditCardCashOutFactory()
    # cccof.generate_date(small_fraud_gap=5, big_fraud_gap=40, start_year=2022, start_month=2, start_day=10,
    #                     user_quantity=4, store_quantity=5, duration=20)
    # storeFraudFactory = StoreFraudFactory()
    # storeFraudFactory.create_abnormal_register_data('20220501', 1000)
    # cf = ConsumptionFactory()
    # cf.generate_data(2022, 5, 1, 60)
    # transFactory = TransFactory()
    # transFactory.createFraudTransTable()
    # cf = ScalperFraudFactory()
    # cf.generate_data(fraud_gap=40, start_year=2022, start_month=2, start_day=1, duration=3, quantity=10)
    # cccof = CreditCardCashOutFactory()
    # cccof.generate_date(small_fraud_gap=5, big_fraud_gap=30, start_year=2022, start_month=2, start_day=1,
    #                     user_quantity=60, store_quantity=20)
    # registerFraudFactory = RegisterFraudFactory()
    # registerFraudFactory.create_abnormal_register_data('20220201', 30)

    # s = StoreService()
    # u = s.selectStoreByS1('930391665226114')
    # print(u)


#############
# S22 -01
# S24 -02
# S31 -03
