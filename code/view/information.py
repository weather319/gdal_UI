# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_information import  Ui_Information
from mplCodeWrapper import MyMplCanvas, MyStaticMplCanvas, MyDynamicMplCanvas
import sys

class informationwindow(QtWidgets.QWidget):
    def __init__(self):
        super(informationwindow,self).__init__()
        self.UI=Ui_Information()
        self.UI.setupUi(self)
        

        self.widget = MyStaticMplCanvas()
        self.widget.setMinimumSize(QtCore.QSize(0, 150))
        self.widget.setObjectName("widget")
        self.UI.verticalLayout.addWidget(self.widget)
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
