#!/usr/bin/env python
# -*- coding: utf-8 -*-
#http://stackoverflow.com/questions/4629595/using-pysides-qtwebkit-under-windows-with-py2exe
#http://qt-project.org/wiki/Packaging_PySide_applications_on_Windows
__author__ = 'joseph'

from distutils.core import setup  
import py2exe  
import sys

# If run without args, build executables, in quiet mode.
if len(sys.argv) == 1:
    sys.argv.append("py2exe")
    sys.argv.append("-q")

MANIFEST_TEMPLATE = """
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
  <assemblyIdentity
    version="5.0.0.0"
    processorArchitecture="x86"
    name="%(prog)s"
    type="win32"
  />
  <description>%(prog)s</description>
  <trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">
    <security>
      <requestedPrivileges>
        <requestedExecutionLevel
            level="asInvoker"
            uiAccess="false">
        </requestedExecutionLevel>
      </requestedPrivileges>
    </security>
  </trustInfo>
  <dependency>
    <dependentAssembly>
      <assemblyIdentity
            type="win32"
            name="Microsoft.VC90.CRT"
            version="9.0.21022.8"
            processorArchitecture="x86"
            publicKeyToken="1fc8b3b9a1e18e3b">
      </assemblyIdentity>
    </dependentAssembly>
  </dependency>
  <dependency>
    <dependentAssembly>
        <assemblyIdentity
            type="win32"
            name="Microsoft.Windows.Common-Controls"
            version="6.0.0.0"
            processorArchitecture="X86"
            publicKeyToken="6595b64144ccf1df"
            language="*"
        />
    </dependentAssembly>
  </dependency>
</assembly>
"""
RT_MANIFEST = 24

INCLUDES = ["encodings","encodings.*","subprocess","PySide.QtNetwork","app.*","app.utils.*"] 

options = {"py2exe" :
    {"compressed" : 1,
     "optimize" : 2,
     "bundle_files" : 3,
     "includes" : INCLUDES,
     "excludes" : [],
     "dll_excludes": [ "MSVCP90.dll","MSVCR90.dll","MSVCM90.dll"] }}

windows = [{"script": "PtProject.py",
      "icon_resources": [(0, "res\\fav.ico")],
      #"other_resources" : [(RT_MANIFEST, 1,MANIFEST_TEMPLATE % dict(prog="PtPorject"))],
      }]

setup(name = "PtPorject",
      version = "1.0",
      description = "PtPorject",
      author = "joseph",
      author_email ="author@project.com",
      maintainer = "Maintainer Name",
      maintainer_email = "you@project.com",
      license = "wxWindows Licence",
      url = "http://projecthomepage.com",
      data_files = [
            "MSVCP90.dll","MSVCR90.dll","MSVCM90.dll","Microsoft.VC90.CRT.manifest",        
            ("res",[
              "res\\title.png",
              "res\\fav.ico"
              ]),
            ('imageformats',
              [
                'C:\\Python26\\Lib\\site-packages\\PySide\\plugins\\imageformats\\qgif4.dll',
                'C:\\Python26\\Lib\\site-packages\\PySide\\plugins\\imageformats\\qjpeg4.dll',
                'C:\\Python26\\Lib\\site-packages\\PySide\\plugins\\imageformats\\qico4.dll'
                ])
            ],
      #zipfile=None,
      options = options,
      windows = windows,
      )

