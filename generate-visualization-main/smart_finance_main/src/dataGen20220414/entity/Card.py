class Card:
    card_id = 0             #Card number
    owner_type = ''          #Owner type
    owner_id = 0             #Owner ID number:User：0、1、2、3。。。Merchant:0、1、2、3。。。
    C4 = ''
    C5 = ''
    C6 = ''
    C7 = ''
    C8 = ''
    C9 = ''
    C10 = ''
    C11 = ''
    abnormal = 0
    abnormal_state = {}

    def __init__(self, card_id, owner_type, owner_id, C4, C5, C6, C7, C8,C9,C10,C11, abnormal=0, abnormal_state= {"Gambling_violation": 0, "Fake_registration": 0,"Credit_card_fraud":0, "Scalper_marketing":0, "Merchant_violation":0,"Abnormal_transfer":0}):
        self.card_id = card_id
        self.owner_type = owner_type
        self.owner_id = owner_id
        self.C4 = C4
        self.C5 = C5
        self.C6 = C6
        self.C7 = C7
        self.C8 = C8
        self.C9 = C9
        self.C10 = C10
        self.C11 = C11
        self.abnormal = abnormal
        self.abnormal_state = abnormal_state

    #set
    def setcard_id(self, card_id):
        self.card_id = card_id

    def setowner_type(self, owner_type):
        self.owner_type = owner_type

    def setowner_id(self, owner_id):
        self.owner_id = owner_id

    def setC4(self, C4):
        self.C4 = C4

    def setC5(self, C5):
        self.C5 = C5

    def setC6(self, C6):
        self.C6 = C6

    def setC7(self, C7):
        self.C7 = C7

    def setC8(self, C8):
        self.C8 = C8

    def setC9(self,C9):
        self.C9 = C9

    def setC10(self,C10):
        self.C10 = C10

    def setC11(self,C11):
        self.C11 = C11

    def setAbnormal(self, abnormal):
        self.abnormal = abnormal

    def setAbnormal_state(self, abnormal_state):
        self.abnormal_state = abnormal_state

    #get
    def getcard_id(self):
        return self.card_id

    def getowner_type(self):
        return self.owner_type

    def getowner_id(self):
        return self.owner_id

    def getC4(self):
        return self.C4

    def getC5(self):
        return self.C5

    def getC6(self):
        return self.C6

    def getC7(self):
        return self.C7

    def getC8(self):
        return self.C8

    def getC9(self):
        return self.C9

    def getC10(self):
        return self.C10

    def getC11(self):
        return self.C11

    def getAbnormal(self):
        return self.abnormal

    def getAbnormal_state(self):
        return self.abnormal_state

    def get_card_info(self):
        return {"card_id" : self.getcard_id(),"owner_type": self.getowner_type().__str__()  , "owner_id": self.getowner_id(), "C4": self.C4().__str__() ,
               "C5" : self.getC5().__str__() , "C6" : self.getC6().__str__()  , "C7": self.getC7().__str__() ,"C8": self.getC8().__str__(), "C9":self.getC9(),"C10":self.getC10(),"C11":self.getC11(),"abnormal":self.getAbnormal(), "abnormal_state":self.getAbnormal_state() }

    def __str__(self):
        return "Card：[" + self.getcard_id() + "owner_type：" + self.getowner_type().__str__() + "owner_id：" + self.getowner_id() + "C4：" + self.getC4().__str__() +\
               "C5：" + self.getC5().__str__() + "C6：" + self.getC6().__str__()  + "C7：" + self.getC7().__str__() + "C8：" + self.getC8().__str__() + "C9:"+self.getC9().__str__() + "C10:" + self.getC10().__str__() + "C11:" + self.getC11().__str__() + self.getAbnormal_state()   + "]"
