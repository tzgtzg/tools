import sys
import os
import json
import math
import glob
import json
import re
from ReadExecl import ParseExecl
currentPath = os.getcwd()
# configPath = os.path.join(currentPath, "config.csv")
configPath = os.path.join(currentPath, "config.xlsx")

class ConfigParse():

	# def getInstance(self):
	# 	if not hasattr(ConfigParse, '_instance'):
	# 		ConfigParse._instance = ConfigParse()
	# 	return ConfigParse._instance

	def __init__(self):  
		self.jsonData = {}
		self.readDataFromConfigCsv()
		
	def readDataFromConfigCsv(self):
		pe = ParseExecl()
		self.cfJsonStr = pe.ExeclToJson(configPath,"config")
		self.jsonData = eval(self.cfJsonStr)
		print self.jsonData
		self.initReadConfig()

	def initReadConfig(self):
		self.comCf = self.jsonData["common"]
		self.iosCf = self.jsonData["Ios"]
		self.androidCf = self.jsonData["Android"]
		self.initCommonConfig()

	def initCommonConfig(self):
		self.unityEnginPath = self.comCf["1"]["value"]
		self.project_Path = self.comCf["2"]["value"]
		self.user_name = self.comCf["3"]["value"]
		self.passWorld = self.comCf["4"]["value"]
		self.TestFun = self.comCf["5"]["value"]
		self.buildIosFun = self.comCf["6"]["value"]
		self.buildAndroidFun = self.comCf["7"]["value"]

	def getIosConfigById(self,id):
		return self.jsonData["Ios"][""+id]

	def getAndroidConfigStrById(self,id):
		self.androidCfStr = self.jsonData["Android"][""+id]
		return self.androidCfStr


	def getProjectPath(self):
		return self.project_Path

	def getUnityEnginPath(self):
		return self.unityEnginPath

	def getUnityUserName(self):
		return self.user_name


	def getUnityPassWord(self):
		return self.passWorld

	def getBuildIosFun(self):
		return self.buildIosFun

	def getBuildAndroidFun(self):
		return self.buildAndroidFun

gConfigParse = ConfigParse()
