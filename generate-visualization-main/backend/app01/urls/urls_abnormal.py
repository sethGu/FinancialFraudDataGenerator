from django.urls import re_path as url
from app01.views.views_abnormal import BasicDatas_views, trans_view1, trans_view2, other_views, duration

urlpatterns = [
    url('abnormal/download/', other_views.download),
    url('abnormal/RecreateTable/', other_views.RecreateTable),
    url('abnormal/userInit/', BasicDatas_views.userInit),
    url('abnormal/storeInit/', BasicDatas_views.storeInit),
    url('abnormal/cardInit/', BasicDatas_views.cardInit),
    url('abnormal/user/', BasicDatas_views.user),
    url('abnormal/store/', BasicDatas_views.store),
    url('abnormal/card/', BasicDatas_views.card),
    url('abnormal/durationChoose/', duration.durationChoose),
    url('abnormal/durationSet/', duration.durationSet),
    url('abnormal/consumptionInit/', trans_view1.consumptionInit),
    url('abnormal/transferInit/', trans_view1.transferInit),
    url('abnormal/consumption/', trans_view1.consumption),
    url('abnormal/transfer/', trans_view1.transfer),
    url('abnormal/AbnormalTransInit/', trans_view2.AbnormalTransInit),
    url('abnormal/AbnormalTrans/', trans_view2.AbnormalTrans_2),
]
