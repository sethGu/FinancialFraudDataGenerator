# -*- coding: utf-8 -*-
"""
  Author: LiangJing
   Time : 2023/5/15
    File: enterprise_export_csv.py
"""

from src.dataGen20220414.service.EnterpriseService import EnterpriseService
from pandas import DataFrame

def get_enterprises(path, filename="enterprise.csv"):
    DataFrame().to_csv(path + filename, index=False, encoding='gb18030') #lcf
    enterpriseService = EnterpriseService()
    enterpriseList = enterpriseService.selectEnterprises()
    first = True
    for enterprise in enterpriseList:
        data = {
            'id': [str(enterprise.id)+'\t'],
            'socialId': [str(enterprise.socialId) + '\t'],
            'name': [str(enterprise.name) + '\t'],
            'registerId': [str(enterprise.registerId) + '\t'],
            'represent': [str(enterprise.represent) + '\t'],
            'type': [str(enterprise.type) + '\t'],
            'builtTime': [str(enterprise.builtTime) + '\t'],
            'regAmount': [str(enterprise.regAmount) + '\t'],
            'checkTime': [str(enterprise.checkTime) + '\t'],
            'regLocate': [str(enterprise.regLocate) + '\t'],
            'state': [str(enterprise.state) + '\t'],
            'locate': [str(enterprise.locate) + '\t'],
            'busScope': [str(enterprise.busScope) + '\t'],

        }
        df = DataFrame(data, columns=["id", "socialId", "name", "registerId", "represent", "type", "builtTime", "regAmount", "checkTime", "regLocate",
                             "state", "locate", "busScope"])
        # df.to_csv (path + filename, mode="a" ,index = False, header=first,encoding='gb18030')
        df.to_csv(path + filename, mode="a", index=False, header=first, encoding='gb18030')
        first = False

def out_put(path = '../../datas/工商企业/'):
    get_enterprises(path)
if __name__ == '__main__':
    out_put(path = '../../datas')