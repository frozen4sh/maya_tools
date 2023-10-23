import sys
sys.version
scriptPath=r'C:\python377\Lib\site-packages'
sys.path.append(scriptPath)
scriptPath=r'Z:\Private_Folder\kyuseokKim\site-packages'
sys.path.append(scriptPath)
import maya.cmds as cmds
import requests
import numpy as np
import json 
import pymel.core as pm
import requests
import base64
#file_path=r'Z:/DigitalHuman/rvh/ml/nohsikPark/data/maya/gv5yPJcQ_asset/8k/asset_source/MetaHumans/nohsikPark_ID/SourceAssets/nohsikPark_ID_ARkit_scene.mb'
#pm.openFile(file_path, force=True)
#deleteKey=["nohsikPark_ID_ARkit_rig1:MouthPressRight_CTRL","nohsikPark_ID_ARkit_rig:MouthDimpleLeft_CTRL","nohsikPark_ID_ARkit_rig:MouthShrugLower_CTRL","nohsikPark_ID_ARkit_rig1:MouthRollLower_CTRL","nohsikPark_ID_ARkit_rig1:MouthSmileLeft_CTRL","nohsikPark_ID_ARkit_rig1:EyeSquintRight_CTRL","nohsikPark_ID_ARkit_rig:TongueOut_CTRL","nohsikPark_ID_ARkit_rig1:CheekPuff_CTRL","nohsikPark_ID_ARkit_rig1:BrowDownRight_CTRL","nohsikPark_ID_ARkit_rig:EyeLookUpLeft_CTRL","nohsikPark_ID_ARkit_rig1:JawLeft_CTRL","nohsikPark_ID_ARkit_rig:MouthLeft_CTRL","nohsikPark_ID_ARkit_rig:CheekSquintLeft_CTRL","nohsikPark_ID_ARkit_rig1:CheekSquintRight_CTRL","nohsikPark_ID_ARkit_rig:MouthStretchRight_CTRL","nohsikPark_ID_ARkit_rig:MouthSmileRight_CTRL","nohsikPark_ID_ARkit_rig:EyeSquintRight_CTRL","nohsikPark_ID_ARkit_rig1:EyeLookDownRight_CTRL","nohsikPark_ID_ARkit_rig:EyeLookOutLeft_CTRL","nohsikPark_ID_ARkit_rig1:MouthFrownLeft_CTRL","nohsikPark_ID_ARkit_rig1:JawForward_CTRL","nohsikPark_ID_ARkit_rig:MouthLowerDownLeft_CTRL","nohsikPark_ID_ARkit_rig:MouthRollUpper_CTRL","nohsikPark_ID_ARkit_rig:MouthFrownRight_CTRL","nohsikPark_ID_ARkit_rig:NoseSneerLeft_CTRL","nohsikPark_ID_ARkit_rig:MouthUpperUpLeft_CTRL","nohsikPark_ID_ARkit_rig1:MouthUpperUpLeft_CTRL","nohsikPark_ID_ARkit_rig:JawLeft_CTRL","nohsikPark_ID_ARkit_rig1:MouthRollUpper_CTRL","nohsikPark_ID_ARkit_rig:MouthRight_CTRL","nohsikPark_ID_ARkit_rig:MouthUpperUpRight_CTRL","nohsikPark_ID_ARkit_rig1:MouthRight_CTRL","nohsikPark_ID_ARkit_rig1:MouthShrugLower_CTRL","nohsikPark_ID_ARkit_rig:EyeLookinRight_CTRL","nohsikPark_ID_ARkit_rig1:BrowOuterUpLeft_CTRL","nohsikPark_ID_ARkit_rig:MouthSmileLeft_CTRL","nohsikPark_ID_ARkit_rig:MouthShrugUpper_CTRL","nohsikPark_ID_ARkit_rig:MouthFunnel_CTRL","nohsikPark_ID_ARkit_rig:MouthPressLeft_CTRL","nohsikPark_ID_ARkit_rig1:CheekSquintLeft_CTRL","nohsikPark_ID_ARkit_rig1:MouthLowerDownRight_CTRL","nohsikPark_ID_ARkit_rig:EyeLookinLeft_CTRL","nohsikPark_ID_ARkit_rig1:BrowinnerUp_CTRL","nohsikPark_ID_ARkit_rig1:EyewideLeft_CTRL","nohsikPark_ID_ARkit_rig1:EyeLookUpLeft_CTRL","nohsikPark_ID_ARkit_rig1:MouthLowerDownLeft_CTRL","nohsikPark_ID_ARkit_rig1:MouthStretchRight_CTRL","nohsikPark_ID_ARkit_rig:MouthDimpleRight_CTRL","nohsikPark_ID_ARkit_rig1:EyeSquintLeft_CTRL","nohsikPark_ID_ARkit_rig1:MouthDimpleLeft_CTRL","nohsikPark_ID_ARkit_rig1:MouthPressLeft_CTRL","nohsikPark_ID_ARkit_rig1:NoseSneerLeft_CTRL","nohsikPark_ID_ARkit_rig:MouthPucker_CTRL","nohsikPark_ID_ARkit_rig1:MouthShrugUpper_CTRL","nohsikPark_ID_ARkit_rig:NoseSneerRight_CTRL","nohsikPark_ID_ARkit_rig:EyewideRight_CTRL","nohsikPark_ID_ARkit_rig1:EyeLookOutRight_CTRL","nohsikPark_ID_ARkit_rig1:MouthUpperUpRight_CTRL","nohsikPark_ID_ARkit_rig:MouthFrownLeft_CTRL","nohsikPark_ID_ARkit_rig:MouthRollLower_CTRL","nohsikPark_ID_ARkit_rig1:MouthDimpleRight_CTRL","nohsikPark_ID_ARkit_rig1:MouthSmileRight_CTRL","nohsikPark_ID_ARkit_rig:JawRight_CTRL","nohsikPark_ID_ARkit_rig1:EyeLookUpRight_CTRL","nohsikPark_ID_ARkit_rig1:JawRight_CTRL","nohsikPark_ID_ARkit_rig1:JawOpen_CTRL","nohsikPark_ID_ARkit_rig1:EyeLookOutLeft_CTRL","nohsikPark_ID_ARkit_rig:CheekSquintRight_CTRL","nohsikPark_ID_ARkit_rig:EyewideLeft_CTRL","nohsikPark_ID_ARkit_rig:EyeLookOutRight_CTRL","nohsikPark_ID_ARkit_rig1:BrowOuterUpRight_CTRL","nohsikPark_ID_ARkit_rig1:TongueOut_CTRL","nohsikPark_ID_ARkit_rig1:EyewideRight_CTRL","nohsikPark_ID_ARkit_rig1:MouthFrownRight_CTRL","nohsikPark_ID_ARkit_rig:BrowinnerUp_CTRL","nohsikPark_ID_ARkit_rig:BrowOuterUpLeft_CTRL","nohsikPark_ID_ARkit_rig:EyeBlinkRight_CTRL","nohsikPark_ID_ARkit_rig:MouthLowerDownRight_CTRL","nohsikPark_ID_ARkit_rig:BrowDownLeft_CTRL","nohsikPark_ID_ARkit_rig1:EyeLookDownLeft_CTRL","nohsikPark_ID_ARkit_rig:MouthStretchLeft_CTRL","nohsikPark_ID_ARkit_rig:JawForward_CTRL","nohsikPark_ID_ARkit_rig:EyeSquintLeft_CTRL","nohsikPark_ID_ARkit_rig:BrowDownRight_CTRL","nohsikPark_ID_ARkit_rig1:MouthPucker_CTRL","nohsikPark_ID_ARkit_rig1:NoseSneerRight_CTRL","nohsikPark_ID_ARkit_rig1:MouthFunnel_CTRL","nohsikPark_ID_ARkit_rig:CheekPuff_CTRL","nohsikPark_ID_ARkit_rig1:BrowDownLeft_CTRL","nohsikPark_ID_ARkit_rig:EyeLookDownLeft_CTRL","nohsikPark_ID_ARkit_rig:EyeBlinkLeft_CTRL","nohsikPark_ID_ARkit_rig:MouthPressRight_CTRL","nohsikPark_ID_ARkit_rig1:EyeLookinRight_CTRL","nohsikPark_ID_ARkit_rig:JawOpen_CTRL","nohsikPark_ID_ARkit_rig:BrowOuterUpRight_CTRL","nohsikPark_ID_ARkit_rig1:EyeBlinkRight_CTRL","nohsikPark_ID_ARkit_rig:EyeLookDownRight_CTRL","nohsikPark_ID_ARkit_rig1:EyeLookinLeft_CTRL","nohsikPark_ID_ARkit_rig1:MouthStretchLeft_CTRL","nohsikPark_ID_ARkit_rig:EyeLookUpRight_CTRL","nohsikPark_ID_ARkit_rig1:MouthLeft_CTRL","nohsikPark_ID_ARkit_rig1:EyeBlinkLeft_CTRL","nohsikPark_ID_ARkit_rig2:MouthStretchLeft_CTRL" ,"nohsikPark_ID_ARkit_rig2:MouthUpperUpLeft_CTRL" ,"nohsikPark_ID_ARkit_rig2:BrowOuterUpRight_CTRL" ,"nohsikPark_ID_ARkit_rig2:EyeLookinRight_CTRL" ,"nohsikPark_ID_ARkit_rig2:JawForward_CTRL" ,"nohsikPark_ID_ARkit_rig2:EyeLookOutLeft_CTRL" ,"nohsikPark_ID_ARkit_rig2:EyeSquintRight_CTRL" ,"nohsikPark_ID_ARkit_rig2:MouthSmileRight_CTRL" ,"nohsikPark_ID_ARkit_rig2:MouthPressLeft_CTRL" ,"nohsikPark_ID_ARkit_rig2:EyeSquintLeft_CTRL" ,"nohsikPark_ID_ARkit_rig2:MouthFrownRight_CTRL" ,"nohsikPark_ID_ARkit_rig2:MouthLowerDownRight_CTRL" ,"nohsikPark_ID_ARkit_rig2:MouthRollUpper_CTRL" ,"nohsikPark_ID_ARkit_rig2:MouthShrugLower_CTRL" ,"nohsikPark_ID_ARkit_rig2:EyeBlinkLeft_CTRL" ,"nohsikPark_ID_ARkit_rig2:EyeBlinkRight_CTRL" ,"nohsikPark_ID_ARkit_rig2:JawLeft_CTRL" ,"nohsikPark_ID_ARkit_rig2:BrowDownRight_CTRL" ,"nohsikPark_ID_ARkit_rig2:MouthLeft_CTRL" ,"nohsikPark_ID_ARkit_rig2:NoseSneerLeft_CTRL" ,"nohsikPark_ID_ARkit_rig2:MouthPressRight_CTRL" ,"nohsikPark_ID_ARkit_rig2:MouthUpperUpRight_CTRL" ,"nohsikPark_ID_ARkit_rig2:MouthDimpleRight_CTRL" ,"nohsikPark_ID_ARkit_rig2:MouthLowerDownLeft_CTRL" ,"nohsikPark_ID_ARkit_rig2:MouthStretchRight_CTRL" ,"nohsikPark_ID_ARkit_rig2:JawRight_CTRL" ,"nohsikPark_ID_ARkit_rig2:BrowDownLeft_CTRL" ,"nohsikPark_ID_ARkit_rig2:EyeLookOutRight_CTRL" ,"nohsikPark_ID_ARkit_rig2:CheekSquintRight_CTRL" ,"nohsikPark_ID_ARkit_rig2:CheekPuff_CTRL" ,"nohsikPark_ID_ARkit_rig2:MouthPucker_CTRL" ,"nohsikPark_ID_ARkit_rig2:MouthFrownLeft_CTRL" ,"nohsikPark_ID_ARkit_rig2:EyeLookUpLeft_CTRL" ,"nohsikPark_ID_ARkit_rig2:MouthDimpleLeft_CTRL" ,"nohsikPark_ID_ARkit_rig2:EyeLookDownLeft_CTRL" ,"nohsikPark_ID_ARkit_rig2:TongueOut_CTRL" ,"nohsikPark_ID_ARkit_rig2:MouthRight_CTRL" ,"nohsikPark_ID_ARkit_rig2:JawOpen_CTRL" ,"nohsikPark_ID_ARkit_rig2:EyeLookDownRight_CTRL" ,"nohsikPark_ID_ARkit_rig2:BrowOuterUpLeft_CTRL" ,"nohsikPark_ID_ARkit_rig2:EyewideRight_CTRL" ,"nohsikPark_ID_ARkit_rig2:CheekSquintLeft_CTRL" ,"nohsikPark_ID_ARkit_rig2:EyeLookinLeft_CTRL" ,"nohsikPark_ID_ARkit_rig2:MouthFunnel_CTRL" ,"nohsikPark_ID_ARkit_rig2:MouthSmileLeft_CTRL" ,"nohsikPark_ID_ARkit_rig2:BrowinnerUp_CTRL" ,"nohsikPark_ID_ARkit_rig2:NoseSneerRight_CTRL" ,"nohsikPark_ID_ARkit_rig2:MouthRollLower_CTRL" ,"nohsikPark_ID_ARkit_rig2:EyeLookUpRight_CTRL" ,"nohsikPark_ID_ARkit_rig2:EyewideLeft_CTRL" ,"nohsikPark_ID_ARkit_rig2:MouthShrugUpper_CTRL" ]
# import key 
arkit61={'EyeBlinkLeft':2,     'EyeLookDownLeft':3,     'EyeLookInLeft':4,     'EyeLookOutLeft':5,     'EyeLookUpLeft':6,     'EyeSquintLeft':7,     'EyeWideLeft':8,     'EyeBlinkRight':9,     'EyeLookDownRight':10,     'EyeLookInRight':11,     'EyeLookOutRight':12,     'EyeLookUpRight':13,     'EyeSquintRight':14,     'EyeWideRight':15,     'JawForward':16,     'JawRight':17,     'JawLeft':18,     'JawOpen':19,     'MouthClose':20,     'MouthFunnel':21,     'MouthPucker':22,     'MouthRight':23,     'MouthLeft':24,     'MouthSmileLeft':25,     'MouthSmileRight':26,     'MouthFrownLeft':27,     'MouthFrownRight':28,     'MouthDimpleLeft':29,     'MouthDimpleRight':30,     'MouthStretchLeft':31,     'MouthStretchRight':32,     'MouthRollLower':33,     'MouthRollUpper':34,     'MouthShrugLower':35,     'MouthShrugUpper':36,     'MouthPressLeft':37,     'MouthPressRight':38,     'MouthLowerDownLeft':39,     'MouthLowerDownRight':40,     'MouthUpperUpLeft':41,     'MouthUpperUpRight':42,     'BrowDownLeft':43,     'BrowDownRight':44,     'BrowInnerUp':45,     'BrowOuterUpLeft':46,     'BrowOuterUpRight':47,     'CheekPuff':48,     'CheekSquintLeft':49,     'CheekSquintRight':50,     'NoseSneerLeft':51,     'NoseSneerRight':52,     'TongueOut':53}
rarkit61={2:'EyeBlinkLeft',    3:'EyeLookDownLeft',    4:'EyeLookInLeft',    5:'EyeLookOutLeft',    6:'EyeLookUpLeft',    7:'EyeSquintLeft',    8:'EyeWideLeft',    9:'EyeBlinkRight',    10:'EyeLookDownRight',    11:'EyeLookInRight',    12:'EyeLookOutRight',    13:'EyeLookUpRight',    14:'EyeSquintRight',    15:'EyeWideRight',    16:'JawForward',    17:'JawRight',    18:'JawLeft',    19:'JawOpen',    20:'MouthClose',    21:'MouthFunnel',    22:'MouthPucker',    23:'MouthRight',    24:'MouthLeft',    25:'MouthSmileLeft',    26:'MouthSmileRight',    27:'MouthFrownLeft',    28:'MouthFrownRight',    29:'MouthDimpleLeft',    30:'MouthDimpleRight',    31:'MouthStretchLeft',    32:'MouthStretchRight',    33:'MouthRollLower',    34:'MouthRollUpper',    35:'MouthShrugLower',    36:'MouthShrugUpper',    37:'MouthPressLeft',    38:'MouthPressRight',    39:'MouthLowerDownLeft',    40:'MouthLowerDownRight',    41:'MouthUpperUpLeft',    42:'MouthUpperUpRight',    43:'BrowDownLeft',    44:'BrowDownRight',    45:'BrowInnerUp',    46:'BrowOuterUpLeft',    47:'BrowOuterUpRight',    48:'CheekPuff',    49:'CheekSquintLeft',    50:'CheekSquintRight',    51:'NoseSneerLeft',    52:'NoseSneerRight',    53:'TongueOut',    54:'HeadYaw',    55:'HeadPitch',    56:'HeadRoll',    57:'LeftEyeYaw',    58:'LeftEyePitch',    59:'LeftEyeRoll',    60:'RightEyeYaw',    61:'RightEyePitch',    62:'RightEyeRoll'    }
arkitCtrl={'EyeBlinkLeft':"EyeBlinkLeft",'EyeLookDownLeft':"EyeLookDownLeft",'EyeLookInLeft':"EyeLookinLeft",'EyeLookOutLeft':"EyeLookOutLeft",'EyeLookUpLeft':"EyeLookUpLeft",'EyeSquintLeft':"EyeSquintLeft",'EyeWideLeft':"EyewideLeft",'EyeBlinkRight':"EyeBlinkRight",'EyeLookDownRight':"EyeLookDownRight",'EyeLookInRight':"EyeLookinRight",'EyeLookOutRight':"EyeLookOutRight",'EyeLookUpRight':"EyeLookUpRight",'EyeSquintRight':"EyeSquintRight",'EyeWideRight':"EyewideRight",'JawForward':"JawForward",'JawRight':"JawLeft",'JawLeft':"JawRight",'JawOpen':"JawOpen",'MouthFunnel':"MouthFunnel",'MouthPucker':"MouthPucker",'MouthRight':"MouthLeft",'MouthLeft':"MouthRight",'MouthSmileLeft':"MouthSmileLeft",'MouthSmileRight':"MouthSmileRight",'MouthFrownLeft':"MouthFrownLeft",'MouthFrownRight':"MouthFrownRight",'MouthDimpleLeft':"MouthDimpleLeft",'MouthDimpleRight':"MouthDimpleRight",'MouthStretchLeft':"MouthStretchLeft",'MouthStretchRight':"MouthStretchRight",'MouthRollLower':"MouthRollLower",'MouthRollUpper':"MouthRollUpper",'MouthShrugLower':"MouthShrugLower",'MouthShrugUpper':"MouthShrugUpper",'MouthPressLeft':"MouthPressLeft",'MouthPressRight':"MouthPressRight",'MouthLowerDownLeft':"MouthLowerDownLeft",'MouthLowerDownRight':"MouthLowerDownRight",'MouthUpperUpLeft':"MouthUpperUpLeft",'MouthUpperUpRight':"MouthUpperUpRight",'BrowDownLeft':"BrowDownLeft",'BrowDownRight':"BrowDownRight",'BrowInnerUp':"BrowinnerUp",'BrowOuterUpLeft':"BrowOuterUpLeft",'BrowOuterUpRight':"BrowOuterUpRight",'CheekPuff':"CheekPuff",'CheekSquintLeft':"CheekSquintLeft",'CheekSquintRight':"CheekSquintRight",'NoseSneerLeft':"NoseSneerLeft",'NoseSneerRight':"NoseSneerRight",'TongueOut':"TongueOut"}  
#씬에 싸운드및 키가 있으면 삭제
deleteA = pm.ls(type='audio')
#pm.delete(deleteA)
def deleteARkitKey():
    deleteKey=["EyeSquintLeft_CTRL","BrowDownRight_CTRL","JawForward_CTRL","MouthRollUpper_CTRL","EyeBlinkRight_CTRL","MouthStretchRight_CTRL","MouthLowerDownLeft_CTRL","MouthFrownRight_CTRL","EyeLookinLeft_CTRL","CheekPuff_CTRL","MouthLowerDownRight_CTRL","MouthUpperUpLeft_CTRL","EyeLookinRight_CTRL","EyeLookOutLeft_CTRL","NoseSneerLeft_CTRL","TongueOut_CTRL","JawRight_CTRL","MouthPressRight_CTRL","BrowOuterUpRight_CTRL","CheekSquintRight_CTRL","BrowinnerUp_CTRL","MouthShrugLower_CTRL","MouthDimpleLeft_CTRL","MouthShrugUpper_CTRL","MouthLeft_CTRL","BrowOuterUpLeft_CTRL","EyeLookOutRight_CTRL","MouthFunnel_CTRL","MouthPucker_CTRL","CheekSquintLeft_CTRL","EyeLookUpLeft_CTRL","EyeBlinkLeft_CTRL","EyeLookDownRight_CTRL","MouthPressLeft_CTRL","MouthDimpleRight_CTRL","MouthRight_CTRL","NoseSneerRight_CTRL","EyewideRight_CTRL","JawLeft_CTRL","EyeLookDownLeft_CTRL","BrowDownLeft_CTRL","EyeSquintRight_CTRL","MouthSmileRight_CTRL","MouthUpperUpRight_CTRL","MouthStretchLeft_CTRL","MouthFrownLeft_CTRL","MouthSmileLeft_CTRL","EyewideLeft_CTRL","EyeLookUpRight_CTRL","MouthRollLower_CTRL","JawOpen_CTRL"]
    #씬에 싸운드및 키가 있으면 삭제
    deleteA = pm.ls(type='audio')
    pm.delete(deleteA)
    for i in deleteKey:
        pm.cutKey(i+'.tx')
        pm.PyNode(i+'.tx').set(0)  
"""         
for i in deleteKey:
    pm.cutKey(i+'.tx')
    pm.PyNode(i+'.tx').set(0)
"""    
#프로그래바 생성 부분 
def create_progressBar_Win(titleString):
    delete_progressBar_Win()    
    progress_window = cmds.window(u'Run_DNA_calibration',title=titleString,widthHeight=[300,10])
    cmds.columnLayout()
    progress_control = cmds.progressBar(u'Run_DNA_calibration_progressBar',maxValue=100, width=300)
    cmds.showWindow(progress_window)
# 프로그래스바 업데이트 함수
def update_progress_bar(value):
    cmds.progressBar('Run_DNA_calibration_progressBar', edit=True, progress=value)
#프로그래바 삭제 부분 
def delete_progressBar_Win():
    if cmds.window(u'Run_DNA_calibration', q=True, ex=True):
        cmds.deleteUI(u'Run_DNA_calibration', window=True)        
def setServer(presetInt=0,soundNumberInt=0):
    #start        
    KEY_WAV = "wav"
    url = "http://192.168.10.229:20041/history"
    headers = {
        "Content-Type": "application/json"
    }
    
    payload = json.dumps({
          "model_number": 0,        
          "wav_number": soundNumberInt,        
          "wav_type": 3
    })
    #response = requests.request("POST", url, headers=headers, data=payload)
    response = requests.request("POST", url, headers=headers, data=payload)
    inData = json.loads(response.text)
    return inData
def setSound(inData):
    decord2byte = base64.b64decode(inData["wav"])
    # 사운드 파일 경로
    sound_file_path = "D:\\your_sound_file.wav"
    with open(sound_file_path, "wb") as output_file:
        output_file.write(decord2byte)
    # Sound 노드 생성
    sound_node = cmds.shadingNode('audio', asUtility=True)
    # 사운드 파일 연결
    cmds.setAttr(sound_node + '.filename', sound_file_path, type='string')
    # 타임 슬라이더에 사운드 노드 연결
    time_slider = mel.eval("$tempVar = $gPlayBackSlider")
    cmds.timeControl(time_slider, e=True, sound=sound_node)
def MH_ARkitKeyAnimation(keyName,CtrlName):
    endframe=len(inData[keyName])
    pm.playbackOptions( minTime='0sec', maxTime=endframe )    
    if endframe !=2:
        pm.playbackOptions( minTime='0sec', maxTime=endframe )
        addFloat=1.0/endframe
        create_progressBar_Win('...'+keyName)
        progressNum=0
        newCSV=inData[keyName]
        #print ( len(newCSV) )
        for i in range(0,endframe):
            tx='translateX'
            for j in range(0,52):
                if rarkit61[j+2] != 'MouthClose':
                    #print ( arkitCtrl[rarkit61[j+2]] )
                    pm.setKeyframe(CtrlName+arkitCtrl[rarkit61[j+2]]+'_CTRL', attribute=tx, v = float( newCSV[i][j] ), t=i )            
            update_progress_bar( int(progressNum*100 ) ) 
            progressNum=progressNum+addFloat  
        delete_progressBar_Win()  
def getJsonInData(inData,stringJsonKey):
    # 총 프레임
    create_progressBar_Win('Create Key')
    progressNum=0    
    endframe=len(inData[stringJsonKey])
    pm.playbackOptions( minTime='0sec', maxTime=endframe )
    addFloat=1.0/endframe
    
    newCSV=inData[stringJsonKey]
    #print ( len(newCSV) )
    for i in range(0,endframe):
        tx='translateX'
        for j in range(0,52):
            if rarkit61[j+2] != 'MouthClose':
                #print ( arkitCtrl[rarkit61[j+2]] )
                pm.setKeyframe(arkitCtrl[rarkit61[j+2]]+'_CTRL', attribute=tx, v = float( newCSV[i][j] ), t=i )            
        update_progress_bar( int(progressNum*100 ) ) 
        progressNum=progressNum+addFloat      
    delete_progressBar_Win()  
    
    print ( endframe )        
def sound_wav(inData,model_number,wav_number,src,task,clip_num,etc,take_num):
    create_progressBar_Win('Create Sound')
    progressNum=0
    decord2byte = base64.b64decode(inData["wav"])
    # 사운드 파일 경로
    filename = f"{src}_{task}_{etc}_{clip_num}_{take_num}.wav"
    full = os.path.join("d:", filename)    
    #sound_file_path = "D:\\your_sound_file.wav"
    with open(full, "wb") as output_file:
        output_file.write(decord2byte)
    # Sound 노드 생성
    sound_node = cmds.shadingNode('audio', asUtility=True)
    # 사운드 파일 연결
    cmds.setAttr(sound_node + '.filename', full.replace('d:','D:\\'), type='string')
    # 타임 슬라이더에 사운드 노드 연결
    time_slider = mel.eval("$tempVar = $gPlayBackSlider")
    cmds.timeControl(time_slider, e=True, sound=sound_node)
    delete_progressBar_Win()  
# 실행부분
def http_192_168_10_229_20041_history(model_number,wav_number,src,task,clip_num):
    deleteARkitKey()
    pm.currentUnit(time='ntsc')        
    create_progressBar_Win('...http.........')
    progressNum=0
    wavNum=wav_number

    #MH_ARkitKeyAnimation('json','')
    #src = 'Arkit'
    #task = 'history'
    etc ='00'
    #clip_num='031'
    take_num=take_num='{0:02d}'.format(wavNum)
    
    
    # 서버 프리셋 사운드넘버 변경부분
    inData=setServer(0,wavNum)    
    #setSound(inData)
    sound_wav(inData,model_number,wav_number,src,task,clip_num,etc,take_num)
    getJsonInData(inData,"json")    
    filename = f"{src}_{task}_{etc}_{clip_num}_{take_num}.mov"
    full = os.path.join("d:", filename)
    
    pm.playblast(f=full ,sound="audio1",format='qt' ,sequenceTime=0,clearCache=1,viewer=1,showOrnaments=1,fp=0,percent=100,compression="H.264",quality=100,h=1024,w=1024)
    filename = f"{src}_{task}_{etc}_{clip_num}_{take_num}.mb"
    full = os.path.join("d:", filename)
    pm.saveAs(full)
for i in range(0,5):
    http_192_168_10_229_20041_history(0,i,'Arkit','history','031')

"""
delete_progressBar_Win()  
MH_ARkitKeyAnimation('json_gt',"nohsikPark_ID_ARkit_rig:")
MH_ARkitKeyAnimation('json_pr',"nohsikPark_ID_ARkit_rig1:")
MH_ARkitKeyAnimation('json_pr_old',"nohsikPark_ID_ARkit_rig2:")
pm.mel.eval('playButtonForward;')
print(len(inData['json_gt']))
print(len(inData['json_pr']))
print(len(inData['json_pr_old']))
"""
