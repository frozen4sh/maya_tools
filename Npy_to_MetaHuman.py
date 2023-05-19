# "D:\Justin\Facegood\TEST.fbx" 에서 작동함

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

list = ["brow_lower_l","tongue_Scale__X","tongue_Scale_Y","tongue_Scale__Y","tongue_Scale_Z","tongue_Scale__Z","nose_out_l","nose_out_r","tongue_u","tongue_u_u","brow_raise_d","cheek_suck_r","mouth_stretch_u","tongue_u_d","tooth_d_d","tongue_d","tooth_r","tooth_d_u","cheek_UP","eye_blink1_l","eye_blink1_r","eye_blink2_l","eye_blink2_r","eye_lidTight_l","eye_lidTight_r","eye_shutTight_l","eye_shutTight_r","brow_lower_r","eye_upperLidRaise_l","eye_upperLidRaise_r","eye_downLidRaise_l","eye_downLidRaise_r","jaw_sideways_l","jaw_sideways_r","jaw_thrust_c","mouth_chew_c","mouth_chinRaise_d","mouth_chinRaise_u","brow_raise_c","mouth_dimple_l","mouth_dimple_r","mouth_funnel_dl","mouth_funnel_dr","mouth_funnel_ul","mouth_funnel_ur","mouth_lipCornerDepressFix_l","mouth_lipCornerDepressFix_r","mouth_lipCornerDepress_l","mouth_lipCornerDepress_r","brow_raise_l","mouth_lipCornerPullOpen_l","mouth_lipCornerPullOpen_r","mouth_lipCornerPull_l","mouth_lipCornerPull_r","mouth_lipStretchOpen_l","mouth_lipStretchOpen_r","mouth_lipStretch_l","mouth_lipStretch_r","mouth_lowerLipDepress_l","mouth_lowerLipDepress_r","brow_raise_r","mouth_lowerLipProtrude_c","mouth_oh_c","mouth_oo_c","mouth_pressFix_c","mouth_press_l","mouth_press_r","mouth_pucker_l","mouth_pucker_r","mouth_screamFix_c","mouth_sideways_l","cheek_puff_l","mouth_sideways_r","mouth_stretch_c","mouth_suck_dl","mouth_suck_dr","mouth_suck_ul","mouth_suck_ur","mouth_upperLipRaise_l","mouth_upperLipRaise_r","nose_wrinkle_l","nose_wrinkle_r","cheek_puff_r","tooth_l","eye_lookDown1_l","eye_lookDown2_l","eye_lookLeft_l","eye_lookRight_l","eye_lookUp_l","eye_lookDown1_r","eye_lookDown2_r","eye_lookLeft_r","eye_lookRight_r","cheek_raise_l","eye_lookUp_r","tongue_Rot_1X","tongue_Rot__1X","tongue_Rot_2X","tongue_Rot__2X","tongue_Rot_3X","tongue_Rot__3X","tongue_Rot_1Y","tongue_Rot__1Y","tongue_Rot_2Y","cheek_raise_r","tongue_Rot__2Y","tongue_Rot_3Y","tongue_Rot__3Y","tongue_Rot_1Z","tongue_Rot__1Z","tongue_Rot_2Z","tongue_Rot__2Z","tongue_Rot_3Z","tongue_Rot__3Z","tongue_Scale_X","cheek_suck_l"]


frames = np.load(fullpath)
frames.shape
len(frames[3294])
print (frames[3294])


# 값을 BS 하나씩 넣어서 확인 해보고 싶을때

# for i in range(0,6000):
#     cmds.currentTime(i)
#     cmds.setAttr('blendShape7.'+list[63] , frames[i][63])
#     cmds.setKeyframe('blendShape7.'+list[63])
#     # cmds.setAttr('blendShape7.'+list[1] , frames[i][1])
#     # cmds.setKeyframe('blendShape7.'+list[1])    

   
for i in range(0,3294):
    cmds.currentTime(i)
    cmds.setAttr('blendShape7.'+list[1] , frames[i][1])
    cmds.setKeyframe('blendShape7.'+list[0])
    numi=0
    for j in frames[i]:
        cmds.setAttr('blendShape7.'+list[numi] , j)
        cmds.setKeyframe('blendShape7.'+list[numi])
        numi=numi+1