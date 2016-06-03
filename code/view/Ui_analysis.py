# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Anaconda3\Workspace\WQA\view\analysis.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Analysis(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(548, 406)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        
        '''上方图片显示窗体'''
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        
        '''下方按钮模块'''
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setMinimumSize(QtCore.QSize(125, 0))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setMinimumSize(QtCore.QSize(125, 0))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        #设置模块比例为9:1
        self.verticalLayout.setStretch(0, 9)
        self.verticalLayout.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "WQA_Analysis"))
        self.pushButton.setText(_translate("Form", "上传"))
        self.pushButton_2.setText(_translate("Form", "分析"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Analysis()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

