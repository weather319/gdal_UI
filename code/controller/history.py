# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget, QHBoxLayout,QLabel, QApplication
from PyQt5.QtGui import QPixmap,QImage,QPainter
import sys
sys.path.append("..")
from view.Ui_history import  Ui_History
from model.SqlGis import gdal_sqlite


class historywindow(QWidget):
    def __init__(self):
        super(historywindow,self).__init__()
        self.view=Ui_History()
        self.view.setupUi(self)
        self.SQL = gdal_sqlite() 
        self.MapId = 'LT51190381991204BJC00'  # TODO:修改为从用户列表处选择的返回值

        self.get_imagepath()
        self.show_riverlist()
        self.show_maplist()
        self.show_image()

        '''TODO:self.model'''
    def updata_mapid(self,MapId):
        self.MapId = MapId

    def get_imagepath(self):
        self.image_path = self.SQL.Read_River_Map(self.MapId)
    
    def get_riverlist(self):
        self.riverlist = self.SQL.Read_riverlist()

    def get_maplist(self):
        self.maplist = self.SQL.Read_maplist()

    def show_riverlist(self):
        self.get_riverlist()
        for i in range(len(self.riverlist.index)):
            self.view.comboBox.addItem("")
            self.view.comboBox.setItemText(i, self.riverlist.RiverName[i]) 
        

    def show_maplist(self):
        
        pass


    def show_image(self):
        print (self.image_path)
        self.Image = QImage()
        self.Image.load(self.image_path)
        if self.Image == None:
            print ("图像读取错误")
            sys.exit()
        else:
            self.view.widget.resize(800,650)
            height = self.view.widget.size().height()
            width = self.view.widget.size().width()
            pixmap = QPixmap.fromImage(self.Image.scaledToHeight(height))
            '''TODO: 修改图像分辨率为适应值'''
            self.imagelabel = QLabel(self.view.widget)
            self.imagelabel.setPixmap(pixmap)
            pix_x = pixmap.size().width()
            pix_y = pixmap.size().height()
            x = int((width - pix_x)/2)
            print (width,height,pix_x,pix_y,x)
            print (self.view.widget.getContentsMargins())
            self.imagelabel.move(10+x,0)
    

	
if __name__ == "__main__":
     app = QApplication(sys.argv)
     history = historywindow()
     app.setQuitOnLastWindowClosed(True)
     history.show()
     sys.exit(app.exec_())
