# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Anaconda3\Workspace\WQA\view\information.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView

class Ui_Information(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(285, 537)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(30)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
#        需要实现文字不可编辑
        self.verticalLayout.addWidget(self.tableWidget)
#        self.widget = QtWidgets.QWidget(Form)
#        self.widget.setMinimumSize(QtCore.QSize(0, 150))
#        self.widget.setObjectName("widget")
#        self.verticalLayout.addWidget(self.widget)
#        self.widget_2 = QtWidgets.QWidget(Form)
#        self.widget_2.setMinimumSize(QtCore.QSize(0, 150))
#        self.widget_2.setObjectName("widget_2")
#        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "WQA_Information"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "A"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "B"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "C"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "E"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "2"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "3"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "4"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Form", "q1212"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Form", "121212"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("Form", "121"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("Form", "2121"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Information()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
