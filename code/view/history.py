# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_history import  Ui_History
import sys

class historywindow(QtWidgets.QWidget):
    def __init__(self):
        super(historywindow,self).__init__()
        self.UI=Ui_History()
        self.UI.setupUi(self)
        
if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     history = historywindow()
     app.setQuitOnLastWindowClosed(True)
     history.show()
     sys.exit(app.exec_())
