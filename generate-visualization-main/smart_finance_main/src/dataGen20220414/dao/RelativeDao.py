import json
import sys
from src.dataGen20220414.entity.Relative import Relative
from src.utils.config import get_mysql_connection


class RelativeDao():
    def __init__(self):
        pass

    def createRelativeTable(self, table_name):
        sql = """
            create table """ + table_name + """(
                `id` int(0) NOT NULL auto_increment comment 'id主键',
                `user_id` int(0) NOT NULL comment 'user id',
                `gender` int(0) NULL DEFAULT NULL COMMENT '性别',
                `age` int(0) NULL DEFAULT NULL COMMENT '年龄',
                `childList` json NULL DEFAULT NULL COMMENT '孩子集合',
                `f_id` int(0) NULL DEFAULT NULL comment 'father id',
                `m_id` int(0) NULL DEFAULT NULL comment 'mather id',
                `c_id` int(0) NULL DEFAULT NULL comment 'couple id',
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
            print("createRelative`Table:", result)
            sys.exit()
        finally:
            db.close()

    def insertRelative(self,relative, table_name):
        # try:
            db = get_mysql_connection()
            cursor = db.cursor()
            user_id = relative.id
            gender = relative.male
            age = relative.age
            childList = json.dumps(relative.childList)
            fId = relative.fId
            mId= relative.mId
            coupleId = relative.coupleId
            sql = """
                    insert into """ + table_name + """(id, user_id, gender, age,childList,f_id,m_id,c_id)
                    values(%s, %s, %s, %s,%s,%s,%s,%s)
                    """
            item = [None,user_id,gender,age,childList,fId,mId,coupleId]
            cursor.execute(sql, item)
            db.commit()

    def selectRelative(self, table_name):
        sql_select = """
            select id, user_id, gender, age,childList,f_id,m_id,c_id
            from 
        """ + table_name
        db = get_mysql_connection()
        cursor = db.cursor()
        cursor.execute(sql_select)
        relativeList = cursor.fetchall()
        return relativeList

    def selectRelativeById(self, user_id, table_name):
        sql_select = """
            select id, user_id, gender, age,childList,f_id,m_id,c_id
            from """ + table_name + """
            where user_id = %s
        """
        db = get_mysql_connection()
        cursor = db.cursor()
        cursor.execute(sql_select, user_id)
        list = cursor.fetchone()
        return list