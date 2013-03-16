#!/usr/bin/env python
# -*- coding=utf-8 -*-
import os
import subprocess
import traceback
from urllib import unquote
from app.utils.ptdebug import PtDebug

def res(code,data):
    return {'error':code,'data':data}

def trace_back():  
    try:  
        return traceback.format_exc()  
    except:  
        return '' 
def urldecode(url):
    result={}
    url=url.split("?",1)
    if len(url)==2:
        for i in url[1].split("&"):
            i=i.split("=",1)
            if len(i)==2:
                result[unquote(i[0])]=unquote(i[1])
    return result

def parseNetstat(res):
        pids = []
        try:
            d =  res.split("\r\n")
            for r in d:
                if r:
                    pid = r.split()[-1]
                    if int(pid) >0:
                        pids.append(int(pid))
        except:
            pass
        return pids

def getPidByPort(port):
    cmd ="netstat -nao | findstr :%d" % port
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    res = p.stdout.read()
    if res:
        return parseNetstat(res)
    else:
        return []

def killPidByPort(port):
    pids = getPidByPort(port)
    debug = PtDebug()
    for pid in pids:
        t =  "kill PID :%d" % pid
        debug.dump(t)
        res = os.popen("taskkill /PID %d /F" % pid)
        #print res.read()
        #os.kill(pid,9)

if __name__ == '__main__':
    pass