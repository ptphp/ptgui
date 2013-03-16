#!/usr/bin/env python
# -*- coding=utf-8 -*-
import simplejson as json
from PySide import QtCore
from app.utils.common import trace_back

class Dynload():
    def __init__(self,package,imp_list):
        self.package=package
        self.imp=imp_list
    def getobject(self):
        return __import__(self.package, globals(), locals(),self.imp, -1)
    def getClassInstance(self,classstr,*args):
        return getattr(self.getobject(),classstr)(*args)    
    def execfunc(self,method,*args):
        return getattr(self.getobject(),method)(*args)
    def execMethod(self,instance,method,*args):
        return getattr(instance,method)(*args)

class ClientApi(QtCore.QObject):
    def __init__(self,parent=None):
        super(ClientApi,self).__init__(parent)  
        
#--------------------------------------------------------------------------------传入参数
#----{
#----    "_package":"app.controller",
#----    "_class":"Controller",
#----    "_function":"all",
#----    "_args":{
#----             "project":"name",
#----             },
#----}
#--------------------------------------------------------------------------------

    @QtCore.Slot(str)
    def call(self,data):
        _data = json.loads(data)
        #print _data        
        if _data['_package'] == "app.mainwindow":   
            self.callbackMainWindow(_data)            
        else:            
            result = {}         
            try:  
                status = 0                        
                packageName = _data['_package']
                className = _data['_class']
                methodName = _data['_function']
                
                #dyn=Dynload(packageName,['*'])
                
                #ins=dyn.getClassInstance(className)
                #res = dyn.execMethod(ins, methodName)
                #dyn.execfunc('test','Hello','function!')
                
                #print packageName,className,methodName
                the_class = getattr(__import__(packageName, globals(), locals(),['*'], -1),className)
                instance = the_class()
                method = getattr(instance, methodName)
                #print method
                res = method(_data['_args'])        
                result['data'] = res                      
            except:
                status = 1
                res = trace_back()
                #print res         
                res = res.replace("\"","'")
                res = res.replace("\n","<br>")
                result['message'] = res
            
            result['error'] = status
            #print result
            self.callback(result)
        
    def callbackMainWindow(self,data):     
        self.emit(QtCore.SIGNAL("callbackMainWindow(QString)"),json.dumps(data,skipkeys=True))
        
    def callback(self,data):
        self.emit(QtCore.SIGNAL("callback(QString)"),json.dumps(data,skipkeys=True))
        
        