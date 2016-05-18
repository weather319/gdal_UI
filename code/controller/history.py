# -*- coding: utf-8 -*-
#from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QHBoxLayout,QLabel, QApplication) 
from PyQt5.QtGui import QPixmap,QImage
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
        '''
        SQL = gdal_sqlite()
        SQL.change_sqlpath('/Users/chensiye/mystuff/gdal_UI/data/water_sensing.db')
        choiceMapId = 'LT51190381991204BJC00'  # TODO:修改为从用户列表处选择的返回值
        image_path = SQL.Read_River_Map(choiceMapId)
        image = QImage(image_path)
        '''
        self.cvImage = cv2.imread(r'/Users/chensiye/zhizi.jpg')
        height, width, byteValue = self.cvImage.shape
        height = int(height/2)
        width = int(width/2)
        self.cvImage = cv2.resize(self.cvImage,(height,width))
        byteValue = byteValue * width
        self.resize(height,width)
        cv2.cvtColor(self.cvImage, cv2.COLOR_BGR2RGB, self.cvImage)

        self.mQImage = QImage(self.cvImage, width, height, byteValue, QImage.Format_RGB888)

        myPixmap = QPixmap.fromImage(self.mQImage)
        myLabel = QLabel(self)
        myLabel.setPixmap(myPixmap)
        hbox = QHBoxLayout(self)
        hbox.addWidget(myLabel)  
        self.setLayout(hbox)  
        self.move(0, 0)  
        self.show()

    def paintEvent(self, QPaintEvent):
        painter = QPainter()
        painter.begin(self)
        painter.drawImage(0, 0, self.mQImage)
        painter.end()
	
if __name__ == "__main__":
     app = QApplication(sys.argv)
     history = historywindow()
     app.setQuitOnLastWindowClosed(True)
     history.show()
     sys.exit(app.exec_())
