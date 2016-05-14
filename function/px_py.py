# -*- coding: utf-8 -*-

from osgeo import gdal
import osr
import os,sys



'''把得到的平面直角坐标转化成WGS84经纬度坐标'''
'''原始坐标的投影系统用sr来表示，是由读取的TIF遥感图像决定的'''
def wkt_WGS84(xsize,ysize,wkt):
	'''首先建立2个投影坐标系，然后分别导入相应的坐标参数'''
	object_Long = osr.SpatialReference()
	object_xy = osr.SpatialReference()
	object_xy.ImportFromWkt(wkt)
	object_Long.SetWellKnownGeogCS("WGS84")
	'''建立转化方程，返回WGS84经纬度'''
	ct = osr.CoordinateTransformation(object_xy,object_Long)
	Latitude,longitude,High = ct.TransformPoint(xsize,ysize)
	print ('经过转化的WGS84经纬度为(%s,%s)' %(Latitude,longitude))
	return Latitude,longitude
'''把经纬度转化成平面直角坐标系统'''
def WGS84_wkt(Latitude,longitude,wkt):
	object_Long = osr.SpatialReference()
	object_xy = osr.SpatialReference()
	object_xy.ImportFromWkt(wkt)
	object_Long.SetWellKnownGeogCS("WGS84")
	ct = osr.CoordinateTransformation(object_Long,object_xy)
	xsize,ysize,zsize = ct.TransformPoint(Latitude,longitude,0.0)
	GeoX = float(int(xsize+0.5))
	GeoY = float(int(ysize+0.5))
	print ('经过转化的仿射坐标为(%s,%s)' %(xsize,ysize))
	return GeoX,GeoY

def Geo_Points(FileX,FileY,GT):
	GeoX = GT[0] + FileX * GT[1] + FileY * GT[2]
	GeoY = GT[3] + FileX * GT[4] + FileY * GT[5]
	print ('转化后的仿射坐标为(%s,%s)' %(GeoX,GeoY))
	return GeoX,GeoY

def File_points(GeoX,GeoY,GT):
	FileX = float((GeoX * GT[5] - GeoY * GT[2] -  GT[0] * GT[5] + GT[2] * GT[3]) /  (GT[1] * GT[5] - GT[2] * GT[4]))
 	FileY = float((GeoX * GT[4] - GeoY * GT[1] -  GT[0] * GT[4] + GT[1] * GT[3]) /  (GT[2] * GT[4] - GT[1] * GT[5]))
 	FileX = int(FileX+0.5)
 	FileY = int(FileY+0.5)
 	print ('转化后的图像坐标为(%s,%s)' %(FileX,FileY))
 	return FileX,FileY


"""
'''测试，读取文件'''
path_sys = os.path.abspath(os.path.dirname(sys.argv[0]))
filePath_1 = '/Users/chensiye/LT51190381991204BJC00/LT51190381991204BJC00_B1.TIF'
filePath_2 = '../LT51190392000309BJC00_B1.TIF'
dataset = gdal.Open(filePath_1)
#dataset = gdal.Open(path_sys+'/'+filePath_2) 
''' 使用绝对路径+相对路径避免不同操作系统的路径问题'''

'''获得tif的坐标，其中左上角的坐标为[0],[3]'''
adfGeoTransform = dataset.GetGeoTransform()
'''获得tif的投影坐标系统'''
wkt = dataset.GetProjectionRef()

''' 右下角的仿射坐标x,y'''
nXSize = dataset.RasterXSize #列数
nYSize = dataset.RasterYSize #行数
zero_x,zero_y = Geo_Points(0,0,adfGeoTransform)
rd_x,rd_y = Geo_Points(nXSize,nYSize,adfGeoTransform)


print ('所读取遥感图片的仿射系统参数为[{}]'.format(adfGeoTransform))
'''测试，把原点和右下角点转换成经纬度)'''
print ('原点的仿射坐标为(%s,%s)' %(zero_x,zero_y))
WGS84_zero_x,WGS84_zero_y= wkt_WGS84(zero_x,zero_y,wkt)
print ('右下角的仿射坐标为(%s,%s)' %(rd_x,rd_y))
WGS84_rd_x,WGS84_rd_y = wkt_WGS84(rd_x,rd_y,wkt)

'''测试，把得到的2个经纬度转化回仿射坐标'''
print ('原点的经纬度为(%s,%s)' %(WGS84_zero_x,WGS84_zero_y))
xsize0,ysize0 = WGS84_wkt(WGS84_zero_x,WGS84_zero_y,wkt)

'''测试，把仿射坐标对应到图像坐标'''
print ('右下角的图像坐标为(%s,%s)' %(nXSize,nYSize))
print ('右下角的仿射坐标为(%s,%s)' %(rd_x,rd_y))
file_rd_x,file_rd_y = File_points(rd_x,rd_y,adfGeoTransform)







arrSlope = [] # 用于存储每个像素的（X，Y）坐标
for i in range(nYSize):
    row = []
    for j in range(nXSize):
        px = adfGeoTransform[0] + j * adfGeoTransform[1] + i * adfGeoTransform[2]
        py = adfGeoTransform[3] + j * adfGeoTransform[4] + i * adfGeoTransform[5]
        col = [px, py]
        row.append(col)
    arrSlope.append(row)

print(len(arrSlope))


"""
