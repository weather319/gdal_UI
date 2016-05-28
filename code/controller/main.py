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
        '''TODO：view文件构建qt的布局。
        contro函数中的py文件，负责构造具体内容、按钮样式、生成图片等
        所有的触发公共接口都留到main.py中，后期根据具体需求考虑多线程。 '''
        self.view=Ui_MainWindow()
        self.view.setupUi(self)
        '''TODO:调整背景
        self.setAutoFillBackground(True) # 设置背景颜色
        self.setStyleSheet("background-color:black;")
        self.setBackgroundRole(QtGui.QPalette.Midlight)
        '''
        self.page = historywindow()
        self.widget = informationwindow()

        self.page.setObjectName("page")
        self.view.stackedWidget.addWidget(self.page)
    
        self.widget.setObjectName("widget")
        self.view.gridLayout.addWidget(self.widget, 0, 1, 4, 1)

    def update_information():
        '''TODO:把history.py的函数调用中的数据接口部分放到main中，
            目的是：用户在选取MapId后，数据库的操作放到main中'''
        pass

    def upadte_history():
        pass



def main():
     app = QtWidgets.QApplication(sys.argv)
     main = mainwindow()
     app.setQuitOnLastWindowClosed(True)    
     main.show()
     sys.exit(app.exec_())
