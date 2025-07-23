# -*- coding: utf-8 -*-
"""
  Author: LiangJing
   Time : 2023/5/14
    File: EnterpriseService.py
"""

import random
import string
import datetime
import json
import time
from dateutil.relativedelta import relativedelta
from random import choice
import os

BASE_DIR =  os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.dataGen20220414.dao.EnterpriseDao import EnterpriseDao
from src.dataGen20220414.entity.Enterprise import Enterprise

class EnterpriseService():
    def __init__(self):

        self.EnterpriseDao = EnterpriseDao()
    def createEnterpriseTable(self):
        '''
        创建Enterprise表 梁静
        :return:
        '''
        # for name in self.table_names.values():
        self.EnterpriseDao.createEnterpriseTable()

    def insertEnterprises(self,enterpriseList):
        '''
        批量插入Enterprise 梁静
        :param enterpriseList:
        :return:
        '''
        self.EnterpriseDao.insertEnterprises(enterpriseList)

    def selectEnterprises(self):
        '''
        查询所有企业
        :return:
        '''
        select_res = self.EnterpriseDao.selectEnterprises()
        enterpriseList = []
        for item in select_res:
            id, socialId, name, registerId, represent, type, builtTime, regAmount, checkTime, regLocate, state, locate, busScope  = item
            enterprise = Enterprise(id, socialId, name, registerId, represent, type, builtTime, regAmount, checkTime, regLocate, state, locate, busScope)

            enterpriseList.append(enterprise)
        return enterpriseList


    def createEnterprise():
        """
        生成企业信息
        """
        # 生成统一社会信用代码
        socialId = ('91' + ''.join(random.choice(string.digits) for _ in range(6)) +
                     ''.join(random.choice('ABCDEFGHJKLMNPQRTUWXY' + string.digits) for _ in range(10)))
        # 生成15位注册号
        registerId = ''.join(random.sample('123456789', 1)) + ''.join(random.choice(string.digits) for _ in range(14))
        # 生成注册资本，服从威布尔分布
        regAmount = 0
        while regAmount<100:
            regAmount = random.weibullvariate(1000, 1.5)
        regAmount = round(regAmount, 2)
        # 企业注册时间范围
        MINTIME = datetime.datetime(1990, 1, 1).strftime('%Y%m%d')  # 设置时间范围的开始时间
        MAXTIME = datetime.datetime.now().strftime('%Y%m%d')  # 设置时间范围的结束时间
        builtTime = EnterpriseService.get_later_time(MINTIME)  #成立日期
        checkTime = EnterpriseService.get_before_time(MAXTIME) #核准日期
        if checkTime <= builtTime:
            checkTime = EnterpriseService.get_before_time(MAXTIME)

        represent = EnterpriseService.random_name_representative()
        state = '存续'
        name, type, regLocate, locate, busScope = EnterpriseService.random_name_business()
        # print(socialId, name, registerId, represent, type, builtTime, regAmount,
        #                 checkTime, regLocate, state,locate, busScope)

        enterprise = Enterprise(None,socialId, name, registerId, represent, type, builtTime, regAmount,
                        checkTime, regLocate, state,locate, busScope)
        return enterprise



    # 生成法定代表人姓名
    def random_name_representative():
        # 百家姓姓氏
        firstName = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅皮卞齐康伍余元卜顾孟平" \
                    "黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计伏成戴谈宋茅庞熊纪舒屈项祝董粱杜阮蓝闵席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田樊胡凌霍虞万支柯昝管卢莫经房裘缪干解应宗丁宣贲邓郁单杭洪包诸左石崔吉钮" \
                    "龚程嵇邢滑裴陆荣翁荀羊於惠甄麴家封芮羿储靳汲邴糜松井段富巫乌焦巴弓牧隗山谷车侯宓蓬全郗班仰秋仲伊宫宁仇栾暴甘钭厉戎祖武符刘景詹束龙叶幸司韶郜黎蓟薄印宿白怀蒲邰从鄂索咸籍赖卓蔺屠蒙池乔阴欎胥能苍" \
                    "双闻莘党翟谭贡劳逄姬申扶堵冉宰郦雍舄璩桑桂濮牛寿通边扈燕冀郏浦尚农温别庄晏柴瞿阎充慕连茹习宦艾鱼容向古易慎戈廖庾终暨居衡步都耿满弘匡国文寇广禄阙东殴殳沃利蔚越夔隆师巩厍聂晁勾敖融冷訾辛阚那简饶空" \
                    "曾毋沙乜养鞠须丰巢关蒯相查後荆红游竺权逯盖益桓公晋楚闫法汝鄢涂钦归海帅缑亢况后有琴梁丘左丘商牟佘佴伯赏南宫墨哈谯笪年爱阳佟言福百家姓终"
        # 百家姓中双姓氏
        firstName2 = "万俟司马上官欧阳夏侯诸葛闻人东方赫连皇甫尉迟公羊澹台公冶宗政濮阳淳于单于太叔申屠公孙仲孙轩辕令狐钟离宇文长孙慕容鲜于闾丘司徒司空亓官司寇仉督子颛孙端木巫马公西漆雕乐正壤驷公良拓跋夹谷宰父谷梁段干百里东郭南门呼延羊舌微生梁丘左丘东门西门南宫南宫"
        # 女孩名字
        girl = '秀娟英华慧巧美娜静淑惠珠翠雅芝玉萍红娥玲芬芳燕彩春菊兰凤洁梅琳素云莲真环雪荣爱妹霞香月莺媛艳瑞凡佳嘉琼勤珍贞莉桂娣叶璧璐娅琦晶妍茜秋珊莎锦黛青倩婷姣婉娴瑾颖露瑶怡婵雁蓓纨仪荷丹蓉眉君琴蕊薇菁梦岚苑婕馨瑗琰韵融园艺咏卿聪澜纯毓悦昭冰爽琬茗羽希宁欣飘育滢馥筠柔竹霭凝晓欢霄枫芸菲寒伊亚宜可姬舒影荔枝思丽'
        # 男孩名字
        boy = '伟刚勇毅俊峰强军平保东文辉力明永健世广志义兴良海山仁波宁贵福生龙元全国胜学祥才发武新利清飞彬富顺信子杰涛昌成康星光天达安岩中茂进林有坚和彪博诚先敬震振壮会思群豪心邦承乐绍功松善厚庆磊民友裕河哲江超浩亮政谦亨奇固之轮翰朗伯宏言若鸣朋斌梁栋维启克伦翔旭鹏泽晨辰士以建家致树炎德行时泰盛雄琛钧冠策腾楠榕风航弘'
        # 名
        name = '中笑贝凯歌易仁器义礼智信友上都卡被好无九加电金马钰玉忠孝'

        # 10%的机遇生成双数姓氏
        if choice(range(100)) > 10:
            firstName_name = firstName[choice(range(len(firstName)))]
        else:
            i = choice(range(len(firstName2)))
            firstName_name = firstName2[i:i + 2]
        #     return firstName_name
        sex = choice(range(2))
        name_1 = ""
        # 生成并返回一个名字
        if sex > 0:
            girl_name = girl[choice(range(len(girl)))]
            if choice(range(2)) > 0:
                name_1 = name[choice(range(len(name)))]
            return firstName_name + name_1 + girl_name
        else:
            boy_name = boy[choice(range(len(boy)))]
            if choice(range(2)) > 0:
                name_1 = name[choice(range(len(name)))]
            return firstName_name + name_1 + boy_name

    # 生成企业名称   辽源市     亨通   物流仓储    有限公司
    #             行政区域 + 字号 + 行业号   +  组织形式
    def random_name_business():
        # (1) 先随机从293个地级市选一个作为行政区域
        name_city = []
        with open(BASE_DIR + "/src/json_file/city.txt", "r", encoding="utf-8") as f:
            for a in f:
                name_city.append(a)
        first_name = choice(name_city)

        # (2) 随机选取一个字代表字号
        name_center = []
        with open(BASE_DIR + "/src/json_file/zihao.txt", "r", encoding="utf-8") as f:
            for a in f:
                name_center.append(a)
        second_name = choice(name_center)

        # (3) 随机选取行业号
        with open(BASE_DIR + "/src/json_file/hangyehao.json", "r", encoding="utf-8") as f:
            json_file = json.load(f)
        name_hangyehao = choice(json_file)
        third_name = list(name_hangyehao.keys())[0]

        # (4) 随机生成公司类型
        company = ["无限责任公司", "有限责任公司", "两合公司", "股份有限公司", "股份两合公司"]
        fourth_name = choice(company)

        company_name = first_name.rstrip("\n") + second_name.rstrip("\n") + third_name + fourth_name
        company_type = fourth_name.rstrip("\n")
        company_regist = first_name.rstrip("\n") + "市场监督管理局"
        company_location = first_name.rstrip("\n")
        company_business_scope = list(name_hangyehao.values())[0]

        return company_name, company_type, company_regist, company_location, company_business_scope




    def get_before_time(cur_time):
        y = random.randint(0, 10)
        m = random.randint(0, 12)
        d = random.randint(0, 30)

        the_date = datetime.datetime.strptime(cur_time, '%Y%m%d')
        result_date = the_date - relativedelta(years=y, months=m, days=d)  # 往前推y年m月d日
        result = result_date.strftime('%Y%m%d')  # 格式化成字符串形式
        return result

    def get_later_time(cur_time):
        y = random.randint(0, 30)
        m = random.randint(0, 12)
        d = random.randint(0, 30)

        the_date = datetime.datetime.strptime(cur_time, '%Y%m%d')
        result_date = the_date + relativedelta(years=y, months=m, days=d)  # 往后推y年m月d日
        result = result_date.strftime('%Y%m%d')  # 格式化成字符串形式
        return result

