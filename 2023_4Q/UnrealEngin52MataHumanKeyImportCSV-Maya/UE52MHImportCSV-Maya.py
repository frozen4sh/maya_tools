import pymel.core as pm
import csv
import maya.cmds as cmds
import time
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
start_time = time.time()        
UR_52_CTRL=["CTRL_C_eyesAim.Location.X","CTRL_C_eyesAim.Location.Y","CTRL_C_eyesAim.Location.Z","CTRL_C_eyesAim.Rotation.X","CTRL_C_eyesAim.Rotation.Y","CTRL_C_eyesAim.Rotation.Z","CTRL_C_eyesAim.Scale.X","CTRL_C_eyesAim.Scale.Y","CTRL_C_eyesAim.Scale.Z","CTRL_L_eyeAim.Location.X","CTRL_L_eyeAim.Location.Y","CTRL_L_eyeAim.Location.Z","CTRL_L_eyeAim.Rotation.X","CTRL_L_eyeAim.Rotation.Y","CTRL_L_eyeAim.Rotation.Z","CTRL_L_eyeAim.Scale.X","CTRL_L_eyeAim.Scale.Y","CTRL_L_eyeAim.Scale.Z","CTRL_R_eyeAim.Location.X","CTRL_R_eyeAim.Location.Y","CTRL_R_eyeAim.Location.Z","CTRL_R_eyeAim.Rotation.X","CTRL_R_eyeAim.Rotation.Y","CTRL_R_eyeAim.Rotation.Z","CTRL_R_eyeAim.Scale.X","CTRL_R_eyeAim.Scale.Y","CTRL_R_eyeAim.Scale.Z","CTRL_convergenceSwitch","CTRL_C_jaw.X","CTRL_C_jaw.Y","CTRL_R_jaw_clench","CTRL_C_jaw_openExtreme","CTRL_C_jaw_fwdBack","CTRL_L_jaw_clench","CTRL_L_neck_mastoidContract","CTRL_L_neck_stretch","CTRL_neck_digastricUpDown","CTRL_R_neck_stretch","CTRL_neck_throatExhaleInhale","CTRL_R_neck_mastoidContract","CTRL_neck_throatUpDown","CTRL_L_jaw_chinCompress","CTRL_R_jaw_ChinRaiseD","CTRL_R_jaw_ChinRaiseU","CTRL_L_jaw_ChinRaiseU","CTRL_R_jaw_chinCompress","CTRL_L_jaw_ChinRaiseD","CTRL_R_mouth_lipsBlow","CTRL_R_mouth_lipsPressU","CTRL_L_mouth_lipsTogetherU","CTRL_L_mouth_lipsTogetherD","CTRL_R_mouth_lipSticky","CTRL_L_mouth_lipSticky","CTRL_R_mouth_lipsTogetherU","CTRL_L_mouth_lipsPressU","CTRL_L_mouth_lipsBlow","CTRL_R_mouth_lipsTogetherD","CTRL_R_mouth_stretchLipsClose","CTRL_L_mouth_stretchLipsClose","CTRL_C_tongue_press","CTRL_C_tongue_bendTwist.X","CTRL_C_tongue_bendTwist.Y","CTRL_C_tongue_tipMove.X","CTRL_C_tongue_tipMove.Y","CTRL_C_tongue_move.X","CTRL_C_tongue_move.Y","CTRL_C_tongue_wideNarrow","CTRL_C_tongue_inOut","CTRL_C_tongue_roll","CTRL_C_mouth.X","CTRL_C_mouth.Y","CTRL_L_mouth_upperLipRaise","CTRL_L_mouth_sharpCornerPull","CTRL_L_mouth_cornerPull","CTRL_L_mouth_dimple","CTRL_L_mouth_cornerDepress","CTRL_L_mouth_stretch","CTRL_L_mouth_lowerLipDepress","CTRL_R_mouth_lowerLipDepress","CTRL_R_mouth_stretch","CTRL_L_mouth_towardsD","CTRL_R_mouth_stickyInnerU","CTRL_R_mouth_funnelU","CTRL_C_neck_swallow","CTRL_R_mouth_stickyOuterD","CTRL_C_mouth_stickyD","CTRL_L_mouth_towardsU","CTRL_R_mouth_stickyInnerD","CTRL_R_mouth_lipBiteD","CTRL_R_mouth_funnelD","CTRL_R_mouth_stickyOuterU","CTRL_C_mouth_stickyU","CTRL_L_mouth_tightenD","CTRL_L_mouth_pressU","CTRL_R_mouth_tightenD","CTRL_L_mouth_stickyInnerU","CTRL_L_mouth_funnelD","CTRL_L_mouth_suckBlow","CTRL_L_mouth_tightenU","CTRL_R_mouth_tightenU","CTRL_L_mouth_pressD","CTRL_L_mouth_funnelU","CTRL_R_mouth_towardsU","CTRL_L_mouth_stickyOuterD","CTRL_R_mouth_purseD","CTRL_L_mouth_lipBiteU","CTRL_R_mouth_pressD","CTRL_R_mouth_pressU","CTRL_L_mouth_purseD","CTRL_R_mouth_lipBiteU","CTRL_R_mouth_suckBlow","CTRL_L_mouth_purseU","CTRL_R_mouth_towardsD","CTRL_L_mouth_stickyInnerD","CTRL_L_mouth_lipBiteD","CTRL_R_mouth_purseU","CTRL_L_mouth_stickyOuterU","CTRL_R_mouth_cornerDepress","CTRL_R_mouth_upperLipRaise","CTRL_R_mouth_dimple","CTRL_R_mouth_sharpCornerPull","CTRL_R_mouth_cornerPull","CTRL_R_ear_up","CTRL_L_ear_up","CTRL_R_nose.X","CTRL_R_nose.Y","CTRL_L_nose.X","CTRL_L_nose.Y","CTRL_L_eye.X","CTRL_L_eye.Y","CTRL_L_eye_blink","CTRL_R_eye.X","CTRL_R_eye.Y","CTRL_R_eye_blink","CTRL_R_eye_pupil","CTRL_L_eye_pupil","CTRL_C_eye.X","CTRL_C_eye.Y","CTRL_C_eye_parallelLook","CTRL_L_eye_cheekRaise","CTRL_L_eye_squintInner","CTRL_L_eye_lidPress","CTRL_L_nose_wrinkleUpper","CTRL_R_nose_wrinkleUpper","CTRL_R_eye_squintInner","CTRL_R_eye_cheekRaise","CTRL_R_eye_lidPress","CTRL_R_brow_lateral","CTRL_L_brow_lateral","CTRL_R_brow_down","CTRL_L_brow_down","CTRL_L_brow_raiseOut","CTRL_L_brow_raiseIn","CTRL_R_brow_raiseIn","CTRL_R_brow_raiseOut","CTRL_lookAtSwitch","CTRL_C_teethD.X","CTRL_C_teethD.Y","CTRL_C_teethU.X","CTRL_C_teethU.Y","CTRL_C_teeth_fwdBackU","CTRL_L_mouth_corner.X","CTRL_L_mouth_corner.Y","CTRL_R_mouth_corner.X","CTRL_R_mouth_corner.Y","CTRL_C_teeth_fwdBackD","CTRL_R_eye_faceScrunch","CTRL_L_mouth_pushPullU","CTRL_R_eyelashes_tweakerOut","CTRL_R_mouth_thicknessU","CTRL_L_mouth_pushPullD","CTRL_L_mouth_thicknessU","CTRL_R_mouth_cornerSharpnessD","CTRL_C_mouth_lipShiftD","CTRL_R_mouth_lipsRollD","CTRL_L_eyelashes_tweakerOut","CTRL_L_mouth_thicknessD","CTRL_R_mouth_cornerSharpnessU","CTRL_C_mouth_lipShiftU","CTRL_R_eyelashes_tweakerIn","CTRL_R_mouth_lipsRollU","CTRL_L_eye_eyelidU","CTRL_L_mouth_lipsRollD","CTRL_L_mouth_cornerSharpnessD","CTRL_R_mouth_thicknessD","CTRL_L_eye_eyelidD","CTRL_L_mouth_lipsRollU","CTRL_L_mouth_cornerSharpnessU","CTRL_L_nose_nasolabialDeepen","CTRL_L_eye_faceScrunch","CTRL_R_mouth_pushPullU","CTRL_R_mouth_lipsTowardsTeethD","CTRL_L_mouth_lipsTowardsTeethD","CTRL_R_eye_eyelidU","CTRL_L_eyelashes_tweakerIn","CTRL_R_nose_nasolabialDeepen","CTRL_R_mouth_pushPullD","CTRL_L_mouth_lipsTowardsTeethU","CTRL_R_eye_eyelidD","CTRL_R_mouth_lipsTowardsTeethU","CTRL_R_mouth_lipsPressD","CTRL_L_mouth_lipsPressD","CTRL_faceGUIfollowHead","CTRL_eyesAimFollowHead","CTRL_C_tongue_thickThin","CTRL_R_mouth_thicknessInwardU","CTRL_L_mouth_thicknessInwardU","CTRL_R_mouth_thicknessInwardD","CTRL_L_mouth_thicknessInwardD"]

UR_52_index_Dic = {string: index for index, string in enumerate(UR_52_CTRL)}

getcsvFile = pm.fileDialog2(fileMode=1,fileFilter="*.csv")
newCSV=[]
f = open(getcsvFile[0],'r')
rdr = csv.reader(f) 
for line in rdr:
    newCSV.append(line)
f.close()
addFloat=1.0/len(UR_52_CTRL)
create_progressBar_Win('...ing 80% wait 1 minute')
progressNum=0
#print ( len(newCSV) ) 
for i in range(0,len(UR_52_CTRL)):
    ctrlattry=''
    if pm.objExists ( UR_52_CTRL[i] ):
        ctrlattry=UR_52_CTRL[i]+'.translateY'
        #pass
        #print ('yes',UR_52_CTRL[i])
    else:        
        #print ('no',UR_52_CTRL[i])
        ctrlattry=UR_52_CTRL[i].replace('Location.', 'translate').replace('Rotation.', 'rotate').replace('Scale.', 'scale')
    if pm.objExists ( ctrlattry )==False:  
        ctrlattry=ctrlattry.replace('.X','.translateX').replace('.Y','.translateY').replace('_thicknessInwardU','_thicknessU.translateY').replace('_thicknessInwardD','_thicknessD.translateY')
    if pm.objExists ( ctrlattry )==False:  
        ctrlattry = ctrlattry.replace('tongue_wideNarrow','tongue_narrowWide.translateY').replace('tongue_thickThin','tongue_press.translateY').replace('tongue_move.translateX','tongue.translateX').replace('tongue_move.translateY','tongue.translateY').replace('tongue_tipMove.translateX','tongue_tip.translateX').replace('tongue_tipMove.translateY','tongue_tip.translateY').replace('tongue_bendTwist.translateX','tongue_roll.translateX').replace('tongue_bendTwist.translateY','tongue_roll.translateY')    
    if pm.objExists ( ctrlattry )==False:                 
        print (ctrlattry)
    for j in range(1,len(newCSV)):
        #print (ctrlattry,newCSV[j][i])
        stringNumber= UR_52_index_Dic[UR_52_CTRL[i]]
        if (newCSV[j][stringNumber]) !='':
            cmds.setKeyframe(ctrlattry.split('.')[0], attribute=ctrlattry.split('.')[1], v = float(newCSV[j][stringNumber]), t=j )

    update_progress_bar( int(progressNum*100 ) ) 
    #print ('%f'%progressNum,int(progressNum*100))
    progressNum=progressNum+addFloat     
#실행 시간: 156.4198 초    
"""
addFloat=1.0/len(newCSV)
for j in range(1,len(newCSV)):
    for i in range(0,len(UR_52_CTRL)):
        ctrlattry=''
        if pm.objExists ( UR_52_CTRL[i] ):
            ctrlattry=UR_52_CTRL[i]+'.translateY'
            #pass
            #print ('yes',UR_52_CTRL[i])
        else:        
            #print ('no',UR_52_CTRL[i])
            ctrlattry=UR_52_CTRL[i].replace('Location.', 'translate').replace('Rotation.', 'rotate').replace('Scale.', 'scale')
        if pm.objExists ( ctrlattry )==False:  
            ctrlattry=ctrlattry.replace('.X','.translateX').replace('.Y','.translateY').replace('_thicknessInwardU','_thicknessU.translateY').replace('_thicknessInwardD','_thicknessD.translateY')
        if pm.objExists ( ctrlattry )==False:  
            ctrlattry = ctrlattry.replace('tongue_wideNarrow','tongue_narrowWide.translateY').replace('tongue_thickThin','tongue_press.translateY').replace('tongue_move.translateX','tongue.translateX').replace('tongue_move.translateY','tongue.translateY').replace('tongue_tipMove.translateX','tongue_tip.translateX').replace('tongue_tipMove.translateY','tongue_tip.translateY').replace('tongue_bendTwist.translateX','tongue_roll.translateX').replace('tongue_bendTwist.translateY','tongue_roll.translateY')    
        if pm.objExists ( ctrlattry )==False:                 
            print (ctrlattry)        
        stringNumber= UR_52_index_Dic[UR_52_CTRL[i]]
        cmds.setKeyframe(ctrlattry.split('.')[0], attribute=ctrlattry.split('.')[1], v = float(newCSV[j][stringNumber]), t=j )        
    update_progress_bar( int(progressNum*100 ) ) 
    progressNum=progressNum+addFloat   
#실행 시간: 301.3223 초
"""        
delete_progressBar_Win()
end_time = time.time()
execution_time = end_time - start_time  
print(f"실행 시간: {execution_time:.4f} 초",getcsvFile)
