# -*- coding: utf-8 -*-

from osgeo import gdal
import numpy as np
import cv2
from matplotlib import pyplot as plt


def color_cluster(image):
    # 创建图像副本，创建图像矩阵
    img = image.copy()
    m, n, c = np.shape(img)
    samples = np.zeros([m, n, c], dtype=np.float32)
    clusters = np.zeros([m, n], dtype=np.int32)
"""
cv2.kmeans(data, K, bestLabels, criteria, attempts, flags) 
（1）data: 分类数据，最好是np.float32的数据，每个特征放一列。之所以是np.float32原因是这种数据类型运算速度快，同样的数据下如果是uint型数据将会慢死你。 
(2) K: 分类数，opencv2的kmeans分类是需要已知分类数的。 
(3) bestLabels：预设的分类标签：没有的话 None 
(4) criteria：迭代停止的模式选择，这是一个含有三个元素的元组型数。格式为（type,max_iter,epsilon） 
其中，type又有两种选择： 
—–cv2.TERM_CRITERIA_EPS :精确度（误差）满足epsilon停止。 
—- cv2.TERM_CRITERIA_MAX_ITER：迭代次数超过max_iter停止。 
—-cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER，两者合体，任意一个满足结束。 
（5）attempts：重复试验kmeans算法次数，将会返回最好的一次结果 
（6）flags：初始类中心选择，两种方法 
cv2.KMEANS_PP_CENTERS ; cv2.KMEANS_RANDOM_CENTERS
"""
