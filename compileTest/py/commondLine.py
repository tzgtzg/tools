import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
import math
from Xcode import gXCBuild
from config import gConfigParse
from optparse import OptionParser
import traceback

unityEnginPath = gConfigParse.getUnityEnginPath()
project_Path = gConfigParse.getProjectPath()
log_file = os.getcwd() + "/unity_log.log"
COMMONDLINE_BuildIos_FUN = gConfigParse.getBuildIosFun()
COMMONDLINE_BuildAndroid_Fun = gConfigParse.getBuildAndroidFun()
user_name = gConfigParse.getUnityUserName()
passWorld = gConfigParse.getUnityPassWord()

def Usage():
    print '-h,--help: print help message.'
    print '-l,  -- lua    to lua  table    --json  to json '

# 最后一个 为传递参数 json 字符串
def call_unity_static_funcArg(funNme,arg):
	cmd = '%s -batchmode -projectPath %s -quit -logFile %s -executeMethod %s  -nographics -username %s -password %s %s'%(unityEnginPath,project_Path,log_file,funNme,user_name,passWorld,arg)
	print "executeMethod  :" + cmd
	os.system(cmd)

def call_unity_static_func(funNme):
    cmd = '%s -batchmode -projectPath %s -quit -logFile %s -executeMethod %s -nographics -username %s -password %s'%(unityEnginPath,project_Path,log_file,funNme,user_name,passWorld)
    print('run cmd:  ' + cmd)
    os.system(cmd)	

def main():
	parser = OptionParser(usage="")
	# parser.add_option("-l","--language",action="store",dest="languages",help="-l,  -- lua    to lua  table file    --json  to json  --js  to js file")
	parser.add_option("-p","--platform",action="store",dest="platform",help="-p,  -- ios   android")
	parser.add_option("-c","--configId",action="store",dest="configId",help="-i,  -- 配置 id")

	(options,args) = parser.parse_args()
	#print options.languages
	#print args
	# if options.languages == "lua" or options.languages == "json" or options.languages == "js":
	# 	readAllExecl(options.languages)
	# print("options  options  languages", options.platform)
	# print("options  options  languages", options.configId)
	if options.platform == None :
		raise Exception("platform   empty")
		return 
	if options.configId == None :
		raise Exception("configId   empty")
		return

	if  options.platform == "Ios" :
		# ios build
		print "options.platform   Ios"
		call_unity_static_func(COMMONDLINE_BuildIos_FUN)
		gXCBuild.initXcodeBuildCf(options.configId)
		gXCBuild.xCodeBuildApp()
		gXCBuild.RunAppExportIpa()
	elif options.platform == "Android" :
		print "options.platform   Android"
		# android build
		androidCf = gConfigParse.getAndroidConfigStrById(options.configId)
		paramStr = ""
		for key in androidCf:
			paramStr= paramStr + key + ":" + str(androidCf[key]) + ","
		paramStr =paramStr[0:-1]
		print paramStr
		call_unity_static_funcArg(COMMONDLINE_BuildAndroid_Fun,paramStr)


	print "create  all success : "   + project_Path
	os.system("pause")

if __name__ == "__main__":
	main()