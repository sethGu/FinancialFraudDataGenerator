from __future__ import unicode_literals
import json
from django.core import serializers
from django.db.models import Q
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from app01.models import AbnormalTrans, AbnormalFT
from collections import defaultdict
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from smart_finance_main import api_DataGeneration


# 异常转账
@require_http_methods(["POST"])
def AbnormalTrans_2(request):
    postBody = request.body
    # postBody = b"{'gang_num':2, 'start_date':'20220201', 'duration':30}"
    p = postBody.decode()
    p = eval(p)
    gang_num = p['gang_num']
    start_date = p['start_date']
    duration = p['duration']

    print("生成异常转账开始")
    api_DataGeneration.api_AbnormalTrans(gang_num, start_date, duration)
    print("生成异常转账结束")
    return AbnormalTransDisplay()


@require_http_methods(["GET"])
def AbnormalTransInit(request):
    return AbnormalTransDisplay()


def AbnormalTransDisplay():
    normal_num = AbnormalTrans.objects.filter(abnormal=0).count()
    AbnormalTrans_num = AbnormalFT.objects.filter(f23='83').count()

    transfer_lists = AbnormalFT.objects.filter().values('f10', 'f14', 'f13').order_by('f14', 'f13')
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
    AbnormalTrans_datas = [
        {
            'name': "正常交易",
            'value': normal_num
        },
        {
            'name': "异常转账交易",
            'value': AbnormalTrans_num
        }
    ]

    return JsonResponse(
        {
            "code": 200,
            "data": {
                "data_1": AbnormalTrans_datas,
                "data_2": {
                    "trans_amount": trans_amount,
                    "trans_time": trans_time
                }
            }
        },
        json_dumps_params={'ensure_ascii': False}
    )
