# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_main import Ui_MainWindow
from history import historywindow
from information import informationwindow
import sys

class mainwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainwindow,self).__init__()
        self.UI=Ui_MainWindow()
        self.UI.setupUi(self)
        
        self.page = historywindow()
        self.page.setObjectName("page")
        self.UI.stackedWidget.addWidget(self.page)
        
        self.widget = informationwindow()
        self.widget.setObjectName("widget")
        self.UI.gridLayout.addWidget(self.widget, 0, 1, 4, 1)
        
if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     main = mainwindow()
     app.setQuitOnLastWindowClosed(True)
     main.showMaximized()
     sys.exit(app.exec_())
