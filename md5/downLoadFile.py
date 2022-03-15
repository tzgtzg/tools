#!/usr/bin/python
# build_native.py
# Build native codes
import sys
import os, os.path
import shutil
from hashlib import md5
from optparse import OptionParser

import urllib2
import urllib
import json

downLoadConfig =[]
downLoadConfig.append("config_21010_01")
downLoadConfig.append("config_21010_02")
downLoadConfig.append("config_21010_03")
downLoadConfig.append("config_21010_04")
downLoadConfig.append("config_21010_05")
downLoadConfig.append("config_21010_06")
downLoadConfig.append("config_21010_07")
downLoadConfig.append("config_21010_08")
downLoadConfig.append("config_21010_09")
downLoadConfig.append("config_21011_01")
downLoadConfig.append("config_21011_02")
downLoadConfig.append("config_21011_03")
downLoadConfig.append("config_21011_04")
downLoadConfig.append("config_21011_05")
downLoadConfig.append("config_21011_06")
downLoadConfig.append("config_21011_07")
downLoadConfig.append("config_61102_01")
downLoadConfig.append("config_61102_02")
downLoadConfig.append("config_61102_03")
downLoadConfig.append("config_61102_04")
downLoadConfig.append("config_61102_05")
downLoadConfig.append("config_22002_01_01")
downLoadConfig.append("config_22002_01_02")
downLoadConfig.append("config_22002_01_03")
downLoadConfig.append("config_22002_01_04")
downLoadConfig.append("config_22002_01_05")
downLoadConfig.append("config_22002_02_01")
downLoadConfig.append("config_22002_02_02")
downLoadConfig.append("config_22002_02_03")
downLoadConfig.append("config_22002_02_04")
downLoadConfig.append("config_22002_03_01")
downLoadConfig.append("config_22002_03_02")
downLoadConfig.append("config_22002_03_03")
downLoadConfig.append("config_22002_03_04")
downLoadConfig.append("config_22002_04_01")
downLoadConfig.append("config_22002_04_02")
downLoadConfig.append("config_22002_04_03")
downLoadConfig.append("config_22002_04_04")
downLoadConfig.append("config_22002_04_05")
downLoadConfig.append("config_22007_01_01")
downLoadConfig.append("config_22007_01_02")
downLoadConfig.append("config_22007_01_03")
downLoadConfig.append("config_22007_01_04")
downLoadConfig.append("config_22007_01_05")
downLoadConfig.append("config_22007_02_01")
downLoadConfig.append("config_22007_02_02")
downLoadConfig.append("config_22007_02_03")
downLoadConfig.append("config_22007_02_04")
downLoadConfig.append("config_22007_02_05")
downLoadConfig.append("config_22007_02_06")
downLoadConfig.append("config_22007_02_07")
downLoadConfig.append("config_22007_03_01")
downLoadConfig.append("config_22007_03_02")
downLoadConfig.append("config_22007_03_03")
downLoadConfig.append("config_22007_03_04")
downLoadConfig.append("config_22007_03_05")
downLoadConfig.append("config_22007_03_06")
downLoadConfig.append("config_22007_04_01")
downLoadConfig.append("config_22007_04_02")
downLoadConfig.append("config_22007_04_03")
downLoadConfig.append("config_22007_04_04")
downLoadConfig.append("config_22007_04_05")
downLoadConfig.append("config_22007_04_06")
downLoadConfig.append("config_11001_00")
downLoadConfig.append("config_11001_01")
downLoadConfig.append("config_11001_02")
downLoadConfig.append("config_11001_03")
downLoadConfig.append("config_11001_04")
downLoadConfig.append("config_11001_05")
downLoadConfig.append("config_11001_06")
downLoadConfig.append("config_11001_07")
downLoadConfig.append("config_11001_08")
downLoadConfig.append("config_11002_00")
downLoadConfig.append("config_11002_01")
downLoadConfig.append("config_11002_02")
downLoadConfig.append("config_11002_03")
downLoadConfig.append("config_11002_04")
downLoadConfig.append("config_11002_05")
downLoadConfig.append("config_11002_06")
downLoadConfig.append("config_11002_07")
downLoadConfig.append("config_11002_08")
downLoadConfig.append("config_11002_09")
downLoadConfig.append("config_11002_10")
downLoadConfig.append("config_11002_11")
downLoadConfig.append("config_11002_12")
downLoadConfig.append("config_11002_13")
downLoadConfig.append("config_11002_14")
downLoadConfig.append("config_11002_15")
downLoadConfig.append("config_11002_16")
downLoadConfig.append("config_11002_17")
downLoadConfig.append("config_80122_00")
downLoadConfig.append("config_80122_01")
downLoadConfig.append("config_80122_02")
downLoadConfig.append("config_11201_00")
downLoadConfig.append("config_11201_01")
downLoadConfig.append("config_11201_02")
downLoadConfig.append("config_11201_03")
downLoadConfig.append("config_11201_04")
downLoadConfig.append("config_11201_05")
downLoadConfig.append("config_11201_06")
downLoadConfig.append("config_11201_07")
downLoadConfig.append("config_11201_08")
downLoadConfig.append("config_11201_09")
downLoadConfig.append("config_11201_10")
# downLoadConfig.append("config_62101_00")
# downLoadConfig.append("config_62101_01")
# downLoadConfig.append("config_62101_02")
# downLoadConfig.append("config_62101_03")
# downLoadConfig.append("config_62101_04")
# downLoadConfig.append("config_62101_05")
# downLoadConfig.append("config_62101_06")
# downLoadConfig.append("config_62101_07")
# downLoadConfig.append("config_62101_08")
downLoadConfig.append("config_62119_00")
downLoadConfig.append("config_62119_01")
downLoadConfig.append("config_62119_02")
downLoadConfig.append("config_62119_03")
downLoadConfig.append("config_62119_04")
downLoadConfig.append("config_62119_05")
downLoadConfig.append("config_62119_06")
downLoadConfig.append("config_62119_07")
downLoadConfig.append("config_62119_08")
downLoadConfig.append("config_21032_01")
downLoadConfig.append("config_21032_02")
downLoadConfig.append("config_21033_01")
downLoadConfig.append("config_21033_02")
downLoadConfig.append("config_21028_01")
downLoadConfig.append("config_21028_02")
downLoadConfig.append("config_21034_01")
downLoadConfig.append("config_21034_02")
downLoadConfig.append("config_21035_01")
downLoadConfig.append("config_21035_02")
downLoadConfig.append("config_21029_01")
downLoadConfig.append("config_21029_02")
downLoadConfig.append("config_21036_01")
downLoadConfig.append("config_21036_02")


currentPath =os.getcwd()

# sku 下载相关地址
url ="https://block-app-small-api.bloks.com/"
tokenParam = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhcHBrZXkiOiI1ZDNjOGVhYzBiMGM0MDI3OGZhNWMxOGFmY2I4MjNiVSIsImF2YXRhciI6IiIsImNsaWVudF9pZCI6IiIsImV4cCI6MTU5Mjk5MTIzNywiaGVscF91aWQiOjcwMDAwMDY1LCJpYXQiOjE1OTI5OTAzMzcsIm5pY2tuYW1lIjoiIiwib3BlbmlkIjoiIiwidWlkIjo3MDAwMDA2N30.qsqFgBsyraosJ9Z_HHv_pZYKXoSSG6mCqbpvWvT2docqN1_N61SAvw6nBX6-j0-A9IUIGs_GBIm9iNylDsmmiw"

def ExeclToJson(path):
	workbook  = xlrd.open_workbook(path)
	# [u'sheet1', u'sheet2']
	#print workbook.sheet_names() 
	adict = {}
	for k in workbook.sheet_names():
		sheet=workbook.sheet_by_name(k)   # sheet索引从0开始
		# sheet的名称，行数，列数
		#print sheet.name,sheet.nrows,sheet.ncols
	 	mlist =[]
 		adict[k] = {}

 		reservedNum = 2;   #  预留 行数  第一行  预留填备注
		# for i in range(1,sheet.nrows):     第一行  预留填备注
		for i in range(1 + reservedNum,sheet.nrows):  
			data = {}
			#print TransformationType(sheet.cell_value(0,0))
			for j in range(0,sheet.ncols):
				 value = TransformationType(sheet.cell_value(i,j))
				 #print type(value)
				 if  isinstance(value , str):
					
					 if isJsonString(value):					
						data[TransformationType(sheet.cell_value(0+reservedNum,j))] = eval(value)
					 else:
						data[TransformationType(sheet.cell_value(0+reservedNum,j))] = value
				 else:
				 	 # print TransformationType(sheet.cell_value(0,j))
					 data[TransformationType(sheet.cell_value(0+reservedNum,j))] = value
						
			# adict[TransformationType(sheet.cell_value(i,0))]= data
			# mlist.append(data)
			
			# adict[""+k] = mlist
			adict[""+k][TransformationType(sheet.cell_value(i,0))] = data

	
	data = json.dumps(adict,sort_keys=True,indent=1,ensure_ascii=False)
	return data

def isJsonString(str):
	try:
		eval(str)
	except Exception,e :
		return False     
	return True	

def TransformationType(var):
	#print  type(var)
	if isinstance(var ,float) : #type(var) == 'float':
		# print("var  ", var)
		if var == int(var) : 
			str1 = int(var)
		else:
			str1 = round(var,2)
	elif isinstance(var, unicode): #type(var) == 'unicode':
		 str1 = var.encode("utf-8")
	else:
		raise Exception("type  is  not  deal ")
		str1 = var
	return str1


def DownLoadFile(configId,platform):
	_url = url+"unity/modelswithpic?appid=1000&model_sku_ids=" +configId +""+"&token="+tokenParam+"&uid=70000065&platform="+platform
	print("downPath1111  " , configId)
	response = urllib2.urlopen(_url)
	jsonData = response.read()
	jsonObj  = json.loads(jsonData)
	fileList = []
	for x in range(len(jsonObj["data"])):
		fileUrl = jsonObj["data"][x]["ConfigUrl"]
		fileList.append(fileUrl)
	downPath = os.path.join(currentPath,platform)
	isExit = os.path.exists(downPath)
	if not isExit:
		os.makedirs(downPath)
	for x in range(len(fileList)):
		print("downPath  " , os.path.join(downPath,configId))
		print("downPath  url " , fileList[x])
		f = urllib2.urlopen(fileList[x]) 
		with open(os.path.join(downPath,configId), "wb") as code:
			code.write(f.read())
		

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
	execlJosn = ExeclToJson(os.path.join(currentPath,"jr_datacsv","JrSkuCar.csv"))
	print(execlJosn)
	for x in range(len(downLoadConfig)):
		print  11111
		# DownLoadFile(downLoadConfig[x],"android")
		# DownLoadFile(downLoadConfig[x],"ios")
	# md5_file()
	# test()
	
	print "end    end   end "
