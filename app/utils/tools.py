#!/usr/bin/env python
# -*- coding=utf-8 -*-
import os
import subprocess
from singleton import singleton
from app.utils.config import Config

@singleton
class Tools(object):
    config = Config()
    def run(self,args):
        localPath = self.config.dir['ptproject']
        print localPath
        param = args['param']
        app = args['app']

        appPath = {}
        if os.path.isfile(r"C:\progra~1\Google\Chrome\Application\chrome.exe"):
            appPath['Chrome'] = r"C:\progra~1\Google\Chrome\Application\chrome.exe"
        else:
            appPath['Chrome'] = r"C:\progra~2\Google\Chrome\Application\chrome.exe"
        appPath['python']= "python"
        appPath['Sublime']= os.path.join(localPath,r"..\Local\SublimeText2\sublime.exe")
        appPath['Vi']     = os.path.join(localPath,"Core","Bin","vi.exe")
        appPath['sqlite'] = os.path.join(localPath,"Core","Bin","SQLiteSpy.exe")
        appPath['explorer'] = r"explorer.exe"
        print args
        if app == 'explorer':
            if param == '':
                param = self.config.ptproject_dir
            else:
                if '/' in param:
                    param = param.replace('/','\\')

        cmd = r"%s %s" % (appPath[app],param)
        print cmd
        subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)


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