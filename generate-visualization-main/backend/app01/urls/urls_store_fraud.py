from django.urls import re_path as url
from app01.views.views_store_fraud import BasicDatas_views, trans_view1, trans_view2, duration, other_views

urlpatterns = [
    url('store_fraud/download/', other_views.download),
    url('store_fraud/RecreateTable/', other_views.RecreateTable),
    url('store_fraud/userInit/', BasicDatas_views.userInit),
    url('store_fraud/storeInit/', BasicDatas_views.storeInit),
    url('store_fraud/cardInit/', BasicDatas_views.cardInit),
    url('store_fraud/user/', BasicDatas_views.user),
    url('store_fraud/store/', BasicDatas_views.store),
    url('store_fraud/card/', BasicDatas_views.card),
    url('store_fraud/durationChoose/', duration.durationChoose),
    url('store_fraud/durationSet/', duration.durationSet),
    url('store_fraud/consumptionInit/', trans_view1.consumptionInit),
    url('store_fraud/transferInit/', trans_view1.transferInit),
    url('store_fraud/consumption/', trans_view1.consumption),
    url('store_fraud/transfer/', trans_view1.transfer),
    url('store_fraud/storeFraudInit/', trans_view2.storeFraudInit),
    url('store_fraud/storeFraud/', trans_view2.storeFraud),
]
