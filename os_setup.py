#!/usr/bin/env python
# -*- coding=utf-8 -*-

import os,sys
from app.utils.fileIO import File
from app.utils.osenv import OsEnv
from app.utils.winregistry import Registry



if __name__ == '__main__':
	PTP_HOME = os.path.abspath(os.path.join(os.getcwd(),"../"))
	PATH_PYTHON = "C:\\Python26"

	pythonEnvList = [
			PATH_PYTHON,
			os.path.join(PATH_PYTHON,"Scripts")
		]

	print "PTPROJECT Path is : "+PTP_HOME
	osenv = OsEnv()
	osenv.setupGitEtc(PTP_HOME)

	osenv.setupEnv(PATH_PYTHON,PTP_HOME,pythonEnvList)
	pythonModule = [
		'simplejson',
		'pyside',
		'python-registr',
		'py2exe'
	]

	osenv.installPythonModule(pythonModule)

	reg = Registry()
	reg.setRightKeyForVi(PTP_HOME)
	reg.setRightKeyForSublime(PTP_HOME)
