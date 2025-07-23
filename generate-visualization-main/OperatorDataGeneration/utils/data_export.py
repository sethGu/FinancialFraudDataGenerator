# @Time    : 2023/5/17 22:01
# @Author  : SuperRich Liu
import os

from OperatorDataGeneration.src import mysql_db
import pandas as pd


def export(path):
    conn = mysql_db.MysqlDB()
    tablename = 'operator'
    contents = conn.select(tablename=tablename, fields='*')
    conn.close()
    df = pd.DataFrame(
        columns=[
            'id',
            'original_ID',
            'contactor',
            'contactor_ID',
            'mobile_phone_brand',
            'mobile_operating_system',
            'pv',
            'terminal_type',
            'video_website',
            'shopping_website',
            'overseas_taobao_shopping_channel',
            'automotive_website',
            'real_estate_website',
            'travel_website',
            'highest_calling',
            'city_number',
            'day_calling',
            'night_calling',
            'three_month_calling',
        ]
    )
    for index, content in enumerate(contents):
        df.loc[index] = [
            content[0],
            content[1],
            content[2],
            content[3],
            content[4],
            content[5],
            content[6],
            content[7],
            content[8],
            content[9],
            content[10],
            content[11],
            content[12],
            content[13],
            content[14],
            content[15],
            content[16],
            content[17],
            content[18],
        ]
    df.to_csv(os.path.join(path, 'operator.csv'), index=False, encoding='gbk')


if __name__ == '__main__':
    export()
