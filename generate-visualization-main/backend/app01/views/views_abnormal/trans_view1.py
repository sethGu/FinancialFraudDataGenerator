from __future__ import unicode_literals
import datetime
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from app01.models import AbnormalTrans

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from smart_finance_main import api_DataGeneration


@require_http_methods(["POST"])
def consumption(request):
    postBody = request.body
    # postBody = b"{'date':'20220201','duration':10}"
    p = postBody.decode()
    # print(p)
    p = eval(p)
    year = int(p['date'][:4])
    month = int(p['date'][4:6])
    day = int(p['date'][-2:])
    duration = p['duration']
    print("Start generating normal consumption")
    api_DataGeneration.api_consumption("Abnormal_transfer", year, month, day, duration)
    print("End generating normal consumption")
    return consumptionDisplay()


@require_http_methods(["GET"])
def consumptionInit(request):
    return consumptionDisplay()


def consumptionDisplay():
    consumption_num = AbnormalTrans.objects.filter(abnormal=0, t2='01').count()
    consumption_lists = AbnormalTrans.objects.filter(abnormal=0, t2='01').values('t17', 't2', 't23', 't19').order_by('t23', 't19')
    # print(consumption_num)
    # print(consumption_lists)
    for foo in consumption_lists:
        hour = foo["t19"][:2]
        minutes = foo["t19"][2:4]
        seconds = foo["t19"][-2:]
        foo["time"] = foo["t23"] + "-" + hour + ":" + minutes + ":" + seconds
        # print(consumption_lists)
    trans_amount = []
    trans_time = []
    for i in consumption_lists:
        trans_amount.append(i["t17"])
        trans_time.append(i["time"])

    return JsonResponse(
        {
            "code": 200,
            "data": {
                "trans_amount": trans_amount,
                "trans_time" : trans_time
            }
        },
        json_dumps_params={'ensure_ascii': False}
    )


@require_http_methods(["POST"])
def transfer(request):
    postBody = request.body
    # postBody = b"{'date':'20220201','duration':30}"
    p = postBody.decode()
    # print(p)
    p = eval(p)
    year = int(p['date'][:4])
    month = int(p['date'][4:6])
    day = int(p['date'][-2:])
    duration = p['duration']  # duration >= 30
    print("Start generating normal transfer")
    api_DataGeneration.api_relative("Abnormal_transfer", year, month, day, duration)
    print("End generating normal transfer")
    return transferDisplay()


@require_http_methods(["GET"])
def transferInit(request):
    return transferDisplay()


def transferDisplay():
    transfer_num = AbnormalTrans.objects.filter(abnormal=0, t2='03').count()
    transfer_lists = AbnormalTrans.objects.filter(abnormal=0, t2='03').values('t17', 't2', 't23', 't19').order_by('t23', 't19')
    # print(transfer_num)
    # print(transfer_lists)
    for foo in transfer_lists:
        hour = foo["t19"][:2]
        minutes = foo["t19"][2:4]
        seconds = foo["t19"][-2:]
        foo["time"] = foo["t23"] + "-" + hour + ":" + minutes + ":" + seconds
        # print(transfer_lists)
    trans_amount = []
    trans_time = []
    for i in transfer_lists:
        trans_amount.append(i["t17"])
        trans_time.append(i["time"])

    return JsonResponse(
        {
            "code": 200,
            "data": {
                "trans_amount": trans_amount,
                "trans_time" : trans_time
            }
        },
        json_dumps_params={'ensure_ascii': False}
    )
