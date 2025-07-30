from django.urls import re_path as url
from app01.views.views_credit_card import BasicDatas_views, trans_view1, trans_view2, duration, other_views


urlpatterns = [
    url('credit_card/download/', other_views.download),
    url('credit_card/RecreateTable/', other_views.RecreateTable),
    url('credit_card/userInit/', BasicDatas_views.userInit),
    url('credit_card/storeInit/', BasicDatas_views.storeInit),
    url('credit_card/cardInit/', BasicDatas_views.cardInit),
    url('credit_card/user/', BasicDatas_views.user),
    url('credit_card/store/', BasicDatas_views.store),
    url('credit_card/card/', BasicDatas_views.card),
    url('credit_card/durationChoose/', duration.durationChoose),
    url('credit_card/durationSet/', duration.durationSet),
    url('credit_card/consumptionInit/', trans_view1.consumptionInit),
    url('credit_card/transferInit/', trans_view1.transferInit),
    url('credit_card/consumption/', trans_view1.consumption),
    url('credit_card/transfer/', trans_view1.transfer),
    url('credit_card/CreditCardCashOutInit/', trans_view2.CreditCardCashOutInit),
    url('credit_card/CreditCardCashOut/', trans_view2.CreditCardCashOut),
]
