from django.urls import re_path as url
from app01.views.views_register import BasicDatas_views, trans_view1, trans_view2, other_views, duration

urlpatterns = [
    # 数据下载
    url('register/download/', other_views.download),
    # 数据删除
    url('register/RecreateTable/', other_views.RecreateTable),
    # 基础数据初始化
    url('register/userInit/', BasicDatas_views.userInit),  # 用户生成
    url('register/storeInit/', BasicDatas_views.storeInit),  # 商户生成
    url('register/cardInit/', BasicDatas_views.cardInit),  # 银行卡生成
    # 基础数据生成
    url('register/user/', BasicDatas_views.user),  # 用户生成
    url('register/store/', BasicDatas_views.store),  # 商户生成
    url('register/card/', BasicDatas_views.card),  # 银行卡生成
    url('register/durationChoose/', duration.durationChoose),  # 日期选择
    url('register/durationSet/', duration.durationSet),
    # 正常交易初始化
    url('register/consumptionInit/', trans_view1.consumptionInit),  # 消费生成
    url('register/transferInit/', trans_view1.transferInit),  # 转账生成
    # 正常交易生成
    url('register/consumption/', trans_view1.consumption),  # 消费生成
    url('register/transfer/', trans_view1.transfer),  # 转账生成
    # 异常交易初始化
    url('register/registerFraudInit/', trans_view2.registerFraudInit),  # 伪冒注册欺诈
    # 异常交易生成
    url('register/registerFraud/', trans_view2.registerFraud),  # 伪冒注册欺诈

]
