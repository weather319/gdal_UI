# -*- coding: utf-8 -*-



from PyQt4 import QtCore, QtGui
from PyQt4 import phonon
from Ui_video import Ui_videofrom
import sys
 
class mainvideo(QtGui.QWidget):
    def __init__(self):
        super(mainvideo, self).__init__()
        self.UI=Ui_videofrom()
        self.UI.setupUi(self)
        self.mediaObject = phonon.Phonon.MediaObject(self)
        self.mediaObject.stateChanged.connect(self.stateChanged)  # 对象改变时
        self.mediaObject.tick.connect(self.tick)  # 链接到时间
        self.setupUi()
        self.connect(self.UI.BtnOpen, QtCore.SIGNAL('customContextMenuRequested (const QPoint&)'), self.openright)
        self.connect(self.UI.BtnOpen, QtCore.SIGNAL('clicked()'), self.alert)
        
        self.UI.videoPlayer =phonon.Phonon.VideoWidget(self)
        self.UI.verticalLayout_player.addWidget(self.UI.videoPlayer)


    def setupUi(self):
        self.playAction = QtGui.QAction(self.style().standardIcon(QtGui.QStyle.SP_MediaPlay), "Play",self, shortcut="Ctrl+P", enabled=False, triggered=self.mediaObject.play)
        self.pauseAction = QtGui.QAction(self.style().standardIcon(QtGui.QStyle.SP_MediaPause), "Pause", self, shortcut="Ctrl+A", enabled=False, triggered=self.mediaObject.pause)
        self.stopAction = QtGui.QAction(self.style().standardIcon(QtGui.QStyle.SP_MediaStop), "Stop",  self, shortcut="Ctrl+S", enabled=False,triggered=self.mediaObject.stop)
         # 添加工具条  包含 播放， 暂停， 重新开始
        bar = QtGui.QToolBar()
        bar.addAction(self.playAction)
        bar.addAction(self.pauseAction)
        bar.addAction(self.stopAction)
        self.UI.horizontalLayout_btn.addWidget(bar)
         #  显示LED时间
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Light, QtCore.Qt.darkGray)
        self.timeLcd = self.UI.lcdNumber
        self.timeLcd.setPalette(palette)
        self.timeLcd.display('00:00')
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)  # PyQT禁止窗口最大化按钮：
        self.setFixedSize(self.width(), self.height())   # PyQT禁止调整窗口大小:





    # button 右键菜单
    def openright(self):
        popMenu = QtGui.QMenu()
        popMenu.addAction(QtGui.QAction(QtGui.QIcon(':chrome.ico'), u'音频文件', self,  enabled=True, triggered=self.openaudio))
        popMenu.addAction(QtGui.QAction(QtGui.QIcon(':myfavicon.ico'), u'视频文件', self,  enabled=True, triggered=self.openvideo))
        popMenu.exec_(QtGui.QCursor.pos())
 
 
    # 选择打开音频
    def openaudio(self):
        file = self.addFiles('audio')
        self.mediaObject.setCurrentSource(phonon.Phonon.MediaSource(file))
         # 初始化音频的输出按钮
        self.audioOutput = phonon.Phonon.AudioOutput(phonon.Phonon.VideoCategory, self)
        phonon.Phonon.createPath(self.mediaObject, self.audioOutput)
         # 连接到音量
        self.UI.volumeSlider.setAudioOutput(self.audioOutput)
        self.UI.seekSlider.setMediaObject(self.mediaObject)
        self.mediaObject.play()
        

    # 选择打开视频文件
    def openvideo(self):
        file = self.addFiles('video')
        self.mediaObject.setCurrentSource(phonon.Phonon.MediaSource(file))   # 加载当前的源文件
        phonon.Phonon.createPath(self.mediaObject, self.UI.videoPlayer)
        # 初始化视频输出
        self.UI.videoPlayer.setAspectRatio(phonon.Phonon.VideoWidget.AspectRatioAuto)
        # 初始化音频的输出按钮
        self.audioOutput  =phonon.Phonon.AudioOutput(phonon.Phonon.VideoCategory, self)
        phonon.Phonon.createPath(self.mediaObject, self.audioOutput)
        # 连接到音量按钮
        self.UI.volumeSlider.setAudioOutput(self.audioOutput)
        self.UI.seekSlider.setMediaObject(self.mediaObject)
        self.mediaObject.play()



    def alert(self):
        QtGui.QMessageBox.question(self, (u'提示'),(u'请右键选择打开文件！'),QtGui.QMessageBox.Ok)
        
     # 选择文件
    def addFiles(self,filetype='all'):
        if filetype=='audio':
             tips=u'选择音频文件'
             expand = 'Image Files(*.mp3 *.wav)'
        elif filetype=='video':
            tips = u'选择视频文件'
            expand = 'Image Files(*.mp4 *.avi)'
        else:
            tips =u'请选择播放文件'
            expand = 'Image Files(*.mp3 *.wav *.mp4 *.avi)'
         # getOpenFileName  只能选择一个    getOpenFileNames  可多个选择
        files = QtGui.QFileDialog.getOpenFileName(self, tips,QtGui.QDesktopServices.storageLocation(QtGui.QDesktopServices.MusicLocation), expand)    # QStringList getOpenFileNames (QWidget parent = None, QString caption = QString(), QString directory = QString(), QString filter = QString(), Options options = 0)
        
        if not files:
            return ''
         
        return files
     # 改变状态
    def stateChanged(self, newState):
 
         if newState == phonon.Phonon.ErrorState:
             if self.mediaObject.errorType() == phonon.Phonon.FatalError:
                 QtGui.QMessageBox.warning(self, "Fatal Error",
                         self.mediaObject.errorString())
             else:
                 QtGui.QMessageBox.warning(self, "Error",
                         self.mediaObject.errorString())
 
         elif newState == phonon.Phonon.PlayingState:
             self.playAction.setEnabled(False)
             self.pauseAction.setEnabled(True)
             self.stopAction.setEnabled(True)
 
         elif newState == phonon.Phonon.StoppedState:
             self.stopAction.setEnabled(False)
             self.playAction.setEnabled(True)
             self.pauseAction.setEnabled(False)
             self.timeLcd.display("00:00")
 
 
         elif newState == phonon.Phonon.PausedState:
             self.pauseAction.setEnabled(False)
             self.stopAction.setEnabled(True)
             self.playAction.setEnabled(True)
     # 时间显示
    def tick(self, time):
        displayTime = QtCore.QTime(0, (time / 60000) % 60, (time / 1000) % 60)
        self.timeLcd.display(displayTime.toString('mm:ss'))
 
 
 
    def keyPressEvent(self, event):
          if event.key() ==QtCore.Qt.Key_Escape:
              self.close()
 
 
if __name__ == "__main__":
     app=QtGui.QApplication(sys.argv)
     mainapp = mainvideo()
     app.setQuitOnLastWindowClosed(True)
     mainapp.show()
     sys.exit(app.exec_())
