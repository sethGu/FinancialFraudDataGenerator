from __future__ import unicode_literals
import json
from django.core import serializers
from django.db.models import Q
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from app01.models import StoreTrans, StoreFT
from collections import defaultdict
import sys
import os
sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from smart_finance_main import api_DataGeneration


# 商户违规
@require_http_methods(["POST"])
def storeFraud(request):

    postBody = request.body
    p = postBody.decode()
    p = eval(p)
    ymd = p['ymd']
    number_of_stores = p['number_of_stores']

    print("生成商户违规开始")
    api_DataGeneration.api_storeFraud(ymd, number_of_stores)
    # api_DataGeneration.api_storeFraud()
    print("生成商户违规结束")
    return storeFraudDisplay()


@require_http_methods(["GET"])
def storeFraudInit(request):
    return storeFraudDisplay()


def storeFraudDisplay():
    normal_num = StoreTrans.objects.filter(abnormal=0).count()
    storeFraud_num = StoreFT.objects.filter(f23='86').count()

    transfer_lists = StoreFT.objects.filter().values('f10', 'f14', 'f13').order_by('f14', 'f13')
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

    storeFraud_datas = [
        {
            'name': "正常交易",
            'value': normal_num
        },
        {
            'name': "商户违规交易",
            'value': storeFraud_num
        }
    ]

    return JsonResponse(
        {
            "code": 200,
            "data": {
                "data_1": storeFraud_datas,
                "data_2": {
                    "trans_amount": trans_amount,
                    "trans_time": trans_time
                }
            }
        },
        json_dumps_params={'ensure_ascii': False}
    )
