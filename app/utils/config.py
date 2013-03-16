#!/usr/bin/env python
# -*- coding=utf-8 -*-
from singleton import singleton
import os
import re
import sys

def makeDir(path):
    if os.path.isdir(path) == False:
        makeDir(os.path.dirname(path))
        return os.mkdir(path)    
    return True

tmp_setting_ini = """
ptphp_version=1.0
php_version=5.4.7
port = 8999
host = localhost
"""
@singleton
class Config(object):
    #------------------------------------------------------------------------------ 程序主目录
    ptproject_dir    = None
    #------------------------------------------------------------------------------ GUI目录
    ptgui_dir        = None    
    #------------------------------------------------------------------------------ PHP Server目录
    phpserver_dir     = None
    
    dir = {}   
    
    ports            = []
    runports         =[]
    ptproject_config_ini = None
    parser           = None
    ini              = None
    
    
    settings_db_path = None

    projects_dir     = None
    projects_list    = []
    php_dir          = None
    wintitle = ""
    setting = {}
    path = {}
           
    def setPaths(self, cwd): 
        self.wintitle       = u"PtProject v1.0 开发工具"
        self.app_dirname    = "PtWebos"
        
        self.ptgui_dir     = cwd
        self.ptproject_dir = os.path.abspath(os.path.join(self.ptgui_dir,"../")) 
               
        self.dir['ptgui']        = cwd
        self.dir['ptproject']    = os.path.abspath(os.path.join(self.ptgui_dir,"../"))   
        self.path['phpserver']   = os.path.join('usr','PHP','5.4.7','php')
        self.dir['ptphp']        = os.path.join(self.app_dirname,'Framework','PtPHP','1.0')
        self.dir['public']       = os.path.join(self.app_dirname,'Application')
        self.path['phpserver_ini'] = os.path.join('usr','PHP','server.ini')
        self.path['phpserver_router'] = os.path.join('usr','PHP','router.php')
        