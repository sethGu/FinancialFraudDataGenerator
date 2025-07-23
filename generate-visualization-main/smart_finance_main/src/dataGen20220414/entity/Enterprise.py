# -*- coding: utf-8 -*-
"""
  Author: LiangJing
   Time : 2023/5/14
    File: Enterprise.py
"""


class Enterprise:

    def __init__(self, id='',socialId='', name='', registerId='', represent='', type='', builtTime='', regAmount='',
                 checkTime='', regLocate='', state='存续', locate='', busScope=''):
        self.id = id
        self.socialId = socialId
        self.name = name
        self.registerId = registerId
        self.represent = represent
        self.type = type
        self.builtTime = builtTime
        self.regAmount = regAmount
        self.checkTime = checkTime
        self.regLocate = regLocate
        self.state = state
        self.locate = locate
        self.busScope = busScope

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setSocialId(self, socialId):
        self.socialId = socialId

    def getSocialId(self):
        return self.socialId

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setRegisterId(self, registerId):
        self.registerId = registerId

    def getRegisterId(self):
        return self.registerId

    def setRepresent(self, represent):
        self.represent = represent

    def getRepresent(self):
        return self.represent

    def setType(self, type):
        self.type = type

    def getType(self):
        return self.type

    def setBuiltTime(self, builtTime):
        self.builtTime = builtTime

    def getBuiltTime(self):
        return self.builtTime

    def setRegAmount(self, regAmount):
        self.regAmount = regAmount

    def getRegAmount(self):
        return self.regAmount

    def setCheckTime(self, checkTime):
        self.checkTime = checkTime

    def getCheckTime(self):
        return self.checkTime

    def setRegLocate(self, regLocate):
        self.regLocate = regLocate

    def getRegLocate(self):
        return self.regLocate

    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state

    def setLocate(self, locate):
        self.locate = locate

    def getLocate(self):
        return self.locate

    def setBusScope(self, busScope):
        self.busScope = busScope

    def getBusScope(self):
        return self.busScope
