from django.urls import re_path as url
from app01.views.views_gambling import BasicDatas_views, trans_view1, trans_view2, other_views, duration

urlpatterns = [
    url('gambling/download/', other_views.download),
    url('gambling/RecreateTable/', other_views.RecreateTable),
    url('gambling/userInit/', BasicDatas_views.userInit),
    url('gambling/storeInit/', BasicDatas_views.storeInit),
    url('gambling/cardInit/', BasicDatas_views.cardInit),
    url('gambling/user/', BasicDatas_views.user),
    url('gambling/store/', BasicDatas_views.store),
    url('gambling/card/', BasicDatas_views.card),
    url('gambling/durationChoose/', duration.durationChoose),
    url('gambling/durationSet/', duration.durationSet),
    url('gambling/consumptionInit/', trans_view1.consumptionInit),
    url('gambling/transferInit/', trans_view1.transferInit),
    url('gambling/consumption/', trans_view1.consumption),
    url('gambling/transfer/', trans_view1.transfer),
    url('gambling/GamblingTransInit/', trans_view2.GamblingTransInit),
    url('gambling/GamblingTrans/', trans_view2.GamblingTrans_2),
]
