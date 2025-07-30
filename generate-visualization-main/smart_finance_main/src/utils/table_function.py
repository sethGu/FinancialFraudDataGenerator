# -*- coding:utf-8 -*-
# @Time     :2022/4/1 21:49
# @Author   :Guo Jiayu
import json
import math
import random
import re

from src.utils.config import BASE_DIR
from src.utils.functions import read_json_file


def get_consume_time_limit(c_type):
    jsonfile = BASE_DIR+'/json_file/consume_time_limit.json'
    dic = read_json_file(jsonfile)
    keys = dic.keys()
    if c_type not in keys:
        return "c_type error!"
    return dic[c_type]


def get_consume_rank(user, c_type):
    jsonfile = BASE_DIR+'/json_file/consume_rank.json'
    dic = read_json_file(jsonfile)
    keys = dic.keys()
    if c_type not in keys:
        return "c_type error!"

    c_type_rank = dic[c_type]

    wage = user['wage']
    wage_list = list(c_type_rank.keys())
    i = 0
    for i in range(len(wage_list)):
        if i == (len(wage_list) - 1):
            break
        cur = int(wage_list[i])
        if wage < cur:
            print("hello")
            break
    # [75, 20, 5]
    rank_percentage = c_type_rank[wage_list[i]]
    r = random() * 100

    rank = 0
    percentage_sum = 0
    for rank in range(len(rank_percentage)):
        percentage_sum += rank_percentage[rank]
        if r <= percentage_sum:
            break

    return rank

def get_consume_inclination(user):
    jsonfile = BASE_DIR+'/json_file/consume_inclination.json'
    dic = read_json_file(jsonfile)
    wage_list = list(dic.keys())

    wage = user['wage']

    i = 0
    for i in range(len(wage_list)):
        if i == (len(wage_list) - 1):
            break
        cur = int(wage_list[i])
        if wage < cur:
            break

    c_type_percentage = dic[wage_list[i]]
    # print(c_type_percentage)

    c_types = list(c_type_percentage.keys())

    c_type_values = list(c_type_percentage.values())

    r = random.random() * 100

    # print(r)
    type = 0
    percentage_sum = 0
    for type in range(len(c_type_values)):
        percentage_sum += c_type_values[type]
        if r <= percentage_sum:
            break

    return c_types[type]

def get_consume_time(c_rank):
    jsonfile = BASE_DIR+'/src/json_file/store_open_time.json'
    dic = read_json_file(jsonfile)

    c_rank = c_rank.replace("(Low)","")
    c_rank = c_rank.replace("(Medium)","")
    c_rank = c_rank.replace("(High)","")

    time_duration = dic[c_rank]
    # tmp = len(timeList)
    # timeInterval = timeList[random.randint(0, len(timeList)) - 1]
    # time = random.randint(timeInterval[0]*60*60, timeInterval[1]*60*60)
    #
    # h = math.floor(time / 3600)
    # time -= h * 3600
    # m = math.floor(time / 60)
    # time -= m * 60
    # s = math.floor(time)
    #
    # h = '0' + h.__str__() if h < 10 else h.__str__()
    # m = '0' + m.__str__() if m < 10 else m.__str__()
    # s = '0' + s.__str__() if s < 10 else s.__str__()
    # return h + "" + m + "" + s
    # return h + ":" + m + ":" + s
    patten = '(\d{1,2}:\d{1,2})'
    # ['9:00', '15:00']
    duration = re.findall(patten, time_duration)

    start_minute, end_minute = 0, 24 * 60

    for i in range(2):
        r = re.findall('(\d{1,2})', duration[i])

        if i == 0:
            start_minute = int(r[0]) * 60 + int(r[1])
        else:
            end_minute = int(r[0]) * 60 + int(r[1])

    trans_time = random.randint(start_minute, end_minute)
    trans_time = str("%02d" % (int(trans_time / 60) % 24)) + \
                 str("%02d" % int(trans_time % 60)) + \
                 str("%02d" % random.randint(0, 59))
    return trans_time