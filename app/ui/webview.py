'''
Created on Jan 22, 2013

@author: joseph
'''
from PySide import QtGui,QtCore,QtWebKit
from PySide.QtCore import Qt

class MyWebView(QtWebKit.QWebView):    

    def __init__(self,stacker):
        super(MyWebView,self).__init__() 
        #https://deptinfo-ensip.univ-poitiers.fr/ENS/pyside-docs/PySide/QtWebKit/QWebSettings.html
        settings = QtWebKit.QWebSettings.globalSettings()
        
        self.settings().setAttribute(QtWebKit.QWebSettings.WebAttribute.DeveloperExtrasEnabled, True)
        self.settings().setAttribute(QtWebKit.QWebSettings.LocalStorageEnabled, True)
        self.settings().setAttribute(QtWebKit.QWebSettings.LocalStorageDatabaseEnabled, True)
        self.settings().setFontSize(QtWebKit.QWebSettings.DefaultFontSize,12)
        # or globally:
        # QWebSettings.globalSettings().setAttribute(
        #     QWebSettings.WebAttribute.DeveloperExtrasEnabled, True)
        self.inspect = QtWebKit.QWebInspector()
        self.inspect.setPage(self.page())
    
