# -*- coding: utf-8 -*-
#! /usr/bin/env python

import sys
from PyQt4 import QtGui, QtCore

import os, string
import math

THUMB_WIDTH = 128
THUMB_HEIGHT = 128
THUMB_MIN = 64
THUMB_MAX = 256
FILE_TYPE = ['jpg', 'jpeg', 'tif', 'bmp', 'gif']

class ImageWidget(QtGui.QWidget):
    
    #单选,上一个被选择的对象
    prevSelected = None
    
    """
    Use this widget to display image.
    """
    def __init__(self):
        super(ImageWidget, self).__init__()
        self.id = 0
        self.displayText = ''      #显示的文字
        self.version = ''
        self.status = 0
        self.path = ''
        self.showStatus = True
        self.selected = False
        self.isHightlight = False
        self.thumb = QtGui.QImage()
        self.initAttrib()
    
    def initAttrib(self):
        self.name_font = QtGui.QFont()
        self.bg_color = QtGui.QColor(50, 50, 50)
        self.hightlight = QtGui.QColor(255, 255, 255, 100)
        self.edge_size = 5
        self.pen_selected = QtGui.QPen(QtGui.QColor(255, 255, 0))
        self.pen_selected.setWidth(self.edge_size) 
        self.pen_selected.setJoinStyle(QtCore.Qt.MiterJoin)
#        self.setToolTip('aaaa\nbbbb\ncccc')

    def assetFile(self):
        return self.path + "_asset_.txt"

    def thumbFile(self):
        return self.path + "_thumb_.png"

    def informationFile(self):
        return self.path + "_information_.txt"

    def getPublishPath(self):
        current_version = self.version
        if not current_version:
            current_version = '000'
        new_version = int(string.atof(current_version)) + 1
        return '%s/%03d' % (self.path, new_version)

    def getVersionPath(self, version):
        return '%s/%s' % (self.path, version)

    def getCurrentVersionPath(self):
        return self.getVersionPath(self.version)

    def setThumb(self, thumb = None):
        if not thumb:
            thumb = self.thumbFile()
        if os.path.isfile(thumb):
            self.thumb.load(QtCore.QString(thumb))
            self.repaint()
            return True

    def paintAsThumb(self, painter):
        name_height = max(self.height() * 0.15, 20)
        name_ty = self.height() - self.edge_size * 2
        # draw background
        painter.fillRect(self.rect(), self.bg_color)
        painter.drawImage(self.rect(), self.thumb)
        # draw hightlight
        if self.isHightlight and not self.selected:
            painter.fillRect(self.rect(), self.hightlight)
        # draw name
        painter.setPen(QtGui.QPen(QtGui.QColor(255, 255, 255)))
        self.name_font.setPixelSize(name_height)
        painter.setFont(self.name_font)
        #脚标字符
        painter.drawText(self.edge_size, name_ty, str(self.displayText))
        
        if self.status:
            title_height = self.edge_size + name_height
            p1 = QtCore.QPoint(0, 0)
            p2 = QtCore.QPoint(0, title_height)
            p3 = QtCore.QPoint(title_height, 0)
            painter.setPen(QtCore.Qt.NoPen)
            painter.fillRect(0, 0, self.width(), title_height, QtGui.QColor(40, 40, 40, 40))
            if self.status == 1:
                painter.setBrush(QtGui.QBrush(QtGui.QColor(255, 0, 0)))
            elif self.status == 2:
                painter.setBrush(QtGui.QBrush(QtGui.QColor(0, 255, 0)))
            elif self.status == 3:
                painter.setBrush(QtGui.QBrush(QtGui.QColor(0, 0, 255)))
            painter.drawConvexPolygon(p1, p2, p3)

        if self.version:
            version_x = self.width() - self.edge_size - name_height * 1.5
            version_y = name_height
            painter.setPen(QtGui.QPen(QtGui.QColor(255, 255, 255)))
            painter.drawText(version_x, version_y, '%s' % self.version)

        # draw selected
        if self.selected:
            painter.setPen(self.pen_selected)
            painter.setBrush(QtCore.Qt.NoBrush)
            painter.drawRect(self.edge_size/2, self.edge_size/2,\
                self.width() - self.edge_size, self.height() - self.edge_size)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        self.paintAsThumb(painter)

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.setSelected()

    def mouseDoubleClickEvent(self, event):
        self.emit(QtCore.SIGNAL('doubleClick'))
    
    def enterEvent(self, event):
        self.isHightlight = True
        self.repaint()

    def leaveEvent(self, event):
        self.isHightlight = False
        self.repaint()
    
    #设定当前为选中状态
    def setSelected(self):
        #取消其他缩略图的选择状态, 当前设为选择状态
        if ImageWidget.prevSelected != None:
            ImageWidget.prevSelected.selected = False
            ImageWidget.prevSelected.repaint()
        self.selected = True
        self.repaint()
        ImageWidget.prevSelected = self
        
        self.onWidgetClicked()
        self.emit(QtCore.SIGNAL("click"), self.id)
    
    def onWidgetClicked(self):
        print 'on widget clicked'
    
class ImageContainer(QtGui.QFrame):
    
    def __init__(self, widgets = None):
        super(ImageContainer, self).__init__()
        
        containerLayout = QtGui.QVBoxLayout()
        
        #初始化Slider
        self.zoomSlider = QtGui.QSlider()
        self.zoomSlider.setOrientation(QtCore.Qt.Horizontal)
        self.zoomSlider.setMinimum(THUMB_MIN)
        self.zoomSlider.setMaximum(THUMB_MAX)
        self.zoomSlider.setValue(THUMB_WIDTH)
        self.zoomSlider.setFixedWidth(128)
        self.zoomSlider.setFixedHeight(10)
        
        #Slider设定
        QtCore.QObject.connect(self.zoomSlider, QtCore.SIGNAL('valueChanged(int)'), self.setItemSize)

        self.item_scrollarea = QtGui.QScrollArea()
        self.item_area = QtGui.QWidget()
        self.item_scrollarea.setWidget(self.item_area)
        
        containerLayout.addWidget(self.zoomSlider)
        containerLayout.addWidget(self.item_scrollarea)
        
        self.widget_w = THUMB_WIDTH
        self.widget_h = THUMB_HEIGHT
        self.min_width = THUMB_MIN
        self.max_height = THUMB_MAX
        self.asset_space = 2
        self.auto_space = False

        self.setWindowOpacity(0.0)
        
        self.setLayout(containerLayout)
        
        #缩略图对象列表
        self.ImageWidgetList = {}
    
    def addWidget(self, widget):
        widget.setParent(self.item_area)
        widget.resize(self.widget_w, self.widget_h)
        widget.show()
        #添加到列表
        self.ImageWidgetList[str(widget.id)] = widget
    
    def addWidgets(self, widgets):
        for widget in widgets:
            self.addWidget(widget)
        self.layout()
            
    def clearAll(self):
        widgets = self.item_area.children()
        if widgets:
            for widget in widgets:
                widget.setParent(None)
        
        self.ImageWidgetList.clear()
        
        
    def layout(self):
        w = self.width() - 20
        widgets = self.item_area.children()

        num_x = max(math.ceil(w / (self.widget_w + self.asset_space)), 1)  # Can do -1
        num_y = max(math.ceil(w / (self.widget_h + self.asset_space)), 1)
        self.item_area.resize(w, num_y * (self.widget_h + self.asset_space) + 50)

        main_w = self.item_area.width()
        main_h = self.item_area.height()
        num_x = max(math.ceil(main_w / (self.widget_w + self.asset_space)), 1)  # Can do -1
        num_y = max(math.ceil(main_h / (self.widget_h + self.asset_space)), 1)
        
        x = 0
        y = 0
        for i in range(len(widgets)):
            space_x = 0
            if self.auto_space:
                space_x = (main_w - self.asset_space * 2 - num_x * (self.widget_w + self.asset_space)) / num_x
            widgets[i].move(self.asset_space * 2 + x * (self.widget_w + self.asset_space + space_x), \
                self.asset_space*2 + y * (self.widget_h + self.asset_space))
            x += 1
            if x >= num_x:
                x = 0
                y += 1
                
    def resizeEvent(self, event):
        self.layout()
    
    def changeItemSize(self, mount):
        widgets = self.item_area.children()
        self.widget_w += mount
        if self.widget_w > self.max_height:
            self.widget_w = self.max_height
        elif self.widget_w < self.min_width:
            self.widget_w = self.min_width
        
        self.widget_h += mount
        if self.widget_h > self.max_height:
            self.widget_h = self.max_height
        elif self.widget_h < self.min_width:
            self.widget_h = self.min_width
        
        for a in widgets:
            a.resize(self.widget_w, self.widget_h)
        
        self.layout()
        
    def setItemSize(self, size):
        widgets = self.item_area.children()
        
        self.widget_w = size
        self.widget_h = size
        
        for a in widgets:
            a.resize(size, size)
        
        self.layout()
    
    #设定指定id为选中状态
    def setSelected(self, id):
        print 'ImageContainer -> setSelected    ', id
        self.ImageWidgetList[str(id)].setSelected()

class MainWindow(QtGui.QWidget):    
    
    def __init__(self):
        app = QtGui.QApplication(sys.argv)
        super(MainWindow, self).__init__()
        
        self.setWindowTitle("Image Viewer")
        self.resize(1280,800)
        
        #屏幕居中
        self.screen = QtGui.QDesktopWidget().screenGeometry()
        self.size = self.geometry()
        self.move((self.screen.width()-self.size.width())/2, (self.screen.height()-self.size.height())/2)
        
        self.show()
        
        mainSpliter = QtGui.QSplitter(QtCore.Qt.Horizontal)
        
        #文件夹列表model
        self.dirModel = QtGui.QDirModel(self)
        
        #只显示文件夹
        self.dirModel.setFilter(QtCore.QDir.Dirs|QtCore.QDir.NoDotAndDotDot)
        
        #文件夹列表view
        self.dirTreeView = QtGui.QTreeView()
        
        #绑定model
        self.dirTreeView.setModel(self.dirModel)
        
        self.dirTreeView.hideColumn(1)
        self.dirTreeView.hideColumn(2)
        self.dirTreeView.hideColumn(3)
        
        #DirTree事件响应
        self.dirTreeView.selectionModel().selectionChanged.connect(self.dirTreeClicked)
        
        mainLayout = QtGui.QVBoxLayout()
        mainSpliter.addWidget(self.dirTreeView)
        
        self.imageContainer = ImageContainer(mainSpliter)
#        self.imageContainer.setGeometry(self.imageContainer.geometry().x(), self.imageContainer.geometry().y(), 100, self.imageContainer.geometry().height())
        self.imageContainer.setMinimumWidth(self.geometry().width()*0.7)
        mainSpliter.addWidget(self.imageContainer)
        
        mainLayout.addWidget(mainSpliter)
        
        self.setLayout(mainLayout)
        
        sys.exit(app.exec_())
    
    def dirTreeClicked(self):
        print 'dirTreeClicked'
        
        self.imageContainer.clearAll()
        
        #获取选择的路径
        pathSelected = self.dirModel.filePath(self.dirTreeView.selectedIndexes()[0])
        print 'pathSelected   ', pathSelected
        #遍历路径下的媒体文件
        for item in os.listdir(pathSelected):
            if item.split('.')[-1] in FILE_TYPE:
                print item
                #添加widget
                try:
                    widget = ImageWidget()
                    widget.displayText = item
                    widget.setThumb(unicode(pathSelected +'/' + item))
                    self.imageContainer.addWidget(widget)
                except:
                    pass
#        self.imageContainer.layout()
        
def main():    
    
    MainWindow()
    
if __name__ == '__main__':
    main()
