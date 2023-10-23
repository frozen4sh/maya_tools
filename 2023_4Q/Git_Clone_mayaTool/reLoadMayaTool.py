# script edit window 에 파일을 주면 실행전까지 윈도우 만들어줌 
import sys
import os
sys.version
scriptPath=r'C:\python377\Lib\site-packages'
sys.path.append(scriptPath)
import pymel.core as pm
import shutil
def createPY( filepatha ):
    #print (os.path.normpath(filepatha.pop()))
    filepathb=os.path.normpath(filepatha)
    #filepathb=filepatha.pop()
    scriptWindow_name = "ScriptWindowa"
    if pm.window(scriptWindow_name, exists=True):
        pm.deleteUI( scriptWindow_name, window=True )
    fileb = open( filepathb , "r",encoding="UTF-8")
    strings = fileb.readlines()
    stringA=''
    for i in strings:
        stringA=stringA+i
    #print(strings)
    fileb.close()        
    pm.window(scriptWindow_name,title="==== python script ==== - cmdScrollFieldExecuter -")
    pm.columnLayout()
    pm.cmdScrollFieldExecuter('cmdScrollFieldExecuterA',width=700, height=400, sourceType="python",t=stringA,sla=1,showLineNumbers=1)
    pm.button(l='Run script on selected Text',c='cmds.cmdScrollFieldExecuter("cmdScrollFieldExecuterA",e=1,exc=1)',w=700,h=30)
    pm.showWindow()  
def mainWinMenuItem():      
    MainMayaWindow = pm.language.melGlobals['gMainWindow'] 
    menu_name = "ViveLabMenu"
    if pm.menu(menu_name, exists=True):
        pm.deleteUI(menu_name)
    menu = pm.menu(menu_name, label="ViveStudiosLab",p=MainMayaWindow)
    drivePath='Z:/Private_Folder/kyuseokKim/test_Git/'
    import json
    jsonopenPath=  os.path.normpath( drivePath+'ui/button.json' )
    with open(jsonopenPath, "r") as json_file:
        loaded_data = json.load(json_file)
    buttonDic=loaded_data["buttonDic"]
    buttonImageDic=loaded_data["buttonImageDic"]
    buttonCommandDic=loaded_data["buttonCommandDic"]     
    alist=[]
    for i in buttonDic:
        a=pm.menuItem(i, subMenu=True, label=i )
        alist.append(a)
        if i in buttonImageDic:
            pm.menuItem(a, edit=1, i = drivePath+buttonImageDic[i][0])    
        for j in buttonDic[i]:
            if j !='':            
                b=cmds.menuItem(j, label=j )
                if j in buttonImageDic:
                    pm.menuItem(b, edit=1, i = drivePath+buttonImageDic[j][0])       
                if j in buttonCommandDic:
                    pyfilename=j
                    command = 'createPY("' + drivePath + buttonCommandDic[j][0] + '")'
                    pm.menuItem(b, edit=True, c=command)
        cmds.setParent( '..', menu=True )
mainWinMenuItem()
