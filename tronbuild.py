#!/usr/bin/env python

__author__ = 'Elliott Saille'


import os
import os.path
from linecache import getline
import re

tron = "/var/www/subdomains/mirror/tron/daily/source/tron/Tron.bat"
versionstorage = "/var/www/subdomains/mirror/tron/daily/version.txt"
builddir = "/var/www/subdomains/mirror/tron/daily/builds"
buildfilepre = "Tron-"
buildfilepost = "-Build.tar.gz"
versionregex = re.compile(r"\d{1,2}\.\d{1,2}\.\d{1,2}")

versionline = getline(tron, 7)
version = versionregex.search(versionline)
version = version.group()
print version

if os.path.isfile(tron):
        if not os.path.isfile(versionstorage):
                buildfile = buildfilepre + version + buildfilepost
                buildfilepath = os.path.join(builddir, buildfile)
                if os.path.isfile(buildfilepath):
                        print( "Build file exists, however version file does not")
                        #os.remove(buildfilepath)
                print("No version file found, creating version file.")
                versionfile = open(versionstorage,"w")
                versionfile.write(version)
                versionfile.close()



else:
        print("Whoops looks like tron's not where it should be. You should probably check that out!")
        exit(1)