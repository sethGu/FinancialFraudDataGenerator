import random
from src.dataGen20220414.entity.Relative import Relative
from src.dataGen20220414.service.RelativeService import RelativeService
from src.dataGen20220414.service.UserService import UserService


def from_distributin_to_one_anser(kx, glfb):
    # 先求sum
    sum = [0 for i in range(len(glfb))]
    sum[0] = glfb[0]
    for i in range(1, len(glfb)):
        sum[i] = sum[i - 1] + glfb[i]
    a = random.random()
    for i in range(len(sum)):
        if i <= sum[i]:
            return kx[i]


class RelativeFactory:
    # 等待成为父母的集合，元素为person的id
    waitToBeParent = []
    # 等待成为孩子的集合，元素为person的id
    waitToBeChild = []
    # key为person的id，val为person对象
    personDic = {}
    # 年龄分层dic，key为年龄区间，val为id集合
    ageInterval = {}

    def __init__(self, scene):
        self.relativeService = RelativeService(scene)
        self.userService = UserService(scene)

    def createRelative(self):
        '''
        创建关系图
        :return: personDic
        '''
        self.initVal()
        self.createCoupleEdge()
        self.createParentAndChildEdge(30, 0.7)
        return self.personDic

    def initVal(self):
        '''
        # 通过查询数据库获取所有user，初始化waitToBeParent,waitToBeChild,personDic,ageInterval
        :return: None
        '''
        #从数据库读出user

        human_list = self.userService.selectUsers()
        # for item in res_list:
        #     id,age,gender,job,wage,card, abnormal, abnormal_state, user_no, loc_id= item
        #     # print(item)
        #     user = User(id = id ,age = age, gender=gender,job=job, wage= wage,
        #                 card= card, abnormal = abnormal, abnormal_state = abnormal_state,
        #                 user_no = user_no)
        #     human_list.append(user)
        # 由读出的human_list初始化本类中属性的一些列表和字典
        for human in human_list:  # 数据库：for i in range(len(数据库返回的human记录列表)): 每个是元组
            id , age, gender ,job  = human.getId(), human.getAge(),human.getGender(), human.getJob()
            person = Relative(id, gender, age)
            self.waitToBeParent.append(id)
            self.waitToBeChild.append(id)
            self.personDic[id] = person

        # 填写self.ageInterval字典
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
        '''
        # 根据ageInterval字典，选择并更新配偶，更新personDict
        :return: None
        '''
        age_married_rate_map = {"20-30": 0.1, "30-40": 0.2, "40-50": 0.15, "50-60": 0.2, "60-70": 0.15,
                                "70-80": 0.15,
                                "80-90": 0.25, "90-100": 0.2,"100-110" : 0}

        age_gap = ["-5~-3", "-3~0", "0~3", "3~5", "5-7"]  # 女生的正数就是男生比女生大几岁，负数就是男生比女生小几岁，这样加上这个数就行。男生相反，这样减去这个数就行
        age_gap_distribution = [0.1, 0.1, 0.3, 0.3, 0.2]

        for key, value in self.ageInterval.items():
            if key in ["0-10", "10-20"]:  # 只在20岁以上的各年龄段中的人选一些人结婚
                continue
            # 不同年龄段的人单身率不同，所以选出组成couple的人数也不同
            married_rate = age_married_rate_map[key]
            temp_list = value
            random.shuffle(temp_list)  # 打乱一下
            ma_ls = []
            ma_ls = random.sample(temp_list, int(len(temp_list) * married_rate))  # 把选出来要在这一个年龄段中让他结婚的人放在ma_ls中
            # print("要选出marry的人的list：", ma_ls)
            for mar_per_id in ma_ls:  # 为选出要结婚的配偶，得到mate_id
                mar_per_age, mar_per_gender, mar_per_coupleId= self.personDic[mar_per_id].age, self.personDic[
                    mar_per_id].male, self.personDic[mar_per_id].coupleId
                # print("这个人的id，age，gender:", mar_per_id,mar_per_age,mar_per_gender)
                if mar_per_coupleId != -1:  # 如果这个人已经不单身，不再为他选择配偶
                    continue

                # 形成candidate_mate的list
                candidate_list = []

                # 为了得到candidate_mate，先要计算年龄差
                nlc = from_distributin_to_one_anser(age_gap, age_gap_distribution)
                # print("nlc=",nlc)
                ls = nlc.strip("\"").strip("\'").split("~")
                # print("年龄差范围是",ls)
                zb = int(ls[0]);
                yb = int(ls[1])  # 这是年龄差的范围
                can_nl = []
                for i in range(zb, yb + 1):
                    can_nl.append(i)
                # print("可能的年龄差列表",can_nl)
                jtnlc = random.choice(can_nl)
                # print("具体年龄差",jtnlc)
                # 计算具体的target年龄
                if mar_per_gender == 0:  # 是女生，加上年龄差，否则减去
                    target_age = mar_per_age + jtnlc
                else:
                    target_age = mar_per_age - jtnlc
                if target_age > 99:
                    continue
                # 在目标年龄所在的年龄段之中寻找，这里后面可能要加上行业的限制
                # print("target age",target_age)
                st_age = (target_age // 10) * 10
                ed_age = st_age + 10
                age_range = str(st_age) + "-" + str(ed_age)
                # print("age_range=",age_range)
                candidate_list.extend(self.ageInterval[age_range])
                # print("candidate_list=",candidate_list)

                # 得到mate_id
                find = False
                cnt = 0
                while find == False:
                    can_id = random.choice(candidate_list)
                    can_gend, can_age, can_coupleid  = self.personDic[can_id].male, self.personDic[can_id].age, \
                                                      self.personDic[can_id].coupleId
                    cnt += 1
                    if cnt == 20:       #最多循环random20次，还找不到就不结了
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
        '''
        # 根据waitToBeParent和waitToBeChild和personDic，为personDic中的每个val更新childList，fId和mId属性
        :param childInterval:孩子和母亲的年龄最大间隔（最小间隔默认为20），必须为十的倍数
        :param dinkPercent: 丁克概率
        :return:
        '''
        startAge = 90
        while startAge >= childInterval:
            endAge = startAge + 10
            sourceInterval = str(startAge) + '-' + str(endAge)
            parentList = self.ageInterval[sourceInterval]
            for parent in parentList:
                # 首先得在备选家长中
                if parent not in self.waitToBeParent:
                    continue
                # 查找其配偶id
                parentCouple = self.personDic[parent].coupleId
                # 获取女方的年龄
                ageM = self.personDic[parent].age

                if parentCouple != -1:
                    ageM = self.personDic[parent].age if self.personDic[parent].male == 0 else self.personDic[
                        parentCouple].age
                ageM = ageM - ageM % 10
                # 获取孩子年龄区间
                targetMin = ageM - childInterval
                targetMax = ageM - 20
                kidList = []
                while targetMin + 10 <= targetMax:
                    if self.ageInterval[str(targetMin) + '-' + str(targetMin + 10)]:
                        kidList.extend(self.ageInterval[str(targetMin) + '-' + str(targetMin + 10)])
                    targetMin = targetMin + 10
                # 丁克的概率，反复循环判断以生成多个孩子
                while random.randint(0, 100) >= dinkPercent * 100:
                    # 得有孩子能够被选择
                    while len(kidList) > 0:
                        # 孩子得在备选孩子集合中
                        if kidList[0] not in self.waitToBeChild:
                            kidList.remove(kidList[0])
                            continue
                        # 构建parent和child的边
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
#         a = person.coupleId   #id 的couple是a
#         pd = rf.personDic
#         if a != -1:
#             b = pd[a].coupleId  #a 的couple是id
#             print( id,a )
#             if ( b != id ):
#                 print("error")
