# @Time    : 2023/5/17 20:50
# @Author  : SuperRich Liu
from OperatorDataGeneration.src import operator
from OperatorDataGeneration.src import mysql_db


def generation(total):  # total是生成的数据量
    conn = mysql_db.MysqlDB()
    tablename = 'operator'
    attrdict = {
        'original_ID': "varchar(200) NULL DEFAULT NULL COMMENT '原始ID'",
        'contactor': "varchar(200) NULL DEFAULT NULL COMMENT '触点'",
        'contactor_ID': "varchar(200) NULL DEFAULT NULL COMMENT '触点ID'",
        'mobile_phone_brand': "varchar(200) NULL DEFAULT NULL COMMENT '手机品牌'",
        'mobile_operating_system': "varchar(200) NULL DEFAULT NULL COMMENT '手机操作系统'",
        'pv': "varchar(200) NULL DEFAULT NULL COMMENT 'pv'",
        'terminal_type': "varchar(200) NULL DEFAULT NULL COMMENT '终端类型'",
        'video_website': "varchar(200) NULL DEFAULT NULL COMMENT '视频网站'",
        'shopping_website': "varchar(200) NULL DEFAULT NULL COMMENT '购物网站'",
        'overseas_taobao_shopping_channel': "varchar(200) NULL DEFAULT NULL COMMENT '海淘购物渠道'",
        'automotive_website': "varchar(200) NULL DEFAULT NULL COMMENT '汽车网站'",
        'real_estate_website': "varchar(200) NULL DEFAULT NULL COMMENT '房产网站'",
        'travel_website': "varchar(200) NULL DEFAULT NULL COMMENT '旅游网站'",
        'highest_calling': "decimal(18,0) NULL DEFAULT 0 COMMENT '当月内用户日最高主叫通话次数'",
        'city_number': "decimal(18,0) NULL DEFAULT 0 COMMENT '当月与该号码通话的对端所属城市数量'",
        'day_calling': "decimal(18,0) NULL DEFAULT 0 COMMENT '工作日白天主叫通话次数'",
        'night_calling': "decimal(18,0) NULL DEFAULT 0 COMMENT '工作日夜间通话天数'",
        'three_month_calling': "decimal(18,0) NULL DEFAULT 0 COMMENT '近三月月均主叫通话次数'",
    }
    constraint = "PRIMARY KEY(`id`)"
    conn.creatTable(tablename=tablename, attrdict=attrdict, constraint=constraint)
    for i in range(total):
        ope = operator.Operator()
        ope.set_original_ID()
        ope.set_contactor()
        ope.set_contactor_ID()
        ope.set_mobile_phone_brand()
        ope.set_mobile_operating_system()
        ope.set_pv()
        ope.set_terminal_type()
        ope.set_video_website()
        ope.set_shopping_website()
        ope.set_overseas_taobao_shopping_channel()
        ope.set_automotive_website()
        ope.set_real_estate_website()
        ope.set_travel_website()
        ope.set_highest_calling()
        ope.set_city_number()
        ope.set_day_calling()
        ope.set_night_calling()
        ope.set_three_month_calling()
        conn.insert(tablename=tablename, params=ope.get_all_items())
    conn.close()



if __name__ == '__main__':
    generation(2)
