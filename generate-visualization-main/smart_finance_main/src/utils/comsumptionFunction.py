import json
import random

from src.utils.config import BASE_DIR


def get_consume_type(user, consume_type_times):
    f1 = open(BASE_DIR +"/src/json_file/consume_inclination.json", 'r', encoding="UTF-8")
    consume_inclination = json.load(f1)
    # print(consume_inclination)
    f2 = open(BASE_DIR +"/src/json_file/consume_time_limit.json", 'r', encoding="UTF-8")
    consume_time_limit = json.load(f2)
    # print(consume_time_limit)
    # print('user:', user)
    # print('consume_type_times:', consume_type_times)

    consume_type = ''
    for key in list(consume_inclination.keys()):
        if key == '-':
            consume_type = random_key(consume_inclination[key])
            break
        if user['wage'] <= int(key):
            consume_incl = consume_inclination[key].copy()
            for k in consume_type_times.keys():
                if consume_type_times[k] >= consume_time_limit[k][1]:
                    consume_incl.pop(k)
            consume_type = random_key(consume_incl)
            break

    return consume_type

def random_key(rate):
    start = 0
    randnum = random.randint(0, sum(list(rate.values())))
    # print(rate)
    for key in rate.keys():
        start += int(rate[key])
        if randnum <= start:
            return key

def get_consume_rank(user, c_type):
    f3 = open(BASE_DIR +"/src/json_file/consume_subclass_ratio.json", 'r', encoding="UTF-8")
    consume_rank = json.load(f3)

    f4 = open(BASE_DIR + "/src/json_file/store_generate_ratio.json", 'r', encoding="UTF-8")
    sub_classes = json.load(f4)
    sub_class = sub_classes[c_type]
    big_class = consume_rank[c_type]

    # rank_dict = {0:'Low',1:'Medium',2:'High'}
    # rank = 0
    # c_type_rank_dict = consume_rank[c_type]
    # for key in list(c_type_rank_dict):
    #     if key == '-':
    #         rank = random_index(c_type_rank_dict[key])
    #         break
    #     if user['wage'] <= int(key):
    #         rank = random_index(c_type_rank_dict[key])
    #         break
    # return rank_dict[rank]

    wage_list = [30000, 50000, 100000, 200000, 500000, float('inf')]
    index = 0
    for i in range(6):
        if user.getWage() < wage_list[i]:
            index = i
            break
    sub_class_ratio = big_class[str(int(wage_list[index])) if index != 5 else "-"]

    sum_ = sum(sub_class_ratio)
    pro_list = [0 for i in range(len(sub_class_ratio))]
    for i in range(len(sub_class_ratio)):
        if i == 0:
            pro_list[i] = sub_class_ratio[i] / sum_
        else:
            pro_list[i] = pro_list[i - 1] + sub_class_ratio[i] / sum_
    r = random.random()
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
    has_sub_class = ["Catering", "Healthcare", "Residence", "Entertainment", "Household_items_and_services"]
    if c_type in has_sub_class:
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
        rank_dict = {0:'Low',1:'Medium',2:'High'}
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
    start = 0
    randnum = random.randint(0, 100)
    # print(rate)
    for index, scope in enumerate(rate):
        start += scope
        if randnum <= start:
            return index


def get_store_by_type_rank(c_type, c_rank, marchant_list):
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
    card_list = user.getCard()


    return random.choice(card_list)

def get_amount(store):
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