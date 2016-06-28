# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Anaconda3\Workspace\WQA\view\history.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_History(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1920, 1080)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        '''下拉，月份选择（左上角部分布局，通过弹簧调整位置）'''
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        '''
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        '''
        self.horizontalLayout_2.addWidget(self.comboBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 2)
        self.horizontalLayout_2.setStretch(3, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(0, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        
        '''图片列表'''
        self.treeWidget = QtWidgets.QTreeWidget(Form)
        self.treeWidget.setObjectName("treeWidget")
        self.verticalLayout_2.addWidget(self.treeWidget)
        
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        #设置左边模块比例1:12
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(2, 12)
        self.verticalLayout_2.setStretch(3, 1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        
        '''右边图片显示窗体'''
        '''更改为graphicsView'''
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setObjectName("graphicsView")

        self.verticalLayout.addWidget(self.graphicsView)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        
        '''右下放大缩小按钮（通过弹簧调整位置）'''
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.horizontalLayout_3.setStretch(3, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        #设置右边模块比例为12:1
        self.verticalLayout.setStretch(0, 12)
        self.verticalLayout.setStretch(1, 1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        #设置左边模块与右边模块比例为1:4
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "WQA_History"))
        self.label.setText(_translate("Form", "水体："))
        self.pushButton.setText(_translate("Form", "+"))
        self.pushButton_2.setText(_translate("Form", "-"))


if __name__ == "__main__":

    def show_image():
        from PIL import Image
        from PIL.ImageQt import ImageQt
        #img = Image.open(self.image_path)
        img = Image.open('/Users/chensiye/zhizi.jpg')
        w, h = img.size
        imgQ = ImageQt(img)

        pixMap = QtGui.QPixmap.fromImage(imgQ)
        scene = QtWidgets.QGraphicsScene()
        scene.addPixmap(pixMap)
        return scene
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_History()
    ui.setupUi(Form)
    view = ui.graphicsView
    scene = show_image()
    view.setScene(scene)
    
    Form.show()
    view.fitInView(QtCore.QRectF(0, 0, 1024, 1024), QtCore.Qt.KeepAspectRatio)
    sys.exit(app.exec_())

