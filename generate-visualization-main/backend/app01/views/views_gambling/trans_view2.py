from __future__ import unicode_literals
import json
from django.core import serializers
from django.db.models import Q
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from app01.models import GamblingTrans, GamblingFT
from collections import defaultdict
import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from smart_finance_main import api_DataGeneration


# Gambling_violation
@require_http_methods(["POST"])
def GamblingTrans_2(request):
    postBody = request.body
    # postBody = b"{'date':'20220201', 'duration':10, 'store_quantity':15, 'user_quantity':30}"
    p = postBody.decode()
    p = eval(p)

    is_in_opening_time = p['is_in_opening_time']
    personal_trans_time_ratio = p['personal_trans_time_ratio']
    low_rank_store_ratio = p['low_rank_store_ratio']
    middle_rank_store_ratio = p['middle_rank_store_ratio']
    high_rank_store_ratio = p['high_rank_store_ratio']
    gambling_user_ratio = p['gambling_user_ratio']

    year = int(p['date'][:4])
    month = int(p['date'][4:6])
    day = int(p['date'][-2:])
    duration = p['duration']
    store_quantity = p['store_quantity']
    user_quantity = p['user_quantity']

    print("Start generating gambling")

    api_DataGeneration.api_GamblingTrans(is_in_opening_time, personal_trans_time_ratio, low_rank_store_ratio,
                                         middle_rank_store_ratio, high_rank_store_ratio,
                                         gambling_user_ratio, year, month, day, duration, store_quantity, user_quantity)

    # api_DataGeneration.api_GamblingTrans()
    print("End generating gambling")

    return GamblingTransDisplay()


@require_http_methods(["GET"])
def GamblingTransInit(request):
    return GamblingTransDisplay()


def GamblingTransDisplay():
    normal_num = GamblingTrans.objects.filter(abnormal=0).count()
    GamblingTrans_num = GamblingFT.objects.filter(f23='85').count()

    transfer_lists = GamblingFT.objects.filter().values('f10', 'f14', 'f13').order_by('f14', 'f13')
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
    # print(trans_amount[0], trans_time[0])
    # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=")

    GamblingTrans_datas = [
        {
            'name': "Normal transaction",
            'value': normal_num
        },
        {
            'name': "Gambling transaction",
            'value': GamblingTrans_num
        }
    ]

    return JsonResponse(
        {
            "code": 200,
            "data": {
                "data_1": GamblingTrans_datas,
                "data_2": {
                    "trans_amount": trans_amount,
                    "trans_time": trans_time
                }
            }
        },
        json_dumps_params={'ensure_ascii': False}
    )
