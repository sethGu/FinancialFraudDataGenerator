
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
    try:
        content = content.replace('\n','')
        end_flag = ['?', '!', '.', '？', '！', '。', '…']
        content_len = len(content)
        sentences = []
        tmp_char = ''
        for idx, char in enumerate(content):
            tmp_char += char

            if (idx + 1) == content_len:
                sentences.append(tmp_char)
                break

            if char in end_flag:
                next_idx = idx + 1
                if not content[next_idx] in end_flag:
                    sentences.append(tmp_char)
                    tmp_char = ''

        return sentences
    except:
        return ''


def check_contain_chinese(check_str):
    for ch in check_str.encode('utf-8').decode('utf-8'):
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


def clean_sentence(sentence):
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
    with open(jsonfile, encoding='utf8') as f:
        dic = json.load(f)

    return dic

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def get_later_time(cur_time, duration):
    the_date = datetime.datetime.strptime(cur_time, '%Y%m%d%H')
    result_date = the_date + datetime.timedelta(hours=duration)
    d = result_date.strftime('%Y%m%d%H')
    return d

def get_before_time(cur_time):
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