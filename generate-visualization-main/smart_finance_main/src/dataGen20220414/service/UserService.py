import json
import random

from src.dataGen20220414.dao.UserDao import UserDao
from src.dataGen20220414.entity.User import User

class UserService():
    def __init__(self, scene):

        self.userDao = UserDao()

        self.table_names = {"Scalper_marketing": 'marketing_user', "Credit_card_fraud": 'credit_user', "Abnormal_transfer": 'abnormal_user', "Fake_registration": 'register_user', "Gambling_violation": 'gambling_user',
                        "Merchant_violation": 'store_user'}
        self.scene = self.table_names[scene]
    def createUserTable(self):
        # for name in self.table_names.values():
        self.userDao.createUserTable(self.scene)

    def insertUsers(self,userList):
        self.userDao.insertUsers(userList, self.scene)

    def selectUsers(self):
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
        normal_user = self.userDao.selectNormalUser(self.scene)
        random.shuffle(normal_user)
        fraud_user = normal_user[0:quantity]

        normal_user = normal_user[quantity:]

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

    @staticmethod
    def createUser(age=None, gender=None, job=None, wage=None, abnormal=None, abnormal_state=None, user_no=None):
        jobMap = \
            {
                0: 'Agriculture,Forestry,Animal_husbandry,Fishery', 1: 'Mining', 2: 'Manufacturing', 3: 'Electricity,Heat,Gas,Water_production_and_supply', 4: 'Construction', 5: 'Wholesale_and_retail', 6: 'Transportation,Warehousing,Postal', 7: 'Accommodation_and_catering',
                8: 'Information_transmission,Software,Information_technology_services', 9: 'Financial', 10: 'Real_estate', 11: 'Rental_and_business_services', 12: 'Scientific_research_and_technical_services', 13: 'Water_conservancy,Environment,Public_facilities_management',
                14: 'Residential_services,Repair,Other_service', 15: 'Education', 16: 'Health_and_social_work', 17: 'Culture,Sports,Entertainment', 18: 'Public_administration,Social_security,Social'
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
            abnormal_state = {"Gambling_violation": 0, "Fake_registration": 0,"Credit_card_fraud":0, "Scalper_marketing":0, "Merchant_violation":0, "Abnormal_transfer":0}
            # abnormal_state = json.dumps(abnormal_state)
        if user_no is None:
            user_no = ''.join(random.sample('zyxwvu0123456789tsrqponmlkjihgfedcba', 13))
        place = random.choice(["0001", "0002", "0003"])
        user = User(age, gender, jobMap[job], wage, abnormal=abnormal, abnormal_state=abnormal_state,
                    user_no=user_no, loc_id=place)
        return user

    @staticmethod
    def createGender():
        return random.randint(0, 1)

    @staticmethod
    def createAge():
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
            raise AttributeError("ageIndex value is incorrect")

    @staticmethod
    def createJob():
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
        jobProportion_ = [0.039143409, 0.083816044, 0.365543269, 0.391785151, 0.473055995, 0.520800422, 0.574600668,
                          0.590486222, 0.601895736, 0.633403547, 0.646217309, 0.665350186, 0.6852729519999999,
                          0.7010707399999999, 0.7057223109999999, 0.8358785339999999, 0.8804634029999999,
                          0.8911707929999999, 1.0000000009999999]
        # cur = 0.0
        # for i in range(len(jobProportion)):
        #     cur += jobProportion[i]
        #     jobProportion_.append(cur)

        r = random.random()
        for i in range(len(jobProportion_)):
            if r < jobProportion_[i]:
                return i
        return 0

    @staticmethod
    def createWage(job, age, gender):
        floatRate = 0.5

        maxAge, minAge = 60, 22

        if gender == 1:
            maxAge = 55

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
        if age > maxAge or age < minAge:
            return 0

        r = random.uniform(-floatRate, floatRate)
        wage = int(wages[job] * (1 + r))
        wage -= wage % 100
        return wage