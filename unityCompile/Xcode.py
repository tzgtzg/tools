import sys
import os
import json
import xlrd
import math
import types
import glob
import re

from config import gConfigParse
from pbxproj import XcodeProject

class XcodePY():
	#  构造函数
	# def __init__(self, realpart, imagpart):  
 #        self.r = realpart
 #        self.i = imagpart

 	def __init__(self):
 		print "XcodePY  init"

 	def setXcodeProjectSetting(self):
 		XcodeProjectPath = '/Volumes/work/U3D/Test/Xcode/Unity-iPhone.xcodeproj/project.pbxproj'
 		project = XcodeProject.load(XcodeProjectPath)
 		# https://github.com/kronenthaler/mod-pbxproj/wiki   具体命令

 	def initXcodeBuildCf(self,id):
 		self.cf = gConfigParse.getIosConfigById(id)

	def xCodeBuildApp(self):
		print "-----------  xCodeBuildApp  begin -------------"
		
		workPath = self.cf["workPath"]
		schemeStr =	self.cf["scheme"]
		configrationRd = self.cf["buildType"]
		archive_Path = self.cf["archive_Path"]
		signIdentity = self.cf["code_sign_identity"]
		# profile_uid ="dfc7c78b-d051-4383-9a23-3b6f74e91566"
		profile_uid = self.cf["provisioning_profile"]

		cmd = 'xcodebuild archive -project %s -scheme %s -configuration %s -archivePath %s CODE_SIGN_IDENTITY="%s" PROVISIONING_PROFILE=%s'%(workPath,schemeStr,configrationRd,archive_Path,signIdentity,profile_uid)
		os.system(cmd)

		print "-----------  xCodeBuildApp  end -------------"

	def RunAppExportIpa(self):
		print "------------     RunAppToIpa    begin    -----------------"

		archive_Path = self.cf["archive_Path"] + ".xcarchive"
		exportIpa_Path = self.cf["ipaOutPath"]
		OptionsPlist = self.cf["ExportOptions"]
		signIdentity = self.cf["code_sign_identity"]
		profile_uid = self.cf["provisioning_profile"]

		cmd = 'xcodebuild  -exportArchive -archivePath %s -exportPath %s -exportOptionsPlist %s CODE_SIGN_IDENTITY="%s" PROVISIONING_PROFILE=%s'%(archive_Path,exportIpa_Path,OptionsPlist,signIdentity,profile_uid)
		os.system(cmd)

		print "------------     RunAppToIpa    end    -----------------"


 # xcrun altool --validate-app -f target/$ipa_name -t ios --apiKey $akey --apiIssuer $auser  --verbose #验证app的有效性
 #    xcrun altool --upload-app -f target/$ipa_name -t ios --apiKey $akey --apiIssuer $auser --verbose #上传app 到应用商店和testflight

gXCBuild=XcodePY()