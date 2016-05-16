# -*- coding: utf-8 -*-

import sqlite3
import os
import sys

'''
SQLite数据库是一款非常小巧的嵌入式开源数据库软件，也就是说
没有独立的维护进程，所有的维护都来自于程序本身。
在python中，使用sqlite3创建数据库的连接，当我们指定的数据库文件不存在的时候
连接对象会自动创建数据库文件；如果数据库文件已经存在，则连接对象不会再创建
数据库文件，而是直接打开该数据库文件。
连接对象可以是硬盘上面的数据库文件，也可以是建立在内存中的，在内存中的数据库
执行完任何操作后，都不需要提交事务的(commit)

创建在硬盘上面： conn = sqlite3.connect('c:\\test\\test.db')
创建在内存上面： conn = sqlite3.connect('"memory:')

下面我们一硬盘上面创建数据库文件为例来具体说明：
conn = sqlite3.connect('c:\\test\\hongten.db')
其中conn对象是数据库链接对象，而对于数据库链接对象来说，具有以下操作：

commit()            --事务提交
rollback()          --事务回滚
close()             --关闭一个数据库链接
cursor()            --创建一个游标

cu = conn.cursor()
这样我们就创建了一个游标对象：cu
在sqlite3中，所有sql语句的执行都要在游标对象的参与下完成
对于游标对象cu，具有以下具体操作：

execute()           --执行一条sql语句
executemany()       --执行多条sql语句
close()             --游标关闭
fetchone()          --从结果中取出一条记录
fetchmany()         --从结果中取出多条记录
fetchall()          --从结果中取出所有记录
scroll()            --游标滚动

'''

path_sys = os.path.abspath(os.path.dirname(sys.argv[0]))

def get_conn(path="/Users/chensiye/mystuff/UI_2016.4.27/data/water_sensing.db"):
    '''连接到数据库，如果文件路径存在则连接，如果不存在，则报错'''
    if os.path.exists(path) and os.path.isfile(path):
        conn = sqlite3.connect(path)
        print('成功连接到[{}]的数据库'.format(path))
        return conn
    else:
        print('打开错误，请检查路径')


def insert_db_string(content,value,table,conn):
	sql = "INSERT INTO "+ table +" " + " ("+value+") " +\
			"VALUES(%s)" 
	conn.execute(sql %content)
	conn.commit()

def select_db(value,table,conn):
	sql = "SELECT "+ value + " from "+ table
	select = conn.execute(sql)
	return select
"""
def extract_picture(cursor, picture_id):
    sql = "SELECT PICTURE, TYPE, FILE_NAME FROM PICTURES WHERE id = :id"
    param = {'id': picture_id}
    cursor.execute(sql, param)
    ablob, ext, afile = cursor.fetchone()
    filename = afile + ext
    with open(filename, 'wb') as output_file:
        output_file.write(ablob)
    return filename

"""
    
    


DB_NAME = 'water_sensing1.db'
#conn = sqlite3.connect(DB_NAME)
#conn = get_coon(DB_NAME)
# print "Opened databas sucessfully"
"""
#修改数据库表
conn.execute("update COMPANY set SALARY=30000 where ID=3")
print "Update the table"
conn.commit()
"""
"""
#conn.execute("alter table WaterQuality drop PRIMARY KEY (MapId)")
#conn.execute("update Map set ToUser='LT51190381991204BJC00_mask.jpg' where Time='19910204'")
select = conn.execute("SELECT A, B, C, D  from WaterQuality")
for row in select:
print row
# print row[1]
# print row[2]
# print row[3]
conn.commit()
conn.close()
"""