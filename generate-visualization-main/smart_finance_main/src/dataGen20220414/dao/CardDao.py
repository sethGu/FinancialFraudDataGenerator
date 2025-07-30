import json
import sys

from src.dataGen20220414.entity.Card import Card
from src.dataGen20220414.dao.UserDao import UserDao
from src.utils.config import get_mysql_connection


class CardDao():
    def __init__(self):
        pass

    # Create store database table
    def createCardTable(self, table_name):
        # sql = """
        #             CREATE TABLE `card`  (
        #                 `card_id` int(0) NOT NULL AUTO_INCREMENT COMMENT 'Card id',
        #                 `owner_type` varchar(50) NULL DEFAULT NULL COMMENT 'Owner type',
        #                 `owner_id` int(30) NULL DEFAULT NULL COMMENT 'Owner ID',
        #                 `C4` varchar(100) NULL DEFAULT NULL UNIQUE COMMENT 'C4',
        #                 `C5` varchar(100) NULL DEFAULT NULL COMMENT 'C5',
        #                 `C6` varchar(100) NULL DEFAULT NULL COMMENT 'C6',
        #                 `C7` varchar(100) NULL DEFAULT NULL COMMENT 'C7',
        #                 `C8` varchar(100) NULL DEFAULT NULL COMMENT 'C8',
        #                 `C9` varchar(100) NULL DEFAULT NULL COMMENT 'C9',
        #                 `C10` varchar(100) NULL DEFAULT NULL COMMENT 'C10',
        #                 `C11` varchar(100) NULL DEFAULT NULL COMMENT 'C11',
        #                 `abnormal` int(0) NULL DEFAULT 0 COMMENT 'Is abnormal',
        #                 `abnormal_state` json NULL DEFAULT NULL COMMENT 'Abnormal type',
        #                 PRIMARY KEY (`card_id`) USING BTREE
        #             ) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;
        #             """
        sql = """CREATE TABLE """  + """`""" + table_name + """`(
                        `card_id` int(0) NOT NULL AUTO_INCREMENT COMMENT 'Card id',
                        `owner_type` varchar(50) NULL DEFAULT NULL COMMENT 'Owner type',
                        `owner_id` int(30) NULL DEFAULT NULL COMMENT 'Owner ID',
                        `C4` varchar(100) NULL DEFAULT NULL UNIQUE COMMENT 'C4',
                        `C5` varchar(100) NULL DEFAULT NULL COMMENT 'C5',
                        `C6` varchar(100) NULL DEFAULT NULL COMMENT 'C6',
                        `C7` varchar(100) NULL DEFAULT NULL COMMENT 'C7',
                        `C8` varchar(100) NULL DEFAULT NULL COMMENT 'C8',
                        `C9` varchar(100) NULL DEFAULT NULL COMMENT 'C9',
                        `C10` varchar(100) NULL DEFAULT NULL COMMENT 'C10',
                        `C11` varchar(100) NULL DEFAULT NULL COMMENT 'C11',
                        `abnormal` int(0) NULL DEFAULT 0 COMMENT 'Is abnormal',
                        `abnormal_state` json NULL DEFAULT NULL COMMENT 'Abnormal type',
                        PRIMARY KEY (`card_id`) USING BTREE
                    ) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;
                    """
        try:
            db = get_mysql_connection()
            cursor = db.cursor()
            s = """DROP TABLE IF EXISTS `""" + table_name + """`;"""
            cursor.execute(s)
            cursor.execute(sql)
        except Exception as result:
            # print(result)
            db.close()
            sys.exit()
        finally:
            db.close()

    def insertCard(self,card, table_name):
        db = get_mysql_connection()
        cursor = db.cursor()

        card_id = card.getcard_id()
        owner_type = card.getowner_type()
        owner_id = card.getowner_id()
        C4 = card.getC4()
        C5 = card.getC5()
        C6 = card.getC6()
        C7 = card.getC7()
        C8 = card.getC8()
        C9 = card.getC9()
        C10 = card.getC10()
        C11 = card.getC11()
        abnormal = card.getAbnormal()

        abnormal_state = json.dumps(card.getAbnormal_state(), ensure_ascii=False)
        # sql = """
        #                         insert into `card`(owner_type, owner_id, C4, C5, C6, C7, C8, C9, C10, C11, abnormal, abnormal_state)
        #                         values(%s, %s, %s, %s, %s, %s,%s, %s,%s, %s, %s, %s)
        #                         """
        sql = """insert into """ + """`""" + table_name + """`(owner_type, owner_id, C4, C5, C6, C7, C8, C9, C10, C11, abnormal, abnormal_state) values(%s, %s, %s, %s, %s, %s,%s, %s,%s, %s, %s, %s)"""
        item = [owner_type, owner_id, C4, C5, C6, C7, C8,C9,C10,C11, abnormal,
                abnormal_state]
        # print(item)
        cursor.execute(sql, item)
        db.commit()


    @staticmethod
    def selectNormalCard(table_name):
        sql_select = """
                    select card_id,owner_type,owner_id,C4,C5,C6,C7,C8,C9,C10,C11,abnormal,abnormal_state
                    from """ + table_name


        db = get_mysql_connection()
        cursor = db.cursor()

        cursor.execute(sql_select)

        select_res = cursor.fetchall()
        return select_res


    @staticmethod
    def selectFraudCard(fraud_category, table_name):
        sql_select = """
                select card_id,owner_type,owner_id,C4,C5,C6,C7,C8,C9,C10,C11,abnormal,abnormal_state
                from 
            """ + table_name

        db = get_mysql_connection()
        cursor = db.cursor()

        cursor.execute(sql_select)

        select_res = cursor.fetchall()
        return select_res

    @staticmethod
    def selectCardInfoByC4(C4, table_name):
        '''

        :param C4
        :return:
        '''
        sql_select = """
            select card_id,owner_type,owner_id,C4,C5,C6,C7,C8,C9,C10,C11,abnormal,abnormal_state
            from """ + table_name + """
            where C4 = %s
        """
        db = get_mysql_connection()
        cursor = db.cursor()
        item = [C4]
        cursor.execute(sql_select, item)
        select_res = cursor.fetchone()

        return select_res

    def updateCardState(self, C4, fraud_category, table_name):
        sql_select = """
            select abnormal,abnormal_state
            from """ + table_name + """ 
            where C4 = %s
        """
        db = get_mysql_connection()
        cursor = db.cursor()
        item = [C4]
        cursor.execute(sql_select, item)
        select_res = cursor.fetchone()
        abnormal, abnormal_state = select_res

        abnormal_state = json.loads(abnormal_state)
        if fraud_category == '' or fraud_category == None:
            abnormal = 0
            abnormal_state = dict.fromkeys(abnormal_state, 0)
        else:
            abnormal = 1
            abnormal_state[fraud_category] = 1

        sql_update = """
            update """ + table_name + """
            set abnormal = %s, abnormal_state = %s
            where C4 = %s
        """
        abnormal_state = json.dumps(abnormal_state, ensure_ascii=False)
        item = [abnormal, abnormal_state, C4]
        res = cursor.execute(sql_update, item)
        db.commit()
        return res

    @staticmethod
    def selectCardByOwnerId(ownerId, table_name):
        '''

        :return:
        '''
        sql_select = """
            select card_id,owner_type,owner_id,C4,C5,C6,C7,C8,C9,C10,C11,abnormal,abnormal_state
            from """ + table_name + """
            where owner_id = %s
        """
        db = get_mysql_connection()
        cursor = db.cursor()
        item = [ownerId]
        cursor.execute(sql_select, item)
        select_res = cursor.fetchall()

        return select_res

    @staticmethod
    def selectTransferCardByOwnerId(ownerId, table_name):
        '''

        :return:
        '''
        sql_select = """
                select card_id,owner_type,owner_id,C4,C5,C6,C7,C8,C9,C10,C11,abnormal,abnormal_state
                from """ + table_name + """
                where owner_id = %s and C5 = %s and owner_type = %s
            """
        db = get_mysql_connection()
        cursor = db.cursor()
        item = [ownerId, '01', 'Regular_user']
        cursor.execute(sql_select, item)
        select_res = cursor.fetchall()

        return select_res