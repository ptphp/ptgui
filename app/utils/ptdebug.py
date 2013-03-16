#!/usr/bin/env python
# -*- coding=utf-8 -*-
import simplejson as json
from singleton import singleton

@singleton
class PtDebug(object):
    traceData = []
    def dump(self,data):
        self.traceData.append(data)
    def trace(self,data):
        res = ""
        for row in self.traceData:
            res += "<p>"
            res += json.dumps(row)
            res += "</p>"
        #res =  res.replace("\"","\\\"")
        res =  res.replace("\"","'")
        return res
