# -*- coding: utf-8 -*-
"""
  Author: LiangJing
   Time : 2023/5/14
    File: EnterpriseDao.py
"""

import json
import sys

from src.utils.config import get_mysql_connection
from src.dataGen20220414.entity.Enterprise import Enterprise


class EnterpriseDao():

    # 创建enterprise数据库表
    def createEnterpriseTable(self):
        '''
        创建enterprise表
        :return:
        '''
        sql = """
                CREATE TABLE `enterprise`  (
                    `id` int(0) not null auto_increment comment 'id主键',
                    `socialId` varchar(20) null default null comment '',
                    `name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '' ,
                    `registerId` varchar(20) null default null comment '',
                    `represent` varchar(20) null default null comment '',
                    `type` varchar(20) null default null comment '',
                    `builtTime` varchar(10) null default null comment '',
                    `regAmount` varchar(20) null default null comment '',
                    `checkTime` varchar(10) null default null comment '',
                    `regLocate` varchar(20) null default null comment '',
                    `state` varchar(10) null default null comment '',
                    `locate` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '' ,
                    `busScope` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '' ,
                    PRIMARY KEY (`id`) USING BTREE
                ) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;
                """
        try:
            db = get_mysql_connection()
            cursor = db.cursor()
            cursor.execute('DROP TABLE IF EXISTS `enterprise`;')
            cursor.execute(sql)
        except Exception as result:
            print("createUserTable:", result)
            db.close()
            sys.exit()
        finally:
            db.close()

    # 将enterpriseList插入到数据库enterprise表中
    def insertEnterprises(self, enterpriseList):
        try:
            db = get_mysql_connection()
            cursor = db.cursor()
            for enterprise in enterpriseList:
                socialId = enterprise.getSocialId()
                name = enterprise.getName()
                registerId = enterprise.getRegisterId()
                represent = enterprise.getRepresent()
                type = enterprise.getType()
                builtTime = enterprise.getBuiltTime()
                regAmount = enterprise.getRegAmount()
                checkTime = enterprise.getCheckTime()
                regLocate = enterprise.getRegLocate()
                state = enterprise.getState()
                locate = enterprise.getLocate()
                busScope = enterprise.getBusScope()
                sql = """
                                insert into enterprise(id,socialId, name, registerId, represent, type, builtTime, regAmount,
                                checkTime, regLocate,state,locate,busScope)
                                values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                """
                item = [None, socialId, name, registerId, represent, type, builtTime, regAmount,
                        checkTime, regLocate, state, locate, busScope]
                print(item)

                cursor.execute(sql, item)
                db.commit()
        except Exception as result:
            print(result)
            db.close()
            sys.exit()
        finally:
            db.close()


    def selectEnterprises(self):
        sql_select = """
            select id, socialId, name, registerId, represent, type, builtTime, regAmount, checkTime, regLocate, state,locate, busScope
            from enterprise"""

        db = get_mysql_connection()
        cursor = db.cursor()
        cursor.execute(sql_select)
        select_res = cursor.fetchall()
        return select_res