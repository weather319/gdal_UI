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

path_sys = os.path.abspath(os.path.dirname(__file__))
#os.path.dirname(path_sys)
def get_conn(path=path_sys + "/../data/water_sensing.db"):
    '''连接到数据库，如果文件路径存在则连接，如果不存在，则报错'''
    if os.path.exists(path) and os.path.isfile(path):
        conn = sqlite3.connect(path)
        print('成功连接到[{}]的数据库'.format(path))
        return conn
    else:
        print('数据库不存在，请检查路径')

def insert_db_blob(table,keywords,content):
	conn = get_conn()
	blob = sqlite3.Binary(content)
	""" 目的是把内容转化成blob格式，然后保存到sql中 """
	try:
		sqli = "INSERT INTO "+ table +" " + " ("+value+") " +\
			"VALUES(%s);"
		conn.execute("INSERT INTO MAP (MapId,ToUserGetRiver) VALUES(%b);"\
					,(MapId,blob)
		conn.commit()
		conn.close()
	except :
		print ("写入数据库失败")
		conn.close()
def update_db():


def insert_db_string(table,value,content,conn):
	sqli = "INSERT INTO "+ table +" " + " ("+value+") " +\
			"VALUES(%s);" 
	conn.execute(sqli %content)
	conn.commit()

def select_db(value,table,keywords,param,conn):
	sql = "SELECT "+ value + " FROM "+ table + " WHERE " + keywords \
			+" =:" + keywords
	cursor = conn.cursor()
	#print (sql,param)
	select = cursor.execute(sql,param)
	return select


"""
name = os.path.join(os.path.dirname(__file__) + '../')
print name
get_conn()


#修改数据库表
conn.execute("update COMPANY set SALARY=30000 where ID=3")
print "Update the table"
conn.commit()

#conn.execute("alter table WaterQuality drop PRIMARY KEY (MapId)")
#conn.execute("update Map set ToUser='LT51190381991204BJC00_mask.jpg' where Time='19910204'")
select = conn.execute("SELECT A, B, C, D  from WaterQuality")

"""