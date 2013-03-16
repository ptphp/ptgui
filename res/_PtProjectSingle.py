#!/usr/bin/env python
# -*- coding=utf-8 -*-
from PySide import QtGui,QtWebKit
from PySide import QtCore
import subprocess
import ConfigParser
import os
import simplejson as json
from Utils import Config,urldecode,killPidByPort,trace_back,PtDebug
from qSingleApplication import QSingleApplication
try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	_fromUtf8 = lambda s: s

class ClientApi(QtCore.QObject):
	def __init__(self, parent=None):
		super(ClientApi, self).__init__(parent)

	@QtCore.Slot(str,str)
	def call(self,module, param):
		config = Config()
		data = {}
		try:
			_p = json.loads(param)
			#print _p
			mList = module.split('.')

			packageName = mList[0]
			className = mList[1]
			methodName = mList[2]
			#print className,methodName
			the_class = getattr(__import__(packageName),className)
			instance = the_class()
			method = getattr(instance, methodName)
			#print method
			res = method(_p['data'])
			status = 0
		except:
			status = 1
			res = trace_back()  
			res = res.replace("\"","'")
			res = res.replace("\n","<br>")

		data['res'] = res
		data['status'] = status
		#print data
		self.callback(data)

	def callback(self,data):
		#print json.dumps(data)	
		#print json.dumps(data,skipkeys=True)
		self.emit(QtCore.SIGNAL("callback(QString)"),json.dumps(data,skipkeys=True))
	
class MainWindow(QtGui.QMainWindow):
	debug = PtDebug()
	def __init__(self):
		super(MainWindow, self).__init__()		
		self.config = Config()
		message = ""
		title_icon = QtGui.QIcon()
		title_icon.addPixmap(QtGui.QPixmap("res/title.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.setWindowIcon(title_icon)
		self.setWindowTitle('PtProject v1.0 开发工具'.decode('utf-8'))
		self.setMinimumSize(400,240)
		self.resize(600,700)
		self.setGeometry(10, 30, 600, 700)

		widget = QtGui.QWidget()

		self.setCentralWidget(widget)
		self.webView = QtWebKit.QWebView()
		self.mainframe = self.webView.page().mainFrame()
		#初始化目录
		self.setDir()
		self.url = "file:///%s/Asserts/index.html" % self.config.ptproject_dir.replace('\\','/')
		
		self.webView.setUrl(QtCore.QUrl(_fromUtf8(self.url)))
		self.mainframe.javaScriptWindowObjectCleared.connect(self.populateJavaScriptWindowObject)
		self.webView.settings().setAttribute(QtWebKit.QWebSettings.WebAttribute.DeveloperExtrasEnabled, True)
		# or globally:
		# QWebSettings.globalSettings().setAttribute(
		#     QWebSettings.WebAttribute.DeveloperExtrasEnabled, True)
		inspect = QtWebKit.QWebInspector()
		inspect.setPage(self.webView.page())	
		inspect.setWindowIcon(title_icon)			
		
		debugWidget = QtGui.QWidget()

		layout = QtGui.QVBoxLayout()
		layout.setContentsMargins(0, 0, 0, 0)
		
		layout.addWidget(self.webView)
		layout.addWidget(inspect)
		layout.addWidget(debugWidget)
		widget.setLayout(layout)
		#self.setCentralWidget(self.webView)

		self.createActions()
		self.createMenus()		
		self.statusBar().showMessage(message)
		QtCore.QObject.connect(self.webView,QtCore.SIGNAL("urlChanged (const QUrl&)"), self.link_clicked)	

		self.isWindow()
		self.trayIcon = QtGui.QSystemTrayIcon(self)
		self.trayIcon.setIcon(title_icon)
		self.trayIcon.show()
		self.trayIcon.activated.connect(self.trayClick)
		self.trayIcon.setToolTip(u"PtProject 开发工具")
		self.trayMenu()
			
	def test(self):
		msg = """{"status": 1, "res": "Traceback (most recent call last):<br>  File 'D:\\PtProject\\PtGUI-dev\\app.py', line 36, in call<br>    res = method(_p['data11'])<br>KeyError: 'data11'<br>"}"""
		#print msg
		js ="""
			alert(\"%s\");
			""" % msg.replace('\"',"\\\"")
		#print js
		self.mainframe.evaluateJavaScript(js)	

	def link_clicked(self,url):
		for row in self.debug.traceData:
			print row
		self.debug.traceData = []
		href = url.toString()
		if "project_detail" in href:
			req = urldecode(href)
			self.mainframe.evaluateJavaScript("var projectName = '%s';" % req['pro'])

		
	def callback(self,msg):
		#print msg
		msg = msg.replace('\"',"\\\"")
		js ="""try{
				setCallbackParam(\"%s\");
			}catch(e){
				alert(e.name  +   " :  "   +  e.message);
			}
			""" % msg
		#print js
		self.mainframe.evaluateJavaScript(js)
	def populateJavaScriptWindowObject(self):
		clientApi = ClientApi()
		self.mainframe.addToJavaScriptWindowObject('clientApi', clientApi)
		self.connect(clientApi, QtCore.SIGNAL("callback(QString)"), self.callback)

	def setDir(self):		

		self.config.parser = ConfigParser.ConfigParser()

		self.config.ptgui_dir = os.path.abspath(os.getcwd())

		self.config.ini = os.path.join(self.config.ptgui_dir,'config.ini')

		self.config.ptproject_dir = os.path.abspath(os.path.join(self.config.ptgui_dir,"../"))
		
		self.config.settings_db_path = os.path.join(self.config.ptgui_dir,"settings.db")		

		self.config.projects_dir = os.path.join('workspace','projects')

		self.config.php_dir = os.path.join('local','Server','php')


		if os.path.exists(self.config.ini) == True:
			self.config.parser.readfp(open(self.config.ini,"r"))
		else:
			section_name = 'dir'
			self.config.parser.add_section(section_name)
			self.config.parser.set(section_name, "ptgui_dir", self.config.ptgui_dir)
			self.config.parser.set(section_name, "ptproject_dir", self.config.ptproject_dir)
			self.config.parser.set(section_name, "ptproject_config_ini", self.config.ini)
			self.config.parser.write(open(self.config.ini,"w"))

	def openExe(self,cmd):
		handle = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

	def openFirefox(self): 
		exePath = os.path.join(self.config.ptproject_dir,'local','Tools','firfox','firefox.exe')
		self.openExe(exePath)   

	def openSublime(self):  
		exePath = os.path.join(self.config.ptproject_dir,'local','Tools','SublimeText2','sublime.exe')
		self.openExe(exePath)

	def openVi(self):
		exePath = os.path.join(self.config.ptproject_dir,'local','bin','vi.exe')
		self.openExe(exePath)

	def openGit(self):
		exePath = os.path.join(self.config.ptproject_dir,'local','Git','GitBash.vbs %s' % self.config.ptproject_dir)
		self.openExe(exePath)

	def createActions(self):        
		self.openFirefoxAct = QtGui.QAction("Open &Firefox",self,
				triggered=self.openFirefox)
		self.openViAct = QtGui.QAction("Open &Vi",self,
				triggered=self.openVi)
		self.openSublimeAct = QtGui.QAction('Open &Sublime',self,
				triggered=self.openSublime)        

		self.openGitAct = QtGui.QAction('&Git',self,
				triggered = self.openGit)

	def createMenus(self):
		self.toolsMenu = self.menuBar().addMenu("&Tools")
		self.toolsMenu.addAction(self.openFirefoxAct)
		self.toolsMenu.addAction(self.openViAct)
		self.toolsMenu.addAction(self.openSublimeAct)

		self.coreMenu = self.menuBar().addMenu('&Core')
		self.coreMenu.addAction(self.openGitAct)

	def closeEvent(self, event):
		#reply = QtGui.QMessageBox.question(self, 'Message',
					#"Are you sure to quit?", QtGui.QMessageBox.Yes | 
					#QtGui.QMessageBox.No, QtGui.QMessageBox.No)
		
		if self.trayIcon.isVisible():
			self.hide()
			event.ignore()

		#if reply == QtGui.QMessageBox.Yes:
			#os.system("Taskkill /f /t /im php.exe")
			#event.accept()
		#else:
			#event.ignore()

	def trayClick(self,reason):
		if reason==QtGui.QSystemTrayIcon.DoubleClick: #双击
			self.showNormal()
		elif reason==QtGui.QSystemTrayIcon.MiddleClick: #中击
			self.showMessage()
		else:
			pass

	def showMessage(self):
		icon=QtGui.QSystemTrayIcon.Information
		self.trayIcon.showMessage(u"提示信息",u"点我干嘛？",icon)

	def trayMenu(self):
		self.minimizeAction = QtGui.QAction(u"最小化", self,triggered=self.hide)
		self.maximizeAction = QtGui.QAction(u"最大化",self,triggered=self.showMaximized)
		self.restoreAction = QtGui.QAction(u"还原", self,triggered=self.showNormal)
		self.quitAction = QtGui.QAction(u"退出", self,triggered=QtGui.qApp.quit)
		self.trayIconMenu = QtGui.QMenu(self)
		self.trayIconMenu.addAction(self.minimizeAction)
		self.trayIconMenu.addAction(self.maximizeAction)
		self.trayIconMenu.addAction(self.restoreAction)
		self.trayIconMenu.addSeparator() #间隔线
		self.trayIconMenu.addAction(self.quitAction)
		self.trayIcon.setContextMenu(self.trayIconMenu) #右击托盘

	def getArgsFromOtherInstance(self, args):
		QtGui.QMessageBox.information(self, self.tr("Received args from another instance"),args)
if __name__ == '__main__':
	import sys
	app = QSingleApplication(sys.argv)
	app.setApplicationName("PtProject V 1.0")
	window = MainWindow()
	app.singleStart(window)
	sys.exit(app.exec_())

