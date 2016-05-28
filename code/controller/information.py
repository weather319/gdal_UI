# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
import sys
sys.path.append("..")
from view.Ui_information import  Ui_Information
from model.mplCodeWrapper import MyMplCanvas, MyStaticMplCanvas, MyDynamicMplCanvas
from model.DrawTable import Gis_DrawTable 
from model.SqlGis import gdal_sqlite


class informationwindow(QtWidgets.QWidget):
    def __init__(self):
        super(informationwindow,self).__init__()
        self.view=Ui_Information()
        self.view.setupUi(self)
        self.DT = Gis_DrawTable()
        self.SQL = gdal_sqlite()
        '''TODO:修改为从用户列表处选择的返回值'''
        self.MapId = 'LT51190381991204BJC00'

        '''静态画布'''
        self.widget = MyStaticMplCanvas()
        self.widget.setMinimumSize(QtCore.QSize(0, 150))
        self.widget.setObjectName("widget")
        self.view.verticalLayout.addWidget(self.widget)
        '''动态画布'''
        self.widget_2 = MyDynamicMplCanvas()
        self.widget_2.setMinimumSize(QtCore.QSize(0, 150))
        self.widget_2.setObjectName("widget_2")
        self.view.verticalLayout.addWidget(self.widget_2)
        '''创建表格'''
        self.creat_table()
        
    '''TODO:creat_table函数移植到main函数中'''    
    def creat_table(self):
        self.view.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.view.tableWidget.resizeRowsToContents()
        self.view.tableWidget.setAlternatingRowColors(True)
        '''从数据库获取水质表，根据水质表具体内容，循环建立表格的行、列。'''
        
        waterframe = self.SQL.Read_WaterQuality(self.MapId)
        print (waterframe)
        print (type(waterframe.ix[1,1]))
        self.view.tableWidget = self.DT.draw_table(waterframe,self.view.tableWidget)






if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     information = informationwindow()
     app.setQuitOnLastWindowClosed(True)
     information.show()
     sys.exit(app.exec_())
