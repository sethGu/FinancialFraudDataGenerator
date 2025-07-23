from django.urls import re_path as url
from app01.views.views_credit_card import BasicDatas_views, trans_view1, trans_view2, duration, other_views


urlpatterns = [
    # 数据下载
    url('credit_card/download/', other_views.download),
    # 数据删除
    url('credit_card/RecreateTable/', other_views.RecreateTable),
    # 基础数据初始化
    url('credit_card/userInit/', BasicDatas_views.userInit),  # 用户生成
    url('credit_card/storeInit/', BasicDatas_views.storeInit),  # 商户生成
    url('credit_card/cardInit/', BasicDatas_views.cardInit),  # 银行卡生成
    # 基础数据生成
    url('credit_card/user/', BasicDatas_views.user),  # 用户生成
    url('credit_card/store/', BasicDatas_views.store),  # 商户生成
    url('credit_card/card/', BasicDatas_views.card),  # 银行卡生成
    url('credit_card/durationChoose/', duration.durationChoose),  # 日期选择
    url('credit_card/durationSet/', duration.durationSet),
    # 正常交易初始化
    url('credit_card/consumptionInit/', trans_view1.consumptionInit),  # 消费生成
    url('credit_card/transferInit/', trans_view1.transferInit),  # 转账生成
    # 正常交易生成
    url('credit_card/consumption/', trans_view1.consumption),  # 消费生成
    url('credit_card/transfer/', trans_view1.transfer),  # 转账生成
    # 异常交易初始化
    url('credit_card/CreditCardCashOutInit/', trans_view2.CreditCardCashOutInit),  # 信用卡违规套现
    # 异常交易生成
    url('credit_card/CreditCardCashOut/', trans_view2.CreditCardCashOut),  # 信用卡违规套现

]
