# 160 개 컨트롤러 버전

import maya.cmds as cmds
import pymel.core as pm
import sys
#scriptpath =r'C:\Python27\Lib\site-packages'
scriptpath =r'C:\Users\hyh14\AppData\Local\Programs\Python\Python312\Lib\site-packages'
sys.path.append(scriptpath)
import numpy as np
import requests


cmds.file( r"Z:\DigitalHuman\rvh\ml\yehunhwang\data\maya\TTS_Danielle_full_rig.mb" , open=True )

# text_file_path = r"D:\Justin\Audio2Face\Postman\TTS_Voice_001_M1_03.txt"
# data_str=None
# with open(text_file_path, 'r') as f:
#     data_str = f.readlines()

wav_file = r"Z:\DigitalHuman\rvh\ml\yehunhwang\data\wav\TTS_Voice_001.wav"
with open(wav_file, 'rb') as f:
    getdata=requests.post('http://192.168.10.229:8401/uploadfiles', files={'files': f})
data_str = ''
data_str = getdata.text

# 텍스트를 저장할 파일을 엽니다. 
file = open(r"Z:\DigitalHuman\rvh\ml\yehunhwang\data\numpy\temp\TTS_Voice_001_M0.txt", "w")

# 파일에 쓸 텍스트를 작성합니다. 
text = getdata.text 
file.write(text)

# 파일을 닫습니다. 
file.close()

lista = ["browDownL","browDownR","browLateralL","browLateralR","browRaiseInL","browRaiseInR","browRaiseOuterL","browRaiseOuterR","earUpL","earUpR","eyeBlinkL","eyeBlinkR","eyeLidPressL","eyeLidPressR","eyeWidenL","eyeWidenR","eyeSquintInnerL","eyeSquintInnerR","eyeCheekRaiseL","eyeCheekRaiseR","eyeFaceScrunchL","eyeFaceScrunchR","eyeUpperLidUpL","eyeUpperLidUpR","eyeRelaxL","eyeRelaxR","eyeLowerLidUpL","eyeLowerLidUpR","eyeLowerLidDownL","eyeLowerLidDownR","eyeLookUpL","eyeLookUpR","eyeLookDownL","eyeLookDownR","eyeLookLeftL","eyeLookLeftR","eyeLookRightL","eyeLookRightR","eyePupilWideL","eyePupilWideR","eyePupilNarrowL","eyePupilNarrowR","eyeParallelLookDirection","eyelashesUpINL","eyelashesUpINR","eyelashesUpOUTL","eyelashesUpOUTR","eyelashesDownINL","eyelashesDownINR","eyelashesDownOUTL","eyelashesDownOUTR","noseWrinkleL","noseWrinkleR","noseWrinkleUpperL","noseWrinkleUpperR","noseNostrilDepressL","noseNostrilDepressR","noseNostrilDilateL","noseNostrilDilateR","noseNostrilCompressL","noseNostrilCompressR","noseNasolabialDeepenL","noseNasolabialDeepenR","mouthCheekSuckL","mouthCheekSuckR","mouthCheekBlowL","mouthCheekBlowR","mouthLipsBlowL","mouthLipsBlowR","mouthLeft","mouthRight","mouthUp","mouthDown","mouthUpperLipRaiseL","mouthUpperLipRaiseR","mouthLowerLipDepressL","mouthLowerLipDepressR","mouthCornerPullL","mouthCornerPullR","mouthStretchL","mouthStretchR","mouthStretchLipsCloseL","mouthStretchLipsCloseR","mouthDimpleL","mouthDimpleR","mouthCornerDepressL","mouthCornerDepressR","mouthPressUL","mouthPressUR","mouthPressDL","mouthPressDR","mouthLipsPurseUL","mouthLipsPurseUR","mouthLipsPurseDL","mouthLipsPurseDR","mouthLipsTowardsUL","mouthLipsTowardsUR","mouthLipsTowardsDL","mouthLipsTowardsDR","mouthFunnelUL","mouthFunnelUR","mouthFunnelDL","mouthFunnelDR","mouthLipsTogetherUL","mouthLipsTogetherUR","mouthLipsTogetherDL","mouthLipsTogetherDR","mouthUpperLipBiteL","mouthUpperLipBiteR","mouthLowerLipBiteL","mouthLowerLipBiteR","mouthLipsTightenUL","mouthLipsTightenUR","mouthLipsTightenDL","mouthLipsTightenDR","mouthLipsPressL","mouthLipsPressR","mouthSharpCornerPullL","mouthSharpCornerPullR","mouthStickyUC","mouthStickyUINL","mouthStickyUINR","mouthStickyUOUTL","mouthStickyUOUTR","mouthStickyDC","mouthStickyDINL","mouthStickyDINR","mouthStickyDOUTL","mouthStickyDOUTR","mouthLipsStickyLPh1","mouthLipsStickyLPh2","mouthLipsStickyLPh3","mouthLipsStickyRPh1","mouthLipsStickyRPh2","mouthLipsStickyRPh3","mouthLipsPushUL","mouthLipsPushUR","mouthLipsPushDL","mouthLipsPushDR","mouthLipsPullUL","mouthLipsPullUR","mouthLipsPullDL","mouthLipsPullDR","mouthLipsThinUL","mouthLipsThinUR","mouthLipsThinDL","mouthLipsThinDR","mouthLipsThickUL","mouthLipsThickUR","mouthLipsThickDL","mouthLipsThickDR","mouthCornerSharpenUL","mouthCornerSharpenUR","mouthCornerSharpenDL","mouthCornerSharpenDR","mouthCornerRounderUL","mouthCornerRounderUR","mouthCornerRounderDL","mouthCornerRounderDR","mouthUpperLipTowardsTeethL","mouthUpperLipTowardsTeethR","mouthLowerLipTowardsTeethL","mouthLowerLipTowardsTeethR","mouthUpperLipShiftLeft","mouthUpperLipShiftRight","mouthLowerLipShiftLeft","mouthLowerLipShiftRight","mouthUpperLipRollInL","mouthUpperLipRollInR","mouthUpperLipRollOutL","mouthUpperLipRollOutR","mouthLowerLipRollInL","mouthLowerLipRollInR","mouthLowerLipRollOutL","mouthLowerLipRollOutR","mouthCornerUpL","mouthCornerUpR","mouthCornerDownL","mouthCornerDownR","mouthCornerWideL","mouthCornerWideR","mouthCornerNarrowL","mouthCornerNarrowR","tongueUp","tongueDown","tongueLeft","tongueRight","tongueOut","tongueIn","tongueRollUp","tongueRollDown","tongueRollLeft","tongueRollRight","tongueTipUp","tongueTipDown","tongueTipLeft","tongueTipRight","tongueWide","tongueNarrow","tonguePress","jawOpen","jawLeft","jawRight","jawFwd","jawBack","jawClenchL","jawClenchR","jawChinRaiseDL","jawChinRaiseDR","jawChinRaiseUL","jawChinRaiseUR","jawChinCompressL","jawChinCompressR","jawOpenExtreme","neckStretchL","neckStretchR","neckSwallowPh1","neckSwallowPh2","neckSwallowPh3","neckSwallowPh4","neckMastoidContractL","neckMastoidContractR","neckThroatDown","neckThroatUp","neckDigastricDown","neckDigastricUp","neckThroatExhale","neckThroatInhale","teethUpU","teethUpD","teethDownU","teethDownD","teethLeftU","teethLeftD","teethRightU","teethRightD","teethFwdU","teethFwdD","teethBackU","teethBackD","headTurnUpU","headTurnUpM","headTurnUpD","headTurnDownU","headTurnDownM","headTurnDownD","headTurnLeftU","headTurnLeftM","headTurnLeftD","headTurnRightU","headTurnRightM","headTurnRightD","headTiltLeftU","headTiltLeftM","headTiltLeftD","headTiltRightU","headTiltRightM","headTiltRightD","lookAtSwitch" ]


# data_str = ' '.join(map(str, data_str))
data_str = data_str.replace('\n', '').replace('[', '').replace(']', '')
data = np.fromstring(data_str, sep=' ')
data=data.reshape(int( data.shape[0]/160 ),160)
print ( data.shape[0] )

# Set frame range
cmds.playbackOptions(maxTime=data.shape[0])

# Delete the connection from CTRL_expressions - 작동안함(다끊어버림)
# cmds.select('CTRL_expressions')

# for i in lista:
#     pm.disconnectAttr('CTRL_expressions.' + i)
  
for i in range(0,data.shape[0]):
    cmds.currentTime(i)
    #data[i][1] = max(0, min(1, data[i][1]))
    #cmds.setAttr('CTRL_expressions.'+lista[1] , data[i][1])
    #cmds.setKeyframe('CTRL_expressions.'+lista[0])
    numi=0
    for j in data[i]:
        j = max(0, min(1, j))
        cmds.setAttr('CTRL_expressions.'+lista[numi] , j)
        print (i, lista[numi], "{:.8e}".format(j))
        cmds.setKeyframe('CTRL_expressions.'+lista[numi])
        numi=numi+1

cmds.select('CTRL_expressions')