# -*- coding: utf-8 -*-

import os
import numpy as np
from osgeo import gdal

def get_filelist(path):
	""" 返回目录中所有 tif 图像的文件名列表,按照升序排列 """
	filelists = [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.TIF')]
	""" 一般情况下，读取的文件列表是排序的。为了保险起见，再做一次升序排列 """
	filelists = sorted(filelists,reverse = False)
	return filelists

def get_tifdata(filelists):
	""" 函数为读取一个文件夹下的列表，若遥感列表为1个tif，则读取多个文件。
	若列表为7个tif，则分别读取1个文件中对应的通道。
	返回一个rows*cols*bands（行*列*通道）的矩阵 """
	if len(filelists) == 1:
			data = read_tif(file[0])
			if (np.shape(data)[2] == 3):
				print ('成功读取data')
				return data
			else:
				print ("tif为单通道格式，检查tif文件")
	elif len(filelists) == 7:
		band1 = read_tif(filelists[0])
		if len(band1) == 3:
			print ("tif为多通道格式，检查")
		else:
			m,n = np.shape(band1)
			data = np.zeros([m,n,7])
			data[:,:,0] = band1
			i = 1
			for files in filelists[1:]:
				band_i = read_tif(files)
				data[:,:,i] = band_i
				i = i+1
			return data
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

def read_wkt_GT(path):
	if os.path.exists(path) and os.path.isfile(path):
		print ('成功刚打开[{}]的文件读取wkt,GT'.format(path))
		dataset = gdal.Open(path)
		wkt = dataset.GetProjectionRef()
		GT = dataset.GetGeoTransform()
		return wkt,GT
	else:
		print ('路径出错')


import sql
import sqlite3
def insert_image_db(MapId,image):
	sql_path = "/Users/chensiye/mystuff/UI_2016.4.27/data/water_sensing.db"
	conn = sql.get_conn(sql_path)
	#img_blob = sqlite3.Binary(image)
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
	sql_path = "/Users/chensiye/mystuff/UI_2016.4.27/data/water_sensing.db"
	conn = sql.get_conn(sql_path)
	cursor = conn.cursor()
	""" 读取存在数据库中的blob格式图片"""
	try:
		sqli = "SELECT ToUserGetRiver FROM MAP WHERE MapId = :mapid"
		param = {'mapid':MapId} 
		cursor.execute(sqli,param)
		image = cursor.fetchone()
		conn.close()
		return image
	except :
		print ("读取数据库失败")
		conn.close()



'''
path = '/Users/chensiye/LT51190381991204BJC00'
filelists = get_filelist(path)
data = get_tifdata(filelists)
wkt,GT = read_wkt_GT(filelists[0])


import cv2
image_path = "/Users/chensiye/mystuff/gdals/2.jpg"
image = cv2.imread(image_path)
MapId = "LT51190381991204BJC00"
#img_blob = buffer(image)
#insert_image_db(MapId,image)
img = retrieve_image_db(MapId) 
img = np.array(img[0])
img = img.reshape((image.shape))

cv2.imshow("1",img)
cv2.waitKey(0)
cv2.destroyAllWindows

'''

