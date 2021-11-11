#!/usr/bin/python
# build_native.py
# Build native codes


import sys
import os, os.path
import shutil
from hashlib import md5
from optparse import OptionParser
currentPath =os.getcwd()
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
   
def test():
	testStr="11111"
	strs="Jimu-guanwang-20211109142721.apk"
	splitArr =strs.split('-')
	print("splitArr  ", splitArr[0])
	print("splitArr  ", splitArr[1])
	testStr = "%s%s"%(testStr,splitArr[1])
	print("testStr  ", testStr)

if __name__ == '__main__':
	parser = OptionParser()
	parser.add_option("-f", "--filepath", dest="md5file_param", help='md5  file  path', action="append")
	(opts, args) = parser.parse_args()
	md5_file()
	test()
	
	print "end    end   end "
