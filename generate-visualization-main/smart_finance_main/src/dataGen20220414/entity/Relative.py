class Relative:
    # id和user的id相同
    id = -1
    # 性别  0为女，1为男
    male = -1
    # 年龄
    age = -1
    # 孩子集合
    childList = None
    # 父亲和母亲id
    fId = -1
    mId = -1
    # 对象id
    coupleId = -1

    def __init__(self,id,male,age,childList=None,fId=-1,mId=-1,coupleId=-1):
        self.id = id
        self.male = male
        self.age = age
        self.childList = childList if childList != None else []
        self.fId = fId
        self.mId = mId
        self.coupleId = coupleId