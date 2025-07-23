class User:
    job = ''

    age = -1

    wage = -1

    # 0:女 1:男
    gender = -1

    abnormal = 0

    abnormal_state = {}

    # 4位地区字段
    loc_id = ''

    def __init__(self, age, gender, job, wage, id=-1, card=[], abnormal=0,
                 abnormal_state={"赌博违规交易": 0, "伪冒注册欺诈": 0,"信用卡违规套现":0, "黄牛营销欺诈":0, "商户违规":0,"异常转账":0}, user_no=None, loc_id = ''):
        self.id = id
        self.age = age
        self.gender = gender
        self.job = job
        self.wage = wage
        self.card = card
        self.abnormal = abnormal
        self.abnormal_state = abnormal_state
        self.user_no = user_no
        self.loc_id = loc_id

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setCard(self, card):
        self.card = card

    def getCard(self):
        return self.card

    def setJob(self, job):
        self.job = job

    def setAge(self, age):
        self.age = age

    def setWage(self, wage):
        self.wage = wage

    def setGender(self, gender):
        self.gender = gender

    def getJob(self):
        return self.job

    def getAge(self):
        return self.age

    def getWage(self):
        return self.wage

    def getGender(self):
        return self.gender

    def setAbnormal(self, abnormal):
        self.abnormal = abnormal

    def getAbnormal(self):
        return self.abnormal

    def setAbnormal_state(self, abnormal_state):  # 传入一个dict
        self.abnormal_state = abnormal_state

    def getAbnormal_state(self):
        return self.abnormal_state

    def get_user_info(self):
        return {'id': self.id, 'age': self.age, 'job': self.job, 'gender': self.gender, 'wage': self.wage,
                'cards': self.card, 'abnormal': self.abnormal, 'abnormal_state': self.abnormal_state,
                'user_no': self.user_no,'loc_id':self.loc_id}

    def get_user_no(self):
        return self.user_no

    def set_user_no(self, user_no):
        self.user_no = user_no

    def setLoc_id(self, loc_id):
        self.loc_id = loc_id

    def getLoc_id(self):
        return self.loc_id

    def __str__(self):
        return "User" + ":[" + \
               "性别:" + self.getGender().__str__() + \
               ", 年龄:" + self.getAge().__str__() + \
               ", 职业:" + self.getJob() + \
               ", 工资:" + self.getWage().__str__() + \
               ", 异常状态:" + self.abnormal_state + \
               ", 加密的用户号" + self.user_no + \
               ", 地区标识码" + self.loc_id + \
               "]"
