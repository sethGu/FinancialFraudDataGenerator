# -*- coding: utf-8 -*-
"""
  Author: LiangJing
   Time : 2023/5/15
    File: enterprise_generate.py
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
from smart_finance_main import api_DataGeneration
from app01.models import Enterprise
from collections import defaultdict


@require_http_methods(["POST"])
def enterpriseGenerate(request):
    postBody = request.body
    print(postBody)
    p = postBody.decode()
    # print(p)
    p = eval(p)
    number_of_enterprises = p['number_of_enterprises']
    print("生成工商企业开始")
    api_DataGeneration.api_enterprise(number_of_enterprises)
    print("生成工商企业结束")
    return enterpriseDisplay()


@require_http_methods(["GET"])
def enterpriseInit(request):
    return enterpriseDisplay()


@require_http_methods(["GET"])
def fetchList(request):
    enterprise_list = []
    enterprises = Enterprise.objects.all()
    i = 0
    for foo in enterprises:
        one_example = defaultdict(str)
        i += 1
        one_example.update(id=i, socialid=foo.socialid, name=foo.name, registerid=foo.registerid,
                           represent=foo.represent,
                           type=foo.type, builttime=foo.builttime,
                           regamount=foo.regamount, checktime=foo.checktime, reglocate=foo.reglocate, state=foo.state,
                           locate=foo.locate, busscope=foo.busscope)
        enterprise_list.append(one_example)
    # 解析Query Params
    page = int(request.GET.get('page', 1))
    limit = int(request.GET.get('limit', 10))
    sort = request.GET.get('sort', '+id')
    if sort == '-id':
        enterprise_list = enterprise_list[::-1]
    # 获取pageList
    pageList = enterprise_list[(page - 1) * limit: page * limit]
    return JsonResponse(
        {
            "code": 200,
            "data": {
                "total": len(enterprise_list),
                "items": pageList
            }
        },
        json_dumps_params={'ensure_ascii': False}
    )


def enterpriseDisplay():
    enterprises = Enterprise.objects.all()
    enterprises_example_list = []

    i = 0
    for foo in enterprises:
        i += 1
        one_example = defaultdict(str)
        one_example.update(socialid=foo.socialid, name=foo.name, registerid=foo.registerid, represent=foo.represent,
                           type=foo.type, builttime=foo.builttime,
                           regamount=foo.regamount, checktime=foo.checktime, reglocate=foo.reglocate, state=foo.state,
                           locate=foo.locate, busscope=foo.busscope)
        enterprises_example_list.append(one_example)
        # if i==2:
        #     break
    print('工商企业数量：', len(enterprises_example_list))

    area_count = defaultdict(int)
    type_count = defaultdict(int)
    for foo in enterprises:
        area_count[foo.locate] += 1
        type_count[foo.type] += 1
    data_area = list(area_count.keys())
    data_type = list(type_count.keys())

    data_info = []
    for k, v in area_count.items():
        dict_temp = defaultdict()
        dict_temp.update(name=k, value=v)
        data_info.append(dict_temp)
    area_info = {}
    area_info.update(data_area=data_area, data_info=data_info)

    data_type_info = []
    for k, v in type_count.items():
        dict_temp = defaultdict()
        dict_temp.update(name=k, value=v)
        data_type_info.append(dict_temp)
    type_info = {}
    type_info.update(data_type=data_type, data_type_info=data_type_info)

    # print(area_info)

    return JsonResponse(
        {
            "code": 200,
            "data": {
                "enterprises_example_list": enterprises_example_list,
                "area_info": area_info,
                "type_info": type_info,
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
    api_DataGeneration.api_enterprise_table()
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
    api_DataGeneration.api_enterprise_export_csv(path)

    # 开始下载数据
    print('开始下载数据')
    file_path = path + r'enterprise.csv'
    try:
        r = StreamingHttpResponse(open(file_path, "rb"))
        r["content_type"] = "application/octet-stream"
        r["Content-Disposition"] = "attachment;filename=enterprise.csv"
        return r
    except Exception:
        raise Http404("Download error")
