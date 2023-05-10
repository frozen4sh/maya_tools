# import maya.cmds as cmds
# import numpy as np
# # Load the text file
# text_file_path = r"D:\Justin\Audio2Face\Postman\TTS_Voice_001.txt"
# data_str=None
# with open(text_file_path, 'r') as f:
#     data_str = f.readlines()

import maya.cmds as cmds
import sys
#scriptpath =r'C:\Python27\Lib\site-packages'
scriptpath =r'C:\Users\vivestudios\AppData\Local\Programs\Python\Python37\Lib\site-packages'
sys.path.append(scriptpath)
import maya.cmds as cmds
import numpy as np
import os
import sys



fullpath = os.path.join("C:\\Users\\vivestudios\\Downloads\\" , "bs_value_1114_2_01.npy")

print (fullpath)


lista = ["browDownL","browDownR","browLateralL","browLateralR","browRaiseInL","browRaiseInR","browRaiseOuterL","browRaiseOuterR","earUpL","earUpR","eyeBlinkL","eyeBlinkR","eyeLidPressL","eyeLidPressR","eyeWidenL","eyeWidenR","eyeSquintInnerL","eyeSquintInnerR","eyeCheekRaiseL","eyeCheekRaiseR","eyeFaceScrunchL","eyeFaceScrunchR","eyeUpperLidUpL","eyeUpperLidUpR","eyeRelaxL","eyeRelaxR","eyeLowerLidUpL","eyeLowerLidUpR","eyeLowerLidDownL","eyeLowerLidDownR","eyeLookUpL","eyeLookUpR","eyeLookDownL","eyeLookDownR","eyeLookLeftL","eyeLookLeftR","eyeLookRightL","eyeLookRightR","eyePupilWideL","eyePupilWideR","eyePupilNarrowL","eyePupilNarrowR","eyeParallelLookDirection","eyelashesUpINL","eyelashesUpINR","eyelashesUpOUTL","eyelashesUpOUTR","eyelashesDownINL","eyelashesDownINR","eyelashesDownOUTL","eyelashesDownOUTR","noseWrinkleL","noseWrinkleR","noseWrinkleUpperL","noseWrinkleUpperR","noseNostrilDepressL","noseNostrilDepressR","noseNostrilDilateL","noseNostrilDilateR","noseNostrilCompressL","noseNostrilCompressR","noseNasolabialDeepenL","noseNasolabialDeepenR","mouthCheekSuckL","mouthCheekSuckR","mouthCheekBlowL","mouthCheekBlowR","mouthLipsBlowL","mouthLipsBlowR","mouthLeft","mouthRight","mouthUp","mouthDown","mouthUpperLipRaiseL","mouthUpperLipRaiseR","mouthLowerLipDepressL","mouthLowerLipDepressR","mouthCornerPullL","mouthCornerPullR","mouthStretchL","mouthStretchR","mouthStretchLipsCloseL","mouthStretchLipsCloseR","mouthDimpleL","mouthDimpleR","mouthCornerDepressL","mouthCornerDepressR","mouthPressUL","mouthPressUR","mouthPressDL","mouthPressDR","mouthLipsPurseUL","mouthLipsPurseUR","mouthLipsPurseDL","mouthLipsPurseDR","mouthLipsTowardsUL","mouthLipsTowardsUR","mouthLipsTowardsDL","mouthLipsTowardsDR","mouthFunnelUL","mouthFunnelUR","mouthFunnelDL","mouthFunnelDR","mouthLipsTogetherUL","mouthLipsTogetherUR","mouthLipsTogetherDL","mouthLipsTogetherDR","mouthUpperLipBiteL","mouthUpperLipBiteR","mouthLowerLipBiteL","mouthLowerLipBiteR","mouthLipsTightenUL","mouthLipsTightenUR","mouthLipsTightenDL","mouthLipsTightenDR","mouthLipsPressL","mouthLipsPressR","mouthSharpCornerPullL","mouthSharpCornerPullR","mouthStickyUC","mouthStickyUINL","mouthStickyUINR","mouthStickyUOUTL","mouthStickyUOUTR","mouthStickyDC","mouthStickyDINL","mouthStickyDINR","mouthStickyDOUTL","mouthStickyDOUTR","mouthLipsStickyLPh1","mouthLipsStickyLPh2","mouthLipsStickyLPh3","mouthLipsStickyRPh1","mouthLipsStickyRPh2","mouthLipsStickyRPh3","mouthLipsPushUL","mouthLipsPushUR","mouthLipsPushDL","mouthLipsPushDR","mouthLipsPullUL","mouthLipsPullUR","mouthLipsPullDL","mouthLipsPullDR","mouthLipsThinUL","mouthLipsThinUR","mouthLipsThinDL","mouthLipsThinDR","mouthLipsThickUL","mouthLipsThickUR","mouthLipsThickDL","mouthLipsThickDR","mouthCornerSharpenUL","mouthCornerSharpenUR","mouthCornerSharpenDL","mouthCornerSharpenDR","mouthCornerRounderUL","mouthCornerRounderUR","mouthCornerRounderDL","mouthCornerRounderDR","mouthUpperLipTowardsTeethL","mouthUpperLipTowardsTeethR","mouthLowerLipTowardsTeethL","mouthLowerLipTowardsTeethR","mouthUpperLipShiftLeft","mouthUpperLipShiftRight","mouthLowerLipShiftLeft","mouthLowerLipShiftRight","mouthUpperLipRollInL","mouthUpperLipRollInR","mouthUpperLipRollOutL","mouthUpperLipRollOutR","mouthLowerLipRollInL","mouthLowerLipRollInR","mouthLowerLipRollOutL","mouthLowerLipRollOutR","mouthCornerUpL","mouthCornerUpR","mouthCornerDownL","mouthCornerDownR","mouthCornerWideL","mouthCornerWideR","mouthCornerNarrowL","mouthCornerNarrowR","tongueUp","tongueDown","tongueLeft","tongueRight","tongueOut","tongueIn","tongueRollUp","tongueRollDown","tongueRollLeft","tongueRollRight","tongueTipUp","tongueTipDown","tongueTipLeft","tongueTipRight","tongueWide","tongueNarrow","tonguePress","jawOpen","jawLeft","jawRight","jawFwd","jawBack","jawClenchL","jawClenchR","jawChinRaiseDL","jawChinRaiseDR","jawChinRaiseUL","jawChinRaiseUR","jawChinCompressL","jawChinCompressR","jawOpenExtreme","neckStretchL","neckStretchR","neckSwallowPh1","neckSwallowPh2","neckSwallowPh3","neckSwallowPh4","neckMastoidContractL","neckMastoidContractR","neckThroatDown","neckThroatUp","neckDigastricDown","neckDigastricUp","neckThroatExhale","neckThroatInhale","teethUpU","teethUpD","teethDownU","teethDownD","teethLeftU","teethLeftD","teethRightU","teethRightD","teethFwdU","teethFwdD","teethBackU","teethBackD","headTurnUpU","headTurnUpM","headTurnUpD","headTurnDownU","headTurnDownM","headTurnDownD","headTurnLeftU","headTurnLeftM","headTurnLeftD","headTurnRightU","headTurnRightM","headTurnRightD","headTiltLeftU","headTiltLeftM","headTiltLeftD","headTiltRightU","headTiltRightM","headTiltRightD","lookAtSwitch" ]

frames = np.load(fullpath)
frames.shape
len(frames[3294])
print (frames[3294])

# data_str = ' '.join(map(str, data_str))
# data_str = data_str.replace('\n', '').replace('[', '').replace(']', '')
# data = np.fromstring(data_str, sep=' ')
# data=data.reshape(int( data.shape[0]/259 ),259)
# print ( data.shape )

# for i in range(0,3295):
#     cmds.currentTime(i)
#     cmds.setAttr('CTRL_expressions.'+list[1] , frames[i][1])
#     cmds.setKeyframe('CTRL_expressions.'+list[0])
#     numi=0
#     for j in frames[i]:
#         cmds.setAttr('CTRL_expressions.'+list[numi] , j)
#         cmds.setKeyframe('CTRL_expressions.'+list[numi])
#         numi=numi+1

for i in range(0,3294):
    cmds.currentTime(i)
    cmds.setAttr('CTRL_expressions.'+lista[1] , frames[i][1])
    cmds.setKeyframe('CTRL_expressions.'+lista[0])
    numi=0
    for j in frames[i]:
        cmds.setAttr('CTRL_expressions.'+lista[numi] , j)
        cmds.setKeyframe('CTRL_expressions.'+lista[numi])
        numi=numi+1