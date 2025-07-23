import json
import random

from src.dataGen20220414.dao.UserDao import UserDao
from src.dataGen20220414.entity.User import User

class UserService():
    def __init__(self, scene):

        self.userDao = UserDao()

        self.table_names = {"黄牛营销欺诈": 'marketing_user', "信用卡违规套现": 'credit_user', "异常转账": 'abnormal_user', "伪冒注册欺诈": 'register_user', "赌博违规交易": 'gambling_user',
                        "商户违规": 'store_user'}
        self.scene = self.table_names[scene]
    def createUserTable(self):
        '''
        创建User表 赵征明
        :return:
        '''
        # for name in self.table_names.values():
        self.userDao.createUserTable(self.scene)

    def insertUsers(self,userList):
        '''
        批量插入User
        :param userList:
        :return:
        '''
        self.userDao.insertUsers(userList, self.scene)

    def selectUsers(self):
        '''
        查询所有用户，包括异常用户
        :return:
        '''
        select_res = self.userDao.selectUsers(self.scene)
        userList = []
        for item in select_res:
            id, age, gender, job, wage, card, abnormal, abnormal_state, user_no, loc_id = item
            card = json.loads(card)
            user = User(age=age, gender=gender, job=job, wage=wage, id=id, card=card, abnormal=abnormal,
                        abnormal_state=abnormal_state, user_no=user_no, loc_id=loc_id)
            userList.append(user)
        return userList

    def get_fraud_and_normal_user(self,fraud_category, quantity=50):
        '''

        :param quantity: 欺诈用户数量
        :return:
        '''
        # 获取普通用户并将其一部分设为欺诈用户
        normal_user = self.userDao.selectNormalUser(self.scene)
        random.shuffle(normal_user)
        fraud_user = normal_user[0:quantity]

        # 剩下的作为可能的被欺诈用户
        normal_user = normal_user[quantity:]

        # 将挑选出来的用户更新至数据库中，置为欺诈用户
        for u in fraud_user:
            self.userDao.updateUserState(user_id=u.id, fraud_category=fraud_category, table_name=self.scene)

        return fraud_user, normal_user

    def selectNormalUser(self):
        select_res = self.userDao.selectNormalUser(self.scene)
        # userList = []
        # for item in select_res:
        #     id, age, gender, job, wage, card, abnormal, abnormal_state, user_no = item
        #
        #     if abnormal == 0:
        #         user = User(id=id, age=age, gender=gender, job=job, wage=wage, card=card,
        #                     abnormal=abnormal, abnormal_state=abnormal_state, user_no=user_no)
        #         userList.append(user)
        return select_res

    def selectAllUser(self):
        select_res = self.userDao.selectUsers(self.scene)
        userList = []
        for item in select_res:
            id, age, gender, job, wage, card, abnormal, abnormal_state, user_no, loc_id = item

            user = User(id=id, age=age, gender=gender, job=job, wage=wage, card=card,
                        abnormal=abnormal, abnormal_state=abnormal_state, user_no=user_no)
            userList.append(user)
        return userList

    def updateUserState(self,user_id, fraud_category):
        self.userDao.updateUserState(user_id, fraud_category, self.scene)

    # 生成user对象
    @staticmethod
    def createUser(age=None, gender=None, job=None, wage=None, abnormal=None, abnormal_state=None, user_no=None):
        '''
        # 生成用户
        # editor: 20220411顾峻铨
        # 20220411修改后，函数可以接收多个参数
        :param age:
        :param gender:
        :param job:
        :param wage:
        :param abnormal:
        :param abnormal_state:
        :return:
        '''
        jobMap = \
            {
                0: '农、林、牧、渔', 1: '采矿', 2: '制造', 3: '电力、热力、燃气及水产和供应', 4: '建筑', 5: '批发和零售', 6: '交通运输、仓储和邮政', 7: '住宿和餐',
                8: '信息传输、软件和信息技术服务', 9: '金融', 10: '房地产', 11: '租凭和商务服务', 12: '科学研究和技术服务', 13: '水利、环境和公共设施管理',
                14: '居民服务、修理和其他服务', 15: '教育', 16: '卫生和社会工', 17: '文化、体育和娱乐', 18: '公共管理、社会保障和社会'
            }
        if age is None:
            age = UserService.createAge()
        if job is None:
            job = UserService.createJob()
        if gender is None:
            gender = UserService.createGender()
        if wage is None:
            wage = UserService.createWage(job, age, gender)
        if abnormal is None:
            abnormal = 0
        if abnormal_state is None:
            abnormal_state = {"赌博违规交易": 0, "伪冒注册欺诈": 0,"信用卡违规套现":0, "黄牛营销欺诈":0, "商户违规":0, "异常转账":0}
            # abnormal_state = json.dumps(abnormal_state)
        if user_no is None:
            user_no = ''.join(random.sample('zyxwvu0123456789tsrqponmlkjihgfedcba', 13))
        place = random.choice(["0001", "0002", "0003"])
        user = User(age, gender, jobMap[job], wage, abnormal=abnormal, abnormal_state=abnormal_state,
                    user_no=user_no, loc_id=place)
        return user

    # 获取性别
    # 0:女 1:男
    @staticmethod
    def createGender():
        return random.randint(0, 1)

    # 获取用户年龄
    @staticmethod
    def createAge():
        # 18 - 23：6.5 %
        # 24 - 29：7.5 %
        # 30 - 39：17 %
        # 40 - 49：23 %
        # 50 - 59：22 %
        # 60 - 65：7 %
        # 大于66：17 %

        # 累加概率列表
        ageProportion = [0.065, 0.14, 0.31, 0.54, 0.76, 0.83, 1]
        r = random.random()
        ageIndex = -1
        for i in range(ageProportion.__len__()):
            if r < ageProportion[i]:
                ageIndex = i
                break
        if ageIndex == 0:
            return random.randint(18, 23)
        elif ageIndex == 1:
            return random.randint(24, 29)
        elif ageIndex == 2:
            return random.randint(30, 39)
        elif ageIndex == 3:
            return random.randint(40, 49)
        elif ageIndex == 4:
            return random.randint(50, 59)
        elif ageIndex == 5:
            return random.randint(60, 65)
        elif ageIndex == 6:
            return random.randint(66, 100)
        else:
            raise AttributeError("ageIndex值错误")

    # 获取用户职业
    @staticmethod
    def createJob():
        # 各职业所占比例表
        # 农、林、牧、渔业                  0.039143409
        # 采矿业                           0.044672635
        # 制造业                           0.281727225
        # 电力、热力、燃气及水产和供应业      0.026241882
        # 建筑业                           0.081270844
        # 批发和零售业                      0.047744427
        # 交通运输、仓储和邮政业             0.053800246
        # 住宿和餐饮                        0.015885554
        # 信息传输、软件和信息技术服务业      0.011409514
        # 金融业                           0.031507811
        # 房地产业                         0.012813762
        # 租凭和商务服务业                  0.019132877
        # 科学研究和技术服务业              0.019922766
        # 水利、环境和公共设施管理业         0.015797788
        # 居民服务、修理和其他服务业         0.004651571
        # 教育                            0.130156223
        # 卫生和社会工作                   0.044584869
        # 文化、体育和娱乐业                0.01070739
        # 公共管理、社会保障和社会组织       0.108829208

        jobProportion = [
            0.039143409,
            0.044672635,
            0.281727225,
            0.026241882,
            0.081270844,
            0.047744427,
            0.053800246,
            0.015885554,
            0.011409514,
            0.031507811,
            0.012813762,
            0.019132877,
            0.019922766,
            0.015797788,
            0.004651571,
            0.130156223,
            0.044584869,
            0.01070739,
            0.108829208
        ]
        # 转换为递增区间
        jobProportion_ = [0.039143409, 0.083816044, 0.365543269, 0.391785151, 0.473055995, 0.520800422, 0.574600668,
                          0.590486222, 0.601895736, 0.633403547, 0.646217309, 0.665350186, 0.6852729519999999,
                          0.7010707399999999, 0.7057223109999999, 0.8358785339999999, 0.8804634029999999,
                          0.8911707929999999, 1.0000000009999999]
        # cur = 0.0
        # for i in range(len(jobProportion)):
        #     cur += jobProportion[i]
        #     jobProportion_.append(cur)

        # 随机生成[0，1]的数
        r = random.random()
        for i in range(len(jobProportion_)):
            if r < jobProportion_[i]:
                return i
        return 0

    # 根据工作、年龄、性别等获取工资
    # 性别暂时可以不提供
    @staticmethod
    def createWage(job, age, gender):

        # 工资在平均工资上下浮动的比率
        floatRate = 0.5

        # 退休年龄 最小年龄
        maxAge, minAge = 60, 22

        # 男女最大年龄不同
        if gender == 1:
            maxAge = 55

        # 平均工资表
        wages = [
            48540,
            96674,
            82783,
            116728,
            69986,
            96521,
            100642,
            48833,
            177544,
            133390,
            83807,
            92924,
            139851,
            63914,
            60722,
            106474,
            115449,
            112081,
            104487,
        ]
        # 年龄过大过小均无工资
        if age > maxAge or age < minAge:
            return 0

        # 正常年龄  按照职业平均工资上下浮动返回工资
        r = random.uniform(-floatRate, floatRate)
        wage = int(wages[job] * (1 + r))
        wage -= wage % 100
        return wage