#!/usr/bin/env python
# -*- coding=utf-8 -*-
import os
import shutil
from singleton import singleton
from fileIO import File

@singleton
class OsEnv():
    def installPythonModule(self,pythonModule):
        for m in pythonModule:
            cmd = "easy_install %s" % m
            res = os.popen(cmd)
            print res.read()
        
    def getOsEnvVar(self,name):  
        cmd ='wmic ENVIRONMENT where "name=\'%s\' and username=\'<system>\'" get VariableValue /value' % name
        path = os.popen(cmd)
        res =  path.read().strip().replace("VariableValue=","")
        if res == '':
            print "this is no {%s} for name var " % name
            return None
        return res

    def delOsEnvVar(self,name):
        print "*"*40
        if self.getOsEnvVar(name) is not None:
            cmd  = "wmic ENVIRONMENT where \"name='%s'\" delete" % name
            os.popen(cmd)
            print "success delete {%s}" % name
        else:
            print "this is no {%s} for name var " % name

    def setOsEnvVar(self,name,value):
        print "*"*40
        if self.getOsEnvVar(name) is not None:
            cmd ="wmic ENVIRONMENT where \"name='%s' and username='<system>'\" set VariableValue=\"%s\"" % (name,value) 
            print "success update {%s} : {%s}" % (name,value)
        else:
            cmd ="wmic ENVIRONMENT create name=\"%s\",username=\"<system>\",VariableValue=\"%s\"" % (name,value)
            print "success create  {%s} for name var " % name
        print cmd
        os.popen(cmd)

    def getOsPath(self):
        pathStr = self.getOsEnvVar("PATH")
        _pathList = pathStr.split(";")
        #remove reuse var
        pathList = []
        for p in _pathList:     
            if p not in pathList and p:
                #print p
                pathList.append(p.replace('"','').replace("\r\n",""))
        print pathList
        return pathList

    def formatOsPath(self,pathList):
        return ";".join(pathList)

    def setupEnv(self,PATH_PYTHON,PTP_HOME,pythonEnvList):
        print "Python Path is : "+PATH_PYTHON
        self.delOsEnvVar("PTP_HOME")
        self.setOsEnvVar("PTP_HOME",PTP_HOME)

        pythonEnvStr = ';'.join(pythonEnvList)
        self.setOsEnvVar("PYTHON_ENV",pythonEnvStr)

        path_list = self.getOsPath()

        if '%PTP_HOME%' in path_list:
            path_list.remove('%PTP_HOME%')
        if PTP_HOME in path_list:
            path_list.remove(PTP_HOME)

        for pe in pythonEnvList:
            if pe in path_list:
                path_list.remove(pe)                
        if '%PYTHON_ENV%' in path_list:
            path_list.remove('%PYTHON_ENV%')

        #path_list.append(r'%PTP_HOME%')
        #path_list.append(r'%PYTHON_ENV%')
        path_list.append(PTP_HOME)


        for pp in pythonEnvList:
            path_list.append(pp)

        path_str = self.formatOsPath(path_list)
        #path_str = "C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem"
        print path_str
        self.setOsEnvVar("PATH",path_str)

    def setupGitEtc(self,PTP_HOME):
        f = File() 
        _git_exe = os.path.join(PTP_HOME,"Local","Git","Git Bash.vbs")
        git_exe = os.path.join(PTP_HOME,"Local","Git","GitBash.vbs")
        
        if os.path.exists(_git_exe) and os.path.exists(git_exe) == False:
            print _git_exe
            print git_exe
            shutil.copy(_git_exe,git_exe)

        git_profile = os.path.join(PTP_HOME,"Local","Git","etc","profile")
        print "git profile path is : "+git_profile
        if os.path.exists(git_profile):
            content = f.get(git_profile)
            #print content
            if "#PTP_HOME CONFIG" not in content: 
                tmp = """
%s

#PTP_HOME CONFIG
PTP_HOME="$(cd "$PTP_HOME" ; pwd)"
if [ -f $PTP_HOME/etc/profile ]; then
  . $PTP_HOME/etc/profile
fi

#echo $PTP_HOME/etc/profile
        """ % content
                #print tmp
                f.set(git_profile,tmp)