import json
import sys

from src.utils.config import get_mysql_connection


class StoreDao():
    def __init__(self):
        pass

    # 创建store数据库表
    def createStoreTable(self, table_name):

        # sql = """
        #             CREATE TABLE `store`  (
        #                 `id` int(0) NOT NULL AUTO_INCREMENT COMMENT 'id主键',
        #                 `industry` varchar(50) NULL DEFAULT NULL COMMENT '行业',
        #                 `name_` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '商铺名称' ,
        #                 `rank_` varchar(50) NULL DEFAULT NULL COMMENT '等级',
        #
        #                 `consumption_range` json NULL DEFAULT NULL COMMENT '消费区间',
        #                 `opening_hours` varchar(50) NULL DEFAULT NULL COMMENT '营业时间',
        #
        #                 `S1` varchar(50) null default null comment '',
        #                 `S2` varchar(20) null default null COMMENT '',
        #                 `S3` varchar(20) null default null COMMENT '',
        #                 `S4` varchar(20) null default null COMMENT '',
        #                 `S5` varchar(20) null default null COMMENT '',
        #                 `S6` varchar(20) null default null COMMENT '',
        #                 `S7` varchar(20) null default null COMMENT '',
        #                 `S8` varchar(20) null default null COMMENT '',
        #                 `S9` varchar(20) null default null COMMENT '',
        #                 `S10` varchar(20) null default null COMMENT '',
        #                 `S11` varchar(20) null default null COMMENT '',
        #                 `S12` varchar(20) null default null COMMENT '',
        #                 `S13` varchar(20) null default null COMMENT '',
        #                 `S14` varchar(20) null default null COMMENT '',
        #                 `S15` varchar(20) null default null COMMENT '',
        #                 `S16` varchar(20) null default null COMMENT '',
        #                 `S17` varchar(20) null default null COMMENT '',
        #                 `S18` varchar(50) NULL DEFAULT "" COMMENT '',
        #                 `S19` varchar(20) null default null COMMENT '',
        #                 `S20` varchar(20) null default null COMMENT '',
        #                 `S21` varchar(20) null default null COMMENT '',
        #                 `S22` varchar(20) null default null COMMENT '',
        #                 `S23` varchar(200) null default null COMMENT '',
        #                 `S24` varchar(20) null default null COMMENT '',
        #                 `S25` varchar(20) null default null COMMENT '',
        #                 `S26` varchar(20) null default null COMMENT '',
        #                 `S27` varchar(20) null default null COMMENT '',
        #                 `S28` varchar(20) null default null COMMENT '',
        #                 `S29` varchar(20) null default null COMMENT '',
        #                 `S30` json NULL DEFAULT NULL COMMENT '',
        #                 `abnormal` int(0) NULL DEFAULT 0 COMMENT '是否异常',
        #                 `abnormal_state` json NULL DEFAULT NULL COMMENT '异常类型',
        #                 PRIMARY KEY (`id`) USING BTREE
        #             ) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;
        #             """

        sql = """CREATE TABLE """ + """`""" + table_name + """`  (
                        `id` int(0) NOT NULL AUTO_INCREMENT COMMENT 'id主键',
                        `industry` varchar(50) NULL DEFAULT NULL COMMENT '行业',
                        `name_` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '商铺名称' ,
                        `rank_` varchar(50) NULL DEFAULT NULL COMMENT '等级',
                        
                        `consumption_range` json NULL DEFAULT NULL COMMENT '消费区间',
                        `opening_hours` varchar(50) NULL DEFAULT NULL COMMENT '营业时间',
                        
                        `S1` varchar(50) null default null comment '',
                        `S2` varchar(20) null default null COMMENT '',
                        `S3` varchar(20) null default null COMMENT '',
                        `S4` varchar(20) null default null COMMENT '',
                        `S5` varchar(20) null default null COMMENT '',
                        `S6` varchar(20) null default null COMMENT '',
                        `S7` varchar(20) null default null COMMENT '',
                        `S8` varchar(20) null default null COMMENT '',
                        `S9` varchar(20) null default null COMMENT '',
                        `S10` varchar(20) null default null COMMENT '',
                        `S11` varchar(20) null default null COMMENT '',
                        `S12` varchar(20) null default null COMMENT '',
                        `S13` varchar(20) null default null COMMENT '',
                        `S14` varchar(20) null default null COMMENT '',
                        `S15` varchar(20) null default null COMMENT '',
                        `S16` varchar(20) null default null COMMENT '',
                        `S17` varchar(20) null default null COMMENT '',
                        `S18` varchar(50) NULL DEFAULT "" COMMENT '',
                        `S19` varchar(20) null default null COMMENT '',
                        `S20` varchar(20) null default null COMMENT '',
                        `S21` varchar(20) null default null COMMENT '',
                        `S22` varchar(20) null default null COMMENT '',
                        `S23` varchar(200) null default null COMMENT '',
                        `S24` varchar(20) null default null COMMENT '',
                        `S25` varchar(20) null default null COMMENT '',
                        `S26` varchar(20) null default null COMMENT '',
                        `S27` varchar(20) null default null COMMENT '',
                        `S28` varchar(20) null default null COMMENT '',
                        `S29` varchar(20) null default null COMMENT '',
                        `S30` json NULL DEFAULT NULL COMMENT '',
                        `abnormal` int(0) NULL DEFAULT 0 COMMENT '是否异常',
                        `abnormal_state` json NULL DEFAULT NULL COMMENT '异常类型',
                        PRIMARY KEY (`id`) USING BTREE 
                    ) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;"""
        try:
            db = get_mysql_connection()
            cursor = db.cursor()
            s = """DROP TABLE IF EXISTS `""" + table_name + """`;"""
            cursor.execute(s)
            cursor.execute(sql)
        except Exception as result:
            print(result)
            db.close()
            sys.exit()
        finally:
            db.close()



    def insertStores(self,storeList, table_name):
        db = get_mysql_connection()
        cursor = db.cursor()
        for store in storeList:
            id = store.getStore_id()
            industry = store.getIndustry()
            name_ = store.name
            rank_ = store.getLevel()
            consumption_range = store.getCharge_duration()
            consumption_range = json.dumps(consumption_range)
            opening_hours = store.getOpen_duration()
            S30 = store.getS30()
            S1 = store.S1
            abnormal = store.getAbnormal()
            S2= store.S2
            S3 = store.S3
            S4 = store.S4
            S5 = store.S5
            S6 = store.S6
            S7 = store.S7
            S8 = store.S8
            S9 = store.S9
            S10 = store.S10
            S11 = store.S11
            S12 = store.S12
            S13 = store.S13
            S14 = store.S14
            S15 = store.S15
            S16 = store.S16
            S17 = store.S17
            S18 = store.getS18()
            S19 = store.S19
            S20 = store.S20
            S21 = store.S21
            S22 = store.S22
            S23 = store.S23
            S24 = store.S24
            S25 = store.S25
            S26 = store.S26
            S27 = store.S27
            S28 = store.S28
            S29 = store.S29
            # 务必要转换成JSON字符串，否则会因为编译器导致dic中为单引号，使得非JSON格式，而插入失败
            abnormal_state = json.dumps(store.getAbnormal_state())
            sql = """
                        insert into """ + table_name + """(id, industry, name_, rank_,consumption_range,opening_hours,
                        S1, S2, S3, S4,S5, S6,S7,S8,S9,S10,S11,S12,S13, S14, S15, S16,S17,S18,S19,S20,
                        S21,S22,S23,S24,S25,S26,S27,S28,S29,S30, abnormal, abnormal_state)
                        values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s)
                        """
            # sql = """
            #             insert into store(id, industry, name_, rank_ )
            #             values(%s, %s, %s, %s)
            #             """
            # item = [None, industry, name_, rank_]
            item = [None, industry, name_, rank_,consumption_range,opening_hours,S1, S2, S3, S4,S5, S6,S7,S8,S9,S10,S11,S12,S13, S14, S15, S16,S17,S18,S19,S20,S21,S22,S23,S24,S25,S26,S27,S28,S29,S30, abnormal, abnormal_state]
            cursor.execute(sql, item)
            db.commit()
        # except Exception as result:
        #     print(result)
        #     db.close()
        #     sys.exit()
        # finally:
        #     db.close()


    def selectStores(self, table_name):
        sql_select = """
            select id, industry, name_, rank_,consumption_range,opening_hours,S1, S2, S3, S4,S5, S6,S7,S8,S9,S10,S11,S12,S13, S14, S15, S16,S17,S18,S19,S20,S21,S22,S23,S24,S25,S26,S27,S28,S29,S30, abnormal, abnormal_state
            from """ + table_name

        db = get_mysql_connection()
        cursor = db.cursor()
        cursor.execute(sql_select)
        select_res = cursor.fetchall()
        return select_res

    def updateS2OfStore(self,store_id, S2, table_name):
        sql_update = """
            update """ + table_name + """
            set S2 = %s
            where id = %s
            """
        db = get_mysql_connection()
        cursor = db.cursor()
        item = [S2, store_id]
        cursor.execute(sql_update, item)
        db.commit()

    def updateAcctOfStore(self,store_id, S18, table_name):
        sql_update = """
            update """ + table_name + """ 
            set S18 = %s
            where id = %s
            """
        db = get_mysql_connection()
        cursor = db.cursor()
        item = [S18, store_id]
        cursor.execute(sql_update, item)
        db.commit()

    def updateStoreState(self,store_id, fraud_category, table_name):
        '''
        更新商户是否为欺诈商户
        :param store_id:
        :param fraud_category:
        :return:
        '''
        sql_select = """
                select id,abnormal,abnormal_state
                from """ + table_name + """ 
                where id = %s
            """
        db = get_mysql_connection()
        cursor = db.cursor()
        item = [store_id]
        cursor.execute(sql_select, item)
        select_res = cursor.fetchone()
        id, abnormal, abnormal_state = select_res

        abnormal_state = json.loads(abnormal_state)
        if fraud_category == '' or fraud_category == None:
            abnormal = 0
            # 将字典中的所有值设为0
            abnormal_state = dict.fromkeys(abnormal_state, 0)
        else:
            abnormal = 1
            abnormal_state[fraud_category] = 1
        # 更新数据库
        sql_update = """
                update """ + table_name + """
                set abnormal = %s, abnormal_state = %s
                where id = %s
            """
        abnormal_state = json.dumps(abnormal_state, ensure_ascii=False)
        item = [abnormal, abnormal_state, store_id]
        res = cursor.execute(sql_update, item)
        db.commit()
        return res

    def update_S30s(self, store_id, new_S30s, table_name):
        '''
        '''
        S30s = json.dumps(new_S30s, ensure_ascii=False)

        db = get_mysql_connection()
        cursor = db.cursor()
        # 更新数据库
        sql_update = """
                update """ + table_name + """
                set S30 = %s
                where id = %s
            """
        item = [S30s, store_id]
        res = cursor.execute(sql_update, item)
        db.commit()
        return res
    def select_store_by_S1(self, S1, table_name):
        sql_select = """
            select id, industry, name_, rank_,consumption_range,opening_hours,S1, S2, S3, S4,S5, S6,S7,S8,S9,S10,S11,S12,S13, S14, S15, S16,S17,S18,S19,S20,S21,S22,S23,S24,S25,S26,S27,S28,S29,S30, abnormal, abnormal_state
            from """ + table_name + """ 
            where S1 = %s
        """
        item = [S1]
        db = get_mysql_connection()
        cursor = db.cursor()
        cursor.execute(sql_select, item)
        select_res = cursor.fetchone()
        return select_res
