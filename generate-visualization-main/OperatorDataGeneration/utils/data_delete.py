# @Time    : 2023/5/17 22:29
# @Author  : SuperRich Liu
from OperatorDataGeneration.src import mysql_db


def delete():
    conn = mysql_db.MysqlDB()
    tablename = 'operator'
    conn.deleteTable(tablename=tablename)
    conn.auto_increment_from_1(tablename=tablename)
    conn.close()


if __name__ == '__main__':
    delete()
