# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
import sys
sys.path.append("..")
from view.Ui_information import  Ui_Information
from model.mplCodeWrapper import MyMplCanvas, MyStaticMplCanvas, MyDynamicMplCanvas


class informationwindow(QtWidgets.QWidget):
    def __init__(self):
        super(informationwindow,self).__init__()
        self.UI=Ui_Information()
        self.UI.setupUi(self)
        
        '''静态画布'''
        self.widget = MyStaticMplCanvas()
        self.widget.setMinimumSize(QtCore.QSize(0, 150))
        self.widget.setObjectName("widget")
        self.UI.verticalLayout.addWidget(self.widget)
        '''动态画布'''
        self.widget_2 = MyDynamicMplCanvas()
        self.widget_2.setMinimumSize(QtCore.QSize(0, 150))
        self.widget_2.setObjectName("widget_2")
        self.UI.verticalLayout.addWidget(self.widget_2)

        self.UI.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.UI.tableWidget.resizeRowsToContents()
        self.UI.tableWidget.setAlternatingRowColors(True)
        '''TODO:创建一个类，该类的功能是从数据库获取水质表，
        然后根据水质表具体内容，循环建立表格的行、列。
        循环内增加文字居中的代码
        item.setTextAlignment(QtCore.Qt.AlignHCenter |  QtCore.Qt.AlignVCenter)'''

if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     information = informationwindow()
     app.setQuitOnLastWindowClosed(True)
     information.show()
     sys.exit(app.exec_())
