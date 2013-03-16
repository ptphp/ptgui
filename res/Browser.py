#coding:utf-8
import sys
import os
from PySide import QtGui, QtCore
from app.mainwindow import MyWebView
from app.utils.config import Config

def main():
    config = Config()
    #config.ptgui_dir = r"D:\PtProject\PtGUI-dev"
    config.ptgui_dir = os.getcwd()
    app = QtGui.QApplication(sys.argv)
    #font = QtGui.QFont('Serif',12, QtGui.QFont.Light)
    #font.setPixelSize(12)
    #font.setPointSize(12)
    #font.setPointSizeF(12)
    #app.setFont(font)

    url = None
    if len(sys.argv) >1:
        url = sys.argv[1]
        webview = MyWebView(app)
        webview.setUrl(QtCore.QUrl(url))
        webview.show()
    
    sys.exit(app.exec_())
    
if __name__ =="__main__":

    main()
    