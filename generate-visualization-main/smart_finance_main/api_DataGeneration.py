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
from src.utils import enterprise_export_csv
from src.dataGen20220414.factory.EnterpriseFactory import EnterpriseFactory


# 创建用户表
def api_user_table(scene):
    userFactory = UserFactory(scene)
    userFactory.createUserTable()


# 生成用户数据
def api_user(scene, number_of_users=200):
    userFactory = UserFactory(scene)
    userFactory.createUsers(number_of_users)


# 创建商户表
def api_store_table(scene):
    storeFactory = StoreFactory(scene)
    storeFactory.createStoreTable()


# 生成商户数据
def api_store(scene, number_of_stores=50):
    # 创建商户表
    storeFactory = StoreFactory(scene)
    storeFactory.createStores(number_of_stores)


# 创建银行卡表
def api_card_table(scene):
    cardFactory = CardFactory(scene)
    cardFactory.createCardTable()


# 生成银行卡数据
def api_card(scene):
    cardFactory = CardFactory(scene)
    cardFactory.createCards()


# 创建交易表和关系表
def api_trans_table(scene):
    transFactory = TransFactory(scene)
    transFactory.createTransTable()
    transFactory.createFraudTransTable()
    relativeFactory = RelativeFactory(scene)
    relativeFactory.createRelativeTable()


# 创建正常消费
def api_consumption(scene, year=2022, month=2, day=1, duration=30):
    # 创建正常消费
    cf = ConsumptionFactory(scene)
    cf.generate_data(year, month, day, duration)


# 创建关系、生成正常转账数据
def api_relative(scene, year=2022, month=2, day=1, duration=30):
    relativeFactory = RelativeFactory(scene)
    # #创建关系
    # print("start create relation")
    relativeFactory.createRelative()
    # 关系写入数据库
    # print("start write into db")
    relativeFactory.insertRelative()
    # print("insert relative end")
    # 由关系生成亲戚转账数据并插入数据库
    tranferFactory = TransferFactory(scene)
    tranferFactory.generate_relative_transfer_data(year, month, day, duration)


# 欺诈场景
# 1 黄牛营销欺诈场景
def api_MarketingFraud(is_in_opening_time=1, cloth_ratio=0.45, life_service_ratio=0.45, fraud_user_quantity=2,
                       store_quantity=1, start_year=2022, start_month=2, start_day=1,
                       duration=20):
    # fraud_user_quantity 每天的羊毛用户数量  store_quantity 每天的受欺诈商户数量
    mff = MarketingFraudFactory(is_in_opening_time, cloth_ratio, life_service_ratio)
    mff.generate_data(fraud_user_quantity, store_quantity, start_year, start_month, start_day, duration)


# 2 伪冒注册
def api_registerFraud(ymd='20220201', number_of_victims=3):
    registerFraudFactory = RegisterFraudFactory()
    registerFraudFactory.create_abnormal_register_data(ymd, number_of_victims)


# 3 信用卡套现
def api_CreditCardCashOut(personal_cash_out_ratio=0.7, personal_store_ratio=0.8, store_group_size_min=4,
                          store_group_size_max=10, is_in_opening_time=0.7, small_fraud_gap=5, big_fraud_gap=20,
                          start_year=2022, start_month=2, start_day=1,
                          user_quantity=30, store_quantity=10, duration=30):
    cccof = CreditCardCashOutFactory(personal_cash_out_ratio, personal_store_ratio, store_group_size_min,
                                     store_group_size_max, is_in_opening_time)
    cccof.generate_date(small_fraud_gap, big_fraud_gap, start_year, start_month, start_day,
                        user_quantity, store_quantity, duration)


# 4 赌博
def api_GamblingTrans(is_in_opening_time=0.8, personal_trans_time_ratio=0.7, low_rank_store_ratio=0.3,
                      middle_rank_store_ratio=0.6, high_rank_store_ratio=0.1,
                      gambling_user_ratio=0.7, year=2022, month=2, day=11, duration=10, store_quantity=5 * 3,
                      user_quantity=10 * 3):
    # store_quantity需要大于一定值，否则会报错,第二个场景产生数据过少？
    gtf = GamblingTransFactory(is_in_opening_time, personal_trans_time_ratio, low_rank_store_ratio,
                               middle_rank_store_ratio, high_rank_store_ratio,
                               gambling_user_ratio)
    gtf.generate_date(year, month, day, duration, store_quantity, user_quantity)


# 5 商户违规
def api_storeFraud(ymd='20220201', number_of_stores=25):
    storeFraudFactory = StoreFraudFactory()
    storeFraudFactory.create_abnormal_register_data(ymd, number_of_stores)


# 6 异常转账
def api_AbnormalTrans(gang_num=2, start_date='20220201', duration=30):
    AbnormalTrans = AbnormalTransFactory()
    AbnormalTrans.generate_data(gang_num, start_date, duration)

# 数据导出
def api_export_to_csv(scene, path='/datas/'):
    # 输出文件保存地址
    export_to_csv.out_put(scene, path)

# 创建工商企业表
def api_enterprise_table():
    enterpriseFactory = EnterpriseFactory()
    enterpriseFactory.createEnterpriseTable()


# 生成工商企业数据
def api_enterprise(number_of_enterprises=20):
    enterpriseFactory = EnterpriseFactory()
    enterpriseFactory.createEnterprise(number_of_enterprises)


# 数据导出
def api_enterprise_export_csv(path):
    # 输出文件保存地址
    enterprise_export_csv.out_put(path)


if __name__ == '__main__':
    print("start")
    scene = '信用卡违规套现'
    api_user(scene,10)
    api_store(scene,10)
    api_card(scene)
    api_consumption(scene)
    api_relative(scene)
    api_CreditCardCashOut()



    # print("创建企业表")
    # api_enterprise_table()
    # print("生成企业数据")
    # api_enterprise(10)

    # api_enterprise_export_csv(path='./datas/工商企业/')

    # scenes = ["黄牛营销欺诈", "信用卡违规套现", "异常转账", "伪冒注册欺诈", "赌博违规交易",
    #           "商户违规"]
    # scenes = ["商户违规"]
    # for scene in scenes:
    #     print(scene)
    #
    #     # 创建用户表
    #     print("创建用户表")
    #     api_user_table(scene)
    #
    #     # 生成用户数据
    #     print("生成用户数据")
    #     api_user(scene)
    #
    #     # 创建商户表
    #     print("创建商户表")
    #     api_store_table(scene)
    #
    #     # 生成商户数据
    #     print("生成商户数据")
    #     api_store(scene)
    #
    #     # 创建银行卡表
    #     print("创建银行卡表")
    #     api_card_table(scene)
    #
    #     # 生成银行卡
    #     print("生成银行卡")
    #     api_card(scene)
    #
    #     # 创建交易表、关系表
    #     print("创建交易表、关系表")
    #     api_trans_table(scene)
    #
    #     # 创建正常消费
    #     print("创建正常消费")
    #     api_consumption(scene)
    #     #
    #     # 创建关系数据
    #     print("创建关系数据")
    #     api_relative(scene)

    # # 黄牛营销欺诈
    # print("黄牛营销欺诈")
    # api_MarketingFraud()
    #
    # # 伪冒注册
    # print("伪冒注册")
    # api_registerFraud()
    #
    # # 信用卡套现
    # print("信用卡套现")
    # api_CreditCardCashOut()

    # # 赌博
    # print("赌博")
    # api_GamblingTrans()

    # 商户违规
    # print("商户违规")
    # api_storeFraud()
    #
    # # 异常转账
    # print("异常转账")
    # api_AbnormalTrans()

    # # 数据导出
    # print("数据导出")
    # for scene in scenes:
    #     print(scene)
    #     path = os.path.dirname(os.path.abspath(__file__)) + '/datas/' + scene + '/'
    #     api_export_to_csv(scene, path)

    print("end")
