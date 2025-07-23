# -*- coding: utf-8 -*-
"""
  Author: LiangJing
   Time : 2023/5/14
    File: EnterpriseFactory.py
"""

import json
import random
import sys

from src.dataGen20220414.dao.EnterpriseDao import EnterpriseDao
from src.dataGen20220414.service.EnterpriseService import EnterpriseService

from src.utils.config import get_mysql_connection


class EnterpriseFactory:
    def __init__(self):
        '''
        EnterpriseFactory负责创建Enterprise表和批量生成Enterprise
        '''
        self.enterpriseService = EnterpriseService()

    def createEnterpriseTable(self):
        '''
        创建Enterprise数据库表
        by梁静20230514
        :return:
        '''
        self.enterpriseService.createEnterpriseTable()

    def createEnterprise(self, n):
        '''
        批量生成Enterprise
        by梁静20230514
        :param n:要生成的企业数量
        :return:
        '''
        enterpriseList = []
        for i in range(n):
            enterprise = EnterpriseService.createEnterprise()
            enterpriseList.append(enterprise)
            # print(user.get_user_info())
        self.enterpriseService.insertEnterprises(enterpriseList)


