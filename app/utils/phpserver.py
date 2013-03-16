#!/usr/bin/env python
# -*- coding=utf-8 -*-
from app.utils.config import Config
from app.utils.common import getPidByPort, res, killPidByPort
import os
import subprocess

class PHPServer():
    config = Config()    
    def _start(self,host,port,path):
        hostport = "%s:%d" % (host,port)        
        if os.path.isdir(path):      
            phpexe =  os.path.join(self.config.dir['ptproject'],self.config.path['phpserver'])                  
            ini_file = os.path.join(self.config.dir['ptproject'],self.config.path['phpserver_ini'])
            router_file = os.path.join(self.config.dir['ptproject'],self.config.path['phpserver_router'])
            cmd ="%s -S %s -c %s -t %s %s" % (phpexe,hostport,ini_file,path,router_file)  
            #print cmd
            subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            print 'start %s' % cmd
    def _stop(self,port):        
        killPidByPort(port)
        
    def _getPath(self,type,dir,port):
        projects = self.config.dir['projects']
        if(type == 'dev'):    
            path = os.path.join(projects,dir,'Application')
           
        elif type =="test":
            path = os.path.join(projects,dir,'Test')
        elif type =="deploy":
            path = os.path.join(projects,dir,'Public')
        print path
        return path,port
    
    def start(self,args):
        dir = args['dir']
        port = int(args['port'])
        host = args['host']        
        #path,port = self._getPath(type, dir, port)
        print dir,port
        #print args
        
        if getPidByPort(port):
            print 'port is running'
        else:
            self._start(host, port, dir)
        return res(0,1) 
    def restart(self,args): 
        dir = args['dir']
        port = int(args['port'])
        type = args['type']
        host = args['host']         
        self._stop(port)
        path,port = self._getPath(type, dir, port)
        self._start(host, port, path)
        print "restart"
        return res(0,1) 
        
    def stop(self,args):        
        port = args['port']
        self._stop(int(port));  
        print "stop"
        print port  
        return res(0,1) 
    
    def checkRun(self,args):        
        port = args['port']
        #print getPidByPort(port)
        if getPidByPort(port):
            #端口已存在！请重启
            code = 1
        else:
            #端口未启用
            code = 0
            #self.start(args)            
        return res(0,code)
    
        