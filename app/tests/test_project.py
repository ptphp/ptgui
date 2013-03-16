#coding:utf-8
'''
Created on Sep 25, 2012

@author: joseph
'''
from app.project import Project
from app.utils.config import Config
import os
import urllib2
import sys

config = Config()
config.ptgui_dir = r'D:\PtProject\PtGUI-dev'
config.ptproject_dir = os.path.abspath(os.path.join(config.ptgui_dir,"../")) 
config.projects_dir = os.path.join('workspace','projects')
config.php_dir = os.path.join('Local','PHP')

pro = Project()
args = {}
args['name'] = 'amwtest' 
args['port'] = 8001 
args['host'] = 'localhost' 
args['title'] = 'amwtest' 
div = "*" * 60
def main():
    print div,"test all()"
    print pro.all(args)
    
    print div,"test new()"
    print pro.add(args)    
    print div,"test runServer()"
    print pro.runServer(args)['msg']
    print "localhost:8001 web page content is :",urllib2.urlopen("http://localhost:8001").read()
    
    print div,"test stopServer()"
    print pro.stopServer(args)['msg']
    sys.exit()
    print div,"test all()"
    print pro.all(args)
    
    print div,"test detail()"
    res = pro.detail(args)
    for row in res['msg']:
        print row,res['msg'][row]
    
    
    print div,"test remove()"
    print pro.remove(args)['msg']
    print div,"test projects_list()"
    print config.projects_list
    
if __name__ == "__main__":
    main()