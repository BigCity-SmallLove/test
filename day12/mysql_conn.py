# Author:Jacke

import pymysql

# 创建连接
conn = pymysql.connect(host='192.168.0.103', port=3306, user='root', passwd='1234', db='yi')

# 创建游标
cursor = conn.cursor()

# 执行SQL，并返回收影响行数
effect_row = cursor.execute("desc student")
print(effect_row)   #一共有多少行
#print(cursor.fetchone())    #显示一行
print("--------------")
print(cursor.fetchall())        #显示所有详情(类似读文件)

