from django.urls import re_path as url
from app01.views.views_abnormal import BasicDatas_views, trans_view1, trans_view2, other_views, duration

urlpatterns = [
    # 数据下载
    url('abnormal/download/', other_views.download),
    # 数据删除
    url('abnormal/RecreateTable/', other_views.RecreateTable),
    # 基础数据初始化
    url('abnormal/userInit/', BasicDatas_views.userInit),  # 用户生成
    url('abnormal/storeInit/', BasicDatas_views.storeInit),  # 商户生成
    url('abnormal/cardInit/', BasicDatas_views.cardInit),  # 银行卡生成
    # 基础数据生成
    url('abnormal/user/', BasicDatas_views.user),  # 用户生成
    url('abnormal/store/', BasicDatas_views.store),  # 商户生成
    url('abnormal/card/', BasicDatas_views.card),  # 银行卡生成
    url('abnormal/durationChoose/', duration.durationChoose),  # 日期选择
    url('abnormal/durationSet/', duration.durationSet),
    # 正常交易初始化
    url('abnormal/consumptionInit/', trans_view1.consumptionInit),  # 消费生成
    url('abnormal/transferInit/', trans_view1.transferInit),  # 转账生成
    # 正常交易生成
    url('abnormal/consumption/', trans_view1.consumption),  # 消费生成
    url('abnormal/transfer/', trans_view1.transfer),  # 转账生成
    # 异常交易初始化
    url('abnormal/AbnormalTransInit/', trans_view2.AbnormalTransInit),  # 异常转账
    # 异常交易生成
    url('abnormal/AbnormalTrans/', trans_view2.AbnormalTrans_2),  # 异常转账

]
