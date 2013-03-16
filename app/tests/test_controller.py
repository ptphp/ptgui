#coding:utf-8
'''
Created on Sep 25, 2012

@author: joseph
'''
from app.controller import Controller
from app.utils.config import Config
from app.utils.path import Path,makeDir

import  os
import shutil
import sys

div = "*" * 60
config = Config()
config.ptgui_dir = r'D:\PtProject\PtGUI-dev'
config.ptproject_dir = os.path.abspath(os.path.join(config.ptgui_dir,"../")) 
config.projects_dir = os.path.join('workspace','projects')
config.php_dir = os.path.join('Local','php')

projectName = "www"
path = Path()
projectDir = path.getProjectDir(projectName)
makeDir(projectDir)
projectSettingPkl = path.getProjectSettingPkl(projectName)
print div,"project setting dir is :"
print projectSettingPkl

ctl = Controller()
args = {}
node = {}
args['project'] = projectName
args['node'] = node

def test_tableOpt():
    print div,"talbe opt"   
    ctl.dropTable(args) 
    ctl.createTable(args)
    
def test_new():
    print div,"test new()"
    node['title'] = u"首页"
    node['name'] = "index"
    node['rel'] = ""
    node['left'] = 400
    node['top'] = 300
    node['width'] = 100
    node['height'] = 20
    print node
    args['node'] = node
    id = ctl.new(args)['msg']
    print "insert id is : %s" % str(id)
    


def test_all():
    print div,"test all()"
    args['node'] = {}
    res =  ctl.all(args)
    print res
    print "count is : %d " % len(res['msg'])    


def test_update(id):
    print div,"test update()"
    node = {}
    node['name'] = "news"
    node['title'] = u"新闻"
    node['id'] = id
    args['node'] = node
    ctl.update(args)
    print args


def test_detail(id):
    print div,"test detail()"
    node = {}
    node['id'] = id
    args['node'] = node    
    print ctl.detail(args)['msg']
    

def test_remove(id):
    node = {}
    node['id'] = id
    args['node'] = node
    ctl.remove(args)
    print args
    

def test_end():
    print div," remove project"
    ctl.db.deleteDb(ctl.getDbName(projectName))
    shutil.rmtree(projectDir)


def main():    
    test_new()    
    test_all()
    test_update(2)
    test_all()
    sys.exit()
    test_detail(1)
    #test_remove(1)
    test_all()
    #test_end()
    
if __name__ == "__main__":
    main()    
    