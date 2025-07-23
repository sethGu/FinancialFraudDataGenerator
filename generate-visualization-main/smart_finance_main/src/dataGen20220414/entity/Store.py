class Store:
    def __init__(self, store_id, industry, name, level, charge_duration,open_duration,
                 S1, S2,S3,S4,S5,S6,S7,S8,S9,S10,S11,S12,S13, S14, S15, S16,S17,S18,S19,S20,S21,S22,S23,S24,S25,S26,S27,S28,S29,S30,
                 abnormal=0,
                 abnormal_state={"赌博违规交易": 0, "伪冒注册欺诈": 0,"信用卡违规套现":0, "黄牛营销欺诈":0, "商户违规":0,"异常转账":0}
                ):

        self.store_id = store_id
        self.industry = industry
        self.level = level
        self.charge_duration = charge_duration
        self.open_duration = open_duration
        self.card_id = S18
        self.name = name
        self.S30 = S30
        self.abnormal = abnormal
        self.abnormal_state = abnormal_state
        self.S5 = S5
        self.S1 = S1
        self.S2 = S2
        self.S3 = S3
        self.S4 =  S4
        self.S6 = S6
        self.S7 = S7
        self.S8 = S8
        self.S9 = S9
        self.S10 = S10
        self.S11 = S11
        self.S12 = S12
        self.S13 = S13
        self.S14 = S14
        self.S15 = S15
        self.S16 = S16
        self.S17 = S17
        self.S18 = S18
        self.S19 = S19
        self.S20 = S20
        self.S21 = S21
        self.S22 = S22
        self.S23 = S23
        self.S24 = S24
        self.S25 = S25
        self.S26 = S26
        self.S27 = S27
        self.S28 = S28
        self.S29 = S29
    def setStore_id(self, store_id):
        self.store_id = store_id

    def setIndustry(self, industry):

        self.industry = industry

    def setLevel(self, level):

        self.level = level

    def setCharge_duration(self, charge_duration):
        self.charge_duration = charge_duration

    def setOpen_duration(self, open_duration):
        self.open_duration = open_duration

    def setCard_id(self, S18):
        self.S18 = S18

    def getStore_id(self):
        return self.store_id

    def getIndustry(self):
        return self.industry

    def getLevel(self):
        return self.level

    def getCharge_duration(self):
        return self.charge_duration

    def getOpen_duration(self):
        return self.open_duration
    def getCard_id(self):
        return self.card_id
    def getS18(self):
        return self.S18
    def getName(self):
        return self.name

    def getAbnormal(self):
        return self.abnormal

    def setAbnormal(self, abnormal):
        self.abnormal = abnormal

    def setAbnormal_state(self, abnormal_state):  # 传入一个dict
        self.abnormal_state = abnormal_state

    def getAbnormal_state(self):
        return self.abnormal_state

    def getCard_id(self):
        return self.S18

    def setS30(self, S30):
        self.S30 = S30

    def getS30(self):
        return self.S30

    def getS1(self):
        return self.S1
    def setS1(self, S1):
        self.S1 = S1
    def setS5(self,S5):
        self.S5 = S5
    def getS5(self):
        return self.S5
    def getS3(self):
        return  self.S3
    def getS4(self):
        return self.S4
    def getS6(self):
        return self.S6
    def getS7(self):
        return self.S7

    def getS8(self):
        return self.S8
    def getS9(self):
        return self.S9
    def getS10(self):
        return self.S10
    def getS11(self):
        return self.S11
    def getS12(self):
        return self.S12
    def getS13(self):
        return self.S13
    def getS14(self):
        return self.S14
    def getS15(self):
        return self.S15
    def getS16(self):
        return self.S16
    def getS17(self):
        return self.S17

    def get_store_info(self):
        return {"id" : self.getStore_id(),"industry": self.getIndustry()  , "name": self.name,"rank": self.getLevel() ,"consumption_range" : self.getCharge_duration() , "opening_hours" : self.getOpen_duration(),"S30":self.getS30(),"S1":self.S1,"S2":self.S2,"S3":self.S3,"S4":self.S4,"S5":self.S5,"S6":self.S6,"S7":self.S7,"S8":self.S8,"S9":self.S9,
                "S10":self.S10,"S11":self.S11,"S12":self.S12,"S13":self.S13,"S14":self.S14,"S15":self.S15,"S16":self.S16,"S17":self.S17,"S18":self.S18,"S19":self.S19,"S20":self.S20,"S21":self.S21,"S22":self.S22,"S23":self.S23,"S24":self.S24,"S25":self.S25,"S26":self.S26,"S27":self.S27,"S28":self.S28,"S29":self.S29}
