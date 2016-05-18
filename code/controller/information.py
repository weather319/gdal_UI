# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
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
        
if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     information = informationwindow()
     app.setQuitOnLastWindowClosed(True)
     information.show()
     sys.exit(app.exec_())
