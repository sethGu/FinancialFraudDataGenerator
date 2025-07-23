from django.urls import re_path as url
from app01.views.views_gambling import BasicDatas_views, trans_view1, trans_view2, other_views, duration

urlpatterns = [
    # 数据下载
    url('gambling/download/', other_views.download),
    # 数据删除
    url('gambling/RecreateTable/', other_views.RecreateTable),
    # 基础数据初始化
    url('gambling/userInit/', BasicDatas_views.userInit),  # 用户生成
    url('gambling/storeInit/', BasicDatas_views.storeInit),  # 商户生成
    url('gambling/cardInit/', BasicDatas_views.cardInit),  # 银行卡生成
    # 基础数据生成
    url('gambling/user/', BasicDatas_views.user),  # 用户生成
    url('gambling/store/', BasicDatas_views.store),  # 商户生成
    url('gambling/card/', BasicDatas_views.card),  # 银行卡生成
    url('gambling/durationChoose/', duration.durationChoose),  # 日期选择
    url('gambling/durationSet/', duration.durationSet),
    # 正常交易初始化
    url('gambling/consumptionInit/', trans_view1.consumptionInit),  # 消费生成
    url('gambling/transferInit/', trans_view1.transferInit),  # 转账生成
    # 正常交易生成
    url('gambling/consumption/', trans_view1.consumption),  # 消费生成
    url('gambling/transfer/', trans_view1.transfer),  # 转账生成
    # 异常交易初始化
    url('gambling/GamblingTransInit/', trans_view2.GamblingTransInit),  # 赌博
    # 异常交易生成
    url('gambling/GamblingTrans/', trans_view2.GamblingTrans_2),  # 赌博

]
