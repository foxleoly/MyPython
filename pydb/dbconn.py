# -*- coding: utf-8 -*-
"""
author: Leo li 
the script is connect to db
"""
"""
import pymysql
db_conn = pymysql.connect(
    host='1.1.1.1',
    user='myip',
    password='123',
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
"""
from lxml import etree
xmlFile = open('dbip.xml', 'r')
r.xpath(xmlFile)
