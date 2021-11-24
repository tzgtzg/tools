import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
import json
import xlrd
import math
import types
import glob
import re
from optparse import OptionParser
fileTypeArray = [".xlsx",".xls"]

# xlrd 1.2.0  

class ParseExecl(object):
	"""docstring for ClassName"""
	def __init__(self):
		print "ParseExecl  init"
		
	def readAllExecl(self,_type):
		currentPath = os.getcwd()
		#print "currentPath:" + currentPath
		#for dir in [x for x in os.listdir(CUR_PATH) if os.path.isdir(os.path.join(CUR_PATH, x))]:
		for dir in [x for x in os.listdir(currentPath)]:
			localPath = os.path.join(currentPath, dir)
			if os.path.isfile(localPath):
				filesp = os.path.splitext(localPath)				 
				for k in fileTypeArray:
					if filesp[1] == k:				
						filename = os.path.basename(localPath)
						if _type == "json":
							self.readExeclToJson(localPath,filename.split('.')[0])
						elif _type == "lua":
							self.readExeclToLua(localPath,filename.split('.')[0])
						elif _type == "js":
							self.readExeclToJs(localPath,filename.split('.')[0])

	def ExeclToJson(self,path,name):
		workbook  = xlrd.open_workbook(path)
		# [u'sheet1', u'sheet2']
		#print workbook.sheet_names() 
		adict = {}
		
		for k in workbook.sheet_names():
			sheet=workbook.sheet_by_name(k)
			#sheet索引从0开始
			#sheet的名称，行数，列数
			#print sheet.name,sheet.nrows,sheet.ncols
		 	mlist =[]
	 		adict[k] = {}

	 		reservedNum = 0;   #  预留 行数  第一行  预留填备注
			# for i in range(1,sheet.nrows):     第一行  预留填备注
			for i in range(1 + reservedNum,sheet.nrows):  
				data = {}
				#print TransformationType(sheet.cell_value(0,0))
				for j in range(0,sheet.ncols):
					 value = self.TransformationType(sheet.cell_value(i,j))
					 #print type(value)
					 if  isinstance(value , str):
						
						 if self.isJsonString(value):					
							data[self.TransformationType(sheet.cell_value(0+reservedNum,j))] = eval(value)
						 else:
							data[self.TransformationType(sheet.cell_value(0+reservedNum,j))] = value
					 else:
					 	 # print TransformationType(sheet.cell_value(0,j))
						 data[self.TransformationType(sheet.cell_value(0+reservedNum,j))] = value
							
				# adict[TransformationType(sheet.cell_value(i,0))]= data
				# mlist.append(data)
				
				# adict[""+k] = mlist
				adict[""+k][self.TransformationType(sheet.cell_value(i,0))] = data

		
		data = json.dumps(adict,sort_keys=True,indent=1,ensure_ascii=False)
		return data

	def readExeclToJs(self,path,name):
		data = self.ExeclToJson(path,name)
		moduleStr = "module.exports = " 
		newData = moduleStr + data
		f=open(name+'.js','w') 
		f.write(newData)
		f.close()
		print "already create  js :  " + path

	def readExeclToLua(self, path,name):
		
		data = self.ExeclToJson(path,name)


		# 转换成  数组 格式 时  打开 注释 
		# ssdata = re.sub(r'\[','{',data,flags=re.M)
		# ccdata = re.sub(r']','}',ssdata,flags=re.M)
		rightdata = re.sub(r'(")(\w+)(":)','["'+r'\2'+'"]=',data,flags=re.M) 
		
		# print rightdata
		# 添加lua 头
		# \"total_amount\":\""+ price+"\"
		
		localStr = "local " + name + "tab =" + "\n"
		returnstr = "return " + name+"tab"
		f=open(name+'.lua','w') 
		f.write(localStr + rightdata +  "\n" + returnstr)
		f.close()
		print "already create  lua :  " + path


	def readExeclToJson(self,path,name):
		data = self.ExeclToJson(path,name)
		f=open(name+'.json','w') 
		f.write(data)
		f.close()
		print "already create  json :  " + path
		
	def isJsonString(self ,str):
		try:
			eval(str)
		except Exception,e :
			return False     
		return True		

	def TransformationType(self, var):
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
