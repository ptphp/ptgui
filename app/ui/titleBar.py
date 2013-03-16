'''
Created on Jan 22, 2013

@author: joseph
'''
from PySide import QtGui,QtCore,QtWebKit
from PySide.QtCore import Qt

class TitleBar(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)        
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint);
        css = """
QWidget
{
Background: #AA00AA;
color:white;
font:12px bold;
font-weight:bold;
border-radius: 1px;
height: 11px;
}
QHBoxLayout{
Background-image:url('title_bk.png');
font-size:12px;
color: black;

}
QToolButton{
Background:#AA00AA;
font-size:11px;
}
QToolButton:hover{
Background:n #FF00FF;
font-size:11px;
}
"""

        self.setAutoFillBackground(True)
        self.setBackgroundRole(QtGui.QPalette.Highlight)
        self.setStyleSheet(css) 

        self.minimize=QtGui.QToolButton(self);
        self.minimize.setIcon(QtGui.QIcon('img/min.png'));

        self.maximize=QtGui.QToolButton(self);
        self.maximize.setIcon(QtGui.QIcon('img/max.png'));

        close=QtGui.QToolButton(self);
        close.setIcon(QtGui.QIcon('img/close.png'));

        self.minimize.setMinimumHeight(15);
        close.setMinimumHeight(15);
        self.maximize.setMinimumHeight(15);

        label=QtGui.QLabel(self);
        label.setText("");
        label.setMinimumHeight(14);
        self.setWindowTitle("");
        hbox=QtGui.QHBoxLayout(self);

        hbox.addWidget(label);
        hbox.addWidget(self.minimize);
        hbox.addWidget(self.maximize);
        hbox.addWidget(close);
        hbox.insertStretch(1,10);
        hbox.setSpacing(0);
        self.setSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Fixed);
        self.maxNormal=False;

        close.clicked.connect(self.close);
        self.minimize.clicked.connect(self.showSmall);
        self.maximize.clicked.connect(self.showMaxRestore);


    def showSmall(self):        
        self.parent().parent().showMinimized();

    def showMaxRestore(self):
        if(self.maxNormal):
            self.parent().parent().showNormal();
            self.maxNormal= False;
            #self.maximize.setIcon(QtGui.QIcon('img/max.png'));
            #print'1'

        else:
            self.parent().parent().showMaximized();
            self.maxNormal=  True;
            #print '2'
            #self.maximize.setIcon(QtGui.QIcon('img/max2.png'));

    def close(self):
        self.parent().parent().close()        

    def mousePressEvent(self,event):
        box = self.parent().parent()
        if event.button() == Qt.LeftButton:
            box.moving = True; box.offset = event.pos()

    def mouseMoveEvent(self,event):
        box = self.parent().parent()
        if box.moving : box.move( event.globalPos() - box.offset )
