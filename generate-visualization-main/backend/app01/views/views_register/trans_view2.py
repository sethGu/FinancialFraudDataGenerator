from __future__ import unicode_literals
import json
from django.core import serializers
from django.db.models import Q
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from app01.models import RegisterTrans, RegisterFT
from collections import defaultdict
import sys
import os
sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from smart_finance_main import api_DataGeneration


# Fake_registration
@require_http_methods(["POST"])
def registerFraud(request):
    postBody = request.body
    # postBody = b"{'ymd':'20220201', 'number_of_victims':3}"
    p = postBody.decode()
    p = eval(p)
    date = p['date']
    number_of_victims = p['number_of_victims']

    print("Start generating fake registration")
    api_DataGeneration.api_registerFraud(date, number_of_victims)
    print("End generating fake registration")
    return registerFraudDisplay()


@require_http_methods(["GET"])
def registerFraudInit(request):
    return registerFraudDisplay()


def registerFraudDisplay():
    normal_num = RegisterTrans.objects.filter(abnormal=0).count()
    registerFraud_num = RegisterFT.objects.filter(f23='84').count()

    transfer_lists = RegisterFT.objects.filter().values('f10', 'f14', 'f13').order_by('f14', 'f13')
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

    registerFraud_datas = [
        {
            'name': "Normal transaction",
            'value': normal_num
        },
        {
            'name': "Fake registration transaction",
            'value': registerFraud_num
        }
    ]

    return JsonResponse(
        {
            "code": 200,
            "data": {
                "data_1": registerFraud_datas,
                "data_2": {
                    "trans_amount": trans_amount,
                    "trans_time": trans_time
                }
            }
        },
        json_dumps_params={'ensure_ascii': False}
    )
