from __future__ import unicode_literals
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from app01.models import MarketingUser, MarketingStore, MarketingCard
from collections import defaultdict
import sys
import os
sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from smart_finance_main import api_DataGeneration


@require_http_methods(["POST"])
def user(request):
    postBody = request.body
    p = postBody.decode()
    p = eval(p)
    total = p['total']
    print("生成用户开始")
    api_DataGeneration.api_user("黄牛营销欺诈", total)
    print("生成用户结束")
    return userDisplay()


@require_http_methods(["GET"])
def userInit(request):
    return userDisplay()


def userDisplay():
    users = MarketingUser.objects.all()
    user_number = MarketingUser.objects.count()
    user_age = defaultdict(int)
    user_job = defaultdict(int)
    for foo in users:
        user_job[foo.job] += 1

        if foo.age >= 18 and foo.age <= 23:
            user_age['18-23岁'] += 1
        elif foo.age >= 24 and foo.age <= 29:
            user_age['24-29岁'] += 1
        elif foo.age >= 30 and foo.age <= 39:
            user_age['30-39岁'] += 1
        elif foo.age >= 40 and foo.age <= 49:
            user_age['40-49岁'] += 1
        elif foo.age >= 50 and foo.age <= 59:
            user_age['50-59岁'] += 1
        elif foo.age >= 60 and foo.age <= 65:
            user_age['60-65岁'] += 1
        else:
            user_age['>=66岁'] += 1

    user_age_data_1 = ['18-23岁', '24-29岁', '30-39岁', '40-49岁', '50-59岁', '60-65岁', '>=66岁']
    user_age_data_2 = list()

    for key in user_age_data_1:
        user_age_data_2.append(user_age.get(key, 0))
    # print(user_age_data_1, user_age_data_2)

    user_job_data = list()
    for key, value in user_job.items():
        user_job_data.append({"name": key, "value": value})
    # print(user_job_data)

    return JsonResponse(
        {
            "code": 200,
            "data": {
                "user_age_data_1": user_age_data_1,
                "user_age_data_2": user_age_data_2,
                "user_job_data": user_job_data,
                "user_number": user_number
            }
        },
        json_dumps_params={'ensure_ascii': False}
    )


@require_http_methods(["POST"])
def store(request):
    postBody = request.body
    p = postBody.decode()
    p = eval(p)
    total = p['total']
    print("生成商户开始")
    api_DataGeneration.api_store("黄牛营销欺诈", total)
    print("生成商户结束")
    return storeDisplay()


@require_http_methods(["GET"])
def storeInit(request):
    return storeDisplay()


def storeDisplay():
    stores = MarketingStore.objects.all()
    stores_number = MarketingStore.objects.count()
    stores_industry = defaultdict(int)
    stores_rank_ = defaultdict(int)

    for foo in stores:
        stores_industry[foo.industry] += 1
        stores_rank_[foo.rank_field] += 1

    stores_industry_data = []
    for key, value in stores_industry.items():
        stores_industry_data.append([key, value])

    stores_rank__data = []
    for key, value in stores_rank_.items():
        stores_rank__data.append([key, value])

    # print(stores_industry_data)
    # print(stores_rank__data)

    return JsonResponse(
        {
            "code": 200,
            "data": {
                "data_1": stores_industry_data,
                "data_2": stores_rank__data,
                "stores_number": stores_number
            }
        },
        json_dumps_params={'ensure_ascii': False}
    )


@require_http_methods(["POST"])
def card(request):
    postBody = request.body
    p = postBody.decode()
    p = eval(p)
    is_generate = p['is_generate']

    print("生成卡开始")
    api_DataGeneration.api_card("黄牛营销欺诈")
    print("生成卡结束")
    return cardDisplay()


@require_http_methods(["GET"])
def cardInit(request):
    return cardDisplay()


def cardDisplay():
    cards = MarketingCard.objects.all()
    cards_owner_type = defaultdict(int)

    for foo in cards:
        cards_owner_type[foo.owner_type] += 1

    cards_owner_type_data = list()
    for key, value in cards_owner_type.items():
        cards_owner_type_data.append({"name": key, "value": value})
    # print(cards_owner_type_data)

    return JsonResponse(
        {
            "code": 200,
            "data": cards_owner_type_data
        },
        json_dumps_params={'ensure_ascii': False}
    )
