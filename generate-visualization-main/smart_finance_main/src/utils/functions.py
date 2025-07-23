"""
常用函数集合
"""
import datetime
import json
import random
import time
import string


def delete_stopwords(words, stopwords):
    result = []
    for word in words:
        if len(word) == 1:
            continue
        elif word in stopwords:
            continue
        else:
            result.append(word)

    return result


def document2sentences(content):
    """
    将段落或者篇章转为句子集合
    :param content: 篇章内容 []
    :return: []
    """
    try:
        content = content.replace('\n','')
        # 结束符号，包含中文和英文的
        end_flag = ['?', '!', '.', '？', '！', '。', '…']
        content_len = len(content)
        sentences = []
        tmp_char = ''
        for idx, char in enumerate(content):
            # 拼接字符
            tmp_char += char

            # 判断是否已经到了最后一位
            if (idx + 1) == content_len:
                sentences.append(tmp_char)
                break

            # 判断此字符是否为结束符号
            if char in end_flag:
                # 再判断下一个字符是否为结束符号，如果不是结束符号，则切分句子
                next_idx = idx + 1
                if not content[next_idx] in end_flag:
                    sentences.append(tmp_char)
                    tmp_char = ''

        return sentences
    except:
        return ''


def check_contain_chinese(check_str):
    """
    判断一个字符串是否 包含 中文字符
    :param check_str: 字符串
    :return: 包含 True 不包含 False
    """
    for ch in check_str.encode('utf-8').decode('utf-8'):
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


def clean_sentence(sentence):
    """
    清洗单个句子
    :param sentence: 单句字符串
    :return: 清理后的句子字符串
    """
    sentence = sentence.replace('\n', '').replace(' ', '').replace('\t', '').strip()
    return sentence

def getday(y=2017, m=8, d=15, n=1):
    the_date = datetime.datetime(y,m,d)
    result_date = the_date + datetime.timedelta(days=n)
    d = result_date.strftime('%Y%m%d')
    year = int(d[:4])
    month = int(d[4:6])
    day = int(d[6:8])
    return d,(year,month,day)

def read_json_file(jsonfile):
    """
    读取json文件
    :param jsonfile:
    :return: dict
    """
    with open(jsonfile, encoding='utf8') as f:
        dic = json.load(f)

    return dic

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    '''
    智慧金融中账户id的生成函数
    :param size:
    :param chars:
    :return:
    '''
    return ''.join(random.choice(chars) for _ in range(size))

def get_later_time(cur_time, duration):
    '''

    :param cur_time: 当前时间 如2022040810  年月日时
    :param duration: 单位为 h， 获取duration小时后的时间
    :return:
    '''
    the_date = datetime.datetime.strptime(cur_time, '%Y%m%d%H')
    result_date = the_date + datetime.timedelta(hours=duration)
    d = result_date.strftime('%Y%m%d%H')
    return d

def get_before_time(cur_time):
    '''

    :param cur_time: 当前时间 如20221012013130  年月日时分秒
    :param duration:
    :return: h小时 m分钟 s秒之前的时间
    '''
    # d =random.randint(0,1)
    # h = random.randint(0, 23)
    # m = random.randint(0, 59)
    # s = random.randint(0, 59)
    d = 0
    h = 0
    m = random.randint(3, 10)
    s = 0
    the_date = datetime.datetime.strptime(cur_time, '%Y%m%d%H%M%S')
    result_date = the_date - datetime.timedelta(days=d,hours=h,minutes=m,seconds=s)
    result = result_date.strftime('%Y%m%d%H%M%S')
    return result