# -*- coding: utf-8 -*-
"""
author: Leo li 
the script is connect to db
"""
import pymysql
db_conn = pymysql.connect(
    host='10.74.117.245',
    user='myip',
    password='cisco123',
    db='myip',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with db_conn.cursor() as cursor:
        sql = "SELECT * FROM `myip`"
        cursor.execute(sql)
        result = cursor.fetchall()
    db_conn.commit()
#    print (dict(result[0])['ip'])
    print (result)

finally:
    db_conn.close()