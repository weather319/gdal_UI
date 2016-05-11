# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from osgeo import gdal
import numpy as np
import cv2
import os


file1 = '/Users/chensiye/LT51190381991204BJC00/LT51190381991204BJC00_B1.TIF'
file2 = '/Users/chensiye/LT51190381991204BJC00/LT51190381991204BJC00_B2.TIF'
file3 = '/Users/chensiye/LT51190381991204BJC00/LT51190381991204BJC00_B3.TIF'
file4 = '/Users/chensiye/LT51190381991204BJC00/LT51190381991204BJC00_B4.TIF'
file5 = '/Users/chensiye/LT51190381991204BJC00/LT51190381991204BJC00_B5.TIF'
file6 = '/Users/chensiye/LT51190381991204BJC00/LT51190381991204BJC00_B6.TIF'
file7 = '/Users/chensiye/LT51190381991204BJC00/LT51190381991204BJC00_B7.TIF'

def readtif(path):
    if os.path.exists(path) and os.path.isfile(path):
        print ('成功刚打开[{}]的文件'.format(path))
        dataset = gdal.Open(path)
        name = dataset.GetDescription()
        cols = dataset.RasterXSize
        rows = dataset.RasterYSize
        bands = dataset.RasterCount
        print ("%s image is %s Weights ,%s Heights and %s bands."\
             %(name,rows,cols,bands))
        data = dataset.ReadAsArray()
        print np.shape(data)
        return data
    else:
        print ('打开错误，请检查路径')
        sys.exit()



one = readtif(file1)
two = readtif(file2)
three = readtif(file3)
four = readtif(file4)
five = readtif(file5)
six = readtif(file6)
seven = readtif(file7)

#result = data[1]+data[2]-data[3]-data[4]

#result2 = (two+five)/(four+five)
rgb = cv2.merge([three,four,five])
im = cv2.merge([three,five,seven])
#m,n = np.shape(im)
m,n,_ = np.shape(im)
#im = cv2.resize(im,(m/10,n/10))
#rgb = cv2.resize(rgb,(m/10,n/10))

hsv=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
lower_blue=np.array([110,0,0]) 
upper_blue=np.array([130,255,255])
mask=cv2.inRange(hsv,lower_blue,upper_blue)
res=cv2.bitwise_and(rgb,rgb,mask=mask)


"""
#聚类

Z = np.float32(im.reshape((-1,3)))
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 4
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((im.shape))

#绘制直方图

color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([rgb],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()

cv2.imshow("im",im)
cv2.imshow("mask",mask)
cv2.imshow("result",rgb)
cv2.imshow("res",res)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
#cv2.imwrite('/Users/chensiye/LT51190381991204BJC00/LT51190381991204BJC00_rgb.jpg',rgb)
#cv2.imwrite('/Users/chensiye/LT51190381991204BJC00/LT51190381991204BJC00_mask.jpg',res)
