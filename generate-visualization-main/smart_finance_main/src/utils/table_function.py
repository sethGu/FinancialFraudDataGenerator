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
    """
    #日常消费次数限制，表1
    ########
    #目前非日常消费的次数暂设为0-1
    ########
    :param c_type:
    :return: list 第一个值表示最小次数，第二个值表示最大次数
    """

    jsonfile = BASE_DIR+'/json_file/consume_time_limit.json'
    dic = read_json_file(jsonfile)
    keys = dic.keys()
    if c_type not in keys:
        return "c_type error!"
    return dic[c_type]


def get_consume_rank(user, c_type):
    """
    确定消费档次的函数
    # 通过表2获取
    :param user:
    :param c_type:
    :return: 0-低 1-中 2-高
    """
    jsonfile = BASE_DIR+'/json_file/consume_rank.json'
    dic = read_json_file(jsonfile)
    keys = dic.keys()
    if c_type not in keys:
        return "c_type error!"

    # 获取当前类别的等级信息
    c_type_rank = dic[c_type]

    # 获取工资所在范围
    wage = user['wage']
    wage_list = list(c_type_rank.keys())
    #用户工资所在区间
    i = 0
    for i in range(len(wage_list)):
        if i == (len(wage_list) - 1):
            break
        cur = int(wage_list[i])
        if wage < cur:
            print("hello")
            break
    # 获取对应工资对应概率区间
    # [75, 20, 5]
    rank_percentage = c_type_rank[wage_list[i]]
    # 随机产生一个值
    r = random() * 100

    # 根据概率获取消费等级
    rank = 0
    percentage_sum = 0
    for rank in range(len(rank_percentage)):
        percentage_sum += rank_percentage[rank]
        if r <= percentage_sum:
            break

    return rank

def get_consume_inclination(user):
    """
    # 消费倾向表 表3
    # 根据用户工资返回当前消费的商户类型
    :param user:
    :return: 商户类型
    """
    jsonfile = BASE_DIR+'/json_file/consume_inclination.json'
    dic = read_json_file(jsonfile)
    wage_list = list(dic.keys())

    # 获取工资
    wage = user['wage']

    # 用户工资所在区间
    i = 0
    for i in range(len(wage_list)):
        if i == (len(wage_list) - 1):
            break
        cur = int(wage_list[i])
        if wage < cur:
            break

    # 获取工资对应的消费倾向百分比
    c_type_percentage = dic[wage_list[i]]
    # print(c_type_percentage)

    # 各个商户类型
    c_types = list(c_type_percentage.keys())

    # 各个商户类型消费概率
    c_type_values = list(c_type_percentage.values())

    # 随机产生一个值
    r = random.random() * 100

    # print(r)
    # 根据概率获取消费商户类型
    type = 0
    percentage_sum = 0
    for type in range(len(c_type_values)):
        percentage_sum += c_type_values[type]
        if r <= percentage_sum:
            break

    return c_types[type]

def get_consume_time(c_rank):
    """
    获取交易时间
    :param c_rank:消费子类
    :return: hh:mm:ss 时：分：秒 字符串
    """
    jsonfile = BASE_DIR+'/src/json_file/store_open_time.json'
    dic = read_json_file(jsonfile)

    c_rank = c_rank.replace("(低)","")
    c_rank = c_rank.replace("(中)","")
    c_rank = c_rank.replace("(高)","")

    #获取时间区间
    time_duration = dic[c_rank]
    # tmp = len(timeList)
    # #获取时间间隔
    # timeInterval = timeList[random.randint(0, len(timeList)) - 1]
    # #秒为单位
    # time = random.randint(timeInterval[0]*60*60, timeInterval[1]*60*60)
    #
    # # 小时
    # h = math.floor(time / 3600)
    # time -= h * 3600
    # #分钟
    # m = math.floor(time / 60)
    # time -= m * 60
    # #秒
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

    # 开始、结束营业分钟数
    start_minute, end_minute = 0, 24 * 60

    # 计算开始、结束营业分钟数
    for i in range(2):
        r = re.findall('(\d{1,2})', duration[i])

        # 开始时间
        if i == 0:
            start_minute = int(r[0]) * 60 + int(r[1])
        # 结束时间
        else:
            end_minute = int(r[0]) * 60 + int(r[1])

    trans_time = random.randint(start_minute, end_minute)
    # 转为按时间的字符串 并拼接秒
    trans_time = str("%02d" % (int(trans_time / 60) % 24)) + \
                 str("%02d" % int(trans_time % 60)) + \
                 str("%02d" % random.randint(0, 59))
    return trans_time