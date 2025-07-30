from django.urls import re_path as url
from app01.views.views_register import BasicDatas_views, trans_view1, trans_view2, other_views, duration

urlpatterns = [
    url('register/download/', other_views.download),
    url('register/RecreateTable/', other_views.RecreateTable),
    url('register/userInit/', BasicDatas_views.userInit),
    url('register/storeInit/', BasicDatas_views.storeInit),
    url('register/cardInit/', BasicDatas_views.cardInit),
    url('register/user/', BasicDatas_views.user),
    url('register/store/', BasicDatas_views.store),
    url('register/card/', BasicDatas_views.card),
    url('register/durationChoose/', duration.durationChoose),
    url('register/durationSet/', duration.durationSet),
    url('register/consumptionInit/', trans_view1.consumptionInit),
    url('register/transferInit/', trans_view1.transferInit),
    url('register/consumption/', trans_view1.consumption),
    url('register/transfer/', trans_view1.transfer),
    url('register/registerFraudInit/', trans_view2.registerFraudInit),
    url('register/registerFraud/', trans_view2.registerFraud),
]
