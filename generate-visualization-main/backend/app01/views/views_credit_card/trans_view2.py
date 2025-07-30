from __future__ import unicode_literals
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from app01.models import CreditTrans, CreditFT
from collections import defaultdict
import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from smart_finance_main import api_DataGeneration


# Credit_card_fraud
@require_http_methods(["POST"])
def CreditCardCashOut(request):
    postBody = request.body
    p = postBody.decode()
    p = eval(p)

    personal_cash_out_ratio = p['personal_cash_out_ratio']
    personal_store_ratio = p['personal_store_ratio']
    store_group_size_min = p['store_group_size_min']
    store_group_size_max = p['store_group_size_max']
    is_in_opening_time = p['is_in_opening_time']

    small_fraud_gap = p['small_fraud_gap']
    big_fraud_gap = p['big_fraud_gap']
    start_year = int(p['date'][:4])
    start_month = int(p['date'][4:6])
    start_day = int(p['date'][-2:])
    user_quantity = p['user_quantity']
    store_quantity = p['store_quantity']
    duration = p['duration']
    print("Start generating credit card fraud")
    api_DataGeneration.api_CreditCardCashOut(personal_cash_out_ratio, personal_store_ratio,
                                             store_group_size_min,
                                             store_group_size_max, is_in_opening_time, small_fraud_gap, big_fraud_gap,
                                             start_year, start_month, start_day,
                                             user_quantity, store_quantity, duration)
    # api_DataGeneration.api_CreditCardCashOut()
    print("End generating credit card fraud")
    return CreditCardCashOutDisplay()


@require_http_methods(["GET"])
def CreditCardCashOutInit(request):
    return CreditCardCashOutDisplay()


def CreditCardCashOutDisplay():
    normal_num = CreditTrans.objects.filter(abnormal=0).count()
    CreditCardCashOut_num = CreditFT.objects.filter(f23='82').count()

    transfer_lists = CreditFT.objects.filter().values('f10', 'f14', 'f13').order_by('f14', 'f13')
    for foo in transfer_lists:
        hour = foo["f13"][:2]
        minutes = foo["f13"][2:4]
        seconds = foo["f13"][-2:]
        foo["time"] = foo["f14"] + "-" + hour + ":" + minutes + ":" + seconds
        # print(transfer_lists)
    trans_amount = []
    trans_time = []
    for i in transfer_lists:
        trans_amount.append(i["f10"])
        trans_time.append(i["time"])

    CreditCardCashOut_datas = [
        {
            'name': "Normal transaction",
            'value': normal_num
        },
        {
            'name': "Credit card fraud transaction",
            'value': CreditCardCashOut_num
        }
    ]
    # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    # print(trans_amount[0],trans_time[0])
    # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=")
    return JsonResponse(
        {
            "code": 200,
            "data": {
                "data_1": CreditCardCashOut_datas,
                "data_2": {
                    "trans_amount": trans_amount,
                    "trans_time": trans_time
                }
            }
        },
        json_dumps_params={'ensure_ascii': False}
    )
