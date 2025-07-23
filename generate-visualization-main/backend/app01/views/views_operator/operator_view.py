# -*- coding: utf-8 -*-
"""
  Author: LiangJing
   Time : 2023/5/18
    File: operator_view.py
"""

from __future__ import unicode_literals
import datetime
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse, StreamingHttpResponse, Http404
from django.db.models import Count

import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from OperatorDataGeneration import api_operateor_data_generation
from app01.models import Operator
from collections import defaultdict


@require_http_methods(["POST"])
def operatorGenerate(request):
    postBody = request.body
    print(postBody)
    p = postBody.decode()
    # print(p)
    p = eval(p)
    number_of_operators = p['number_of_operators']
    print("生成运营商开始")
    api_operateor_data_generation.api_data_genetation(number_of_operators)
    print("生成运营商结束")
    return operatorDisplay()


@require_http_methods(["GET"])
def operatorInit(request):
    return operatorDisplay()


@require_http_methods(["GET"])
def fetchList(request):
    operator_list = []
    operators = Operator.objects.all()
    i = 0
    for foo in operators:
        i += 1
        one_example = defaultdict(str)
        one_example.update(id=i, original_id=foo.original_id, contactor=foo.contactor, contactor_id=foo.contactor_id,
                           mobile_phone_brand=foo.mobile_phone_brand,
                           mobile_operating_system=foo.mobile_operating_system, pv=foo.pv,
                           terminal_type=foo.terminal_type,
                           video_website=foo.video_website, shopping_website=foo.shopping_website,
                           overseas_taobao_shopping_channel=foo.overseas_taobao_shopping_channel,
                           automotive_website=foo.automotive_website,
                           real_estate_website=foo.real_estate_website, travel_website=foo.travel_website,
                           highest_calling=foo.highest_calling, city_number=foo.city_number,
                           day_calling=foo.day_calling,
                           night_calling=foo.night_calling, three_month_calling=foo.three_month_calling
                           )
        operator_list.append(one_example)
    # 解析Query Params
    page = int(request.GET.get('page', 1))
    limit = int(request.GET.get('limit', 10))
    sort = request.GET.get('sort', '+id')
    if sort == '-id':
        operator_list = operator_list[::-1]
    # 获取pageList
    pageList = operator_list[(page - 1) * limit: page * limit]
    return JsonResponse(
        {
            "code": 200,
            "data": {
                "total": len(operator_list),
                "items": pageList
            }
        },
        json_dumps_params={'ensure_ascii': False}
    )


def operatorDisplay():
    operators = Operator.objects.all()
    operators_example_list = []
    i = 0
    for foo in operators:
        i += 1
        one_example = defaultdict(str)
        one_example.update(original_id=foo.original_id, contactor=foo.contactor, contactor_id=foo.contactor_id,
                           mobile_phone_brand=foo.mobile_phone_brand,
                           mobile_operating_system=foo.mobile_operating_system, pv=foo.pv,
                           terminal_type=foo.terminal_type,
                           video_website=foo.video_website, shopping_website=foo.shopping_website,
                           overseas_taobao_shopping_channel=foo.overseas_taobao_shopping_channel,
                           automotive_website=foo.automotive_website,
                           real_estate_website=foo.real_estate_website, travel_website=foo.travel_website,
                           highest_calling=foo.highest_calling,city_number=foo.city_number,day_calling=foo.day_calling,
                           night_calling=foo.night_calling,three_month_calling=foo.three_month_calling)
        operators_example_list.append(one_example)

    mobile_brand_count = defaultdict(int)
    video_website_count = defaultdict(int)
    shopping_website_count = defaultdict(int)
    overseas_taobao_count = defaultdict(int)
    automotive_website_count = defaultdict(int)
    real_estate_website_count = defaultdict(int)
    travel_website_count = defaultdict(int)

    for foo in operators:
        mobile_brand_count[foo.mobile_phone_brand] += 1
        video_website_count[foo.video_website] += 1
        shopping_website_count[foo.shopping_website] += 1
        overseas_taobao_count[foo.overseas_taobao_shopping_channel] += 1
        automotive_website_count[foo.automotive_website] += 1
        real_estate_website_count[foo.real_estate_website] += 1
        travel_website_count[foo.travel_website] += 1

    phone_type = []
    for k, v in mobile_brand_count.items():
        dict_temp = defaultdict()
        dict_temp.update(name=k, value=v)
        phone_type.append(dict_temp)

    data_info = []
    data_link = []

    data_info.append({'name': '视频网站'})
    for k, v in video_website_count.items():
        data_info.append({'name': k})
        dict_temp = defaultdict()
        dict_temp.update(source='视频网站', target=k, value=v)
        data_link.append(dict_temp)

    data_info.append({'name': '购物网站'})
    for k, v in shopping_website_count.items():
        data_info.append({'name': k})
        dict_temp = defaultdict()
        dict_temp.update(source='购物网站', target=k, value=v)
        data_link.append(dict_temp)

    data_info.append({'name': '海淘电商'})
    for k, v in overseas_taobao_count.items():
        data_info.append({'name': k})
        dict_temp = defaultdict()
        dict_temp.update(source='海淘电商', target=k, value=v)
        data_link.append(dict_temp)

    data_info.append({'name': '汽车网站'})
    for k, v in automotive_website_count.items():
        data_info.append({'name': k})
        dict_temp = defaultdict()
        dict_temp.update(source='汽车网站', target=k, value=v)
        data_link.append(dict_temp)

    data_info.append({'name': '房产网站'})
    for k, v in real_estate_website_count.items():
        data_info.append({'name': k})
        dict_temp = defaultdict()
        dict_temp.update(source='房产网站', target=k, value=v)
        data_link.append(dict_temp)

    data_info.append({'name': '旅游网站'})
    for k, v in travel_website_count.items():
        data_info.append({'name': k})
        dict_temp = defaultdict()
        dict_temp.update(source='旅游网站', target=k, value=v)
        data_link.append(dict_temp)

    website_type = defaultdict()
    website_type.update(data_info=data_info, data_link=data_link)

    return JsonResponse(
        {
            "code": 200,
            "data": {
                "operators_example_list": operators_example_list,
                "phone_type": phone_type,
                "website_type": website_type,

            }
        },
        json_dumps_params={'ensure_ascii': False}
    )


@require_http_methods(["POST"])
def RecreateTable(request):
    postBody = request.body
    postBody = b"{'is_recreate':1}"
    p = postBody.decode()
    p = eval(p)
    is_recreate = p['is_recreate']

    print("重建表开始")
    api_operateor_data_generation.api_data_delete()
    print("重建表结束")

    return JsonResponse(
        {
            "code": 200,
            "data": "success"
        }
    )


@require_http_methods(["GET"])
def download(request):
    # 开始导出数据
    print("开始导出数据")
    path = os.path.dirname(os.path.abspath(__file__)) + r'/datas/'
    print(path)
    api_operateor_data_generation.api_data_export(path)

    # 开始下载数据
    print('开始下载数据')
    file_path = path + r'operator.csv'
    try:
        r = StreamingHttpResponse(open(file_path, "rb"))
        r["content_type"] = "application/octet-stream"
        r["Content-Disposition"] = "attachment;filename=operator.csv"
        return r
    except Exception:
        raise Http404("Download error")
