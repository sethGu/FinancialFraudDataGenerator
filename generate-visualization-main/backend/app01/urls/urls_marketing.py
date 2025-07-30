from django.urls import re_path as url
from app01.views.views_marketing import BasicDatas_views, trans_view1, trans_view2, duration, other_views


urlpatterns = [
    url('marketing/download/', other_views.download),
    url('marketing/RecreateTable/', other_views.RecreateTable),
    url('marketing/userInit/', BasicDatas_views.userInit),
    url('marketing/storeInit/', BasicDatas_views.storeInit),
    url('marketing/cardInit/', BasicDatas_views.cardInit),
    url('marketing/user/', BasicDatas_views.user),
    url('marketing/store/', BasicDatas_views.store),
    url('marketing/card/', BasicDatas_views.card),
    url('marketing/durationChoose/', duration.durationChoose),
    url('marketing/durationSet/', duration.durationSet),
    url('marketing/consumptionInit/', trans_view1.consumptionInit),
    url('marketing/transferInit/', trans_view1.transferInit),
    url('marketing/consumption/', trans_view1.consumption),
    url('marketing/transfer/', trans_view1.transfer),
    url('marketing/MarketingFraudInit/', trans_view2.MarketingFraudInit),
    url('marketing/MarketingFraud/', trans_view2.MarketingFraud),
]
