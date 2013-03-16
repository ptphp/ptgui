#!/usr/bin/env python
# -*- coding=utf-8 -*-
from _winreg import *
from singleton import singleton


"""
Windows Registry Editor Version 5.00
;-------------------------
[HKEY_CLASSES_ROOT\*\shell]

[HKEY_CLASSES_ROOT\*\shell\open with VI]
@="open with VI"

[HKEY_CLASSES_ROOT\*\shell\open with VI\Command]
@="D:\\Dhole\\PtProject\\Core\\Bin\\vi.exe %1"

[HKEY_CLASSES_ROOT\*\shell]

[HKEY_CLASSES_ROOT\*\shell\open with SublimeText2]
@="open with SublimeText2"

[HKEY_CLASSES_ROOT\*\shell\open with SublimeText2\Command]
@="C:\\PtProject\\Local\\SublimeText2\\sublime.exe %1"

"""

@singleton
class Registry():
	def query(self):
		key = OpenKey(HKEY_CLASSES_ROOT, r'*\shell\minVi', 0, KEY_ALL_ACCESS) 
		res = QueryValueEx(key, "")
		print res	
	def setRightKeyForVi(self,root):
		keyVal_root = '*\shell\minVi'
		keyVal_cmd  = '*\shell\minVi\Command'
		name        = ""
		value_root  = "minVi"
		value_cmd   = root+"\\bin\\vi.exe %1"
		self.set(HKEY_CLASSES_ROOT,keyVal_root,name,value_root)
		self.set(HKEY_CLASSES_ROOT,keyVal_cmd,name,value_cmd)
		print "set %s for %s" % (keyVal_cmd,value_root)

	def setRightKeyForSublime(self,root):
		keyVal_root = '*\shell\SublimeText2'
		keyVal_cmd  = '*\shell\SublimeText2\Command'
		name        = ""
		value_root  = "SublimeText2"
		value_cmd   = root+"\\Local\\SublimeText2\\sublime.exe %1"
		self.set(HKEY_CLASSES_ROOT,keyVal_root,name,value_root)
		self.set(HKEY_CLASSES_ROOT,keyVal_cmd,name,value_cmd)
		print "set %s for %s" % (keyVal_cmd,value_root)

	def listall(self):
		try:
			i = 0
			while True:
				subkey = EnumKey(HKEY_USERS, i)
				print subkey
			i += 1
		except WindowsError:
			# WindowsError: [Errno 259] No more data is available    
			pass

	def set(self,root,keyVal,name,value):		
		try:
			key = OpenKey(root, keyVal, 0, KEY_ALL_ACCESS)
		except:
			key = CreateKey(root, keyVal)
		SetValueEx(key, name, 0, REG_SZ, value)
		CloseKey(key)

def main():
	reg = Registry()
	reg.setRightKeyForVi()
	reg.setRightKeyForSublime()

if __name__ == '__main__':
	main()
