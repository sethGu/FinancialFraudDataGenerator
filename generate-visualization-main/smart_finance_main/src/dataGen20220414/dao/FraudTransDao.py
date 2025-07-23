# -*- coding:utf-8 -*-
# @Time     :2022/6/24 15:40
# @Author   :Guo Jiayu
import sys

from src.utils.config import get_mysql_connection


class FraudTransDao:
    def __init__(self):
        pass

    def createFraudTransTable(self, table_name):
        sql = """
            create table """ + table_name + """(
                id int(0) not null auto_increment comment 'id主键',
                F1 varchar(26) null default null comment '',
                F2 varchar(100) null default null comment '',
                F3 varchar(11) null default null comment '',
                F4 varchar(11) null default null comment '',
                F5 varchar (12) null default null comment '',
                F6 varchar(10) null default null comment '',
                F7 varchar(10) null default null comment '',
                F8 varchar(4) null default null comment '',
                F9 varchar(5) null default null comment '',
                F10 decimal(12,2) null default null comment '',
                F11 decimal(12,2) null default null comment '',
                F12 varchar(20) null default null comment '',
                F13 varchar(20) null default null comment '',
                F14 varchar(20) null default null comment '',
                F15 varchar(10) null default null comment '',
                F16 varchar(10) null default null comment '',
                F17 varchar(20) null default null comment '',
                F18 varchar(100) null default null comment '',
                F19 varchar(10) null default null comment '',
                F20 varchar(10) null default null comment '',
                F21 varchar(10) null default null comment '',
                F22 varchar(10) null default null comment '',
                F23 varchar(2) null default null comment '',
                F24 varchar(5) null default null comment '',
                F25 varchar(8) null default null comment '',
                F26 varchar(10) null default null comment '',
                F27 varchar(5) null default null comment '',
                F28 varchar(8) null default null comment '',
                F29 varchar(11) null default null comment '',
                F30 varchar(10) null default null comment '',
                F31 timestamp null default null comment '',
                F32 timestamp null default null comment '',
                F33 varchar(10) null default null comment '',
                F34 varchar(5) null default null comment '',
                F35 decimal(12,2) null default null comment '',
                F36 varchar(4) null default null comment '',
                F37 decimal(12,2) null default null comment '',
                F38 decimal(12,2) null default null comment '',
                F39 varchar(20) null default null comment '',
                F40 varchar(20) null default null comment '',
                F41 varchar(20) null default null comment '',
                F42 varchar(20) null default null comment '',
                F43 varchar(50) null default null comment '',
                F44 decimal(12,2) null default null comment '',
                F45 varchar(10) null default null comment '',
                
                

                PRIMARY KEY (`id`) USING BTREE
            ) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;
            """
        try:
            db = get_mysql_connection()
            cursor = db.cursor()
            s = """DROP TABLE IF EXISTS `""" + table_name + """`;"""
            cursor.execute(s)
            cursor.execute(sql)
        except Exception as result:
            print("createTransTable:", result)
            sys.exit()
        finally:
            db.close()

    def insertFraudTrans(self, fraudTrans, table_name):
        db = get_mysql_connection()
        cursor = db.cursor()
        F1 = fraudTrans.F1
        F2 = fraudTrans.F2
        F3 = fraudTrans.F3
        F4 = fraudTrans.F4
        F5 = fraudTrans.F5
        F6 = fraudTrans.F6
        F7 = fraudTrans.F7
        F8 = fraudTrans.F8
        F9 = fraudTrans.F9
        F10 = fraudTrans.F10
        F11 = fraudTrans.F11
        F12 = fraudTrans.F12
        F13 = fraudTrans.F13
        F14 = fraudTrans.F14
        F15 = fraudTrans.F15
        F16 = fraudTrans.F16
        F17 = fraudTrans.F17
        F18 = fraudTrans.F18
        F19 = fraudTrans.F19
        F20 = fraudTrans.F20
        F21 = fraudTrans.F21
        F22 = fraudTrans.F22
        F23 = fraudTrans.F23
        F24 = fraudTrans.F24
        F25 = fraudTrans.F25
        F26 = fraudTrans.F26
        F27 = fraudTrans.F27
        F28 = fraudTrans.F28
        F29 = fraudTrans.F29
        F30 = fraudTrans.F30
        F31 = fraudTrans.F31
        F32 = fraudTrans.F32
        F33 = fraudTrans.F33
        F34 = fraudTrans.F34
        F35 = fraudTrans.F35
        F36 = fraudTrans.F36
        F37 = fraudTrans.F37
        F38 = fraudTrans.F38
        F39 = fraudTrans.F39
        F40 = fraudTrans.F40
        F41 = fraudTrans.F41
        F42 = fraudTrans.F42
        F43 = fraudTrans.F43
        F44 = fraudTrans.F44
        F45 = fraudTrans.F45

        sql = """
            insert into """ + table_name + """(id,F1, F2, F3, F4, F5,
                 F6, F7, F8, F9, F10, F11, F12, F13,
                 F14, F15, F16, F17, F18, F19, F20, F21,
                 F22, F23, F24, F25, F26, F27, F28, F29,
                 F30, F31, F32, F33, F34, F35, F36, F37,
                 F38, F39, F40, F41, F42, F43,
                 F44, F45)
            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        item = [None, F1, F2, F3, F4, F5,
                 F6, F7, F8, F9, F10, F11, F12, F13,
                 F14, F15, F16, F17, F18, F19, F20, F21,
                 F22, F23, F24, F25, F26, F27, F28, F29,
                 F30, F31, F32, F33, F34, F35, F36, F37,
                 F38, F39, F40, F41, F42, F43,
                 F44, F45]
        cursor.execute(sql, item)
        db.commit()

    def selectFraudTrans(self, table_name):
        sql_select = """
            select id,F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, F13, F14, F15, F16, F17, F18, F19, F20, F21, F22, F23, F24, F25, F26, F27, F28, F29, F30, F31, F32, F33, F34, F35, F36, F37, F38, F39, F40, F41, F42, F43, F44, F45
            from 
            """ + table_name
        db = get_mysql_connection()
        cursor = db.cursor()
        cursor.execute(sql_select)
        select_res = cursor.fetchall()
        return select_res