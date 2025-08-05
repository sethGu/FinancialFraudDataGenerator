import os

import pymysql

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

connection = pymysql.connect(
    # host='localhost',
    host='db',
    user='root',
    password='root',
    db='sf_web_001',
    port=3306,
    charset='utf8')


class get_mysql_connection():
    def __init__(self):
        global connection
        self.connection = connection
        # self.cursor = self.connection.cursor()

    def cursor(self):
        self.connection.ping(reconnect=True)
        return self.connection.cursor()

    def ping(self):
        self.connection.ping(reconnect=True)
    # def execute(self,sql,item=None):
    #     self.cursor.execute(sql,item)

    def close(self):
        print('Close MySQL connection.')
        try:
            self.connection.close()
        except:
            print('The MySQL connection has been closed.')

    def commit(self):
        self.connection.commit()

    # def __del__(self):
    #     try:
    #         self.connection.close()
    #     except:
    #         print('The MySQL connection has been closed.')
