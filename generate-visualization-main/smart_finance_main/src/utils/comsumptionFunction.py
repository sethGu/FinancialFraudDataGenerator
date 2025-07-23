import json
import random

from src.utils.config import BASE_DIR


def get_consume_type(user, consume_type_times):
    """
    # 通过表3和表1获取
    # 通过表3加权随机，通过表1限制不同消费的次数
    :param user:
    :param consume_type_times:
    :return:
    """
    # 加载消费倾向与消费次数限制的json文件
    f1 = open(BASE_DIR +"/src/json_file/consume_inclination.json", 'r', encoding="UTF-8")
    consume_inclination = json.load(f1)
    # print(consume_inclination)
    f2 = open(BASE_DIR +"/src/json_file/consume_time_limit.json", 'r', encoding="UTF-8")
    consume_time_limit = json.load(f2)
    # print(consume_time_limit)
    # print('user:', user)
    # print('consume_type_times:', consume_type_times)

    consume_type = ''
    # 根据消费倾向表中的概率生成每次交易的种类
    for key in list(consume_inclination.keys()):
        if key == '-':
            consume_type = random_key(consume_inclination[key])
            break
        # 根据工资选择消费倾向概率分布
        if user['wage'] <= int(key):
            consume_incl = consume_inclination[key].copy()
            # 如果某种交易已经达到上限，不再考虑
            for k in consume_type_times.keys():
                if consume_type_times[k] >= consume_time_limit[k][1]:
                    consume_incl.pop(k)
            consume_type = random_key(consume_incl)
            break

    return consume_type

def random_key(rate):
    # """随机变量的概率函数"""
    # 参数rate为dic
    # 返回概率事件的键
    start = 0
    randnum = random.randint(0, sum(list(rate.values())))
    # print(rate)
    for key in rate.keys():
        start += int(rate[key])
        if randnum <= start:
            return key

def get_consume_rank(user, c_type):
    """
    确定消费子类的函数
    :param user:
    :param c_type:
    :return:
    """
    # 加载消费倾向与消费次数限制的json文件
    # if c_type == "教育文化":
    #     return None
    f3 = open(BASE_DIR +"/src/json_file/consume_subclass_ratio.json", 'r', encoding="UTF-8")
    consume_rank = json.load(f3)

    # 加载大类的小类
    f4 = open(BASE_DIR + "/src/json_file/store_generate_ratio.json", 'r', encoding="UTF-8")
    sub_classes = json.load(f4)
    # 当前大类下的子类
    sub_class = sub_classes[c_type]
    # 商户大类相关信息
    big_class = consume_rank[c_type]

    # rank_dict = {0:'低',1:'中',2:'高'}
    # rank = 0
    # c_type_rank_dict = consume_rank[c_type]
    # for key in list(c_type_rank_dict):
    #     if key == '-':
    #         rank = random_index(c_type_rank_dict[key])
    #         break
    #     # 根据工资选择消费层次概率分布
    #     if user['wage'] <= int(key):
    #         rank = random_index(c_type_rank_dict[key])
    #         break
    # return rank_dict[rank]

    wage_list = [30000, 50000, 100000, 200000, 500000, float('inf')]
    # 工资所在区间
    index = 0
    for i in range(6):
        if user.getWage() < wage_list[i]:
            index = i
            break
    # 当前工资水平在当前大类下消费子类的概率
    sub_class_ratio = big_class[str(int(wage_list[index])) if index != 5 else "-"]

    sum_ = sum(sub_class_ratio)
    pro_list = [0 for i in range(len(sub_class_ratio))]
    for i in range(len(sub_class_ratio)):
        if i == 0:
            pro_list[i] = sub_class_ratio[i] / sum_
        else:
            pro_list[i] = pro_list[i - 1] + sub_class_ratio[i] / sum_
    r = random.random()
    # 行业小类
    industry = ''
    classes = list(sub_class.keys())
    for i in range(len(pro_list)):
        if r < pro_list[i]:
            if i > 0 and pro_list[i] != pro_list[i - 1]:
                industry = classes[i]
                break
            elif i == 0 and pro_list[i] != 0:
                industry = classes[i]
                break
    has_sub_class = ["餐饮", "医疗保健", "居住", "娱乐", "生活用品及服务"]
    if c_type in has_sub_class:
        # 加载低中高等级的概率
        f5 = open(BASE_DIR + "/src/json_file/exist_three_rank_consume_ratio.json", 'r', encoding="UTF-8")
        sub_class_rank = json.load(f5)
        sub_class_rank = sub_class_rank[industry]
        sub_class_rank = sub_class_rank[str(int(wage_list[index])) if index != 5 else "-"]
        pro_list = [0] * len(sub_class_rank)
        for i in range(len(sub_class_rank)):
            if i > 0:
                pro_list[i] = pro_list[i - 1] + sub_class_rank[i]
            else:
                pro_list[i] = sub_class_rank[i]
        r = random.randint(0, 100)
        rank_dict = {0:'低',1:'中',2:'高'}
        for i in range(len(sub_class_rank)):
            if r < pro_list[i]:
                if i > 0 and pro_list[i] != pro_list[i - 1]:
                    industry = industry + "(" + rank_dict[i] + ")"
                    break
                elif i == 0 and pro_list[i] != 0:
                    industry = industry + "(" + rank_dict[i] + ")"
                    break
    return industry
def random_index(rate):
    # """随机变量的概率函数"""
    # 参数rate为list
    # 返回概率事件的index,0.1.2表示低、中、高层次
    start = 0
    randnum = random.randint(0, 100)
    # print(rate)
    for index, scope in enumerate(rate):
        start += scope
        if randnum <= start:
            return index


def get_store_by_type_rank(c_type, c_rank, marchant_list):
    """
    选择消费对象
    徐昌华
    :param c_type:
    :param c_rank:
    :param marchant_list:
    :return:
    """
    marchant_candidates = []
    for marchant in marchant_list:
        marchant_info = marchant.get_store_info()
        marchant_c_type = marchant_info["industry"]
        marchant_c_rank = marchant_info["rank"]
        if marchant_c_type == c_type and marchant_c_rank==c_rank:
            marchant_candidates.append(marchant)
    marchant = random.choice(marchant_candidates)
    return marchant

def get_user_card(user,store):
    """
    根据消费的用户和商户信息，选择合适的银行卡
    赵征明
    :param user:
    :param marchant:
    :return:
    """

    card_list = user.getCard()


    return random.choice(card_list)

def get_amount(store):
    """
    赵征明
    :param store:
    :return:
    """
    consumption_range = store.getCharge_duration()
    a = random.randint(consumption_range[0],consumption_range[1])
    if a == 0:
        a += 1
    return a

def get_consume_times(user):
    f1 = open(BASE_DIR +"/src/json_file/consume_inclination.json", 'r', encoding="UTF-8")
    consume_inclination = json.load(f1)
    f2 = open(BASE_DIR +"/src/json_file/consume_time_limit.json", 'r', encoding="UTF-8")
    consume_time_limit = json.load(f2)

    wage = user.getWage()
    # print(wage)
    # print(consume_inclination)
    # inclination = consume_inclination['-']
    consume_range = []
    for i in consume_inclination:
        if i == '-':
            continue
        consume_range.append(int(i))
    consume_range.append(0)
    consume_range.sort()
    inclination = consume_inclination['-']
    for i,range_m in enumerate(consume_range):
        if i == 0:
            continue
        if consume_range[i-1] <= wage and wage < consume_range[i] :
            inclination = consume_inclination[str(range_m)]
            break
    times_max = 0
    for c_type in inclination:
        if c_type in consume_time_limit:
            times_max += inclination[c_type] * consume_time_limit[c_type][-1] * 0.02
    randnum = random.randint(0, int(times_max)+i)
    return randnum