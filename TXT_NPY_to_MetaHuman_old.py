import maya.cmds as cmds
import numpy as np
# Load the text file
text_file_path = r"D:\Justin\Audio2Face\Postman\TTS_Voice_001.txt"
data_str=None
with open(text_file_path, 'r') as f:
    data_str = f.readlines()


lista = ["browDownL","browDownR","browLateralL","browLateralR","browRaiseInL","browRaiseInR","browRaiseOuterL","browRaiseOuterR","earUpL","earUpR","eyeBlinkL","eyeBlinkR","eyeLidPressL","eyeLidPressR","eyeWidenL","eyeWidenR","eyeSquintInnerL","eyeSquintInnerR","eyeCheekRaiseL","eyeCheekRaiseR","eyeFaceScrunchL","eyeFaceScrunchR","eyeUpperLidUpL","eyeUpperLidUpR","eyeRelaxL","eyeRelaxR","eyeLowerLidUpL","eyeLowerLidUpR","eyeLowerLidDownL","eyeLowerLidDownR","eyeLookUpL","eyeLookUpR","eyeLookDownL","eyeLookDownR","eyeLookLeftL","eyeLookLeftR","eyeLookRightL","eyeLookRightR","eyePupilWideL","eyePupilWideR","eyePupilNarrowL","eyePupilNarrowR","eyeParallelLookDirection","eyelashesUpINL","eyelashesUpINR","eyelashesUpOUTL","eyelashesUpOUTR","eyelashesDownINL","eyelashesDownINR","eyelashesDownOUTL","eyelashesDownOUTR","noseWrinkleL","noseWrinkleR","noseWrinkleUpperL","noseWrinkleUpperR","noseNostrilDepressL","noseNostrilDepressR","noseNostrilDilateL","noseNostrilDilateR","noseNostrilCompressL","noseNostrilCompressR","noseNasolabialDeepenL","noseNasolabialDeepenR","mouthCheekSuckL","mouthCheekSuckR","mouthCheekBlowL","mouthCheekBlowR","mouthLipsBlowL","mouthLipsBlowR","mouthLeft","mouthRight","mouthUp","mouthDown","mouthUpperLipRaiseL","mouthUpperLipRaiseR","mouthLowerLipDepressL","mouthLowerLipDepressR","mouthCornerPullL","mouthCornerPullR","mouthStretchL","mouthStretchR","mouthStretchLipsCloseL","mouthStretchLipsCloseR","mouthDimpleL","mouthDimpleR","mouthCornerDepressL","mouthCornerDepressR","mouthPressUL","mouthPressUR","mouthPressDL","mouthPressDR","mouthLipsPurseUL","mouthLipsPurseUR","mouthLipsPurseDL","mouthLipsPurseDR","mouthLipsTowardsUL","mouthLipsTowardsUR","mouthLipsTowardsDL","mouthLipsTowardsDR","mouthFunnelUL","mouthFunnelUR","mouthFunnelDL","mouthFunnelDR","mouthLipsTogetherUL","mouthLipsTogetherUR","mouthLipsTogetherDL","mouthLipsTogetherDR","mouthUpperLipBiteL","mouthUpperLipBiteR","mouthLowerLipBiteL","mouthLowerLipBiteR","mouthLipsTightenUL","mouthLipsTightenUR","mouthLipsTightenDL","mouthLipsTightenDR","mouthLipsPressL","mouthLipsPressR","mouthSharpCornerPullL","mouthSharpCornerPullR","mouthStickyUC","mouthStickyUINL","mouthStickyUINR","mouthStickyUOUTL","mouthStickyUOUTR","mouthStickyDC","mouthStickyDINL","mouthStickyDINR","mouthStickyDOUTL","mouthStickyDOUTR","mouthLipsStickyLPh1","mouthLipsStickyLPh2","mouthLipsStickyLPh3","mouthLipsStickyRPh1","mouthLipsStickyRPh2","mouthLipsStickyRPh3","mouthLipsPushUL","mouthLipsPushUR","mouthLipsPushDL","mouthLipsPushDR","mouthLipsPullUL","mouthLipsPullUR","mouthLipsPullDL","mouthLipsPullDR","mouthLipsThinUL","mouthLipsThinUR","mouthLipsThinDL","mouthLipsThinDR","mouthLipsThickUL","mouthLipsThickUR","mouthLipsThickDL","mouthLipsThickDR","mouthCornerSharpenUL","mouthCornerSharpenUR","mouthCornerSharpenDL","mouthCornerSharpenDR","mouthCornerRounderUL","mouthCornerRounderUR","mouthCornerRounderDL","mouthCornerRounderDR","mouthUpperLipTowardsTeethL","mouthUpperLipTowardsTeethR","mouthLowerLipTowardsTeethL","mouthLowerLipTowardsTeethR","mouthUpperLipShiftLeft","mouthUpperLipShiftRight","mouthLowerLipShiftLeft","mouthLowerLipShiftRight","mouthUpperLipRollInL","mouthUpperLipRollInR","mouthUpperLipRollOutL","mouthUpperLipRollOutR","mouthLowerLipRollInL","mouthLowerLipRollInR","mouthLowerLipRollOutL","mouthLowerLipRollOutR","mouthCornerUpL","mouthCornerUpR","mouthCornerDownL","mouthCornerDownR","mouthCornerWideL","mouthCornerWideR","mouthCornerNarrowL","mouthCornerNarrowR","tongueUp","tongueDown","tongueLeft","tongueRight","tongueOut","tongueIn","tongueRollUp","tongueRollDown","tongueRollLeft","tongueRollRight","tongueTipUp","tongueTipDown","tongueTipLeft","tongueTipRight","tongueWide","tongueNarrow","tonguePress","jawOpen","jawLeft","jawRight","jawFwd","jawBack","jawClenchL","jawClenchR","jawChinRaiseDL","jawChinRaiseDR","jawChinRaiseUL","jawChinRaiseUR","jawChinCompressL","jawChinCompressR","jawOpenExtreme","neckStretchL","neckStretchR","neckSwallowPh1","neckSwallowPh2","neckSwallowPh3","neckSwallowPh4","neckMastoidContractL","neckMastoidContractR","neckThroatDown","neckThroatUp","neckDigastricDown","neckDigastricUp","neckThroatExhale","neckThroatInhale","teethUpU","teethUpD","teethDownU","teethDownD","teethLeftU","teethLeftD","teethRightU","teethRightD","teethFwdU","teethFwdD","teethBackU","teethBackD","headTurnUpU","headTurnUpM","headTurnUpD","headTurnDownU","headTurnDownM","headTurnDownD","headTurnLeftU","headTurnLeftM","headTurnLeftD","headTurnRightU","headTurnRightM","headTurnRightD","headTiltLeftU","headTiltLeftM","headTiltLeftD","headTiltRightU","headTiltRightM","headTiltRightD","lookAtSwitch" ]



data_str = ' '.join(map(str, data_str))
data_str = data_str.replace('\n', '').replace('[', '').replace(']', '')
data = np.fromstring(data_str, sep=' ')
data=data.reshape(int( data.shape[0]/259 ),259)
print ( data.shape )

for i in range(0,318):
    cmds.currentTime(i)
    cmds.setAttr('CTRL_expressions.'+lista[0] , data[i][0])
    cmds.setKeyframe('CTRL_expressions.'+lista[0])
    numi=0
    for j in data[i]:
        cmds.setAttr('CTRL_expressions.'+lista[numi] , j)
        cmds.setKeyframe('CTRL_expressions.'+lista[numi])
        numi=numi+1
