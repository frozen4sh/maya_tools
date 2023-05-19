'''
Created on 2023.04.26
Copyright (c) 2023 - VIVESTUDIOS & Justin Yehun Hwang (FrozenAsh)
http://vivestudios.com/
https://github.com/frozen4sh


'''


import maya.cmds as cmds
import os
import pymel.core as pm
import csv

cmds.currentUnit( time='ntsc' )


MH_CTRLs = ('CTRL_L_eye_faceScrunch',
'CTRL_L_mouth_pressD',
'CTRL_R_mouth_sharpCornerPull',
'CTRL_R_mouth_pushPullD',
'CTRL_R_mouth_pushPullU',
'CTRL_C_teethD',
'CTRL_L_mouth_stickyOuterD',
'CTRL_R_mouth_cornerPull',
'CTRL_L_eyelashes_tweakerOut',
'CTRL_R_mouth_suckBlow',
'CTRL_C_teeth_fwdBackD',
'CTRL_neck_throatUpDown',
'CTRL_L_mouth_lipsTowardsTeethU',
'CTRL_R_jaw_ChinRaiseD',
'CTRL_R_mouth_cornerSharpnessD',
'CTRL_R_mouth_stickyInnerD',
'CTRL_L_mouth_towardsU',
'CTRL_R_mouth_lipBiteD',
'CTRL_R_mouth_dimple',
'CTRL_R_eye_squintInner',
'CTRL_L_mouth_cornerDepress',
'CTRL_eyesAimFollowHead',
'CTRL_L_eye_lidPress',
'CTRL_C_mouth_lipShiftD',
'CTRL_L_neck_stretch',
'CTRL_L_mouth_stickyOuterU',
'CTRL_R_mouth_pressU',
'CTRL_L_mouth_pushPullU',
'CTRL_R_mouth_tightenU',
'CTRL_L_mouth_sharpCornerPull',
'CTRL_R_mouth_towardsD',
'CTRL_R_mouth_lipsTogetherU',
'CTRL_L_mouth_cornerPull',
'CTRL_L_nose_wrinkleUpper',
'CTRL_L_mouth_stickyInnerU',
'CTRL_R_mouth_stretch',
'CTRL_L_brow_raiseIn',
'CTRL_neck_digastricUpDown',
'CTRL_L_brow_lateral',
'CTRL_faceGUIfollowHead',
'CTRL_R_mouth_lipsPressU',
'CTRL_R_eyelashes_tweakerIn',
'CTRL_L_mouth_purseU',
'CTRL_R_mouth_lipsTowardsTeethD',
'CTRL_R_mouth_lipsTogetherD',
'CTRL_C_mouth',
'CTRL_R_mouth_lipSticky',
'CTRL_R_nose_wrinkleUpper',
'CTRL_L_mouth_lipsTogetherD',
'CTRL_L_mouth_lowerLipDepress',
'CTRL_R_mouth_thicknessD',
'CTRL_L_mouth_pushPullD',
'CTRL_C_tongue_press',
'CTRL_R_mouth_lowerLipDepress',
'CTRL_L_eye_eyelidU',
'CTRL_R_mouth_cornerSharpnessU',
'CTRL_L_mouth_tightenD',
'CTRL_L_nose',
'CTRL_C_tongue_inOut',
'CTRL_neck_throatExhaleInhale',
'CTRL_R_eye_cheekRaise',
'CTRL_R_mouth_lipBiteU',
'CTRL_L_mouth_stretchLipsClose',
'CTRL_L_mouth_upperLipRaise',
'CTRL_C_mouth_stickyD',
'CTRL_L_mouth_lipsTogetherU',
'CTRL_R_jaw_chinCompress',
'CTRL_R_mouth_corner',
'CTRL_L_mouth_dimple',
'CTRL_L_mouth_lipBiteU',
'CTRL_R_eyelashes_tweakerOut',
'CTRL_L_eye_squintInner',
'CTRL_L_mouth_lipSticky',
'CTRL_R_mouth_towardsU',
'CTRL_L_mouth_thicknessU',
'CTRL_L_mouth_corner',
'CTRL_L_mouth_lipsPressU',
'CTRL_C_neck_swallow',
'CTRL_R_eye_faceScrunch',
'CTRL_C_tongue_roll',
'CTRL_R_eye_lidPress',
'CTRL_R_mouth_lipsRollU',
'CTRL_C_mouth_stickyU',
'CTRL_C_jaw_fwdBack',
'CTRL_L_brow_down',
'CTRL_R_mouth_stretchLipsClose',
'CTRL_C_teeth_fwdBackU',
'CTRL_R_jaw_clench',
'CTRL_L_eyelashes_tweakerIn',
'CTRL_R_mouth_upperLipRaise',
'CTRL_C_eye',
'CTRL_R_mouth_lipsTowardsTeethU',
'CTRL_R_mouth_stickyInnerU',
'CTRL_R_mouth_stickyOuterU',
'CTRL_R_neck_stretch',
'CTRL_R_mouth_thicknessU',
'CTRL_L_mouth_suckBlow',
'CTRL_R_eye_pupil',
'CTRL_R_brow_lateral',
'CTRL_L_mouth_thicknessD',
'CTRL_L_mouth_towardsD',
'CTRL_R_eye',
'CTRL_L_nose_nasolabialDeepen',
'CTRL_C_jaw',
'CTRL_L_mouth_funnelD',
'CTRL_L_mouth_lipsRollU',
'CTRL_R_eye_eyelidD',
'CTRL_L_eye_cheekRaise',
'CTRL_L_neck_mastoidContract',
'CTRL_L_mouth_pressU',
'CTRL_R_mouth_purseU',
'CTRL_L_mouth_stickyInnerD',
'CTRL_R_neck_mastoidContract',
'CTRL_L_mouth_lipsRollD',
'CTRL_L_eye_pupil',
'CTRL_R_nose_nasolabialDeepen',
'CTRL_R_brow_raiseIn',
'CTRL_R_brow_raiseOut',
'CTRL_L_eye_eyelidD',
'CTRL_R_mouth_tightenD',
'CTRL_L_mouth_stretch',
'CTRL_lookAtSwitch',
'CTRL_C_mouth_lipShiftU',
'CTRL_rigLogicSwitch',
'CTRL_C_tongue_narrowWide',
'CTRL_R_jaw_ChinRaiseU',
'CTRL_L_mouth_cornerSharpnessU',
'CTRL_R_nose',
'CTRL_C_teethU',
'CTRL_L_mouth_tightenU',
'CTRL_R_mouth_purseD',
'CTRL_L_mouth_lipsBlow',
'CTRL_L_mouth_cornerSharpnessD',
'CTRL_L_jaw_ChinRaiseD',
'CTRL_R_mouth_lipsRollD',
'CTRL_R_mouth_pressD',
'CTRL_C_tongue',
'CTRL_L_mouth_funnelU',
'CTRL_C_eye_parallelLook',
'CTRL_R_ear_up',
'CTRL_L_jaw_ChinRaiseU',
'CTRL_R_mouth_lipsBlow',
'CTRL_R_brow_down',
'CTRL_L_brow_raiseOut',
'CTRL_C_tongue_tip',
'CTRL_R_eye_eyelidU',
'CTRL_L_jaw_clench',
'CTRL_R_mouth_funnelD',
'CTRL_R_mouth_cornerDepress',
'CTRL_R_mouth_stickyOuterD',
'CTRL_L_mouth_lipBiteD',
'CTRL_L_ear_up',
'CTRL_L_mouth_purseD',
'CTRL_L_mouth_lipsTowardsTeethD',
'CTRL_R_eye_blink',
'CTRL_L_jaw_chinCompress',
'CTRL_L_eye_blink',
'CTRL_R_mouth_funnelU',
'CTRL_C_jaw_openExtreme',
'CTRL_L_eye' )


new_range = cmds.playbackOptions(q=True, min=True), cmds.playbackOptions(q=True, max=True)


cmds.selectKey(MH_CTRLs, uk=1, t=(new_range), f=(new_range), hi="none", cp=0, shape=1 )
cmds.cutKey(an = "keys", cl = 1)


###########################################################

Audio_Name= pm.ls("VIVE_JUSTIN_TTS_*_iPhone")
File_Name= Audio_Name[0].name()

Get_Audio_Source_End=pm.PyNode(File_Name + ".se").get()
Source_End=int(str(Get_Audio_Source_End).split('.')[0]) -1

print(Source_End)
print(File_Name)
cmds.playbackOptions(aet=Source_End)
 

############################################################


PATH=0
FILE=1


filePath = cmds.file(q=True, sceneName=True)
splittedPath = os.path.split(filePath)

fullPath = os.path.join(splittedPath[PATH], File_Name)
print(fullPath)

cmds.file( rename=os.path.join(splittedPath[PATH], File_Name ))
cmds.file( save=True)




###########################################################


cmds.select ('CTRL_expressions')
# # Define function to create UI pop-up
# def create_ui():
#     # Create window
#     window_name = 'Export_Attributes'
#     if cmds.window(window_name, exists=True):
#         cmds.deleteUI(window_name)
#     window = cmds.window(window_name, title='Export Attributes', sizeable=False)
#     cmds.columnLayout(adjustableColumn=True)

#     # Add text fields for start and end frames
#     cmds.text(label='Start Frame:')
#     minTime_int = cmds.playbackOptions(q=1,minTime=1)
#     start_frame_field = cmds.intField(value=minTime_int, minValue=0)
#     cmds.text(label='End Frame:')
#     maxTime_int = cmds.playbackOptions(q=1,maxTime=1)
#     end_frame_field = cmds.intField(value=maxTime_int, minValue=0)

#     # Add button to export attributes
#     cmds.separator(height=10, style='none')
#     cmds.button(label='Export', command=lambda *args: export_attributes(start_frame_field, end_frame_field,window))
#     cmds.showWindow(window)


minTime_int = int(cmds.playbackOptions(q=1,minTime=1))
maxTime_int = int(cmds.playbackOptions(q=1,maxTime=1))

# Define function to export attributes
def export_attributes(a, b):
    
    # # Get start and end frames from UI fields
    # start_frame = cmds.intField(start_frame_field, query=True, value=True)
    # end_frame = cmds.intField(end_frame_field, query=True, value=True)

    # Get selected object
    selected_obj = cmds.ls(selection=True)

    # Get attributes of the selected object
    attributes = cmds.listAttr(selected_obj[0], visible=True, keyable=True)
    # 1~51 184~200
    poplist=[]
    poplistA=range(0,51)
    poplistB=range(183,200)
    poplistD=range(228,259)
    poplist.extend(poplistA)
    poplist.extend(poplistB)
    poplist.extend(poplistD)
    poplistC=[]
    inti=0
    for i in range(len(poplist)):
        inti=inti+1
        poplistC.append(poplist[inti*-1])
    #reverse     
    #print ('ok1',poplistC)
    for i in poplistC:
        attributes.pop(i)
    #print (attributes)    
    
    # Get scene file name without extension
    scene_path = cmds.file(query=True, sceneName=True)
    scene_dir, scene_file = os.path.split(scene_path)
    scene_name, scene_ext = os.path.splitext(scene_file)

    # Open the CSV file in write mode with scene name
    with open(os.path.join(scene_dir, scene_name + '.csv'), 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        # Write header row
        writer.writerow(['Frame'] + attributes)

        # Write data rows for each frame in the range
        for frame in range(a, b+1):
            cmds.currentTime(frame)
            data_rows = [frame]
            for attribute in attributes:
                attribute_value = cmds.getAttr(selected_obj[0] + '.' + attribute)
                data_rows.append(attribute_value)
            writer.writerow(data_rows)
            
    print('Attributes saved to ' + scene_name + '.csv')    
    # cmds.deleteUI(window)
# # Call the create_ui() function to start the UI
# create_ui()
export_attributes(minTime_int, maxTime_int)