# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
import sys
sys.path.append("..")
from view.Ui_main import Ui_MainWindow
from controller.history import historywindow
from controller.information import informationwindow


class mainwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainwindow,self).__init__()
        self.UI=Ui_MainWindow()
        self.UI.setupUi(self)
        #self.setWindowState(QtCore.Qt.WindowMaximized)
        '''
        self.setAutoFillBackground(True) # 设置背景颜色
        self.setStyleSheet("background-color:black;")
        self.setBackgroundRole(QtGui.QPalette.Midlight)
        '''
        self.page = historywindow()
        self.page.setObjectName("page")
        self.UI.stackedWidget.addWidget(self.page)
        
        self.widget = informationwindow()
        self.widget.setObjectName("widget")
        self.UI.gridLayout.addWidget(self.widget, 0, 1, 4, 1)
        print (QtWidgets.QDesktopWidget().availableGeometry())
        print (self.size())
        self.page.updateGeometry()
        print (self.page.size())

def main():
     app = QtWidgets.QApplication(sys.argv)
     main = mainwindow()
     app.setQuitOnLastWindowClosed(True)    
     main.show()
     sys.exit(app.exec_())
