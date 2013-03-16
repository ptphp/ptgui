#coding:utf-8
import sys
import os
from PySide import QtGui
from app.mainwindow import MainWindow
from app.utils.config import Config

def main():
	config = Config()
	config.setPaths(os.getcwd())
	app = QtGui.QApplication(sys.argv)
	win = MainWindow()
	win.show()
	sys.exit(app.exec_())
	
if __name__ =="__main__":
    main()