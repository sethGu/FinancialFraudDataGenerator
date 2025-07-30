from src.dataGen20220414.dao.RelativeDao import RelativeDao
from src.dataGen20220414.entity.Relative import Relative
from src.dataGen20220414.factory.UserFactory import UserFactory
import json


class RelativeService:
    def __init__(self, scene):
        self.relativeDao = RelativeDao()

        self.table_names = {"Scalper_marketing": 'marketing_relative', "Credit_card_fraud": 'credit_relative', "Abnormal_transfer": 'abnormal_relative',
                        "Fake_registration": 'register_relative', "Gambling_violation": 'gambling_relative',
                        "Merchant_violation": 'store_relative'}
        self.scene = self.table_names[scene]
    def createRelativeTable(self):
        self.relativeDao.createRelativeTable(self.scene)

    def addRelative(self, relativeDic):
        for relative in relativeDic.values():
            self.relativeDao.insertRelative(relative, self.scene)

    def getAllRelative(self):
        list = self.relativeDao.selectRelative(self.scene)
        relativeList = []
        for item in list:
            relative = Relative(item[1], item[2], item[3], json.loads(item[4]), item[5], item[6], item[7])
            relativeList.append(relative)
        return relativeList

    def getRelativeById(self, id):
        list = self.relativeDao.selectRelativeById(id, self.scene)
        if list == None:
            return list
        relative = Relative(list[1], list[2], list[3], json.loads(list[4]), list[5], list[6], list[7])
        return relative

    def getNearestNeighborsOfN(self, id, n):
        neighborsDic = {}
        visited = []
        queue = []
        queue2 = []
        queue.append(id)
        level = 0
        while len(queue) > 0 and level < n:
            curId = queue.pop(0)
            visited.append(curId)
            if level not in neighborsDic.keys():
                neighborsDic[level] = []
            neighborsDic[level].append(curId)
            curRelative = self.getRelativeById(curId)
            if curRelative.fId != -1 and curRelative.fId not in visited:
                queue2.append(curRelative.fId)
            if curRelative.mId != -1 and curRelative.mId not in visited:
                queue2.append(curRelative.mId)
            if curRelative.coupleId != -1 and curRelative.coupleId not in visited:
                queue2.append(curRelative.coupleId)
            for childId in curRelative.childList:
                if childId not in visited:
                    queue2.append(childId)
            if len(queue) == 0:
                queue[:] = queue2[:]
                queue2.clear()
                level = level + 1
        return neighborsDic