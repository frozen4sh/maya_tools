import sys
sys.version
scriptPath=r'C:\python377\Lib\site-packages'
sys.path.append(scriptPath)
import maya.cmds as cmds
import requests
import numpy as np
import json 
import pymel.core as pm
import requests
import base64
#file_path=r'Z:/DigitalHuman/rvh/ml/nohsikPark/data/maya/gv5yPJcQ_asset/8k/asset_source/MetaHumans/nohsikPark_ID/SourceAssets/nohsikPark_ID_ARkit_scene.mb";addRecentFile("Z:/DigitalHuman/rvh/ml/nohsikPark/data/maya/gv5yPJcQ_asset/8k/asset_source/MetaHumans/nohsikPark_ID/SourceAssets/nohsikPark_ID_ARkit_scene.mb'
# pm.openFile(file_path, force=True)
deleteKey=["nohsikPark_ID_ARkit_rig1:MouthPressRight_CTRL","nohsikPark_ID_ARkit_rig:MouthDimpleLeft_CTRL","nohsikPark_ID_ARkit_rig:MouthShrugLower_CTRL","nohsikPark_ID_ARkit_rig1:MouthRollLower_CTRL","nohsikPark_ID_ARkit_rig1:MouthSmileLeft_CTRL","nohsikPark_ID_ARkit_rig1:EyeSquintRight_CTRL","nohsikPark_ID_ARkit_rig:TongueOut_CTRL","nohsikPark_ID_ARkit_rig1:CheekPuff_CTRL","nohsikPark_ID_ARkit_rig1:BrowDownRight_CTRL","nohsikPark_ID_ARkit_rig:EyeLookUpLeft_CTRL","nohsikPark_ID_ARkit_rig1:JawLeft_CTRL","nohsikPark_ID_ARkit_rig:MouthLeft_CTRL","nohsikPark_ID_ARkit_rig:CheekSquintLeft_CTRL","nohsikPark_ID_ARkit_rig1:CheekSquintRight_CTRL","nohsikPark_ID_ARkit_rig:MouthStretchRight_CTRL","nohsikPark_ID_ARkit_rig:MouthSmileRight_CTRL","nohsikPark_ID_ARkit_rig:EyeSquintRight_CTRL","nohsikPark_ID_ARkit_rig1:EyeLookDownRight_CTRL","nohsikPark_ID_ARkit_rig:EyeLookOutLeft_CTRL","nohsikPark_ID_ARkit_rig1:MouthFrownLeft_CTRL","nohsikPark_ID_ARkit_rig1:JawForward_CTRL","nohsikPark_ID_ARkit_rig:MouthLowerDownLeft_CTRL","nohsikPark_ID_ARkit_rig:MouthRollUpper_CTRL","nohsikPark_ID_ARkit_rig:MouthFrownRight_CTRL","nohsikPark_ID_ARkit_rig:NoseSneerLeft_CTRL","nohsikPark_ID_ARkit_rig:MouthUpperUpLeft_CTRL","nohsikPark_ID_ARkit_rig1:MouthUpperUpLeft_CTRL","nohsikPark_ID_ARkit_rig:JawLeft_CTRL","nohsikPark_ID_ARkit_rig1:MouthRollUpper_CTRL","nohsikPark_ID_ARkit_rig:MouthRight_CTRL","nohsikPark_ID_ARkit_rig:MouthUpperUpRight_CTRL","nohsikPark_ID_ARkit_rig1:MouthRight_CTRL","nohsikPark_ID_ARkit_rig1:MouthShrugLower_CTRL","nohsikPark_ID_ARkit_rig:EyeLookinRight_CTRL","nohsikPark_ID_ARkit_rig1:BrowOuterUpLeft_CTRL","nohsikPark_ID_ARkit_rig:MouthSmileLeft_CTRL","nohsikPark_ID_ARkit_rig:MouthShrugUpper_CTRL","nohsikPark_ID_ARkit_rig:MouthFunnel_CTRL","nohsikPark_ID_ARkit_rig:MouthPressLeft_CTRL","nohsikPark_ID_ARkit_rig1:CheekSquintLeft_CTRL","nohsikPark_ID_ARkit_rig1:MouthLowerDownRight_CTRL","nohsikPark_ID_ARkit_rig:EyeLookinLeft_CTRL","nohsikPark_ID_ARkit_rig1:BrowinnerUp_CTRL","nohsikPark_ID_ARkit_rig1:EyewideLeft_CTRL","nohsikPark_ID_ARkit_rig1:EyeLookUpLeft_CTRL","nohsikPark_ID_ARkit_rig1:MouthLowerDownLeft_CTRL","nohsikPark_ID_ARkit_rig1:MouthStretchRight_CTRL","nohsikPark_ID_ARkit_rig:MouthDimpleRight_CTRL","nohsikPark_ID_ARkit_rig1:EyeSquintLeft_CTRL","nohsikPark_ID_ARkit_rig1:MouthDimpleLeft_CTRL","nohsikPark_ID_ARkit_rig1:MouthPressLeft_CTRL","nohsikPark_ID_ARkit_rig1:NoseSneerLeft_CTRL","nohsikPark_ID_ARkit_rig:MouthPucker_CTRL","nohsikPark_ID_ARkit_rig1:MouthShrugUpper_CTRL","nohsikPark_ID_ARkit_rig:NoseSneerRight_CTRL","nohsikPark_ID_ARkit_rig:EyewideRight_CTRL","nohsikPark_ID_ARkit_rig1:EyeLookOutRight_CTRL","nohsikPark_ID_ARkit_rig1:MouthUpperUpRight_CTRL","nohsikPark_ID_ARkit_rig:MouthFrownLeft_CTRL","nohsikPark_ID_ARkit_rig:MouthRollLower_CTRL","nohsikPark_ID_ARkit_rig1:MouthDimpleRight_CTRL","nohsikPark_ID_ARkit_rig1:MouthSmileRight_CTRL","nohsikPark_ID_ARkit_rig:JawRight_CTRL","nohsikPark_ID_ARkit_rig1:EyeLookUpRight_CTRL","nohsikPark_ID_ARkit_rig1:JawRight_CTRL","nohsikPark_ID_ARkit_rig1:JawOpen_CTRL","nohsikPark_ID_ARkit_rig1:EyeLookOutLeft_CTRL","nohsikPark_ID_ARkit_rig:CheekSquintRight_CTRL","nohsikPark_ID_ARkit_rig:EyewideLeft_CTRL","nohsikPark_ID_ARkit_rig:EyeLookOutRight_CTRL","nohsikPark_ID_ARkit_rig1:BrowOuterUpRight_CTRL","nohsikPark_ID_ARkit_rig1:TongueOut_CTRL","nohsikPark_ID_ARkit_rig1:EyewideRight_CTRL","nohsikPark_ID_ARkit_rig1:MouthFrownRight_CTRL","nohsikPark_ID_ARkit_rig:BrowinnerUp_CTRL","nohsikPark_ID_ARkit_rig:BrowOuterUpLeft_CTRL","nohsikPark_ID_ARkit_rig:EyeBlinkRight_CTRL","nohsikPark_ID_ARkit_rig:MouthLowerDownRight_CTRL","nohsikPark_ID_ARkit_rig:BrowDownLeft_CTRL","nohsikPark_ID_ARkit_rig1:EyeLookDownLeft_CTRL","nohsikPark_ID_ARkit_rig:MouthStretchLeft_CTRL","nohsikPark_ID_ARkit_rig:JawForward_CTRL","nohsikPark_ID_ARkit_rig:EyeSquintLeft_CTRL","nohsikPark_ID_ARkit_rig:BrowDownRight_CTRL","nohsikPark_ID_ARkit_rig1:MouthPucker_CTRL","nohsikPark_ID_ARkit_rig1:NoseSneerRight_CTRL","nohsikPark_ID_ARkit_rig1:MouthFunnel_CTRL","nohsikPark_ID_ARkit_rig:CheekPuff_CTRL","nohsikPark_ID_ARkit_rig1:BrowDownLeft_CTRL","nohsikPark_ID_ARkit_rig:EyeLookDownLeft_CTRL","nohsikPark_ID_ARkit_rig:EyeBlinkLeft_CTRL","nohsikPark_ID_ARkit_rig:MouthPressRight_CTRL","nohsikPark_ID_ARkit_rig1:EyeLookinRight_CTRL","nohsikPark_ID_ARkit_rig:JawOpen_CTRL","nohsikPark_ID_ARkit_rig:BrowOuterUpRight_CTRL","nohsikPark_ID_ARkit_rig1:EyeBlinkRight_CTRL","nohsikPark_ID_ARkit_rig:EyeLookDownRight_CTRL","nohsikPark_ID_ARkit_rig1:EyeLookinLeft_CTRL","nohsikPark_ID_ARkit_rig1:MouthStretchLeft_CTRL","nohsikPark_ID_ARkit_rig:EyeLookUpRight_CTRL","nohsikPark_ID_ARkit_rig1:MouthLeft_CTRL","nohsikPark_ID_ARkit_rig1:EyeBlinkLeft_CTRL"]
#씬에 싸운드및 키가 있으면 삭제
deleteA = pm.ls(type='audio')
pm.delete(deleteA)
for i in deleteKey:
    pm.cutKey(i+'.tx')
    pm.PyNode(i+'.tx').set(0)

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
pm.currentUnit(time='ntsc')        
create_progressBar_Win('...http.........')
progressNum=0
#start        
KEY_WAV = "wav"
url = "http://192.168.10.229:20040/gtpr"
headers = {
    "Content-Type": "application/json"
}
"""
data = {
    "preset": 0,
    "soundNumber": 1    
}
"""
payload = json.dumps({
  "preset": 1,
  "soundNumber": 6
})
response = requests.request("POST", url, headers=headers, data=payload)
inData = json.loads(response.text)
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
delete_progressBar_Win()  
create_progressBar_Win('...json_pr')
progressNum=0
# import key 
arkit61={'EyeBlinkLeft':2,
     'EyeLookDownLeft':3,
     'EyeLookInLeft':4,
     'EyeLookOutLeft':5,
     'EyeLookUpLeft':6,
     'EyeSquintLeft':7,
     'EyeWideLeft':8,
     'EyeBlinkRight':9,
     'EyeLookDownRight':10,
     'EyeLookInRight':11,
     'EyeLookOutRight':12,
     'EyeLookUpRight':13,
     'EyeSquintRight':14,
     'EyeWideRight':15,
     'JawForward':16,
     'JawRight':17,
     'JawLeft':18,
     'JawOpen':19,
     'MouthClose':20,
     'MouthFunnel':21,
     'MouthPucker':22,
     'MouthRight':23,
     'MouthLeft':24,
     'MouthSmileLeft':25,
     'MouthSmileRight':26,
     'MouthFrownLeft':27,
     'MouthFrownRight':28,
     'MouthDimpleLeft':29,
     'MouthDimpleRight':30,
     'MouthStretchLeft':31,
     'MouthStretchRight':32,
     'MouthRollLower':33,
     'MouthRollUpper':34,
     'MouthShrugLower':35,
     'MouthShrugUpper':36,
     'MouthPressLeft':37,
     'MouthPressRight':38,
     'MouthLowerDownLeft':39,
     'MouthLowerDownRight':40,
     'MouthUpperUpLeft':41,
     'MouthUpperUpRight':42,
     'BrowDownLeft':43,
     'BrowDownRight':44,
     'BrowInnerUp':45,
     'BrowOuterUpLeft':46,
     'BrowOuterUpRight':47,
     'CheekPuff':48,
     'CheekSquintLeft':49,
     'CheekSquintRight':50,
     'NoseSneerLeft':51,
     'NoseSneerRight':52,
     'TongueOut':53}
rarkit61={2:'EyeBlinkLeft',
    3:'EyeLookDownLeft',
    4:'EyeLookInLeft',
    5:'EyeLookOutLeft',
    6:'EyeLookUpLeft',
    7:'EyeSquintLeft',
    8:'EyeWideLeft',
    9:'EyeBlinkRight',
    10:'EyeLookDownRight',
    11:'EyeLookInRight',
    12:'EyeLookOutRight',
    13:'EyeLookUpRight',
    14:'EyeSquintRight',
    15:'EyeWideRight',
    16:'JawForward',
    17:'JawRight',
    18:'JawLeft',
    19:'JawOpen',
    20:'MouthClose',
    21:'MouthFunnel',
    22:'MouthPucker',
    23:'MouthRight',
    24:'MouthLeft',
    25:'MouthSmileLeft',
    26:'MouthSmileRight',
    27:'MouthFrownLeft',
    28:'MouthFrownRight',
    29:'MouthDimpleLeft',
    30:'MouthDimpleRight',
    31:'MouthStretchLeft',
    32:'MouthStretchRight',
    33:'MouthRollLower',
    34:'MouthRollUpper',
    35:'MouthShrugLower',
    36:'MouthShrugUpper',
    37:'MouthPressLeft',
    38:'MouthPressRight',
    39:'MouthLowerDownLeft',
    40:'MouthLowerDownRight',
    41:'MouthUpperUpLeft',
    42:'MouthUpperUpRight',
    43:'BrowDownLeft',
    44:'BrowDownRight',
    45:'BrowInnerUp',
    46:'BrowOuterUpLeft',
    47:'BrowOuterUpRight',
    48:'CheekPuff',
    49:'CheekSquintLeft',
    50:'CheekSquintRight',
    51:'NoseSneerLeft',
    52:'NoseSneerRight',
    53:'TongueOut',
    54:'HeadYaw',
    55:'HeadPitch',
    56:'HeadRoll',
    57:'LeftEyeYaw',
    58:'LeftEyePitch',
    59:'LeftEyeRoll',
    60:'RightEyeYaw',
    61:'RightEyePitch',
    62:'RightEyeRoll'
    }
arkitCtrl={'EyeBlinkLeft':"EyeBlinkLeft",
    'EyeLookDownLeft':"EyeLookDownLeft",
    'EyeLookInLeft':"EyeLookinLeft",
    'EyeLookOutLeft':"EyeLookOutLeft",
    'EyeLookUpLeft':"EyeLookUpLeft",
    'EyeSquintLeft':"EyeSquintLeft",
    'EyeWideLeft':"EyewideLeft",
    'EyeBlinkRight':"EyeBlinkRight",
    'EyeLookDownRight':"EyeLookDownRight",
    'EyeLookInRight':"EyeLookinRight",
    'EyeLookOutRight':"EyeLookOutRight",
    'EyeLookUpRight':"EyeLookUpRight",
    'EyeSquintRight':"EyeSquintRight",
    'EyeWideRight':"EyewideRight",
    'JawForward':"JawForward",
    'JawRight':"JawLeft",
    'JawLeft':"JawRight",
    'JawOpen':"JawOpen",
    'MouthFunnel':"MouthFunnel",
    'MouthPucker':"MouthPucker",
    'MouthRight':"MouthLeft",
    'MouthLeft':"MouthRight",
    'MouthSmileLeft':"MouthSmileLeft",
    'MouthSmileRight':"MouthSmileRight",
    'MouthFrownLeft':"MouthFrownLeft",
    'MouthFrownRight':"MouthFrownRight",
    'MouthDimpleLeft':"MouthDimpleLeft",
    'MouthDimpleRight':"MouthDimpleRight",
    'MouthStretchLeft':"MouthStretchLeft",
    'MouthStretchRight':"MouthStretchRight",
    'MouthRollLower':"MouthRollLower",
    'MouthRollUpper':"MouthRollUpper",
    'MouthShrugLower':"MouthShrugLower",
    'MouthShrugUpper':"MouthShrugUpper",
    'MouthPressLeft':"MouthPressLeft",
    'MouthPressRight':"MouthPressRight",
    'MouthLowerDownLeft':"MouthLowerDownLeft",
    'MouthLowerDownRight':"MouthLowerDownRight",
    'MouthUpperUpLeft':"MouthUpperUpLeft",
    'MouthUpperUpRight':"MouthUpperUpRight",
    'BrowDownLeft':"BrowDownLeft",
    'BrowDownRight':"BrowDownRight",
    'BrowInnerUp':"BrowinnerUp",
    'BrowOuterUpLeft':"BrowOuterUpLeft",
    'BrowOuterUpRight':"BrowOuterUpRight",
    'CheekPuff':"CheekPuff",
    'CheekSquintLeft':"CheekSquintLeft",
    'CheekSquintRight':"CheekSquintRight",
    'NoseSneerLeft':"NoseSneerLeft",
    'NoseSneerRight':"NoseSneerRight",
    'TongueOut':"TongueOut"}       


# 총 프레임
endframe=len(inData["json_gt"])
pm.playbackOptions( minTime='0sec', maxTime=endframe )
addFloat=1.0/endframe

newCSV=inData["json_gt"]
#print ( len(newCSV) )
for i in range(0,endframe):
    tx='translateX'
    for j in range(0,52):
        if rarkit61[j+2] != 'MouthClose':
            #print ( arkitCtrl[rarkit61[j+2]] )
            pm.setKeyframe("nohsikPark_ID_ARkit_rig:"+arkitCtrl[rarkit61[j+2]]+'_CTRL', attribute=tx, v = float( newCSV[i][j] ), t=i )            
    update_progress_bar( int(progressNum*100 ) ) 
    progressNum=progressNum+addFloat  

delete_progressBar_Win()  
create_progressBar_Win('...json_pr')
progressNum=0
    
newCSV1=inData["json_pr"]
endframe=len(inData["json_pr"])
for i in range(0,endframe):
    tx='translateX'
    for j in range(0,52):
        if rarkit61[j+2] != 'MouthClose':
            pm.setKeyframe("nohsikPark_ID_ARkit_rig1:"+arkitCtrl[rarkit61[j+2]]+'_CTRL', attribute=tx, v = float( newCSV1[i][j] ), t=i )            
    update_progress_bar( int(progressNum*100 ) ) 
    progressNum=progressNum+addFloat  
             
delete_progressBar_Win()
pm.mel.eval('playButtonForward;')
