import os

# 基础路径 BASE_DIR = ././YTSystem/
import pymysql

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

connection = pymysql.connect(
    host='localhost',
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
        print('关闭mysql连接')
        try:
            self.connection.close()
        except:
            print('mysql连接已关闭')

    def commit(self):
        self.connection.commit()

    # def __del__(self):
    #     try:
    #         self.connection.close()
    #     except:
    #         print('mysql连接已关闭')
