using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor;
using System;

public class CommondLine : MonoBehaviour {

	static string[] SCENES = FindEnabledEditorScenes();
	public static void CommondLineTest()
	{
		Debug.Log("CommondLineTest  CommondLineTest  CommondLineTest");
	}

	private static string[] FindEnabledEditorScenes()
	{
		List<string> EditorScenes = new List<string>();
		foreach (EditorBuildSettingsScene scene in EditorBuildSettings.scenes)
		{
			if (!scene.enabled) continue;
			EditorScenes.Add(scene.path);
		}
		return EditorScenes.ToArray();
	}

	public static void buildIosApp()
	{
		
		Debug.Log("buildIosApp  buildIosApp  buildIosApp ---------------- ");
		string dataPath = Application.dataPath;
		dataPath = dataPath.Replace("/Assets", "");
		string targetDir = dataPath + "/Xcode";
        FileUtil.DeleteFileOrDirectory(targetDir);

        BuildPipeline.BuildPlayer(SCENES, targetDir, BuildTarget.iOS, BuildOptions.None);
    }

	public static void buildAndroidApp()
	{
		Debug.Log("buildAndroidApp  buildAndroidApp  buildAndroidApp --------------- ");
		string[] paramArr = System.Environment.GetCommandLineArgs();
		// 最后一个为传递参数
		string str = "";
		int length = paramArr.Length;

		// 解析android 端参数
		if (length >= 0)
		{
			str = paramArr[length - 1];
		}
		Debug.Log("GetPassParam  GetPassParam  GetPassParam ---------------- " + str);

		string keypassWord = "keypassWord";
		string keystoreName = "keystoreName";
		string applicationIdentifier = "applicationIdentifier";
		string keyaliasName = "keyaliasName";
		string keyaliasPass = "keyaliasPass";
		string bundleVersionCode = "bundleVersionCode";
		string bundleVersion = "bundleVersion";
		string[] strArr = str.Split(',');
		for (var i = 0; i < strArr.Length; i++)
		{
			string[] strPArr = strArr[i].Split(':');
			string key = strPArr[0];
			string keyValue = strPArr[1];
			if (key.Equals(keystoreName))
			{
				keystoreName = keyValue;
			}
			if (key.Equals(keypassWord)){
				keypassWord = keyValue;
			}
			if (key.Equals(keyaliasName))
			{
				keyaliasName = keyValue;
			}
			if (key.Equals(keyaliasPass))
			{
				keyaliasPass = keyValue;
			}
			if (key.Equals(applicationIdentifier))
			{
				applicationIdentifier = keyValue;
			}
			
			if (key.Equals(bundleVersionCode))
			{
				bundleVersionCode = keyValue;
			}
			if (key.Equals(bundleVersion))
			{
				bundleVersion = keyValue;
			}
		}

        //Debug.Log("GetPassParam  GetPassParam  GetPassParam ---------------- " + applicationIdentifier);
        //Debug.Log("GetPassParam  GetPassParam  GetPassParam ---------------- " + bundleVersion);
        //Debug.Log("GetPassParam  GetPassParam  GetPassParam ---------------- " + bundleVersionCode);
        //Debug.Log("GetPassParam  GetPassParam  GetPassParam ---------------- " + keystoreName);
        //Debug.Log("GetPassParam  GetPassParam  GetPassParam ---------------- " + keypassWord);

        AssetDatabase.Refresh();
        SetAndroidkeyStoreName(applicationIdentifier, bundleVersion, bundleVersionCode, keystoreName, keypassWord, keyaliasName, keyaliasPass);

		DateTime dt = DateTime.Now;

		string timeStr = dt.ToString("yyyy-MM-dd-hh-mm-ss");

		string dataPath = Application.dataPath;
		dataPath = dataPath.Replace("/Assets", "");
		string targetDir = dataPath + "/test_" + timeStr  + ".apk";
		FileUtil.DeleteFileOrDirectory(targetDir);

		BuildPipeline.BuildPlayer(SCENES, targetDir, BuildTarget.Android, BuildOptions.None);
	}

	public static void SetAndroidkeyStoreName(string bundleIdentifier, string bundleVersion ,string verCode,string keyName,string keypass, string keyaliasName, string keyaliasPass)
	{

        //PlayerSettings.companyName = companyNm;
        //PlayerSettings.productName = produceName;
        PlayerSettings.SetApplicationIdentifier(BuildTargetGroup.Android,bundleIdentifier)  ;// "com.playbyone.chyz.bw";
        PlayerSettings.bundleVersion = bundleVersion;
        PlayerSettings.Android.bundleVersionCode =  int.Parse(verCode) ;

        PlayerSettings.Android.keystoreName = keyName;
        PlayerSettings.keystorePass = keypass;

        PlayerSettings.Android.keyaliasName = keyaliasName;
		PlayerSettings.keyaliasPass = keyaliasPass;



	}


	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		
	}
}
