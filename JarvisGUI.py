from JarvisUI1 import Ui_Kelly
from PyQt5 import QtCore , QtGui , QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt , QTimer , QTime , QDate
from PyQt5.uic import loadUiType
import Jarvis
import os
import webbrowser as web
import sys


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    
    def run(self):
        Jarvis.MainTask()

startexe = MainThread()

class Gui_Start(QMainWindow):
   
    def __init__(self):
        super().__init__()

        self.K = Ui_Kelly()
        self.K.setupUi(self)

        self.K.pushButton_start.clicked.connect(self.startTask)
        self.K.pushButton_stop.clicked.connect(self.close)
        self.K.pushButton_chrome.clicked.connect(self.chrome_app)
        self.K.pushButton_snap.clicked.connect(self.snapchat_app)
        self.K.pushButton_whatsapp.clicked.connect(self.whatsapp_app)
        self.K.pushButton_yt.clicked.connect(self.yt_app)
        self.K.pushButton_fb.clicked.connect(self.fb_app)
        
    def chrome_app(self):
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
    def snapchat_app(self):
        web.open("https://web.snapchat.com/?ticket=hCgwKCjE2NzkzMzUyMDIStQEbLs8sasNmBpKVCasjOI8yv15URF9aZong-rrQFft9PZmVC2armZjXkAswnik_ivKSAvjyFJEVDmIx1-YruC2FduNC_En_wew72i9W4fp5fpYwYsSRmUVerSBn9Cf62chvIlrn3kEK--3BvsuIXUXxYDISdcayWXHzCacew3TDbehrgZ9ZHUGsnUk80Glhnyw2wgDsoCIhNFtrIioJ4u_aQSHrlyz5TfXuo36zr3F6IJeO5toC")
    def yt_app(self):
        web.open("https://www.youtube.com/")
    def fb_app(self):
        web.open("https://m.facbook.com/")
    def whatsapp_app(self):
        web.open("https://web.whatsapp.com/")
    
    def startTask(self):
        self.K.lable1 = QtGui.QMovie("G.U.I Material//VoiceReg//Siri_1.gif")
        self.K.Gif_1.setMovie(self.K.lable1)
        self.K.lable1.start()

        self.K.lable2 = QtGui.QMovie("G.U.I Material//ExtraGui//Earth_Template.gif")
        self.K.Gif_2.setMovie(self.K.lable2)
        self.K.lable2.start()

        self.K.lable3 = QtGui.QMovie("G.U.I Material//ExtraGui//Code_Template.gif")
        self.K.Gif_3.setMovie(self.K.lable3)
        self.K.lable3.start()

        self.K.lable4 = QtGui.QMovie("G.U.I Material//ExtraGui//initial.gif")
        self.K.Gif_4.setMovie(self.K.lable4)
        self.K.lable4.start()

        self.K.lable5 = QtGui.QMovie("G.U.I Material//ExtraGui//B.G_Template_1.gif")
        self.K.Gif_5.setMovie(self.K.lable5)
        self.K.lable5.start()

        startexe.start()

GuiApp = QApplication(sys.argv)
kelly_gui = Gui_Start()
kelly_gui.show()
exit(GuiApp.exec_())

