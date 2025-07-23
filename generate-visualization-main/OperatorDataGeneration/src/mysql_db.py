# @Time    : 2023/5/17 20:30
# @Author  : SuperRich Liu
import re

import pymysql


class MysqlDB():
    def __init__(self):
        try:
            self.con = pymysql.connect(
                host="localhost",
                port=3306,
                database="sf_web_001",
                charset="utf8",
                user="root",
                passwd="root"
            )
            self.con.autocommit(0)
            # 所有的查询，都在连接 con 的一个模块 cursor 上面运行的
            self.cur = self.con.cursor()
        except:
            print("DataBase connect error,please check the db config.")

    def creatTable(self, tablename, attrdict, constraint="PRIMARY KEY(`id`)"):
        """创建数据库表
            args：
                tablename  ：表名字
                attrdict   ：属性键值对,{'book_name':'varchar(200) NOT NULL'...}
                constraint ：主外键约束,PRIMARY KEY(`id`)
        """
        # 　判断表是否存在
        if self.isExistTable(tablename):
            # print("%s is exit" % tablename)
            return
        sql = ''
        sql_mid = '`id` int(0) NOT NULL AUTO_INCREMENT,'
        for attr, value in attrdict.items():
            sql_mid = sql_mid + '`' + attr + '`' + ' ' + value + ','
        sql = sql + 'CREATE TABLE IF NOT EXISTS %s (' % tablename
        sql = sql + sql_mid
        sql = sql + constraint
        sql = sql + ') ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic'
        # print('creatTable:' + sql)
        self.executeCommit(sql)

    def executeCommit(self, sql=''):
        """
        执行数据库sql语句，针对更新,删除,事务等操作失败时回滚
        """
        try:
            self.cur.execute(sql)
            self.con.commit()
        except pymysql.Error as e:
            self.con.rollback()
            error = '执行数据库sql语句失败(%s): %s' % (e.args[0], e.args[1])
            print("error:", error)
            return error

    def isExistTable(self, tablename):
        """判断数据表是否存在
            args：
                tablename  ：表名字
            Return:
                存在返回True，不存在返回False
        """
        sql = "select * from %s" % tablename
        print("Ignore next error!!!")
        result = self.executeCommit(sql)
        if result is None:
            return True
        else:
            if re.search("doesn't exist", result):
                return False
            else:
                return True

    def insert(self, tablename, params):
        """
            往表里插入数据，单条数据
            args：
                tablename  ：表名字
                key        ：属性键
                value      ：属性值
        """
        key = []
        value = []
        for k, v in params.items():
            key.append('`' + k + '`')
            value.append(v)
        sql = 'insert into %s' % tablename
        # sql = sql + attrs_sql + values_sql
        sql = sql + '(' + ','.join(key) + ')' + ' values ' + str(tuple(value))
        # print('_insert:' + sql)
        self.executeCommit(sql)

    def executeSql(self, sql=''):
        """
            执行sql语句，针对读操作返回结果集
            args：
                sql  ：sql语句
        """
        try:
            self.cur.execute(sql)
            records = self.cur.fetchall()
            return records
        except pymysql.Error as e:
            error = '执行sql语句失败(%s): %s' % (e.args[0], e.args[1])
            print(error)

    def select(self, tablename, fields='*'):
        """查询数据
            args：
                tablename  ：表名字
                cond_dict  ：查询条件
                order      ：排序条件
            example：
                print mydb.select(table)
                print mydb.select(table, fields=["name"])
                print mydb.select(table, fields=["name", "age"])
                print mydb.select(table, fields=["age", "name"])
        """
        if fields == "*":
            sql = 'select * from %s' % tablename
        else:
            if isinstance(fields, list):
                fields = ",".join(fields)
                sql = 'select %s from %s' % (fields, tablename)
            else:
                print("fields input error, please input list fields.")
        # print('select:' + sql)
        return self.executeSql(sql)

    def dropTable(self, tablename):
        """删除数据库表
            args：
                tablename  ：表名字
        """
        sql = "DROP TABLE  %s" % tablename
        self.executeCommit(sql)

    def deleteTable(self, tablename):
        """清空数据库表
            args：
                tablename  ：表名字
        """
        sql = "DELETE FROM %s" % tablename
        # print("sql=", sql)
        self.executeCommit(sql)

    def auto_increment_from_1(self, tablename):
        sql = f'alter table {tablename} auto_increment=1'
        self.executeCommit(sql)

    def close(self):
        self.con.close()


if __name__ == '__main__':
    conn = MysqlDB()
    print(conn.executeSql('select * from login'))
    conn.close()
