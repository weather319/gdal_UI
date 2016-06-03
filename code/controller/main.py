# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
import sys
sys.path.append("..")
from view.Ui_main import Ui_MainWindow
from controller.history import historywindow
from controller.information import informationwindow
from controller.analysis import analysiswindow
from controller.player import Player


class mainwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainwindow,self).__init__()
        self.UI=Ui_MainWindow()
        self.UI.setupUi(self)
        
        '''
        self.setAutoFillBackground(True) # 设置背景颜色
        self.setStyleSheet("background-color:black;")
        self.setBackgroundRole(QtGui.QPalette.Midlight)
        '''
        self.page = historywindow()
        self.page.setObjectName("page")
        self.UI.stackedWidget.addWidget(self.page)
		
		self.page_2 = analysiswindow()
        self.page_2.setObjectName("page_2")
        self.UI.stackedWidget.addWidget(self.page_2)
		
		self.page_3 = Player(sys.argv[1:])
        self.page_3.setObjectName("page_3")
        self.UI.stackedWidget.addWidget(self.page_3)
        
        self.widget = informationwindow()
        self.widget.setObjectName("widget")
        self.UI.gridLayout.addWidget(self.widget, 0, 1, 4, 1)

def main():
     app = QtWidgets.QApplication(sys.argv)
     main = mainwindow()
     app.setQuitOnLastWindowClosed(True)
     #main.showMaximized()
     main.setWindowState(QtCore.Qt.WindowMaximized)
     main.show()
     sys.exit(app.exec_())
