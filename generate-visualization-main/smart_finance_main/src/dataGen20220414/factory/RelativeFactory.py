import random
from src.dataGen20220414.entity.Relative import Relative
from src.dataGen20220414.service.RelativeService import RelativeService
from src.dataGen20220414.service.UserService import UserService


def from_distributin_to_one_anser(kx, glfb):
    sum = [0 for i in range(len(glfb))]
    sum[0] = glfb[0]
    for i in range(1, len(glfb)):
        sum[i] = sum[i - 1] + glfb[i]
    a = random.random()
    for i in range(len(sum)):
        if i <= sum[i]:
            return kx[i]


class RelativeFactory:
    waitToBeParent = []
    waitToBeChild = []
    personDic = {}
    ageInterval = {}

    def __init__(self, scene):
        self.relativeService = RelativeService(scene)
        self.userService = UserService(scene)

    def createRelative(self):
        self.initVal()
        self.createCoupleEdge()
        self.createParentAndChildEdge(30, 0.7)
        return self.personDic

    def initVal(self):
        human_list = self.userService.selectUsers()
        # for item in res_list:
        #     id,age,gender,job,wage,card, abnormal, abnormal_state, user_no, loc_id= item
        #     # print(item)
        #     user = User(id = id ,age = age, gender=gender,job=job, wage= wage,
        #                 card= card, abnormal = abnormal, abnormal_state = abnormal_state,
        #                 user_no = user_no)
        #     human_list.append(user)
        for human in human_list:
            id , age, gender ,job  = human.getId(), human.getAge(),human.getGender(), human.getJob()
            person = Relative(id, gender, age)
            self.waitToBeParent.append(id)
            self.waitToBeChild.append(id)
            self.personDic[id] = person

        for i in range(0,101,10):
            start = i
            end = start + 10
            age_range = str(start) + "-" + str(end)
            self.ageInterval[age_range]=[]

        for id, person in self.personDic.items():
            age = person.age
            start = (age // 10) * 10
            end = start + 10
            age_range = str(start) + "-" + str(end)
            self.ageInterval[age_range].append(id)

    def createCoupleEdge(self):
        age_married_rate_map = {"20-30": 0.1, "30-40": 0.2, "40-50": 0.15, "50-60": 0.2, "60-70": 0.15,
                                "70-80": 0.15,
                                "80-90": 0.25, "90-100": 0.2,"100-110" : 0}

        age_gap = ["-5~-3", "-3~0", "0~3", "3~5", "5-7"]
        age_gap_distribution = [0.1, 0.1, 0.3, 0.3, 0.2]

        for key, value in self.ageInterval.items():
            if key in ["0-10", "10-20"]:
                continue
            married_rate = age_married_rate_map[key]
            temp_list = value
            random.shuffle(temp_list)
            ma_ls = []
            ma_ls = random.sample(temp_list, int(len(temp_list) * married_rate))
            for mar_per_id in ma_ls:
                mar_per_age, mar_per_gender, mar_per_coupleId= self.personDic[mar_per_id].age, self.personDic[
                    mar_per_id].male, self.personDic[mar_per_id].coupleId
                if mar_per_coupleId != -1:
                    continue

                candidate_list = []

                nlc = from_distributin_to_one_anser(age_gap, age_gap_distribution)
                # print("nlc=",nlc)
                ls = nlc.strip("\"").strip("\'").split("~")
                zb = int(ls[0]);
                yb = int(ls[1])
                can_nl = []
                for i in range(zb, yb + 1):
                    can_nl.append(i)
                jtnlc = random.choice(can_nl)
                if mar_per_gender == 0:
                    target_age = mar_per_age + jtnlc
                else:
                    target_age = mar_per_age - jtnlc
                if target_age > 99:
                    continue
                st_age = (target_age // 10) * 10
                ed_age = st_age + 10
                age_range = str(st_age) + "-" + str(ed_age)
                # print("age_range=",age_range)
                candidate_list.extend(self.ageInterval[age_range])
                # print("candidate_list=",candidate_list)

                find = False
                cnt = 0
                while find == False:
                    can_id = random.choice(candidate_list)
                    can_gend, can_age, can_coupleid  = self.personDic[can_id].male, self.personDic[can_id].age, \
                                                      self.personDic[can_id].coupleId
                    cnt += 1
                    if cnt == 20:
                        break
                    if can_coupleid == -1 and (
                            (mar_per_gender == 1 and can_gend == 0) or (
                            mar_per_gender == 0 and can_gend == 1)) and (
                            can_age == target_age ) :
                            # and (can_job in target_job )
                        self.personDic[mar_per_id].coupleId = can_id
                        self.personDic[can_id].coupleId = mar_per_id
                        find = True

    def createParentAndChildEdge(self, childInterval, dinkPercent):
        startAge = 90
        while startAge >= childInterval:
            endAge = startAge + 10
            sourceInterval = str(startAge) + '-' + str(endAge)
            parentList = self.ageInterval[sourceInterval]
            for parent in parentList:
                if parent not in self.waitToBeParent:
                    continue
                parentCouple = self.personDic[parent].coupleId
                ageM = self.personDic[parent].age

                if parentCouple != -1:
                    ageM = self.personDic[parent].age if self.personDic[parent].male == 0 else self.personDic[
                        parentCouple].age
                ageM = ageM - ageM % 10
                targetMin = ageM - childInterval
                targetMax = ageM - 20
                kidList = []
                while targetMin + 10 <= targetMax:
                    if self.ageInterval[str(targetMin) + '-' + str(targetMin + 10)]:
                        kidList.extend(self.ageInterval[str(targetMin) + '-' + str(targetMin + 10)])
                    targetMin = targetMin + 10
                while random.randint(0, 100) >= dinkPercent * 100:
                    while len(kidList) > 0:
                        if kidList[0] not in self.waitToBeChild:
                            kidList.remove(kidList[0])
                            continue
                        self.personDic[parent].childList.append(kidList[0])
                        if self.personDic[parent].male == 1:
                            self.personDic[kidList[0]].fId = parent
                            if parentCouple != -1:
                                self.personDic[kidList[0]].mId = parentCouple
                        else:
                            self.personDic[kidList[0]].mId = parent
                            if parentCouple != -1:
                                self.personDic[kidList[0]].fId = parentCouple
                        self.waitToBeChild.remove(kidList[0])
                        kidList.remove(kidList[0])
                        break
                self.waitToBeParent.remove(parent)
            startAge = startAge - 10

    def createRelativeTable(self):
        self.relativeService.createRelativeTable()

    def insertRelative(self):
        self.relativeService.addRelative(self.personDic)

#
# if __name__ == '__main__':
#     rf = RelativeFactory()
#     rf.initVal()
#     rf.createCoupleEdge()
#     for id, person in rf.personDic.items():
#         a = person.coupleId
#         pd = rf.personDic
#         if a != -1:
#             b = pd[a].coupleId
#             print( id,a )
#             if ( b != id ):
#                 print("error")
