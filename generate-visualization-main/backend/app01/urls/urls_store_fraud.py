from django.urls import re_path as url
from app01.views.views_store_fraud import BasicDatas_views, trans_view1, trans_view2, duration, other_views

urlpatterns = [
    # 数据下载
    url('store_fraud/download/', other_views.download),
    # 数据删除
    url('store_fraud/RecreateTable/', other_views.RecreateTable),
    # 基础数据初始化
    url('store_fraud/userInit/', BasicDatas_views.userInit),  # 用户生成
    url('store_fraud/storeInit/', BasicDatas_views.storeInit),  # 商户生成
    url('store_fraud/cardInit/', BasicDatas_views.cardInit),  # 银行卡生成
    # 基础数据生成
    url('store_fraud/user/', BasicDatas_views.user),  # 用户生成
    url('store_fraud/store/', BasicDatas_views.store),  # 商户生成
    url('store_fraud/card/', BasicDatas_views.card),  # 银行卡生成
    url('store_fraud/durationChoose/', duration.durationChoose),  # 日期选择
    url('store_fraud/durationSet/', duration.durationSet),
    # 正常交易初始化
    url('store_fraud/consumptionInit/', trans_view1.consumptionInit),  # 消费生成
    url('store_fraud/transferInit/', trans_view1.transferInit),  # 转账生成
    # 正常交易生成
    url('store_fraud/consumption/', trans_view1.consumption),  # 消费生成
    url('store_fraud/transfer/', trans_view1.transfer),  # 转账生成
    # 异常交易初始化
    url('store_fraud/storeFraudInit/', trans_view2.storeFraudInit),  # 商户违规
    # 异常交易生成
    url('store_fraud/storeFraud/', trans_view2.storeFraud),  # 商户违规

]
