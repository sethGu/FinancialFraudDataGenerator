import json
import sys

from src.utils.config import get_mysql_connection
from src.dataGen20220414.entity.User import User


class UserDao():
    def __init__(self):
        pass

    def createUserTable(self, table_name):
        # sql = """
        # CREATE TABLE `user`  (
        #     `id` int(0) NOT NULL AUTO_INCREMENT COMMENT 'ID primary key',
        #     `age` int(0) NULL DEFAULT NULL COMMENT 'Age',
        #     `gender` int(0) NULL DEFAULT NULL COMMENT 'Gender',
        #     `job` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '' ,
        #     `wage` int(0) NULL DEFAULT NULL COMMENT 'Salary',
        #     `card` json NULL DEFAULT NULL COMMENT 'Bank cards held',
        #     `abnormal` int(0) NULL DEFAULT 0 COMMENT 'Is abnormal',
        #     `abnormal_state` json NULL DEFAULT NULL COMMENT 'Abnormal type',
        #     `user_no` varchar(100) NULL DEFAULT NULL UNIQUE COMMENT 'Randomly generated encrypted user ID',
        #     `loc_id` varchar(18) NULL DEFAULT NULL COMMENT 'Region field' ,
        #     PRIMARY KEY (`id`) USING BTREE
        # ) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;
        # """
        sql = """CREATE TABLE """ + """`""" + table_name + """` (
            `id` int(0) NOT NULL AUTO_INCREMENT COMMENT 'ID primary key',
            `age` int(0) NULL DEFAULT NULL COMMENT 'Age',
            `gender` int(0) NULL DEFAULT NULL COMMENT 'Gender',
            `job` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '' ,
            `wage` int(0) NULL DEFAULT NULL COMMENT 'Salary',
            `card` json NULL DEFAULT NULL COMMENT 'Bank cards held',
            `abnormal` int(0) NULL DEFAULT 0 COMMENT 'Is abnormal',
            `abnormal_state` json NULL DEFAULT NULL COMMENT 'Abnormal type',
            `user_no` varchar(100) NULL DEFAULT NULL UNIQUE COMMENT 'Randomly generated encrypted user ID',
            `loc_id` varchar(18) NULL DEFAULT NULL COMMENT 'Region field' ,
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
            print("createUserTable:", result)
            db.close()
            sys.exit()
        finally:
            db.close()

    def insertUsers(self, userList, table_name):
        try:
            db = get_mysql_connection()
            cursor = db.cursor()
            for user in userList:
                age = user.getAge()
                gender = user.getGender()
                job = user.getJob()
                wage = user.getWage()
                abnormal = user.getAbnormal()
                abnormal_state = json.dumps(user.getAbnormal_state(), ensure_ascii=False)
                user_no = user.get_user_no()
                loc_id = user.getLoc_id()
                sql = """insert into """ + table_name + """(age, gender, job, wage, card, abnormal, abnormal_state, user_no, loc_id)
                        values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                # sql = """
                #         insert into user(age, gender, job, wage, card, abnormal, abnormal_state, user_no, loc_id)
                #         values(%s, %s, %s, %s, %s, %s, %s, %s, %s)
                #         """
                item = [age, gender, job, wage, '[]', abnormal, abnormal_state, user_no, loc_id]

                cursor.execute(sql, item)
                db.commit()
        except Exception as result:
            print(result)
            db.close()
            sys.exit()
        finally:
            db.close()

    def selectUsers(self, table_name):
        '''

        :return:
        '''
        # sql_select = """
        # select id,age,gender,job,wage,card, abnormal, abnormal_state, user_no, loc_id
        # from user
        # """
        sql = """select id,age,gender,job,wage,card, abnormal, abnormal_state, user_no, loc_id
        from """ + table_name
        db = get_mysql_connection()
        cursor = db.cursor()
        cursor.execute(sql)
        select_res = cursor.fetchall()
        return select_res

    # def selectFraudUsers(self, fraud_category=None, table_name=None):
    #     # sql_select = """
    #     #         select id,age,gender,job,wage,card,abnormal,abnormal_state,user_no, loc_id
    #     #         from user
    #     #     """
    #     sql = """select id,age,gender,job,wage,card, abnormal, abnormal_state, user_no, loc_id
    #             from""" + table_name
    #     # sql_select = """
    #     #     select id,age,gender,job,wage,card,abnormal,abnormal_state
    #     #     from user
    #     #     where abnormal = %s
    #     # """
    #     db = get_mysql_connection()
    #     cursor = db.cursor()
    #
    #     cursor.execute(sql_select)
    #
    #     select_res = cursor.fetchall()
    #     userList = []
    #     for item in select_res:
    #         id, age, gender, job, wage, card, abnormal, abnormal_state, user_no, loc_id = item
    #         state = json.loads(abnormal_state)
    #
    #         if fraud_category is None:
    #             if abnormal:
    #                 user = User(id=id, age=age, gender=gender, job=job, wage=wage, card=card,
    #                             abnormal=abnormal, abnormal_state=abnormal_state, user_no=user_no, loc_id = loc_id)
    #                 userList.append(user)
    #         else:
    #             if state[fraud_category] == 1:
    #                 user = User(id=id, age=age, gender=gender, job=job, wage=wage, card=card,
    #                             abnormal=abnormal, abnormal_state=abnormal_state, user_no=user_no, loc_id = loc_id)
    #                 userList.append(user)
    #
    #     return userList

    def selectNormalUser(self, table_name):
        sql = """select id,age,gender,job,wage,card, abnormal, abnormal_state, user_no, loc_id
                from""" + table_name
        # sql_select = """
        #     select id,age,gender,job,wage,card,abnormal,abnormal_state
        #     from user
        #     where abnormal = %s
        # """

        db = get_mysql_connection()
        cursor = db.cursor()

        cursor.execute(sql)

        select_res = cursor.fetchall()
        userList = []
        for item in select_res:
            id, age, gender, job, wage, card, abnormal, abnormal_state, user_no, loc_id = item

            if abnormal == 0:
                user = User(id=id, age=age, gender=gender, job=job, wage=wage, card=card,
                            abnormal=abnormal, abnormal_state=abnormal_state, user_no=user_no, loc_id = loc_id)
                userList.append(user)
        return userList

    def addUserCard(self, user_id=None, new_card=None, user_no=None, table_name=None):
        if user_no is None:
            sql_select = """select id,card from """ + table_name + """ where id = %s """
            db = get_mysql_connection()
            cursor = db.cursor()
            item = [user_id]
            cursor.execute(sql_select, item)
            select_res = cursor.fetchone()
            id, card = select_res
            card = json.loads(card)
            c = {"C4": new_card.getC4(), 'C5': new_card.getC5()}
            card.append(c)
            sql_update = """
                        update """ + table_name + """
                        set card = %s
                        where id = %s
                        """
            card = json.dumps(card, ensure_ascii=False)
            item = [card, id]
            res = cursor.execute(sql_update, item)

        else:
            sql_select = """
                            select user_no,card
                            from """ + table_name + """
                            where user_no = %s
                            """
            db = get_mysql_connection()
            cursor = db.cursor()
            item = [user_no]
            cursor.execute(sql_select, item)
            select_res = cursor.fetchone()
            user_no, card = select_res
            card = json.loads(card)
            c = {"C4": new_card.getC4(), 'C5': new_card.getC5()}
            card.append(c)
            sql_update = """update """ + table_name + """ set card = %s where user_no = %s """
            card = json.dumps(card, ensure_ascii=False)
            item = [card, user_no]
            res = cursor.execute(sql_update, item)

        db.commit()
        return res

    def updateUserState(self, user_id, fraud_category, table_name):
        sql_select = """
                select id,abnormal,abnormal_state
                from """ + table_name + """ 
                where id = %s
            """
        db = get_mysql_connection()
        cursor = db.cursor()
        item = [user_id]
        cursor.execute(sql_select, item)
        select_res = cursor.fetchone()
        id, abnormal, abnormal_state = select_res

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
                where id = %s
            """
        abnormal_state = json.dumps(abnormal_state, ensure_ascii=False)
        item = [abnormal, abnormal_state, user_id]
        res = cursor.execute(sql_update, item)
        db.commit()
        return res

    def get_user_info(self, user_id, table_name):
        sql_select = """
            select id,age,gender,job,wage,card,abnormal,abnormal_state,user_no, loc_id
            from """ + table_name + """
            where id = %s
        """
        db = get_mysql_connection()
        cursor = db.cursor()
        item = [user_id]
        cursor.execute(sql_select, item)
        select_res = cursor.fetchone()
        id,age,gender,job,wage,card,abnormal,abnormal_state,user_no, loc_id = select_res
        card = json.loads(card)
        user = User(age=age, gender=gender, job=job, wage=wage, id=id, card=card, abnormal = abnormal, abnormal_state = abnormal_state, user_no = user_no, loc_id = loc_id)
        return user

    @staticmethod
    def get_user_id_by(user_no, table_name):
        sql_select = """
                        select id,card
                        from """ + table_name + """
                        where user_no = %s
                        """
        db = get_mysql_connection()
        cursor = db.cursor()
        item = [user_no]
        cursor.execute(sql_select, item)
        select_res = cursor.fetchone()
        id, card = select_res
        card = json.loads(card)
        return id, card
