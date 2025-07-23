from django.urls import re_path as url
from app01.views.views_marketing import BasicDatas_views, trans_view1, trans_view2, duration, other_views


urlpatterns = [
    # 数据下载
    url('marketing/download/', other_views.download),
    # 数据删除
    url('marketing/RecreateTable/', other_views.RecreateTable),
    # 基础数据初始化
    url('marketing/userInit/', BasicDatas_views.userInit),  # 用户生成
    url('marketing/storeInit/', BasicDatas_views.storeInit),  # 商户生成
    url('marketing/cardInit/', BasicDatas_views.cardInit),  # 银行卡生成
    # 基础数据生成
    url('marketing/user/', BasicDatas_views.user),  # 用户生成
    url('marketing/store/', BasicDatas_views.store),  # 商户生成
    url('marketing/card/', BasicDatas_views.card),  # 银行卡生成
    url('marketing/durationChoose/', duration.durationChoose),  # 日期选择
    url('marketing/durationSet/', duration.durationSet),
    # 正常交易初始化
    url('marketing/consumptionInit/', trans_view1.consumptionInit),  # 消费生成
    url('marketing/transferInit/', trans_view1.transferInit),  # 转账生成
    # 正常交易生成
    url('marketing/consumption/', trans_view1.consumption),  # 消费生成
    url('marketing/transfer/', trans_view1.transfer),  # 转账生成
    # 异常交易初始化
    url('marketing/MarketingFraudInit/', trans_view2.MarketingFraudInit),  # 黄牛营销欺诈
    # 异常交易生成
    url('marketing/MarketingFraud/', trans_view2.MarketingFraud),  # 黄牛营销欺诈

]
