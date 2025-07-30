class Relative:
    id = -1
    male = -1
    age = -1
    childList = None
    fId = -1
    mId = -1
    coupleId = -1

    def __init__(self,id,male,age,childList=None,fId=-1,mId=-1,coupleId=-1):
        self.id = id
        self.male = male
        self.age = age
        self.childList = childList if childList != None else []
        self.fId = fId
        self.mId = mId
        self.coupleId = coupleId