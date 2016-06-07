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
        '''TODO：view文件构建qt的布局。
        contro函数中的py文件，负责构造具体内容、按钮样式、生成图片等
        所有的触发公共接口都留到main.py中，后期根据具体需求考虑多线程。 '''
        self.view=Ui_MainWindow()
        self.view.setupUi(self)
        self.load_windows()
        '''TODO:调整背景
        self.setAutoFillBackground(True) # 设置背景颜色
        self.setStyleSheet("background-color:black;")
        self.setBackgroundRole(QtGui.QPalette.Midlight)
        '''

    def load_windows(self):
        self.page = historywindow()
        self.widget = informationwindow()
        self.page_2 = analysiswindow()
        self.page_3 = Player(sys.argv[1:])

        self.page.setObjectName("page")
        self.view.stackedWidget.addWidget(self.page)
    
        self.widget.setObjectName("widget")
        self.view.gridLayout.addWidget(self.widget, 0, 1, 4, 1)

        
        self.page_2.setObjectName("page_2")
        self.view.stackedWidget.addWidget(self.page_2)     
        
        self.page_3.setObjectName("page_3")
        self.view.stackedWidget.addWidget(self.page_3)

        '''按钮触发'''
        self.view.pushButton.clicked.connect(self.changed_history)
        self.view.pushButton_2.clicked.connect(self.changed_analysis)
        self.view.pushButton_3.clicked.connect(self.changed_video)

    def update_information():
        '''TODO:把history.py的函数调用中的数据接口部分放到main中，
            目的是：用户在选取MapId后，数据库的操作放到main中'''
        pass

    def upadte_history():
        pass

    '''按钮触发对应函数'''  
    def changed_history(self):
        self.view.stackedWidget.setCurrentIndex(0)
    def changed_analysis(self):
        self.view.stackedWidget.setCurrentIndex(1)
    def changed_video(self):
        self.view.stackedWidget.setCurrentIndex(2)


def main():
     app = QtWidgets.QApplication(sys.argv)
     main = mainwindow()
     app.setQuitOnLastWindowClosed(True)    
     main.show()
     sys.exit(app.exec_())



















