# -*- coding:utf-8 -*-
# @Time     :2022/3/15 11:42
# @Author   :Guo Jiayu
import json
import random
import sys

from src.dataGen20220414.dao.UserDao import UserDao
from src.dataGen20220414.service.UserService import UserService
from src.utils.config import get_mysql_connection


class UserFactory:
    def __init__(self, scene):
        self.userService = UserService(scene)

    def createUserTable(self):
        self.userService.createUserTable()

    def createUsers(self, n):
        userList = []
        for i in range(n):
            user = UserService.createUser()
            userList.append(user)
            # print(user.get_user_info())
        self.userService.insertUsers(userList)


