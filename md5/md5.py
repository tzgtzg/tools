#!/usr/bin/python
# build_native.py
# Build native codes


import sys
import os, os.path
import shutil
from hashlib import md5
from optparse import OptionParser
currentPath =os.getcwd()


def test():
	print 1111111

def md5_file():
    for dir in [x for x in os.listdir(currentPath)]:
		localPath = os.path.join(currentPath, dir)
		if os.path.isfile(localPath):
			 m = md5()
			 a_file = open(localPath,'rb')
			 m.update(a_file.read())
			 a_file.close()
			 md5str = m.hexdigest()
			 print"\n"
			 print localPath
			 print  md5str
   

if __name__ == '__main__':
	parser = OptionParser()
	parser.add_option("-f", "--filepath", dest="md5file_param", help='md5  file  path', action="append")
	(opts, args) = parser.parse_args()
	md5_file()
	
	print "end    end   end "
