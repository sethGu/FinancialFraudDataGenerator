from __future__ import unicode_literals
import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import os
import datetime
import time


@require_http_methods(["POST"])
def durationChoose(request):
    postBody = request.body
    # postBody = b'{"date":["2022-10-10T13:34:04.369Z","2022-11-09T13:34:04.369Z"]}'
    p = postBody.decode()
    p = eval(p)
    date = p['date']
    # startDate = date[0].split('T', 1)[0]
    # endDate = date[1].split('T', 1)[0]
    # startDate = startDate.split('-', 3)[0] + startDate.split('-', 3)[1] + startDate.split('-', 3)[2]
    # endDate = endDate.split('-', 3)[0] + endDate.split('-', 3)[1] + endDate.split('-', 3)[2]
    # startDate_s = tuple(time.strptime(startDate, "%Y%m%d"))
    # d1 = datetime.date(startDate_s[0], startDate_s[1], startDate_s[2])
    # endDate_s = tuple(time.strptime(endDate, "%Y%m%d"))
    # d2 = datetime.date(endDate_s[0], endDate_s[1], endDate_s[2])
    # duration = int((d2 - d1).days)
    # print(startDate)
    # print(duration)
    dateSelection_datas = {
        "code": 200,
        "data": date
    }

    dateSelection_path = os.path.dirname(os.path.abspath(__file__)) + '/annoyingDatas/dateSelection.json'

    with open(dateSelection_path, "w") as f:
        json.dump(dateSelection_datas, f)

    return durationInit()


@require_http_methods(["GET"])
def durationSet(request):
    return durationInit()


def durationInit():
    dateSelection_path = os.path.dirname(os.path.abspath(__file__)) + '/annoyingDatas/dateSelection.json'
    with open(dateSelection_path, "r") as read_file:
        dateSelection_datas = json.load(read_file)
    return JsonResponse(dateSelection_datas, json_dumps_params={'ensure_ascii': False})
