#!/usr/bin/env python
# -*- coding=utf-8 -*-
from singleton import singleton

@singleton
class File(object):
    def set(self,path,content):
        f = open(path,"w")
        f.write(content)
        f.close()
    def get(self,path):
        f = open(path,"r")
        content = f.read()
        f.close()
        return content

if __name__ == '__main__':
    pass