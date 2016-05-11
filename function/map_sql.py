# -*- coding: utf-8 -*-

import os
import numpy as np
from osgeo import gdal
import pandas as pd
import pandas.io.sql as pd_sql
import sqlite3

"""
这个功能是为了选择一个遥感地图后，把相应的数据存储到数据库中，并在显示的时候调用数据库
"""


def get_filelist(path):
	""" 返回目录中所有 tif 文件的相对路径,按照升序排列 """
	""" 相对路径的作用，是为了软件保存在不同的地方不会影响到数据的存储"""
	""" 读取到相对路径后，加载时再加上绝对路径"""
	filelists = [os.path.join(os.path.relpath(path),f) for f in os.listdir(path) if f.endswith('.TIF')]
	""" 一般情况下，读取的文件列表是排序的。为了保险起见，再做一次升序排列 """
	filelists = sorted(filelists,reverse = False)
	return filelists

def get_tifdata(filepath):
	""" 函数为读取一个文件夹下的列表，若遥感列表为1个tif，则读取多个文件。
	若列表为7个tif，则分别读取1个文件中对应的通道。
	返回一个rows*cols*bands（行*列*通道）的矩阵 """
	if len(filelist) == 1:
		try:
			data = read_tif(file[0])
			if (np.shape(data)[2] == 3):
				return data
			else:
				print ("tif为单通道格式，检查tif文件")
		except :
			print ("无法打开tif"), file
	elif len(filelist) == 7:
		try:
			band1 = read_tif(filelist[0])
			if len(band1) == 3:
				print ("tif为多通道格式，检查")
			else:
				m,n = np.shape(band1)
				data = np.zeros([m,n,7])
				data[:,:,0] = band1
				i = 1
				for files in filelist[1:]:
					band_i = read_tif(files)
					data[:,:,i] = band_i
					i = i+1
				return data
		except :
			print ("无法打开tif"), file
	else:
		print ("遥感文件参数异常，请确认tif文件数量！")


def read_tif(path):
    if os.path.exists(path) and os.path.isfile(path):
        print ('成功刚打开[{}]的文件'.format(path))
        dataset = gdal.Open(path)
        name = dataset.GetDescription()
        cols = dataset.RasterXSize
        rows = dataset.RasterYSize
        bands = dataset.RasterCount
        print ("%s image is %s Heights,%s Weights and %s bands."\
             %(name,cols,rows,bands))
        data = dataset.ReadAsArray()
        return data
    else:
        print ('打开错误，请检查路径')

def insert_image_db(MapId,image):
	"""先做查询，如果mapid已有，则update,否则插入数据"""
	conn = get_conn()
	img_blob = sqlite3.Binary(image)
	""" 目的是把image转化成blob格式，然后保存到sql中
		数据库表为river，值为ToUserGetRiver """
	try:
		conn.execute("INSERT INTO MAP (MapId,ToUserGetRiver) VALUES(?,?);",(MapId,img_blob))
		conn.commit()
		conn.close()
	except :
		print ("写入数据库失败")
		conn.close()

def retrieve_image_db(MapId):
	conn = get_conn()
	param = {'MapId':MapId} 
	""" 读取存在数据库中的blob格式图片"""
	try:

		"""
		cursor = conn.cursor()
		sqli = "SELECT ToUserGetRiver FROM MAP WHERE MapId = :mapid"
		cursor.execute(sqli,param)
		image = cursor.fetchone()
		"""
		
		select = select_db_string("ToUserGetRiver","MAP","MapId",param,conn)
		image = select.fetchone()
		conn.close()
		return image
	except :
		print ("读取数据库失败")
		conn.close()


#global path_sys = os.path.abspath(os.path.dirname(__file__))
"""#os.path.dirname(path_sys) #读取文件的目录路径 """

def get_conn(path=os.path.abspath(os.path.dirname(__file__)) + "/../data/water_sensing.db"):
    '''连接到数据库，如果文件路径存在则连接，如果不存在，则报错'''
    if os.path.exists(path) and os.path.isfile(path):
        conn = sqlite3.connect(path)
        print('成功连接到[{}]的数据库'.format(path))
        return conn
    else:
        print('数据库不存在，请检查路径')








	

import cv2
image_path = "/Users/chensiye/mystuff/gdals/2.jpg"
image = cv2.imread(image_path)
MapId = {"MapId":"LT51190381991204BJC00"}
"""
#img_blob = buffer(image)
#insert_image_db(MapId,image)
img = retrieve_image_db(MapId) 
img = np.array(img[0])
img = img.reshape((image.shape))

cv2.imshow("1",img)
cv2.waitKey(0)
cv2.destroyAllWindows

base=os.path.basename(picture_file)
afile, ext = os.path.splitext(base)
"""

#path =  "../../../LT51190381991204BJC00/"
path = "/Users/chensiye/LT51190381991204BJC00"
filelist = get_filelist(path)
frame = pd.DataFrame(filelist,\
		index =['path1','path2','path3','path4','path5','path6','path7'],\
		columns = ['MapId'])
frame = frame.T
#conn = sqlite3.connect('test.db')
conn = get_conn()
#pd_sql.to_sql(frame,name = 'PATH',con=conn)
sqli = "SELECT * FROM MAP"
pd_sql.read_sql(sqli,conn)
""" 把frame写入数据库的表中，当Map存在时，插入，行的值插入到MapId的主键位置。"""
pd_sql.to_sql(frame_T,name= 'Map' ,con=conn,if_exists="append",index_label='MapId')

print filelist
#data = get_tifdata(filelist)
#print np.shape(data)
