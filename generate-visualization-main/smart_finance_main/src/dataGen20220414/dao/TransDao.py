import sys
import json

from src.utils.config import get_mysql_connection


class TransDao():
    def __init__(self):
        pass

    def createTransTable(self, table_name):
        sql = """
            create table """ + table_name + """(
                id int(0) not null auto_increment comment 'id主键',
                T1 varchar(100) null default null comment '',
                T2 varchar(10) null default null comment '',
                T3 varchar(20) null default null comment '',
                T4 varchar(20) null default null comment '',
                T5 varchar(10) null default null comment '',
                T6 varchar(1) null default '0' comment '',
                T7 varchar(5) null default null comment '',
                T8 varchar(2) null default null comment '',
                T9 varchar(6) null default null comment '',
                T10 varchar(10) null default null comment '',
                T11 varchar(10) null default null comment '',
                T12 varchar(10) null default null comment '',
                T13 varchar(20) null default null comment '',
                T14 varchar(2) null default null comment '',
                T15 varchar(10) null default null comment '',
                T16 varchar(2) null default null comment '',
                T17 decimal(12,2) null default null comment '',
                T18 varchar(2) null default null comment '',
                T19 varchar(10) null default null comment '',
                T20 varchar(8) null default null comment '',
                T21 varchar(2) null default null comment '',
                T22 varchar(50) null default null comment '',
                T23 varchar(10) null default null comment '',
                T24 varchar(8) null default null comment '',
                T25 varchar(20) null default null comment '',
                T26 varchar(2) null default null comment '',
                T27 varchar(2) null default null comment '',
                T28 varchar(2) null default null comment '',
                T29 varchar(20) null default null comment '',
                T30 varchar(10) null default null comment '',
                T31 varchar(20) null default null comment '',
                T32 varchar(50) null default null comment '',
                T33 varchar(10) null default null comment '',
                T34 varchar(4) null default null comment '',
                T35 varchar(4) null default null comment '',
                T36 varchar(20) null default null comment '',
                T37 varchar(100) null default null comment '', 
                T38 varchar(20) null default null comment '',
                T39 varchar(20) null default null comment '',
                abnormal int(0) NULL DEFAULT 0 COMMENT '是否异常',
                abnormal_state json NULL DEFAULT NULL COMMENT '异常类型',

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

    def insertTrans(self, trans, table_name):
        db = get_mysql_connection()
        cursor = db.cursor()

        T1 = trans.T1
        T2 = trans.T2
        T3 = trans.T3
        T4 = trans.T4
        T5 = trans.T5
        T6 = trans.T6
        T7 = trans.T7
        T8 = trans.T8
        T9 = trans.T9
        T10 = trans.T10
        T11 = trans.T11
        T12 = trans.T12
        T13 = trans.T13
        T14 = trans.T14
        T15 = trans.T2 + '0000000'
        T16 = trans.T16
        T17 = str(trans.T17)
        T18 = trans.T18
        T19 = trans.T19
        T20 = trans.T20
        T21 = trans.T21
        T22 = trans.T22
        T23 = trans.T23
        T24 = trans.T24
        T25 = trans.T25
        T26 = trans.T26
        T27 = trans.T27
        T28 = trans.T28
        T29 = trans.T29
        T30 = trans.T30
        T31 = trans.T31
        T32 = trans.T32
        T33 = trans.T33
        T34 = trans.T34
        T35 = trans.T35
        T36 = trans.T36
        T37 = trans.T37
        T38 = trans.T38
        T39 = trans.T39
        abnormal = trans.abnormal
        abnormal_state = json.dumps(trans.abnormal_state, ensure_ascii=False)

        sql = """
                   insert into """ + table_name + """(id, T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,
                        T11,T12,T13,T14,T15,T16,T17,T18,T19,T20,T21,T22,
                        T23,T24,T25,T26,T27,T28,T29,T30,T31,T32,T33,T34,
                        T35,T36,T37,T38,T39,abnormal,abnormal_state
                )
                values(%s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s, %s, %s,%s,%s, %s, %s, %s,%s,%s, %s, %s, %s,%s,%s, %s, %s, %s,%s,%s,%s, %s, %s, %s,%s,%s,%s,%s)
                """
        item = [None,T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,T18,T19,T20,T21,T22,T23,T24,T25,T26,T27,T28,T29,T30,T31,T32,T33,T34,T35,T36,T37,T38,T39,abnormal, abnormal_state]
        res = cursor.execute(sql, item)
        db.commit()

    def selectTrans(self, table_name):
        sql_select = """
                select id, T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,T18,T19,T20,T21,T22,T23,T24,T25,T26,T27,T28,T29,T30,T31,T32,T33,T34,T35,T36,T37,T38,T39, abnormal, abnormal_state
                from 
                """ + table_name
        db = get_mysql_connection()
        cursor = db.cursor()
        cursor.execute(sql_select)
        select_res = cursor.fetchall()
        return select_res


    def selectTransByTime(self, table_name):
        sql_select = """
                select id, T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,T18,T19,T20,T21,T22,T23,T24,T25,T26,T27,T28,T29,T30,T31,T32,T33,T34,T35,T36,T37,T38,T39, abnormal, abnormal_state
                from """ + table_name + """ order by T23, T19
                """
        db = get_mysql_connection()
        cursor = db.cursor()
        cursor.execute(sql_select)
        select_res = cursor.fetchall()
        return select_res