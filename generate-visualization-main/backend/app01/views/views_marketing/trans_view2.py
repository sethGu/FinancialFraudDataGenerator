from __future__ import unicode_literals
import json
from django.core import serializers
from django.db.models import Q
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from app01.models import MarketingTrans, MarketingFT
from collections import defaultdict
import sys
import os
sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from smart_finance_main import api_DataGeneration


# Scalper_marketing
@require_http_methods(["POST"])
def MarketingFraud(request):
    postBody = request.body
    # postBody = b"{'fraud_user_quantity':2, 'store_quantity':1, 'date':'20220201','duration':20}"
    p = postBody.decode()
    p = eval(p)

    is_in_opening_time = p['is_in_opening_time']
    cloth_ratio = p['cloth_ratio']
    life_service_ratio = p['life_service_ratio']

    fraud_user_quantity = p['fraud_user_quantity']
    store_quantity = p['store_quantity']
    start_year = int(p['date'][:4])
    start_month = int(p['date'][4:6])
    start_day = int(p['date'][-2:])
    duration = p['duration']
    # print(fraud_user_quantity, store_quantity, start_year, start_month, start_day, duration)

    print("Start generating scalper marketing fraud")
    api_DataGeneration.api_MarketingFraud(is_in_opening_time, cloth_ratio, life_service_ratio, fraud_user_quantity,
                                          store_quantity, start_year, start_month,
                                          start_day, duration)
    print("End generating scalper marketing fraud")
    return MarketingFraudDisplay()


@require_http_methods(["GET"])
def MarketingFraudInit(request):
    return MarketingFraudDisplay()


def MarketingFraudDisplay():
    normal_num = MarketingTrans.objects.filter(abnormal=0).count()
    MarketingFraud_num = MarketingFT.objects.filter(f23='81').count()

    transfer_lists = MarketingFT.objects.filter().values('f10', 'f14', 'f13').order_by('f14', 'f13')
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
    # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    # print(trans_amount[0],trans_time[0])
    # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=")

    MarketingFraud_datas = [
        {
            'name': "Normal transaction",
            'value': normal_num
        },
        {
            'name': "Scalper marketing fraud transaction",
            'value': MarketingFraud_num
        }
    ]

    return JsonResponse(
        {
            "code": 200,
            "data": {
                "data_1": MarketingFraud_datas,
                "data_2": {
                    "trans_amount": trans_amount,
                    "trans_time": trans_time
                }
            }
        },
        json_dumps_params={'ensure_ascii': False}
    )
