# -*- coding: utf-8 -*-
'''导入python模块'''
import os
import pandas.io.sql as pd_sql
import pandas as pd
import sqlite3
import ast

'''导入自定义功能'''


'''本功能是查询读取遥感图片的相关信息
一、读取图片的内容包括：
	1 河流ID，Name————》显示下拉框
	2 读取遥感地图列表
	3 读取遥感地图对应的存储路径
	4 读取图片
二、读取水质参数：

三、读取录像

'''
class gdal_sqlite(object):
	def __init__(self):
		self.sql_path = os.path.abspath(os.path.dirname(__file__)) + "/../../data/water_sensing.db"

	def change_sqlpath(self,path):
		self.sql_path = path

	def get_conn(self):
	    '''连接到数据库，如果文件路径存在则连接，如果不存在，则报错'''
	    path = self.sql_path
	    if os.path.exists(path) and os.path.isfile(path):
	        conn = sqlite3.connect(path)
	        print('成功连接到[{}]的数据库'.format(path))
	        return conn
	    else:
	        print('数据库不存在，请检查路径')
	
	'''获取所有的river列表'''
	def Read_riverlist(self):
		sql = "SELECT * FROM River"
		conn = self.get_conn()
		river_list = pd_sql.read_sql(sql,conn)
		conn.close()
		return river_list

	'''读取河流ID,然后用河流ID查找”河流-遥感地图”关系表'''
	def Read_maplist(self,RiverId):
		sql = "SELECT MapId FROM River_Map WHERE RiverId='%s'" %RiverId
		conn = self.get_conn()
		map_list = pd_sql.read_sql(sql,conn)
		conn.close()
		return map_list
		
	'''获取MapId后，读取处理前遥感RGB图片和处理后河流图片'''
	def Read_GisRGB_Map(self,MapId):
		sql = "SELECT RGBImage FROM Map WHERE MapId='%s'" %MapId
		conn = self.get_conn()
		frame = pd_sql.read_sql(sql,conn)
		image_path = frame['RGBImage'][0]
		conn.close()
		return image_path

	def Read_River_Map(self,MapId):
		sql = "SELECT RiverImage FROM Map WHERE MapId='%s'" %MapId
		conn = self.get_conn()
		frame = pd_sql.read_sql(sql,conn)
		image_path = frame['RiverImage'][0]
		conn.close()
		return image_path

	'''获取MapId,读取水质表'''	
	'''FROM (表1 INNER JOIN 表2 ON 表1.字段号=表2.字段号) INNER JOIN 表3 ON 表1.字段号=表3.字段号'''
	def Read_WaterQuality(self,MapId):
		sql = "SELECT ObStation_WaterQuility.StationId,\
						WaterQuility.WaterQualityTime,\
						WaterQuility.WaterQualityInfo,\
						WaterQuility.WaterQualityId \
			FROM (Map_ObStation INNER JOIN ObStation_WaterQuility \
        	ON Map_ObStation.StationId = ObStation_WaterQuility.StationId )\
			INNER JOIN WaterQuility \
			ON ObStation_WaterQuility.WaterQualityId = WaterQuility.WaterQualityId \
        	WHERE Map_ObStation.MapId = '%s' " %MapId
		conn = self.get_conn()
		water_frame = pd_sql.read_sql(sql,conn)
		conn.close()
		dicts = {}
		for i in range(len(water_frame.values)):
			dicts[water_frame["StationId"][i]] = ast.literal_eval(water_frame["WaterQualityInfo"][i])
		water_frame_resut = pd.DataFrame(dicts).T
		return water_frame_resut

	'''获取RiverId，返回录像列表'''
	'''FROM (表1 INNER JOIN 表2 ON 表1.字段号=表2.字段号)'''
	def Read_VedioList(self,RiverId,StartTime,EndTime):
		sql = "SELECT Video.VideoPath,Video.VideoTime \
				FROM Video INNER JOIN River_Video \
        		ON Video.VideoId = River_Video.VideoId \
        		WHERE River_Video.RiverId = '%s'\
        		and Video.VideoTime >= '%s' \
        		and Video.VideoTime <='%s'" %(RiverId,StartTime,EndTime)
		conn = self.get_conn()
		vedio_list = pd_sql.read_sql(sql,conn)
		conn.close()
		return vedio_list




















