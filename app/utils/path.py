#!/usr/bin/env python
# -*- coding=utf-8 -*-
from singleton import singleton
from config import Config
import os
def makeDir(path):
    if os.path.isdir(path) == False:
        makeDir(os.path.dirname(path))
        return os.mkdir(path)    
    return True

@singleton
class Path(object):
    config = Config()
#------------------------------------------------------------------------------ 项目根目录
    def getProjectRoot(self):
        path = os.path.join(self.config.ptproject_dir,self.config.projects_dir)
        makeDir(path)
        return path
#------------------------------------------------------------------------------ 项目目录
    def getProjectDir(self,name):
        return os.path.join(self.getProjectRoot(),name)
    
    
#------------------------------------------------------------------------------ Project Public
    def getProjectPublicDir(self,name):
        return os.path.join(self.getProjectDir(name),"Public")
    
    def getProjectPublicIndexPath(self,name):
        return os.path.join(self.getProjectPublicDir(name),"index.php")
    
    
#------------------------------------------------------------------------------ Project Application

    def getProjectApplicationDir(self,name):
        return os.path.join(self.getProjectDir(name),"Application")
    
    def getProjectApplicationViewDir(self,name):
        return os.path.join(self.getProjectApplicationDir(name),"View","default")
    def getProjectApplicationControllerDir(self,name):
        return os.path.join(self.getProjectApplicationDir(name),"Controller")

    def getProjectSettingDir(self,name):        
        return os.path.join(self.getProjectApplicationDir(name),"config")
    
    def getProjectSettingFile(self,name):
        return os.path.join(self.getProjectSettingDir(name),"setting.php")
    def getProjectSettingDb(self,name):
        return os.path.join(self.getProjectSettingDir(name),"setting.db")
#------------------------------------------------------------------------------ 项目配置文件 cPickle
    def getProjectSettingPkl(self,name):
        return os.path.join(self.getProjectDir(name),"setting.pkl")
#------------------------------------------------------------------------------ PtPHP
    def getFrameworkTplDir(self,name):
        return os.path.join(self.getFrameworkDir(name),"Asserts",'tpl')
    
    def getFrameworkDir(self,name):
        return os.path.join(os.path.dirname(self.getProjectRoot()),"Framework",name)
    
#------------------------------------------------------------------------------ php.exe 路径
    def getPhpExePath(self,name):
        return os.path.join(self.config.ptproject_dir,self.config.php_dir,name,"php")