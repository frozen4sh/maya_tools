# 수철님 61개 결과값을 받으면 To MH ctrl 
import sys
sys.version
scriptPath=r'C:\python377\Lib\site-packages'
sys.path.append(scriptPath)

import requests
import numpy as np
import json 
import pymel.core as pm

dic_iphon61= {"EyeBlinkLeft": 0,"EyeLookDownLeft": 1,"EyeLookInLeft": 2,"EyeLookOutLeft": 3,"EyeLookUpLeft": 4,"EyeSquintLeft": 5,"EyeWideLeft": 6,"EyeBlinkRight": 7,"EyeLookDownRight": 8,"EyeLookInRight": 9,"EyeLookOutRight": 10,"EyeLookUpRight": 11,"EyeSquintRight": 12,"EyeWideRight": 13,"JawForward": 14,"JawRight": 15,"JawLeft": 16,"JawOpen": 17,"MouthClose": 18,"MouthFunnel": 19,"MouthPucker": 20,"MouthRight": 21,"MouthLeft": 22,"MouthSmileLeft": 23,"MouthSmileRight": 24,"MouthFrownLeft": 25,"MouthFrownRight": 26,"MouthDimpleLeft": 27,"MouthDimpleRight": 28,"MouthStretchLeft": 29,"MouthStretchRight": 30,"MouthRollLower": 31,"MouthRollUpper": 32,"MouthShrugLower": 33,"MouthShrugUpper": 34,"MouthPressLeft": 35,"MouthPressRight": 36,"MouthLowerDownLeft": 37,"MouthLowerDownRight": 38,"MouthUpperUpLeft": 39,"MouthUpperUpRight": 40,"BrowDownLeft": 41,"BrowDownRight": 42,"BrowInnerUp": 43,"BrowOuterUpLeft": 44,"BrowOuterUpRight": 45,"CheekPuff": 46,"CheekSquintLeft": 47,"CheekSquintRight": 48,"NoseSneerLeft": 49,"NoseSneerRight": 50,"TongueOut": 51,"HeadYaw": 52,"HeadPitch": 53,"HeadRoll": 54,"LeftEyeYaw": 55,"LeftEyePitch": 56,"LeftEyeRoll": 57,"RightEyeYaw": 58,"RightEyePitch": 59,"RightEyeRoll": 60 }
list_iphon61=["EyeBlinkLeft","EyeLookDownLeft","EyeLookInLeft","EyeLookOutLeft","EyeLookUpLeft","EyeSquintLeft","EyeWideLeft","EyeBlinkRight","EyeLookDownRight","EyeLookInRight","EyeLookOutRight","EyeLookUpRight","EyeSquintRight","EyeWideRight","JawForward","JawRight","JawLeft","JawOpen","MouthClose","MouthFunnel","MouthPucker","MouthRight","MouthLeft","MouthSmileLeft","MouthSmileRight","MouthFrownLeft","MouthFrownRight","MouthDimpleLeft","MouthDimpleRight","MouthStretchLeft","MouthStretchRight","MouthRollLower","MouthRollUpper","MouthShrugLower","MouthShrugUpper","MouthPressLeft","MouthPressRight","MouthLowerDownLeft","MouthLowerDownRight","MouthUpperUpLeft","MouthUpperUpRight","BrowDownLeft","BrowDownRight","BrowInnerUp","BrowOuterUpLeft","BrowOuterUpRight","CheekPuff","CheekSquintLeft","CheekSquintRight","NoseSneerLeft","NoseSneerRight","TongueOut","HeadYaw","HeadPitch","HeadRoll","LeftEyeYaw","LeftEyePitch","LeftEyeRoll","RightEyeYaw","RightEyePitch","RightEyeRoll"]
dicOneByOne={"L_mouth_cornerDepress.translateY":"MouthFrownLeft" ,
     "R_mouth_cornerDepress.translateY":"MouthFrownRight" ,
     "L_mouth_funnelU.translateY":"MouthFunnel" ,
     "R_mouth_funnelU.translateY":"MouthFunnel" ,
     "R_mouth_funnelD.translateY":"MouthFunnel" ,
     "L_mouth_funnelD.translateY":"MouthFunnel" ,
     "L_mouth_lowerLipDepress.translateY":"MouthLowerDownLeft" ,
     "R_mouth_lowerLipDepress.translateY":"MouthLowerDownRight" ,
     "R_mouth_purseD.translateY":"MouthPucker" ,
     "L_mouth_purseU.translateY":"MouthPucker" ,
     "R_mouth_purseU.translateY":"MouthPucker" ,
     "L_mouth_purseD.translateY":"MouthPucker" ,
     "R_mouth_lipBiteD.translateY":"MouthRollLower" ,
     "L_mouth_lipBiteD.translateY":"MouthRollLower" ,
     "R_mouth_lipBiteU.translateY":"MouthRollUpper" ,
     "L_mouth_lipBiteU.translateY":"MouthRollUpper" ,
     "R_jaw_ChinRaiseD.translateY":"MouthShrugLower" ,
     "L_jaw_ChinRaiseD.translateY":"MouthShrugLower" ,
     "L_mouth_upperLipRaise.translateY":"MouthUpperUpLeft" ,
     "R_mouth_upperLipRaise.translateY":"MouthUpperUpRight" ,
     "L_nose.translateY":"NoseSneerLeft" ,
     "R_nose.translateY":"NoseSneerRight" ,
     "L_mouth_dimple.translateY":"MouthDimpleLeft" ,
     "R_mouth_dimple.translateY":"MouthDimpleRight" ,
     "L_mouth_lipsPressU.translateY":"MouthPressLeft" ,
     "R_mouth_lipsPressU.translateY":"MouthPressRight" ,
     "L_brow_down.translateY":"BrowDownLeft" ,
     "L_brow_lateral.translateY":"BrowDownLeft" ,
     "R_brow_down.translateY":"BrowDownRight" ,
     "R_brow_lateral.translateY":"BrowDownRight" ,
     "R_brow_raiseIn.translateY":"BrowInnerUp" ,
     "L_brow_raiseIn.translateY":"BrowInnerUp" ,
     "L_brow_raiseOut.translateY":"BrowOuterUpLeft" ,
     "R_brow_raiseOut.translateY":"BrowOuterUpRight" ,
     "L_eye_cheekRaise.translateY":"CheekSquintLeft" ,
     "R_eye_cheekRaise.translateY":"CheekSquintRight" ,
     "L_eye_squintInner.translateY":"EyeSquintLeft" ,
     "R_eye_squintInner.translateY":"EyeSquintRight" ,
     "L_mouth_suckBlow.translateY":"CheekPuff" ,
     "R_mouth_suckBlow.translateY":"CheekPuff" ,
     "L_mouth_lipsTogetherD.translateY":"MouthClose" ,
     "R_mouth_lipsTogetherU.translateY":"MouthClose" ,
     "L_mouth_lipsTogetherU.translateY":"MouthClose" ,
     "R_mouth_lipsTogetherD.translateY":"MouthClose" ,
     "C_jaw.translateY":"JawOpen" }
dicMult03={"L_mouth_tightenU.translateY":"MouthPucker" ,
     "R_mouth_tightenU.translateY":"MouthPucker" ,
     "L_mouth_tightenD.translateY":"MouthPucker" ,
     "R_mouth_tightenD.translateY":"MouthPucker" ,
     "L_mouth_sharpCornerPull.translateY":"MouthSmileLeft" ,
     "R_mouth_sharpCornerPull.translateY":"MouthSmileRight" ,
     "L_mouth_tightenU.translateY":"MouthPucker" ,
     "R_mouth_tightenU.translateY":"MouthPucker" ,
     "L_mouth_tightenD.translateY":"MouthPucker" ,
     "R_mouth_tightenD.translateY":"MouthPucker" }
dicMult05={"L_mouth_stretch.translateY":"MouthStretchLeft" ,
     "R_mouth_stretch.translateY":"MouthStretchRight" ,
     "R_jaw_ChinRaiseU.translateY":"MouthShrugUpper" ,
     "L_jaw_ChinRaiseU.translateY":"MouthShrugUpper" ,
     "L_mouth_lipsBlow.translateY":"CheekPuff" ,
     "R_mouth_lipsBlow.translateY":"CheekPuff" }
dicMult07={"L_mouth_cornerPull.translateY":"MouthSmileLeft" ,
     "R_mouth_cornerPull.translateY":"MouthSmileRight" }
dicMult_1={"C_jaw_fwdBack.translateY":"JawForward" ,
     "R_neck_mastoidContract.translateY":"MouthStretchRight" ,
     "R_neck_stretch.translateY":"MouthStretchRight" ,
     "L_neck_mastoidContract.translateY":"MouthStretchLeft" ,
     "L_neck_stretch.translateY":"MouthStretchLeft" }
dicdvd02={ "L_mouth_stickyOuterU.translateY":"MouthFunnel" ,
     "R_mouth_stickyOuterU.translateY":"MouthFunnel" ,
     "L_mouth_stickyOuterD.translateY":"MouthFunnel" ,
     "R_mouth_stickyOuterD.translateY":"MouthFunnel" }
dicdvd05={ "L_mouth_stickyInnerU.translateY":"MouthFunnel" ,
     "R_mouth_stickyInnerU.translateY":"MouthFunnel" ,
     "L_mouth_stickyInnerD.translateY":"MouthFunnel" ,
     "R_mouth_stickyInnerD.translateY":"MouthFunnel" ,
     "L_mouth_lipSticky.translateY":"MouthFunnel" ,
     "R_mouth_lipSticky.translateY":"MouthFunnel" }
dicdvd20={ "C_mouth_stickyU .translateY":"MouthFunnel" ,
     "C_mouth_stickyD .translateY":"MouthFunnel" }
dicUpDn={ "R_eye_blink.translateY": ("EyeWideRight","EyeBlinkRight")  ,
     "C_eye.translateY": ("EyeLookDownLeft","EyeLookUpLeft")  ,
     "C_eye.translateX": ("EyeLookInLeft","EyeLookOutLeft")  ,
     "C_jaw.translateX": ("JawLeft","JawRight")  ,
     "C_mouth.translateX": ("MouthLeft","MouthRight")  ,
     "L_eye_blink.translateY": ("EyeWideLeft","EyeBlinkLeft")  }
     
wav_file = r'C:\Users\vive\Downloads\OneDrive_2023-05-09\TTS_Voice_001.wav'
with open(wav_file, 'rb') as f:
    getdata=requests.post('http://192.168.10.220:8000/wav_to_lips', files={'file': f})

getjson = json.loads(getdata.content)
# Set frame range
intMaxTime=len(getjson)
pm.currentUnit(time='ntsc')
pm.playbackOptions(maxTime=intMaxTime+1)

for intFrame in range(intMaxTime):
    #intFrame=0
    dicMHCtrl={}
    for i in dicOneByOne:
        numI=dic_iphon61[dicOneByOne[i]]
        dicMHCtrl[i]=getjson[intFrame][numI]
    for i in dicMult03:    
        numI=dic_iphon61[dicMult03[i]]
        dicMHCtrl[i]=getjson[intFrame][numI]*0.3
    for i in dicMult05:    
        numI=dic_iphon61[dicMult05[i]]
        dicMHCtrl[i]=getjson[intFrame][numI]*0.5
    for i in dicMult07:    
        numI=dic_iphon61[dicMult07[i]]
        dicMHCtrl[i]=getjson[intFrame][numI]*0.7
    for i in dicMult_1:    
        numI=dic_iphon61[dicMult_1[i]]
        dicMHCtrl[i]=getjson[intFrame][numI]*-1  
    for i in dicdvd02:
        numI=dic_iphon61[dicdvd02[i]]
        dicMHCtrl[i]=getjson[intFrame][numI]/2.0 
    for i in dicdvd05:
        numI=dic_iphon61[dicdvd05[i]]
        dicMHCtrl[i]=getjson[intFrame][numI]/5.0  
    for i in dicdvd20:
        numI=dic_iphon61[dicdvd20[i]]
        dicMHCtrl[i]=getjson[intFrame][numI]/20.0  
    for i in dicUpDn:
        numIA=dic_iphon61[dicUpDn[i][0]]
        numIB=dic_iphon61[dicUpDn[i][1]]
        dicMHCtrl[i]=(getjson[intFrame][numIA]*-1)+(getjson[intFrame][numIB])
    pm.currentTime(intFrame+1)
    for i in dicMHCtrl:
        pm.PyNode('CTRL_'+i).set(dicMHCtrl[i])
        pm.setKeyframe('CTRL_'+i)
