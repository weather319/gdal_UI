# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append("..")
from view.Ui_analysis import Ui_Analysis

class analysiswindow(QtWidgets.QWidget):
    def __init__(self):
        super(analysiswindow,self).__init__()
        self.UI=Ui_Analysis()
        self.UI.setupUi(self)
        

        
if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     analysis = analysiswindow()
     app.setQuitOnLastWindowClosed(True)
     analysis.show()
     sys.exit(app.exec_())
