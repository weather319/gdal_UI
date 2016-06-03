# -*- coding: utf-8 -*-
#from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QHBoxLayout,QLabel, QApplication) 
from PyQt5.QtGui import QPixmap,QImage,QPainter
import sys
sys.path.append("..")
from view.Ui_history import  Ui_History
from model.SqlGis import gdal_sqlite
import cv2


class historywindow(QWidget):
    def __init__(self):
        super(historywindow,self).__init__()
        self.UI=Ui_History()
        self.UI.setupUi(self) 
        self.show_image()

    def show_image(self):
        SQL = gdal_sqlite()
        SQL.change_sqlpath('/Users/chensiye/mystuff/gdal_UI/data/water_sensing.db')
        choiceMapId = 'LT51190381991204BJC00'  # TODO:修改为从用户列表处选择的返回值
        image_path = SQL.Read_River_Map(choiceMapId)
        print (image_path)
        self.Image = QImage()
        self.Image.load(image_path)
        if self.Image == None:
            print ("图像读取错误")
            sys.exit()
        else:
            height = self.size().height()
            width = self.size().width()
            pixmap = QPixmap.fromImage(self.Image.scaledToHeight(height))
            '''TODO: 修改图像分辨率为适应值'''
            self.UI.label_4.setPixmap(pixmap)
            pix_x = pixmap.size().width()
            pix_y = pixmap.size().height()
            x = int((width - pix_x)/2)
            print (width,height,pix_x,pix_y,x)
            self.UI.label_4.move(x,0)


        
	
if __name__ == "__main__":
     app = QApplication(sys.argv)
     history = historywindow()
     app.setQuitOnLastWindowClosed(True)
     history.show()
     sys.exit(app.exec_())
